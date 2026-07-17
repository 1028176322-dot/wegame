#!/usr/bin/env python3
# tools/generators/md_to_config.py
# 从 balance/*.md 数值表导出 data/config/<module>.json
# + data/schemas/<module>.schema.json (骨架)
# 确定性：同输入同输出，不修改源 MD。NEEDS-DESIGN 行跳过 + WARN。
#
# 边界测试覆盖:
#   S05 结构化路由 (counter_matrix / armor_reduce / scalars)
#   S29 点号 param_id (plv.L5.dmg_mult) — 原样保留为键名
#   S33 st_ 前缀 — 去命名空间不匹配时保留全键名
#   S33 status_effect_config/UI — '/' 转 '_'
#   S07 true/false 布尔值 — 保留为 JSON boolean
#   S30 [P] 占位符 — 跳过 + WARN
#   S11/S14/S17/S32 带括号注释的 module 名 — 剥离括号
#   S11 (clamp, ...) 非模块行 — 跳过
#   S16 tower_config(S2,消费) — 跨文件聚合到同一模块
#   多子表同一文件 — while 循环避免行重复消费
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

BALANCE_DIR = Path("docs/design/balance")
OUT_CONFIG = Path("data/config")
OUT_SCHEMA = Path("data/schemas")

COLS = ["param_id", "module", "base", "growth", "min", "max",
        "level_link", "unit", "description"]

# ── combat_config 专用结构化路由 ──
# 前缀 → (目标字段, 键名函数)
COMBAT_ROUTE = {
    # prefix -> (target_field, key_fn)      —— prefix match → nested object, key_fn extracts sub-key
    "combat_cm_":    ("counter_matrix", lambda k: k[len("combat_cm_"):]),
    "combat_armor_": ("armor_reduce",   lambda k: k[len("combat_armor_"):]),
}
# scalar fields that match old combat_ prefix but should stay flat
COMBAT_SCALAR_OVERRIDES = {
    "combat_electric_vs_air_override": "electric_vs_air_override",
    "combat_dmg_round":                "dmg_round",
}
# 由设计文档固定、不来自 balance 的 combat 字段
COMBAT_DOC_DEFAULTS = {
    "status_stack_rule": "refresh",
    "damage_formula": "base*level_bonus*growth^lv*counter-armor",
}

# ── remote_config 结构化路由 ──
# rc_ 前缀 param → 特定键名映射
REMOTE_CONFIG_MAP = {
    "rc_exchange_rate":       "exchange_rate",
    "rc_wave_diff_mult":     "wave_diff_mult",
    "rc_drop_mult":          "drop_mult",
    "rc_gold_per_wave_base": "gold_per_wave_base",
    "rc_fetch_interval":     "fetch_interval",
    "rc_inflation_threshold":"inflation_threshold",
}
# remote_config 中由 doc §3.1 固定非 balance 的字段
REMOTE_CONFIG_DOC_DEFAULTS = {
    "flag_monetize":    False,
    "flag_season":      False,
    "show_reload_toast": False,
}


# ── helper 函数 ──

def clean_module_name(raw):
    """去除模块名中的括号注释，如 'meta_config(n_gold1)' → 'meta_config'"""
    s = re.sub(r'\(.*?\)', '', raw).strip()
    if not s:
        return ""
    return s


def sanitize_filename(module):
    """将模块名转安全文件名：'/' → '_'"""
    return module.replace("/", "_")


def parse_value(s):
    """解析 base 列：返回 number / bool / None（跳过）。"""
    s = (s or "").strip()
    if s in ("-", "", "NEEDS-DESIGN", "[P]"):
        return None
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    try:
        return float(s)
    except ValueError:
        return None


def parse_md_tables(md_text):
    """提取含 param_id|module 表头的 markdown 表格，返回行 dict 列表。

    使用原始行（非预过滤），令空行作为天然表间隔；同时检测列数是否与表头一致，
    避免将同文件中的派生汇总表/不同结构表混入当前 balance 表。
    """
    lines = md_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and "param_id" in line and "module" in line:
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            j = i + 2  # 跳过表头与分隔行
            while j < len(lines):
                l = lines[j]
                if not l.strip().startswith("|"):
                    break  # 空行/章节标题 → 表结束
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                if len(cells) != len(header):
                    # 列数多于表头：说明 level_link / description 列含内嵌 '|'（如 S29 反引号公式）
                    # 取前 len(header)-1 列，将剩余合并为最后一列
                    if len(cells) > len(header):
                        prefix = cells[:len(header)-1]
                        suffix = "|".join(cells[len(header)-1:])
                        cells = prefix + [suffix]
                    else:
                        break  # 列数不足 → 不同结构表
                # 全分隔行（单元格由 '-' / ':' 组成，如 ---|---|---|---:）→ 跳过
                if all(set(c).issubset({"-", ":", " "}) for c in cells if c):
                    j += 1
                    continue
                out.append(dict(zip(header, cells)))
                j += 1
            i = j  # 跳到已消费行之后
        else:
            i += 1
    return out


def route_combat(rows):
    """构建结构化 combat_config。

    前缀匹配 → 嵌套对象（counter_matrix / armor_reduce）；
    精确匹配 COMBAT_SCALAR_OVERRIDES → 顶层标量；
    其余 combat_* → 顶层标量（截去 combat_ 前缀）。
    """
    cfg = dict(COMBAT_DOC_DEFAULTS)
    for r in rows:
        pid = r["param_id"]
        val = parse_value(r["base"])
        if val is None:
            print(f"[WARN] combat_config skip: {pid} (base={r['base']})", file=sys.stderr)
            continue
        # 1) 精确匹配标量覆盖
        if pid in COMBAT_SCALAR_OVERRIDES:
            cfg[COMBAT_SCALAR_OVERRIDES[pid]] = val
            continue
        # 2) 前缀匹配 → 嵌套对象
        matched = False
        for prefix, (field, keyfn) in COMBAT_ROUTE.items():
            if pid.startswith(prefix):
                cfg.setdefault(field, {})[keyfn(pid)] = val
                matched = True
                break
        if matched:
            continue
        # 3) 其余 combat_* → 标量
        if pid.startswith("combat_"):
            cfg[pid[len("combat_"):]] = val
    return cfg


def route_remote_config(rows):
    """构建结构化 remote_config（含 doc 默认布尔值）。"""
    cfg = dict(REMOTE_CONFIG_DOC_DEFAULTS)
    for r in rows:
        pid = r["param_id"]
        val = parse_value(r["base"])
        if val is None:
            print(f"[WARN] remote_config skip: {pid} (base={r['base']})", file=sys.stderr)
            continue
        if pid in REMOTE_CONFIG_MAP:
            cfg[REMOTE_CONFIG_MAP[pid]] = val
        elif pid.startswith("rc_"):
            cfg[pid[len("rc_"):]] = val
    return cfg


def build_module(module, rows):
    """通用 builder：参数字段 1:1 映射（去命名空间前缀）。"""
    if module == "combat_config":
        return route_combat(rows)
    if module == "remote_config":
        return route_remote_config(rows)
    # 通用：取模块名前缀后去掉
    # module 如 economy_config → ns = economy_
    # module 如 attribute_def → ns = attribute_  (不匹配 attr_ → 回落全键)
    # module 如 attr_composition → ns = attr_composition_? 不对
    # 改进: 取 prefix 为已知的 param_id 公共前缀
    # 先从 rows 中所有 param_id 推断公共前缀
    pids = [r["param_id"] for r in rows]
    common = find_common_prefix(pids)
    cfg = {}
    for r in rows:
        pid = r["param_id"]
        val = parse_value(r["base"])
        if val is None:
            print(f"[WARN] {module} skip: {pid} (base={r['base']})", file=sys.stderr)
            continue
        # 去公共前缀；无公共前缀则保留全 pid
        if common and pid.startswith(common):
            key = pid[len(common):]
        else:
            key = pid
        cfg[key] = val
    return cfg


def find_common_prefix(pids):
    """从 param_id 列表中找公共前缀（以 '_' 结尾）。"""
    if not pids:
        return ""
    # 取第一个 pid 的各前缀尝试
    parts = pids[0].split("_")
    for end in range(len(parts) - 1, 0, -1):
        cand = "_".join(parts[:end]) + "_"
        if all(p.startswith(cand) for p in pids):
            return cand
    return ""


def generate_schema(module, rows, cfg_keys):
    """生成简单的 schema 骨架（draft-07）。"""
    # 结构化 module 用手写模板；此处生成标量壳
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": module,
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False,
    }
    for k in sorted(cfg_keys):
        schema["properties"][k] = {"type": "number"}
    return schema


def main():
    OUT_CONFIG.mkdir(parents=True, exist_ok=True)
    OUT_SCHEMA.mkdir(parents=True, exist_ok=True)

    # 跨所有 S*.md 收集行，按清洗后的 module 聚合
    all_rows = defaultdict(list)

    for md_path in sorted(BALANCE_DIR.glob("S*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"[ERR] 读取 {md_path.name} 失败: {e}", file=sys.stderr)
            continue

        tables = parse_md_tables(text)
        if not tables:
            continue
        for r in tables:
            raw_mod = r.get("module", "")
            module = clean_module_name(raw_mod)
            if not module:
                print(f"[SKIP] {md_path.name}: 无效模块名 '{raw_mod}' (param_id={r.get('param_id','?')})",
                      file=sys.stderr)
                continue
            all_rows[module].append(r)

    # 逐模块构建 cfg + 写文件
    module_schemas = {}
    for module in sorted(all_rows.keys()):
        rows = all_rows[module]
        cfg = build_module(module, rows)
        if not cfg:
            print(f"[SKIP] {module}: 无有效数值（全部跳过）", file=sys.stderr)
            continue

        fname = sanitize_filename(module)
        out_path = OUT_CONFIG / f"{fname}.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"[OK] {fname}.json: {len(cfg)} keys")

        # 生成 schema 骨架（仅结构化 module 需手写）
        schema = generate_schema(module, rows, cfg.keys())
        schema_path = OUT_SCHEMA / f"{fname}.schema.json"
        schema_path.parent.mkdir(parents=True, exist_ok=True)
        schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2),
                               encoding="utf-8")


if __name__ == "__main__":
    main()

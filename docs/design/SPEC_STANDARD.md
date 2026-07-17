# AI-Readable Spec 标准（v0.1-draft）

> 项目：循环塔防（微信小游戏 · Cocos Creator 3.8.8 / TypeScript）
> 性质：宪法级规范，全 33 系统改造必须遵从
> 决策权：Decision Owner；本文件由主理人游承峰汇编（spec-doc 文档侧 + spec-json 机器侧草案），关键裁决 pending DO 终审
> 关联：GDD.md / systems/S*.md / balance/*.md / i18n/text_config.csv

## 0. 目标与痛点映射

| # | 痛点（AI 写功能代码时卡住） | 本规范解决机制 |
|---|---|---|
| 1 | `[PLACEHOLDER]` 死胡同（文档写占位符，初值在 balance 但没指向） | §2 二选一：`value_ref` 指针 / `NEEDS-DESIGN` |
| 2 | 同参数多处定义无单一事实源（克制矩阵在 S05/S30/balance 各一份） | §1.3 单一事实源铁律 + §5 枚举权威 |
| 3 | 配置数据只有 MD 表格、无机器可读文件 | §1.2 轨道 B：JSON + Schema 唯一数值真相源 |
| 4 | 缺「实现契约」小节（只有 mermaid，无接口/错误码契约） | §3 实现契约 6 子表 |
| 5 | 冲突/待裁定无「当前实现口径」，AI 不敢落地 | §4 `current_implementation` + `pending_decision` + `owner` |

## 1. 双轨制定义

### 1.1 轨道 A — Markdown 设计文档（人读 + 结构化索引）
讲 `why` / 边界 / 异常 / 设计决策 / 冲突与待裁定 / 实现契约（契约是给 AI 的结构化索引，但**终值不在此**）。**不在此**：具体数值（改为 `value_ref` 指针）、机器可读配置（改为 JSON 引用或 NEEDS-DESIGN）。

### 1.2 轨道 B — 机器可读 JSON 配置 + Schema（AI 写代码唯一数值真相源）
- `data/config/<module>.json`：结构化配置（combat_config / tower_config / enemy_config / status_effect_config / wave_config / economy_config / …）
- `data/schemas/<module>.schema.json`：同名配对 JSON Schema（draft-07）
- `data/i18n/<lang>.json`：`{id: text}`，en/zh-TW 空→运行时回退 zh-CN
- 数值参数层：`balance/<system>.json`（按 `param_id` 索引标量）+ schema
- 生成物**不得手编**；改源（MD/CSV）后跑生成器重出

### 1.3 单一事实源铁律
1. 每个 `param_id` / 配置行**只存在一个权威定义**（轨道 B）；MD 只允许**引用**，不允许重定义。
2. 同 `param_id` 不得在两个 balance 文件各写一份（如 `combat_armor_poison` 仅存 `balance/S05_combat.json`）。
3. 枚举值以 S30 权威（`DamageType = physical|magic|poison|control`；`ArmorType = none|light|heavy|magic_immune|air`），禁止各系统本地自定义枚举。
4. 反例（现状须清理）：S05 §2.5.10 C-1 文字仍写「balance 现存 1.5」，但 balance 表已改 0.0——改造后设计文档只留指针 + 权威说明。

## 2. `[PLACEHOLDER]` 处理规则

每个 `[PLACEHOLDER]` 必须**二选一**：

**(a) 已设计 → `value_ref` 指针**
```
value_ref: balance/<system>.json#<param_id>      # 标量调优值
value_ref: config/<module>.json#/<json-pointer>  # 结构化配置行
```
**(b) 未设计 → `NEEDS-DESIGN`**
```
NEEDS-DESIGN (owner: <system_id>, due: <milestone>)
```

**示例（S05 §3 `counter_matrix`）**
```json
// 改造后
{
  "arrow_vs_light":        { "value_ref": "balance/S05_combat.json#combat_cm_arrow_vs_light" },
  "magic_vs_magic_immune": { "value_ref": "balance/S05_combat.json#combat_cm_magic_vs_magic_immune" },
  "electric_vs_air":       { "value_ref": "balance/S05_combat.json#combat_electric_vs_air_override" }
}
```
**未设计项（S05 §2.5 暴击）**：`暴击率: NEEDS-DESIGN (owner: S05, due: P4-tuning)`（对应 balance 的 `combat_crit_rate`/`combat_crit_mult` 标 NEEDS-DESIGN，建议从 JSON 移除，仅在 MD 标注）。

**存量清理（S05 §3 的 12 个 `[PLACEHOLDER]` 字段）**：`counter_matrix.*`→`combat_cm_*`；`armor_reduce.*`→`combat_armor_*`；`projectile_speed/splash_radius/slow_*/poison_*/chain_*`→对应 `combat_*`。

术语统一：禁裸 `[PLACEHOLDER]`、禁「调优杆」作终值占位；终值一律 `value_ref` 或 `NEEDS-DESIGN`。

## 3. 「实现契约」小节模板（每份 S*.md 新增 §5）

含 6 子表（纯 mermaid 图保留为可视化，**不得替代**状态转换表）：

1. **输入数据结构**（字段 / 类型 / 来源 config 字段）
2. **输出数据结构**
3. **跨系统接口调用表**（caller / callee / function / 方向 in-out / 用途）
4. **错误码表**（E# / 场景 / 兜底 / 涉及系统）
5. **状态转换表**（state / event / transition / action，AI 可消费）
6. **数值消费清单**（本系统消费的所有 param_id + 来源文件）

样张（S05 完整 6 表）见 spec-doc 草案 §3，改造时据此套用。

## 4. 冲突 / 待裁定标注规范

每项**三要素齐全**：
- `current_implementation`：AI 现按此写
- `pending_decision`：DO 裁定后切到的值
- `owner`

样张 C-1（魔免系数）/ C-2（毒甲枚举）/ C-7（腐蚀语义）见 spec-doc 草案 §4。

## 5. 命名统一清单（N1–N6，主理人建议采纳，pending DO 终审）

| # | 冲突点 | 推荐处理 |
|---|---|---|
| N1 | 电塔 id | 统一 `t_electric`，**弃用 `t_thunder`**（S11 §3.2 / S29 §3.2 / balance/_index / SYSTEM_BREAKDOWN 残留改） |
| N2 | 腐蚀语义 C-7 | **对齐 S33「护甲削减 cap5」**（非 S28「DoT 可叠」）；S28 §2.6 毒塔被动①文案同步改 |
| N3 | 毒甲枚举 C-2 | `poison` → `air`，**弃 `combat_armor_poison`**；S04 枚举同步改 air |
| N4 | `[PLACEHOLDER]` 术语 | 全项目统一 `value_ref` / `NEEDS-DESIGN` |
| N5 | 枚举权威 | `DamageType`/`ArmorType` 全项目对齐 S30；禁本地自定义 |
| N6 | param_id 前缀注册 | 白名单 `combat_`/`tower_/`econ_/`wave_/`status_`(别名`st_`)/`attr_/`meta_/`lvl_`，Schema 固化 + 跨文件唯一 |

## 6. 文档章节顺序标准

```
0. 元数据头（归属域/优先级/关联F码/版本/依赖/NEEDS-DESIGN 索引）
1. 系统 UI 布局（线框 / 组件表 / 分辨率自适应）
2. 逻辑功能（模块表 / 状态机 / 时序图 / 异常边界表）
3. 配置表设计（字段表 + 多行示例；数值全部 value_ref 或 NEEDS-DESIGN）
4. 美术资源需求
5. 实现契约（§3 模板 6 子表）
6. 冲突与待裁定（§4 三要素格式）
```

## 7. JSON 配置导出规范（轨道 B）

### 7.1 字段机器契约
- **类型**：`number` / `integer` / `string` / `boolean` / `enum`（用 `enum` 关键字）/ `json`
- **单位（x-unit）**：px/s、px、倍、减伤%(0–1小数)、秒、跳、位、gold、木、%、级、次、条、天、MB
- **钳制**：balance `min`/`max` → schema `minimum`/`maximum`（闭区间）；`-`→省略该边界
- **默认**：= `base` 初值；NEEDS-DESIGN 无默认、运行时按「未启用/安全值」兜底
- **必填**：结构化顶层字段 `required`；NEEDS-DESIGN 字段非 required
- **枚举**：`status_stack_rule{refresh,stack}`；`armor_type{none,light,heavy,magic_immune,air}`；`damage_type{physical,magic,poison,control}`
- **格式**：浮点用小数（`0.5`）；减伤 0–1 小数（`0.3`=30%）；倍率基准 `1.0`；整数用 `integer`

### 7.2 导出工具
- `tools/generators/md_to_config.py`：解析 `balance/*.md` 表格 → `data/config/<module>.json` + schema（确定性、不修改源 MD、NEEDS-DESIGN 行跳过 + WARN）
- `tools/generators/csv_to_i18n.py`：`text_config.csv` → `data/i18n/<lang>.json`
- 路由：通用 module `param_id` 去命名空间前缀 1:1 映射；`combat_config` 按前缀路由（`combat_cm_*`→counter_matrix、`combat_armor_*`→armor_reduce、其余同名标量）；`status_stack_rule`/`damage_formula` 由设计文档 default 固定

### 7.3 TS 加载契约（Cocos Creator 3.8.8 / TypeScript）
- `loadConfig<T>(name)`：`resources.load('config/'+name, JsonAsset)`（JSON 须先导出到 `assets/resources/config/`）
- `interface CombatConfig`（类型安全，见附件 A schema 映射）
- **两层兜底**：① 加载/校验层（缺键→schema default；无 default→模块安全默认；越界/NaN→`clamp(min,max)`，无法钳则默认 + S25 告警）② 战斗管线层（E01–E20：矩阵缺键→1.0、armor 未知→none、dmg_type 未知→physical、HP≤0→钳 1、slow_k 钳 0.1、eff_dmg 负数→max(0,…)）
- 远程配置 S21：本地兜底 + 远端按 key 浅合并 + 逐键范围校验（越界保留本地默认）

### 7.4 i18n 导出与回退
- `data/i18n/zh-CN.json = {id: zh-CN}`（真值）；`en.json`/`zh-TW.json = {id: ""}`（空→回退）
- `getText(id, lang)`：取 lang 列；空/缺失→回退 zh-CN；id 不存在→返回 id

### 7.5 单一事实源声明
JSON 运行时唯一真相源；balance MD 表是人类可读镜像（与 JSON 同步维护）；systems MD 是语义说明，值以 JSON 为准。**冲突裁决顺序：JSON > balance MD > systems MD。**

## 8. 治理前置（pending DO 授权，Phase B 硬依赖）

| # | 缺口 | 处理 |
|---|---|---|
| G1 | `data/` 不在 `config/root_allowlist.json` 的 `allowedDirectories` | 改 allowlist 加 `data`；`file_placement_rules` 加 `data/config`/`data/schemas`/`data/i18n`（pattern `*.json`，owner=Executor，generated=true） |
| G2 | `data-config` 域 unassessed（`AUTHORITY_INDEX` 无 current） | 加 `data-config` current 入口（指向 `data/README.md`） |
| G3 | 缺 ADR | 新增 `ADR-00xx` 双轨制数值真相源（与 ADR-0002 并列） |
| G4 | `data/` 目录未建 | `mkdir data/{config,schemas,i18n}` |

> 不解决 G1–G4，Phase B 无法导出 `data/`，双轨制不完整。建议 DO 授权后执行。

## 9. 主理人裁决记录

- **C-7 腐蚀**：采纳 S33「护甲削减 cap5」（理由：S33 是状态机制唯一权威、已落地 `corrosion_val=15%/层 cap5` 并接入 `buff_mod.armor_mult`；伤害管线已消费；改走 DoT 会与 `poison_dot` 角色重叠且需重接管线）。
- **N1–N6**：全部采纳推荐。
- **指针格式** `value_ref: balance/<system>.json#<param_id>` 确认（与 spec-json 对齐）。
- 以上 pending DO 终审；若 DO 反向裁定，回改 §5 / §9。
- **DO 终审确认（2026-07-17）**：S29 `plv.L<n>` 行级→展平为原子化 `plv.L<n>.<field>` 方案(b)；S33 前缀 `st_` 作为 `status_` 别名纳入 N6 白名单，balance 不改名。

## 附录
- 附件 A：`docs/design/schema/combat_config.schema.json`（完整 draft-07 样例，含 `x-param-map` 溯源）
- 附件 B：`tools/generators/md_to_config.py`（MD→JSON 导出脚本草稿）
- 附件 C：`tools/generators/csv_to_i18n.py`（CSV→i18n JSON 导出脚本草稿）

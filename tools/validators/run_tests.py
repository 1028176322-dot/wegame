"""run_tests.py — TEST_COMMAND 入口（检查器自测，含负向 fixture）。

每个检查器用构造输入验证「能正确识别违规」且「对干净输入放行」。
测试失败以 FAIL 明确标出，绝不把 NOT_IMPLEMENTED 写成 PASS。

退出码：0=全部 PASS；1=存在 FAIL；2=自身错误。
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "validators"))

import file_placement_validator as fp  # noqa: E402
import secret_validator as sv  # noqa: E402
import gate_validator as gv  # noqa: E402

PASS = "PASS"
FAIL = "FAIL"
results: list[tuple[str, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL))
    mark = "✅" if ok else "❌"
    print(f"  {mark} {name}" + (f" — {detail}" if detail and not ok else ""))


# --- file_placement_validator 负向 fixture ---
def test_placement() -> None:
    root = REPO_ROOT
    allow = fp.load_root_allowlist(root)
    rules = fp.load_placement_rules(root)

    # 违规1：根级禁止文件
    e1, _ = fp.validate_placement(root, ["random_root_file.txt"], allow, rules)
    record("placement: 根级禁名被拦截", any("random_root_file.txt" in x for x in e1))

    # 违规2：未登记顶层目录
    e2, _ = fp.validate_placement(root, ["evil_dir/x.md"], allow, rules)
    record("placement: 未登记顶层目录被拦截", any("evil_dir" in x for x in e2))

    # 违规3：禁名 *_new.*
    e3, _ = fp.validate_placement(root, ["docs/design/foo_new.md"], allow, rules)
    record("placement: *_new.* 被拦截", any("_new." in x for x in e3))

    # 干净输入：已登记目录应 0 ERROR
    e4, _ = fp.validate_placement(root, ["docs/governance/X.md", "data/config/y.json"], allow, rules)
    record("placement: 合法路径 0 ERROR", len(e4) == 0)


# --- secret_validator 负向 fixture ---
def test_secret() -> None:
    evil = (
        "aws_key = AKIAIOSFODNN7EXAMPLE\n"
        "token: ghp_1234567890abcdefghijklmnopqrstuvwxyz\n"
        "password='S3cr3tV4lueH1ghEntropyX9'\n"
    )
    hits = sv.scan_text(evil)
    rule_ids = {h[0] for h in hits}
    record("secret: AWS 命中", "R-AWS" in rule_ids)
    record("secret: GitHub 命中", "R-GITHUB" in rule_ids)
    record("secret: 赋值高熵命中", "R-ASSIGN" in rule_ids)
    # 脱敏：不得回显明文
    flat = " ".join("".join(str(x) for x in h) for h in hits)
    record("secret: 输出不含明文", "AKIAIOSFODNN7EXAMPLE" not in flat)

    clean = "print('hello world')\nx = 1 + 2\n"
    record("secret: 干净文本 0 命中", len(sv.scan_text(clean)) == 0)


# --- gate_validator 负向 fixture ---
def test_gate() -> None:
    good_index = (
        "| `docs/governance/通用AI项目管理方案.md` | `0bb4b00bfb0a433be144b0b636cf071af2f4ba689f536d8453a631d898ee298e` |\n"
    )
    bad_index = "| `docs/governance/通用AI项目管理方案.md` | `" + "0" * 64 + "` |\n"
    # 真实文件 SHA 必然 != 'deadbeef...'，应报 ERROR
    errs = gv.verify_freeze_locks(REPO_ROOT, bad_index)
    record("gate: 冻结 SHA 漂移被拦截", len(errs) == 1 and "漂移" in errs[0])

    # 真实冻结锁应一致（对当前仓库）
    real_text = (REPO_ROOT / "docs/governance/AUTHORITY_INDEX.md").read_text(encoding="utf-8")
    real_errs = gv.verify_freeze_locks(REPO_ROOT, real_text)
    record("gate: 当前仓库冻结锁一致", len(real_errs) == 0, "; ".join(real_errs[:1]))

    # 非法进度状态（大写词汇，检查器仅校验 [A-Z_]+ 状态词）
    bad_progress = "| Phase X | BOGUS_STATE | DO | E1 | 2026-07-17 |\n"
    perrs = gv.check_progress_statuses(bad_progress)
    record("gate: 非法进度状态被拦截", any("BOGUS_STATE" in p for p in perrs))

    good_progress = "| Phase 5 | verified | DO | E3 | 2026-07-17 |\n"
    record("gate: 合法进度状态通过", len(gv.check_progress_statuses(good_progress)) == 0)


def main() -> int:
    print("=== TEST_COMMAND 自测 ===")
    test_placement()
    test_secret()
    test_gate()

    failed = [n for n, s in results if s == FAIL]
    print(f"\n总计 {len(results)} 项，PASS {len(results)-len(failed)} / FAIL {len(failed)}")
    if failed:
        print(f"[TEST_COMMAND] FAIL: {', '.join(failed)}")
        return 1
    print("[TEST_COMMAND] PASS: 全部检查器自测通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

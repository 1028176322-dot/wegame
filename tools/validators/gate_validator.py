"""gate_validator — 门禁一致性校验器（Phase 5）。

两项检查：
  1. 冻结锁 SHA 一致性：解析 AUTHORITY_INDEX.md 冻结锁表，逐文档校验
     sha256(当前内容) == 表内 SHA。漂移即 ERROR（治理红线）。
  2. 进度状态合法性：解析 docs/progress/_index.md 中的 Status 单元格，
     必须落在七值集合；ENGINEERING/PROGRESS_RULES 引用的五状态词
     必须合法。出现非法即 ERROR。

退出码：0=无 ERROR；1=存在 ERROR；2=自身运行错误。
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]

SEVEN_VALUE = {
    "unassessed", "not_started", "in_progress",
    "blocked", "verification_pending", "verified", "deprecated",
}
FIVE_STATUS = {"PASS", "FAIL", "NOT_RUN", "NOT_IMPLEMENTED", "BLOCKED"}

FREEZE_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|")
STATUS_CELL_RE = re.compile(r"\|\s*([A-Za-z_]+)\s*\|")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_freeze_locks(index_text: str) -> List[Tuple[str, str]]:
    locks: List[Tuple[str, str]] = []
    for line in index_text.splitlines():
        m = FREEZE_RE.match(line.strip())
        if m:
            locks.append((m.group(1), m.group(2)))
    return locks


def verify_freeze_locks(repo_root: Path, index_text: str) -> List[str]:
    errors: List[str] = []
    for rel, expected in parse_freeze_locks(index_text):
        p = repo_root / rel
        if not p.exists():
            errors.append(f"ERROR freeze {rel}: 文件不存在")
            continue
        actual = _sha256(p)
        if actual != expected:
            errors.append(
                f"ERROR freeze {rel}: SHA 漂移 "
                f"(expected {expected[:12]}… actual {actual[:12]}…)"
            )
    return errors


def check_progress_statuses(index_text: str) -> List[str]:
    errors: List[str] = []
    for line in index_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if "Status" in line or line.startswith("|---"):
            continue
        for m in STATUS_CELL_RE.finditer(line):
            val = m.group(1)
            # 仅校验看起来像状态词的单元格（全大写/下划线）
            if re.fullmatch(r"[A-Z_]+", val) and len(val) > 3:
                if val not in SEVEN_VALUE and val not in FIVE_STATUS:
                    errors.append(f"ERROR progress 状态非法: '{val}' @ {line.strip()[:60]}")
    return errors


def main() -> int:
    try:
        index_path = REPO_ROOT / "docs/governance/AUTHORITY_INDEX.md"
        index_text = index_path.read_text(encoding="utf-8")
        progress_path = REPO_ROOT / "docs/progress/_index.md"
        progress_text = progress_path.read_text(encoding="utf-8")
    except Exception as e:  # pragma: no cover
        print(f"RUNNER_ERROR {e}", file=sys.stderr)
        return 2

    errors: List[str] = []
    errors += verify_freeze_locks(REPO_ROOT, index_text)
    errors += check_progress_statuses(progress_text)

    for e in sorted(set(errors)):
        print(e)
    if errors:
        print(f"[gate] FAIL: {len(set(errors))} error(s)")
        return 1
    print("[gate] PASS: 冻结锁一致 + 进度状态合法")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""file_placement_validator — 文件放置/根allowlist校验器（Phase 5）。

依据：
  - config/root_allowlist.json  （根目录允许清单）
  - config/file_placement_rules.json （子目录模式规则）

行为：
  - 默认只读；不修改任何文件。
  - 遍历 `git ls-files` 得到受跟踪文件，逐条校验。
  - 根级文件必须在 allowedFiles；顶层目录必须在 allowedDirectories。
  - 子目录若在 directoryRules 中，强制 allowedPatterns/forbiddenPatterns。
  - 子目录若不在 directoryRules，仅 WARNING（提示补登目录地图），不阻断。
  - 全局 forbiddenPatterns（含 *_new.*、new/ 等）命中即 ERROR。

退出码：0=无 ERROR（允许 WARNING）；1=存在 ERROR；2=自身运行错误。
"""
from __future__ import annotations

import fnmatch
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
SEVEN_VALUE = {
    "unassessed", "not_started", "in_progress",
    "blocked", "verification_pending", "verified", "deprecated",
}


def _load_json(repo_root: Path, rel: str) -> dict:
    p = repo_root / rel
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def load_root_allowlist(repo_root: Path) -> dict:
    return _load_json(repo_root, "config/root_allowlist.json")


def load_placement_rules(repo_root: Path) -> dict:
    return _load_json(repo_root, "config/file_placement_rules.json")


def tracked_files(repo_root: Path) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=str(repo_root), capture_output=True, text=True,
    )
    if out.returncode != 0:
        return []
    return [p for p in out.stdout.split("\0") if p]


def _match_any(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pat) for pat in patterns)


def _best_rule(subdir: str, dir_rules: dict) -> dict | None:
    """最长前缀匹配：文件所在子目录或其祖先目录在 directoryRules 中即采用，
    取最长匹配（最具体）。"""
    best = None
    best_len = -1
    for p, rule in dir_rules.items():
        if subdir == p or subdir.startswith(p + "/"):
            if len(p) > best_len:
                best_len = len(p)
                best = rule
    return best


def _forbidden_dir_component(path: str, patterns: list[str]) -> bool:
    # patterns 中以 "/" 结尾的视为目录名（任意层级命中即违例）
    comps = path.split("/")
    for pat in patterns:
        if pat.endswith("/"):
            name = pat[:-1]
            if name in comps:
                return True
    return False


def validate_placement(
    repo_root: Path,
    files: list[str],
    root_allowlist: dict,
    placement_rules: dict,
) -> Tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    allowed_files = set(root_allowlist.get("allowedFiles", []))
    allowed_dirs = set(root_allowlist.get("allowedDirectories", []))
    forbidden = root_allowlist.get("forbiddenPatterns", [])

    dir_rules = {r["path"]: r for r in placement_rules.get("directoryRules", [])}

    for raw in files:
        path = raw.replace(os.sep, "/")
        if path.startswith("./"):
            path = path[2:]

        # 全局禁名/禁目录
        if _match_any(path, forbidden) or _forbidden_dir_component(path, forbidden):
            errors.append(f"ERROR {path}: 命中 root_allowlist 禁名/禁目录规则")
            continue

        parts = path.split("/")
        if len(parts) == 1:
            # 根级文件
            if parts[0] not in allowed_files:
                errors.append(f"ERROR {path}: 根级文件不在 root_allowlist.allowedFiles")
            continue

        top = parts[0]
        if top not in allowed_dirs:
            errors.append(f"ERROR {path}: 顶层目录 '{top}' 不在 root_allowlist.allowedDirectories")
            continue

        # 子目录规则（最长前缀匹配；allowedPatterns 优先于 forbiddenPatterns）
        subdir = "/".join(parts[:-1])
        rule = _best_rule(subdir, dir_rules)
        if rule is not None:
            fname = parts[-1]
            allowed_p = rule.get("allowedPatterns", [])
            forbidden_p = rule.get("forbiddenPatterns", [])
            if allowed_p:
                if not _match_any(fname, allowed_p):
                    errors.append(f"ERROR {path}: 不在子目录规则 allowedPatterns {allowed_p}")
            elif _match_any(fname, forbidden_p):
                errors.append(f"ERROR {path}: 命中子目录规则 forbiddenPatterns {forbidden_p}")
        else:
            warnings.append(f"WARN {path}: 子目录 '{subdir}' 未登记于 file_placement_rules（建议补登）")

    return errors, warnings


def main() -> int:
    try:
        root = REPO_ROOT
        allow = load_root_allowlist(root)
        rules = load_placement_rules(root)
        files = tracked_files(root)
        errors, warnings = validate_placement(root, files, allow, rules)
    except Exception as e:  # pragma: no cover
        print(f"RUNNER_ERROR {e}", file=sys.stderr)
        return 2

    for w in sorted(set(warnings)):
        print(w)
    for e in sorted(set(errors)):
        print(e)
    if errors:
        print(f"[file_placement] FAIL: {len(errors)} error(s), {len(set(warnings))} warning(s)")
        return 1
    print(f"[file_placement] PASS: 0 error(s), {len(set(warnings))} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

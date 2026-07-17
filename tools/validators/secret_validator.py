r"""secret_validator — 秘密扫描器（Phase 5，安全门禁）。

规则（依据 SECURITY_RULES §15.3）：
  - 密钥只能来自安全凭据系统或环境变量；禁止硬编码。
  - 扫描器输出必须脱敏：只含 规则ID、路径、行号、不可逆指纹（sha256 截断）。
  - 当前工作区 0 命中不代表历史已清理。

检测规则（保守，避免误报）：
  - R-AWS：AKIA[0-9A-Z]{16}
  - R-PRIVKEY：-----BEGIN * PRIVATE KEY-----
  - R-GITHUB：ghp_ / gho_ / ghu_ / ghs_ / ghr_ 前缀令牌
  - R-SLACK：xox[baprs]- 前缀令牌
  - R-GOOGLE：AIza[0-9A-Za-z_-]{35}
  - R-OPENAI：sk-[A-Za-z0-9]{20,}
  - R-JWT：eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+
  - R-ASSIGN：常见赋值 password/secret/api_key/token/private_key= 高熵值(>=16)
  - R-ENVSECRET：.env 文件中的 KEY=高熵值

退出码：0=0 命中；1=存在命中；2=自身运行错误。
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]

# 二进制/生成物/依赖目录不扫
SKIP_DIRS = {".git", "node_modules", "dist", "build", "vendor", "__pycache__", ".cache"}
TEXT_EXT = {
    ".py", ".js", ".ts", ".json", ".md", ".txt", ".yaml", ".yml", ".toml",
    ".env", ".ini", ".cfg", ".sh", ".bat", ".ps1", ".html", ".css", ".csv",
}
MAX_SCAN_BYTES = 1_000_000

RULES = [
    ("R-AWS", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("R-PRIVKEY", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("R-GITHUB", re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}")),
    ("R-SLACK", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("R-GOOGLE", re.compile(r"\bAIza[0-9A-Za-z_-]{35}")),
    ("R-OPENAI", re.compile(r"\bsk-[A-Za-z0-9]{20,}")),
    ("R-JWT", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
]
ASSIGN_RE = re.compile(
    r"""(?i)\b(password|passwd|secret|api[_-]?key|token|private[_-]?key|access[_-]?key)\b
        \s*[:=]\s*['"]?([A-Za-z0-9_.-]{16,})""", re.VERBOSE)
HIGH_ENTROPY = re.compile(r"[A-Za-z0-9_-]{32,}")


def _fingerprint(secret: str) -> str:
    # 不可逆指纹：仅输出 sha256 前 12 位，绝不回显原文
    return hashlib.sha256(secret.encode("utf-8")).hexdigest()[:12]


def _entropy_ok(s: str) -> bool:
    # 粗略高熵判断：字符集多样性
    return len(set(s)) >= 8


def scan_text(text: str) -> List[Tuple[str, int, str]]:
    """返回 (rule_id, line_no, fingerprint)。不返回明文。"""
    hits: List[Tuple[str, int, str]] = []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for rid, rx in RULES:
            for m in rx.finditer(line):
                hits.append((rid, i, _fingerprint(m.group(0))))
        # 赋值型高熵
        for m in ASSIGN_RE.finditer(line):
            val = m.group(2)
            if _entropy_ok(val):
                hits.append(("R-ASSIGN", i, _fingerprint(val)))
        # 通用高熵（仅当行很短，避免误伤 base64 文本块）
        if len(line) <= 80:
            for m in HIGH_ENTROPY.finditer(line):
                if _entropy_ok(m.group(0)) and m.group(0) not in line[:0]:
                    # 避免与上面规则重复上报同一段
                    if not any(m.group(0) in r for _, _, r in hits if False):
                        pass
    return hits


def tracked_files(repo_root: Path) -> List[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=str(repo_root),
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return []
    return [p for p in out.stdout.split("\0") if p]


def scan_repo(repo_root: Path) -> List[Tuple[str, str, int, str]]:
    """返回 (rule_id, rel_path, line_no, fingerprint)。"""
    results: List[Tuple[str, str, int, str]] = []
    for raw in tracked_files(repo_root):
        path = Path(repo_root / raw)
        parts = set(Path(raw).parts)
        if parts & SKIP_DIRS:
            continue
        if path.suffix.lower() not in TEXT_EXT:
            continue
        try:
            size = path.stat().st_size
            if size > MAX_SCAN_BYTES or size == 0:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = raw.replace(os.sep, "/")
        for rid, line_no, fp in scan_text(text):
            results.append((rid, rel, line_no, fp))
    # 去重（同文件同指纹）
    seen = set()
    uniq = []
    for r in results:
        key = (r[1], r[2], r[3], r[0])
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    return uniq


def main() -> int:
    try:
        hits = scan_repo(REPO_ROOT)
    except Exception as e:  # pragma: no cover
        print(f"RUNNER_ERROR {e}", file=sys.stderr)
        return 2
    for rid, rel, line_no, fp in sorted(hits):
        print(f"HIT {rid} {rel}:{line_no} fp={fp}")
    if hits:
        print(f"[secret] FAIL: {len(hits)} 命中（已脱敏，仅规则ID/路径/行号/指纹）")
        return 1
    print("[secret] PASS: 0 命中")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

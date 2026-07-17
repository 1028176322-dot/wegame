"""run_validators.py — VALIDATE_COMMAND 入口（全量门禁）。

依次运行三个只读检查器，聚合退出码：
  - file_placement_validator
  - secret_validator
  - gate_validator

退出码：0=全部无 ERROR；1=任一 ERROR；2=运行器自身错误。
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATORS = [
    "file_placement_validator.py",
    "secret_validator.py",
    "gate_validator.py",
]


def main() -> int:
    rc = 0
    for name in VALIDATORS:
        script = REPO_ROOT / "tools" / "validators" / name
        print(f"--- running {name} ---")
        r = subprocess.run([sys.executable, str(script)], cwd=str(REPO_ROOT))
        if r.returncode != 0:
            rc = 1
    if rc == 0:
        print("[VALIDATE_COMMAND] PASS: 全部检查器 0 ERROR")
    else:
        print("[VALIDATE_COMMAND] FAIL: 存在 ERROR，详见上方输出")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())

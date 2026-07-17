#!/usr/bin/env python3
# tools/generators/csv_to_i18n.py  (DRAFT)
# 从 docs/design/i18n/text_config.csv 导出 data/i18n/<lang>.json
# 约定（i18n/README §2）：en/zh-TW 为空时运行时回退 zh-CN；id 不存在返回 id。
import csv, json
from pathlib import Path

SRC = Path("docs/design/i18n/text_config.csv")
OUT = Path("data/i18n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = SRC.read_text(encoding="utf-8")
    rows = list(csv.DictReader(text.splitlines()))
    zh = {r["id"]: r["zh-CN"] for r in rows}
    en = {r["id"]: r["en"] or "" for r in rows}        # 空串触发运行时回退
    tw = {r["id"]: r["zh-TW"] or "" for r in rows}
    for lang, d in (("zh-CN", zh), ("en", en), ("zh-TW", tw)):
        (OUT / f"{lang}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"[OK] i18n/{lang}.json: {len(d)} keys")


if __name__ == "__main__":
    main()

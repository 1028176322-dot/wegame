<!-- 编码: UTF-8 -->
# data/ — 双轨制数值真相源（current for data-config）

> 本目录是 AI 写功能代码时 `import` 的**唯一机器可读数值真相源**（轨道 B）。
> 源真相在 `docs/design/balance/*.md`（数值表）与 `docs/design/i18n/text_config.csv`（文本）。
> 本目录文件**为生成物，不得手编**；改源后跑 `tools/generators/md_to_config.py` 与 `csv_to_i18n.py` 重出。

## 结构
- `config/<module>.json`：结构化配置（combat_config / tower_config / enemy_config / status_effect_config / wave_config / economy_config / …）
- `schemas/<module>.schema.json`：同名配对 JSON Schema（draft-07，含 `x-param-map` 溯源注解）
- `i18n/<lang>.json`：`{id: text}`，en/zh-TW 空串→运行时回退 zh-CN

## 规范
- 宪法：`docs/design/SPEC_STANDARD.md`
- 单一事实源：JSON > balance MD > systems MD
- 运行时可达性：首个工程任务把 `data/config/*.json` 导出/软链到 `assets/resources/config/`

## 生成
```bash
python tools/generators/md_to_config.py     # balance/*.md -> data/config/*.json
python tools/generators/csv_to_i18n.py       # i18n/text_config.csv -> data/i18n/*.json
```

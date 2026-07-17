<!-- 编码: UTF-8 -->
# ADR-0003 — 双轨制数值真相源（MD 设计文档 + JSON 机器可读配置）

Status: accepted
Date: 2026-07-17
Owner: Decision Owner（用户本人）

## Context

所有系统策划案（GDD / systems/S*.md / balance/*.md / i18n）是 **AI 写功能代码**的输入，而非仅人读。现状为纯 Markdown 人读叙事，AI 消费时卡在 5 处：
1. `[PLACEHOLDER]` 死胡同（文档写占位符，初值在 balance 但没指向）；
2. 同参数多处定义无单一事实源（克制矩阵在 S05/S30/balance 各一份）；
3. 配置数据只有 MD 表格、无机器可读文件（AI 需 parse MD，脆弱）；
4. 缺「实现契约」小节（只有 mermaid 图，无输入/输出/接口/错误码契约）；
5. 冲突/待裁定无「当前实现口径」，AI 不敢落地。

Decision Owner 裁定采用**双轨制**（轨道 A 人读 MD + 轨道 B 机器可读 JSON），并全量改造 33 系统、一并清理命名/语义债。

## Decision

- **轨道 A — Markdown 设计文档**（人读 + 结构化索引）：讲 `why` / 边界 / 异常 / 设计决策 / 冲突与待裁定 / 实现契约；**终值不在此**，具体数值改为 `value_ref` 指针或 `NEEDS-DESIGN`。
- **轨道 B — 机器可读 JSON**（AI 写代码唯一数值真相源）：
  - `data/config/<module>.json`：结构化配置（combat_config / tower_config / enemy_config / status_effect_config / wave_config / economy_config / …）
  - `data/schemas/<module>.schema.json`：同名配对 JSON Schema（draft-07，含 `x-param-map` 溯源）
  - `data/i18n/<lang>.json`：`{id: text}`，en/zh-TW 空串→运行时回退 zh-CN
  - 数值参数层：`balance/<system>.json`（按 `param_id` 索引标量）+ schema
- `data/` 为**生成物，不得手编**；源在 `docs/design/balance/*.md` 与 `docs/design/i18n/text_config.csv`，由 `tools/generators/md_to_config.py` / `csv_to_i18n.py` 重出。
- **单一事实源**：JSON > balance MD > systems MD。每个 `param_id` 仅一个权威定义（轨道 B），MD 只引用不重定义。
- **命名统一 N1–N6**（主理人采纳，pending DO 终审）：电塔统一 `t_electric` 弃 `t_thunder`；腐蚀语义对齐 S33「护甲削减 cap5」；毒甲枚举 `poison→air` 弃 `combat_armor_poison`；`[PLACEHOLDER]` 统一 `value_ref`/`NEEDS-DESIGN`；`DamageType`/`ArmorType` 枚举全项目对齐 S30；`param_id` 前缀白名单（combat_/tower_/econ_/wave_/status_/attr_/meta_/lvl_）由 Schema 固化。

## Alternatives

- **轻量规范化（只改 MD）**：不新增 JSON，AI 直接解析 MD 表格——脆弱、易错，且 `[PLACEHOLDER]` 指向仍模糊。
- **机器优先（JSON 为主）**：最大可读性但设计意图（why/边界）弱，评审困难。

## Trade-offs

- 双轨制增加同步维护成本（MD 与 JSON 须同步），但彻底消除 AI 消费歧义与配置漂移。
- 生成物不得手编，改源重出——改错只在源，JSON 重生即一致。

## Consequences

- `AUTHORITY_INDEX.md`：data-config `unassessed` → `current`（指向 `data/README.md`）。
- `config/root_allowlist.json`：allowedDirectories 加 `data`。
- 新增 `docs/design/SPEC_STANDARD.md`（双轨制宪法）与 `docs/design/schema/combat_config.schema.json`（样例）+ `tools/generators/`（导出脚本）。
- 首个工程任务须把 `data/config/*.json` 导出/软链到 `assets/resources/config/`，并建立 `TEST_COMMAND` / `VALIDATE_COMMAND`（当前 NOT_IMPLEMENTED）。

## Migration

- 现有 `balance/*.md` 数值表为源，跑生成器导出 `data/config/*.json`；`systems/S*.md` 的 §3 数值改为 `value_ref` 指针。
- 冲突项（C-1/C-2/C-7 等）按 SPEC_STANDARD §4 三要素标注 `current_implementation`，AI 按此落地。

## Rollback/Exit

- `data/` 为生成物：删 `data/` + 回退 `root_allowlist` 的 `data` + data-config 改 `unassessed` 即可退出本 ADR，不影响 MD 源。

## Review Trigger

- 引擎升级 / 首个工程任务 / 配置结构大改 / 命名规则调整。

## Related Current Documents

- `data/README.md`（current: data-config）
- `docs/design/SPEC_STANDARD.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `PROJECT_RULES.md`

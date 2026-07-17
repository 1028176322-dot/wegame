<!-- 编码: UTF-8 -->
# ADR-0004 — 测试与质量基线（test-quality current）

> 状态：current（基线 v0.1，待 DO 终审）｜日期：2026-07-17｜Owner：Decision Owner
> 领域：test-quality｜关联：ENGINEERING_RULES §14/§17、tools/validators

## 上下文
项目进入工程化阶段，需为 test-quality 领域确立 current 入口。治理已要求
`TEST_COMMAND` / `VALIDATE_COMMAND` 落地（Phase 5，见 TASK-2026-0717-GOV）。

## 决策
- 以 `tools/validators/` 三件套（文件放置 / 秘密 / 门禁）作为**自动化门禁基线**：
  纯标准库 + 只读 `git ls-files`，返回明确退出码（0/1/2）。
- `TEST_COMMAND` = `python tools/validators/run_tests.py`（负向 fixture 自测，13 项）。
- `VALIDATE_COMMAND` = `python tools/validators/run_validators.py`（全量门禁，当前仓库 0 ERROR）。
- 命令定义集中存放 `config/commands.json`，避免散落。

## 后果
- 正面：核心治理规则有机器检查（成熟度 L2→L3）；进度状态可由机器源生成与校验。
- 负面 / 待定：当前仅为**治理门禁**，不等同于游戏功能测试（单元 / 集成 / 性能）。
  业务测试框架待引擎（Cocos Creator）接入后补充，届时扩展 `tests/` 并登记目录地图。

## 遵循
- 测试纪律（ENGINEERING_RULES §14.4）：占位命令不是 PASS；先失败后修复；不删失败测试。
- 状态词五值：PASS / FAIL / NOT_RUN / NOT_IMPLEMENTED / BLOCKED。
- 证据等级：门禁自测与全量检查均属 E3（自动测试）。

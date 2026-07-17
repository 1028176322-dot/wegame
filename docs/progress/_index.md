<!-- 编码: UTF-8 -->
# 进度总索引

> 依据方案 §7。状态取值见 `docs/governance/PROGRESS_RULES.md`。本索引由个体进度/任务生成或校验，不维护第二套状态。
> Baseline Date: 2026-07-17

## 治理落地进度

| 条目 | Status | Owner | Evidence | Last Verified |
|---|---|---|---|---|
| Phase 0 只读基线 | verified | Decision Owner | `docs/tasks/reports/PHASE0_BASELINE_REPORT.md` | 2026-07-17 |
| Phase 1 权威与入口 | verified | Decision Owner | `PROJECT_RULES.md`、`AUTHORITY_INDEX.md`、ADR-0001 | 2026-07-17 |
| Phase 2 任务与进度 | verified | Decision Owner | 本索引、`docs/tasks/templates/` | 2026-07-17 |
| Phase 3 多AI与恢复 | verified | Decision Owner | `docs/tasks/coordination/` | 2026-07-17 |
| Phase 4 记忆与Skill | verified | Decision Owner | `memory/`、`skills/` | 2026-07-17 |
| Phase 5 工程/安全/门禁 | verified | Decision Owner | 检查器 tools/validators 已实现；TEST/VALIDATE 命令落地（E3：13 项负向 fixture 自测 PASS + 当前仓库全量门禁 0 ERROR） | 2026-07-17 |
| Phase 6 终验与维护 | not_started | Decision Owner | — | — |

## 业务进度

| 条目 | Status | Owner | Block Reason | Unblock Condition |
|---|---|---|---|---|
| 游戏产品设计 | current | Decision Owner | — | 塔防玩法已裁定（ADR-0002 / GDD.md） |
| 技术架构/引擎选型 | current | Decision Owner | — | Cocos Creator 3.8.8 已裁定（TECH_ARCHITECTURE.md / D-03） |
| UX/内容资产 | current | Decision Owner | — | 基线规范已建（docs/design/UX_CONTENT_BASELINE.md / D-08） |
| 测试与质量 | current | Decision Owner | — | 测试框架基线已裁定（ADR-0004 / D-08） |

> 说明：Phase 5 检查器（tools/validators 下的文件放置/秘密/门禁检查）已于 TASK-2026-0717-GOV 实现，VALIDATE_COMMAND/TEST_COMMAND 落地（E3），Phase 5 = verified。业务进度段已与 `AUTHORITY_INDEX.md` 对齐：product-design / tech-architecture / ux-content-assets / test-quality 均为 current。

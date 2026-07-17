<!-- 编码: UTF-8 -->
# PROJECT_MANAGEMENT.md — 项目管理总纲（current）

> 本文件是本项目对《通用 AI 项目管理方案》的落地说明。方法论全文见 `通用AI项目管理方案.md`；本文件只记录本项目的裁剪决定与路由，不复制方法论正文。

## 采用规模

**Standard**（方案 §20.2）：启用全部核心章节 — 权威体系、任务生命周期、多AI协作、进度、记忆、Skill、工程门禁、验证门禁、发布回滚。

## 关键裁剪决定

1. 当前为 prototype 阶段；tech-architecture（Cocos Creator 3.8.8）与 platform-release（微信小游戏）已于 2026-07-17 裁定为 current（见 `AUTHORITY_INDEX.md`）。玩法/产品目标（product-design、gameplay-systems）仍为 `unassessed`，待 Decision Owner 裁定。
2. 单人 + AI 团队：Decision Owner 同时兼任 Release Owner / Integrator；AI 为 Executor。C3 变更须 Decision Owner 独立复核或书面接受风险（方案 §5.3）。
3. Git 已初始化，冻结锁使用 commit SHA 与文件 SHA-256 双轨。
4. 秘密、数据、删除、发布安全门不因规模或阶段降级（方案 §20.2）。

## 落地阶段（方案 §20）

| Phase | 状态 | 交付 |
|---|---|---|
| Phase 0 只读基线 | verified | `docs/tasks/reports/PHASE0_BASELINE_REPORT.md` |
| Phase 1 权威与入口 | verified | `PROJECT_RULES.md`、`AUTHORITY_INDEX.md`、ADR-0001 |
| Phase 2 任务与进度 | verified | `docs/progress/_index.md`、`docs/tasks/templates/` |
| Phase 3 多AI与上下文恢复 | verified | `docs/tasks/coordination/INDEX.md` 及模板 |
| Phase 4 记忆与Skill | verified | `memory/MEMORY_SCHEMA.md`、`skills/` 注册表 |
| Phase 5 工程/安全/门禁 | in_progress | 规则文件已建；检查器（tools/validators）待随首个工程任务实现 |
| Phase 6 终验与维护 | not_started | 待首批业务任务后执行 |

## 治理规则路由

- 文档管理：`DOCUMENT_RULES.md`（方案 §11）
- 进度管理：`PROGRESS_RULES.md`（方案 §7）
- 工程实现：`ENGINEERING_RULES.md`（方案 §14）
- 安全与Git：`SECURITY_RULES.md`（方案 §15、§16）

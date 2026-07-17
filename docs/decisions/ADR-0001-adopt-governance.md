<!-- 编码: UTF-8 -->
# ADR-0001 — 采用《通用 AI 项目管理方案》(Standard 规模) 治理 wegame 项目

Status: accepted
Date: 2026-07-17
Owner: Decision Owner（用户本人）

## Context

`D:\wegame` 为全新游戏开发项目，初始仅含方法论文档、无 Git、无源码。需要在动工前建立可复用的治理体系，避免后续出现范围漂移、多执行者冲突、伪造完成等问题。

## Decision

严格采用 `docs/governance/通用AI项目管理方案.md` 定义的方法论，规模选 **Standard**（方案 §20.2），启用全部核心章节。建立最小治理文件集（入口、权威索引、治理规则、任务/进度/协调、记忆、Skill 注册表、模板），并初始化 Git。

## Alternatives

- Lite 规模：文档少，但本项目为持续开发 + 人机混合，Lite 不足以覆盖多AI协作与工程门禁。
- 不采用治理：会重回 L0 Ad hoc，依赖聊天与个人记忆。

## Trade-offs

Standard 前期有一定治理成本，换取跨会话可恢复、多执行者不冲突、完成声明可复核。

## Consequences

- 根目录仅保留允许清单文件；方法论文档移入 `docs/governance/`（canonical）。
- 角色：Decision Owner=用户（兼 Release Owner/Integrator），Executor=AI。
- 多数产品/技术领域暂为 `unassessed`，随首个决策任务裁定。

## Migration

见 `docs/tasks/reports/PHASE0_BASELINE_REPORT.md` 与 `PROJECT_MANAGEMENT.md` 的 Phase 表。

## Rollback/Exit

治理骨架为独立提交，可整体回退；不涉及业务数据，可逆。

## Review Trigger

引擎/技术栈选型、发布模式变化、团队规模变化、重大事故后（方案 §22.4）。

## Related Current Documents

- `PROJECT_RULES.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/PROJECT_MANAGEMENT.md`

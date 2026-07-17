<!-- 编码: UTF-8 -->
# 工作区长期记忆（curated）— D:\wegame

> 本文件由 WorkBuddy 跨会话自动加载。本工作区受《通用AI项目管理方案》治理，任何项目管理动作必须先遵循以下指令。

## 治理模型（强制）
- 本工作区 `D:\wegame` 是**游戏开发**项目，采用《通用AI项目管理方案》**Standard 规模**治理。
- **唯一启动入口**：任何任务开始前先读 `D:\wegame\PROJECT_RULES.md`，再查 `docs/governance/AUTHORITY_INDEX.md`。
- **强制加载器**：进行任何项目管理/任务执行/记忆沉淀时，加载 `project-governance` Skill（位于 `.workbuddy/skills/project-governance/SKILL.md`；注册于 `skills/skill_registry.json`；安装锁 `skills/install_lock.json`）。
- 角色：用户 = Decision Owner（兼 Release Owner / Integrator）；AI = Executor。
- 规则 canonical 位置：`docs/governance/`；模板：`docs/tasks/templates/`；记忆规范：`memory/MEMORY_SCHEMA.md`。

## 核心约束（永远遵守）
1. 进度用七态（unassessed→verified），完成实施标 `verified`；`accepted` 仅 Decision Owner 可记。
2. 防伪造绿色：状态词只用 PASS/FAIL/NOT_RUN/NOT_IMPLEMENTED/BLOCKED；执行者不得自标 accepted。
3. 破坏性操作四步门：dry-run → hash 一致 → 引用 0 → 构建未引用 → 安全点。
4. 外部动作（提交 / 推送 / 发布 / 删除 / 装依赖）每次单独授权。
5. 单一事实源；并行只在不重叠文件范围；热文件（G0/G1）串行由 Integrator 处理。

## 未决裁决（Decision Owner 待定）
- 玩法/产品目标、主平台、引擎/技术栈、测试与门禁命令、发布模式 — 当前 `unassessed` / `NOT_IMPLEMENTED`。

## 远程
- origin = `git@github.com:1028176322-dot/wegame.git`（SSH）；`main` 已跟踪 `origin/main`。

## 参考
- 采用决策：`docs/decisions/ADR-0001-adopt-governance.md`
- 基线报告：`docs/tasks/reports/PHASE0_BASELINE_REPORT.md`

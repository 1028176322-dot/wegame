<!-- 编码: UTF-8 -->
# 工作区长期记忆（curated）— E:\wegame

> 本文件由 WorkBuddy 跨会话自动加载。本工作区受《通用AI项目管理方案》治理，任何项目管理动作必须先遵循以下指令。

## 治理模型（强制）
- 本工作区 `E:\wegame` 是**游戏开发**项目，采用《通用AI项目管理方案》**Standard 规模**治理。
- **唯一启动入口**：任何任务开始前先读 `E:\wegame\PROJECT_RULES.md`，再查 `docs/governance/AUTHORITY_INDEX.md`。
- **强制加载器**：进行任何项目管理/任务执行/记忆沉淀时，加载 `project-governance` Skill（位于 `.workbuddy/skills/project-governance/SKILL.md`；注册于 `skills/skill_registry.json`；安装锁 `skills/install_lock.json`）。
- 角色：用户 = Decision Owner（兼 Release Owner / Integrator）；AI = Executor。
- 规则 canonical 位置：`docs/governance/`；模板：`docs/tasks/templates/`；记忆规范：`memory/MEMORY_SCHEMA.md`。

## 核心约束（永远遵守）
1. 进度用七态（unassessed→verified），完成实施标 `verified`；`accepted` 仅 Decision Owner 可记。
2. 防伪造绿色：状态词只用 PASS/FAIL/NOT_RUN/NOT_IMPLEMENTED/BLOCKED；执行者不得自标 accepted。
3. 破坏性操作四步门：dry-run → hash 一致 → 引用 0 → 构建未引用 → 安全点。
4. 外部动作（提交 / 推送 / 发布 / 删除 / 装依赖）每次单独授权。
5. 单一事实源；并行只在不重叠文件范围；热文件（G0/G1）串行由 Integrator 处理。

## 执行纪律红线（Decision Owner 强制重申 2026-07-17）
- **所有操作必须严格按项目规则执行，不得因任务轻重而豁免治理流程。**
- 任何会产生文件改动/产出的任务（含看似简单的文档提取、清单生成），动手前必须完整走：① §21.16 启动合规回执（Task ID / Role / Risk / 已读规则 / 适用 current / NEW-MOD-VERIFY-DELETE 范围 / 禁止范围 / Baseline SHA / 多写者冲突 / 验证计划 / Git 计划 / 停止条件）→ ② 建正式任务卡 `docs/tasks/TASK-<ID>.md`（按 TASK_CARD 模板）→ ③ 建 Change List `docs/tasks/coordination/active/CL-<date>-<topic>.md`。
- 仅用会话内 TaskCreate 轻量跟踪即开干，视为**违规**（2026-07-17 美术清单任务 64305f7 因此被 DO 指出，已补建 TASK/CL 纠正）。
- 回溯补录的回执/任务卡/CL 须明确标注「事后补录」，不得伪造成事前执行。
- 外部动作（commit / push / 发布 / 删除 / 装依赖）每次单独授权；`accepted` 仅 DO 可记，Executor 不自标。

## 未决裁决（Decision Owner 待定）
- 玩法/产品目标、主平台、引擎/技术栈、测试与门禁命令、发布模式 — 当前 `unassessed` / `NOT_IMPLEMENTED`。

## 远程
- origin = `git@github.com:1028176322-dot/wegame.git`（SSH）；`main` 已跟踪 `origin/main`。

## 参考
- 采用决策：`docs/decisions/ADR-0001-adopt-governance.md`
- 基线报告：`docs/tasks/reports/PHASE0_BASELINE_REPORT.md`

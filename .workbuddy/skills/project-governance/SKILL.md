---
name: project-governance
description: 在 D:\wegame 工作区进行任何项目管理、任务执行、需求/变更/发布/验证/记忆沉淀时加载。强制遵循《通用AI项目管理方案》的生命周期、门禁与核心约束。
version: 1.0.0
scope: workspace
permissions:
  reads:
    - PROJECT_RULES.md
    - docs/governance/**
    - docs/tasks/templates/**
  writes:
    - docs/tasks/**
    - docs/progress/**
    - docs/decisions/**
    - memory/**
    - .workbuddy/memory/**
  exec: []
  network: []
  secrets: []
triggers:
  - 创建/修改任务卡、需求、变更、发布、验证、复盘
  - 任何会写入 D:\wegame 磁盘内容的实施动作之前
  - 用户提到"按方案""管理项目""任务卡""冻结""验证""发布"
  - 跨会话恢复、交接或沉淀项目记忆
source: docs/governance/通用AI项目管理方案.md
install_lock_ref: skills/install_lock.json
---

# 通用AI项目管理执行协议（project-governance）

本 Skill 是工作区 `D:\wegame` 的**强制治理加载器**。任何项目管理动作都先按本协议执行，详细规则以 `docs/governance/` 下文件为 canonical（单一事实源，不在此复制）。

## 0. 加载顺序（永远先读）
1. `D:\wegame\PROJECT_RULES.md` — 唯一启动入口。
2. `docs/governance/AUTHORITY_INDEX.md` — 确定本次要改写的权威文件与当前冻结 SHA。
3. 对应规则文件：`PROJECT_MANAGEMENT` / `DOCUMENT_RULES` / `PROGRESS_RULES` / `ENGINEERING_RULES` / `SECURITY_RULES`。

## 1. 强制任务生命周期（方案 §8）
1. **任务卡**：新工作用 `docs/tasks/templates/TASK_CARD.md` 在 `docs/tasks/coordination/active/` 建卡（owner / priority / risk / 依赖 / 文件范围）。
2. **影响分析**：列出将读写的文件范围（Impact Map），确认与 `coordination/INDEX.md` 中现有任务**文件范围不重叠**。
3. **冻结**：记录涉及权威文件的当前 commit SHA（或文件 SHA-256）作为冻结锁。
4. **冲突检查**：确认无并发 Writer 写同一文件（热文件 G0/G1 只能由 Integrator 串行）。
5. **执行**：仅改分配到的文件范围；同一文件同一时刻一个 Writer。
6. **验证与证据**：按 `ENGINEERING_RULES.md` 与方案 §17 门禁产出证据，状态词只能用 `PASS / FAIL / NOT_RUN / NOT_IMPLEMENTED / BLOCKED`。
7. **进度**：完成实施标 `verified`（**不是**"完成"）；`accepted` 只能由 Decision Owner 记录，执行者不得自标。
8. **交接/记忆**：跨会话写 `HANDOFF.md` / `CHECKPOINT.json`；任务结束按 `memory/MEMORY_SCHEMA.md` 提交 `inbox/` 补丁，由 Curator 合并。

## 2. 核心约束（永远遵守）
- **单一事实源**：规则以 `docs/governance/` 为 canonical，禁止在多处维护可写副本。
- **防伪造绿色**：`NOT_RUN` / `NOT_IMPLEMENTED` 不得写成 `PASS`；执行者不得自行标 `accepted`。
- **破坏性操作四步门**（方案 §16）：删除/移动/重命名默认 `dry-run` → 目标 hash 一致 → 引用为 0 → 构建未引用 → 建立安全点。
- **外部动作独立授权**：提交、推送、发布、删除、安装依赖、外部写入，每次单独授权，不因"已采用方案"而默认授权。
- **并行隔离**：并行只发生在不重叠文件范围；集成（热文件 G0/G1）始终串行。
- **文件放置**：遵循 `config/file_placement_rules.json` 与根目录允许清单。

## 3. 引用清单
- 入口：`D:\wegame\PROJECT_RULES.md`
- 权威索引：`docs/governance/AUTHORITY_INDEX.md`
- 规则集：`docs/governance/{PROJECT_MANAGEMENT,DOCUMENT_RULES,PROGRESS_RULES,ENGINEERING_RULES,SECURITY_RULES}.md`
- 模板：`docs/tasks/templates/*`
- 记忆规范：`memory/MEMORY_SCHEMA.md`
- 采用决策：`docs/decisions/ADR-0001-adopt-governance.md`

## 4. 安全降级（方案 §13.8）
- 若本文件内容 hash 与 `skills/install_lock.json` 记录不一致 → 标 `quarantined`，停止调用并报 Curator。
- 用户要求偏离上述核心约束时，先提示风险，不擅自绕过；确需偏离须 Decision Owner 显式裁决并记 ADR。

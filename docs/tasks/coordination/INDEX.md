<!-- 编码: UTF-8 -->
# 协调控制面索引

> 依据方案 §10。多AI/多执行者协作的唯一协调入口。

## 目录职责

| 目录 | 内容 |
|---|---|
| `active/` | `TASK_<ID>.json` 活动任务声明（owner/role/status/claimedFiles/plannedNewFiles/lease…） |
| `baselines/` | `BASELINE_<ID>.json` 执行前 SHA 基线 |
| `checkpoints/` | `CHECKPOINT_<ID>.json` 强制检查点 |
| `handoffs/` | `HANDOFF_<ID>.md` 交接/恢复入口 |
| `findings/` | `REVIEW_<ID>.md` 独立审查结论 |

## 文件分级（方案 §10.4）

| 等级 | 示例 | 写权限 |
|---|---|---|
| G0 | PROJECT_RULES、AUTHORITY_INDEX、进度总索引、发布政策 | Decision Owner/Integrator 串行 |
| G1 | 构建入口、依赖锁、共享 schema、注册表、CI | Integrator 或独立 C3 任务 |
| G2 | 单模块源码、测试、局部文档 | 不重叠时可并行 |
| G3 | 带任务ID的报告、checkpoint、handoff | 对应任务独占 |

## 当前活动任务

无。（治理初始化任务由主对话执行，未走多AI租约。）

## 并行/集成规则要点

- 同一文件同一时间只能一个 Writer；热文件（G0/G1）只能由 Integrator 串行修改。
- 租约超时不自动抢占；集成前须来源任务 ready + handoff 完整 + P0/P1 审查关闭。

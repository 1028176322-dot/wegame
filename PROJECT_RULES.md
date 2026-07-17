<!-- 编码: UTF-8 -->
# PROJECT_RULES.md — 项目唯一启动入口

> 本文件是所有执行者（人工 / 单AI / 多AI）的唯一启动入口。
> 任何人在动手前，必须先完整读取本文件，并按其路由到权威索引与任务系统。
> 方法论全文见 `docs/governance/通用AI项目管理方案.md`（canonical，勿在根目录另建副本）。

## 1. 项目初始化变量（方案 §1）

| 变量 | 值 | 说明 |
|---|---|---|
| `PROJECT_NAME` | wegame | 游戏开发项目（名称可由 Decision Owner 更新） |
| `REPO_ROOT` | `.` | 文档中只使用相对路径 |
| `PRIMARY_PRODUCT_ROOT` | `unassessed` | 游戏引擎/源码结构未定，待首个工程任务确定 |
| `DEFAULT_BRANCH` | `main` | |
| `PRIMARY_PLATFORM` | `unassessed` | PC / 主机 / 移动待裁定 |
| `PACKAGE_MANAGER` | `unassessed` | 依赖引擎/技术栈选型 |
| `TEST_COMMAND` | `NOT_IMPLEMENTED` | 尚无测试入口 |
| `VALIDATE_COMMAND` | `NOT_IMPLEMENTED` | 尚无全量门禁入口 |
| `RELEASE_OWNER` | Decision Owner（用户本人） | |
| `INTEGRATOR` | Decision Owner（用户本人） | 当前唯一集成者 |

## 2. 项目画像（方案 §1.2）

| 维度 | 值 |
|---|---|
| 生命周期 | prototype |
| 数据敏感度 | internal |
| 发布模式 | manual（应用商店/受监管发布：unassessed） |
| 运行环境 | unassessed |
| 团队模式 | human-AI |
| 可逆性 | fully-reversible（原型阶段） |
| 采用规模 | **Standard**（方案 §20.2） |

## 3. 角色归属（方案 §5）

| 角色 | 承担者 |
|---|---|
| Decision Owner | 用户本人（业务取舍、范围、最终验收） |
| Release Owner | 用户本人 |
| Integrator | 用户本人（串行集成热文件 G0/G1） |
| Executor | AI 助手（在冻结范围内实施与局部验证） |
| Reviewer | 高风险变更需独立主体；单人时 C3 须用户书面接受风险（方案 §5.3） |

> 约束：同一高风险变更的 Executor 与独立 Reviewer 不得为同一主体。C3 默认等待 Decision Owner 复核或书面风险接受。

## 4. 启动 / 恢复合规回执（方案 §21.16）

任何执行者开始工作前，必须先输出启动或恢复合规回执，无停止条件时才执行下一条唯一动作，不得扩大范围。最简启动语见方案 §21.4。

## 5. 权威路由

- 领域权威索引：`docs/governance/AUTHORITY_INDEX.md`
- 方法论全文：`docs/governance/通用AI项目管理方案.md`
- 治理规则：`docs/governance/`（文档/进度/工程/安全规则）
- 任务系统：`docs/tasks/`（模板见 `docs/tasks/templates/`，协调见 `docs/tasks/coordination/`）
- 进度总索引：`docs/progress/_index.md`
- 项目记忆：`memory/`（活动根，唯一）
- Skill 注册表：`skills/skill_registry.json`

## 6. 硬性底线（方案 §2、§16、§17）

1. 对话不是任务事实源；磁盘文件 + SHA + 证据才是。
2. 写入前冻结目标文件、动作、SHA、验收条件；SHA 漂移即停止。
3. 同一文件同一时间只能有一个 Writer；热文件（G0/G1）只能由 Integrator 串行处理。
4. 删除 / 移动 / 重命名 / 历史重写默认 dry-run，且需单独授权（方案 §16.1 四步门）。
5. `NOT_RUN` / `NOT_IMPLEMENTED` 不得写成 `PASS`；执行者不得自标 `accepted`。
6. 秘密只来自安全凭据/环境变量；扫描输出必须脱敏。
7. 未经授权不 commit / push / force-push / 重写历史。

## 7. 本方案自身也受约束

修改治理文件或方法论文档，需按方案 §22.4 建立独立 Change List 与版本锁，不得在业务任务中顺手降低治理要求。

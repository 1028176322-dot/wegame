<!-- 编码: UTF-8 -->
# ADR-0002 — D-01 玩法裁定：塔防，参考《绿色循环圈》

Status: accepted
Date: 2026-07-17
Owner: Decision Owner（用户本人）

## Context

项目基础变量已裁定（微信小游戏 / Cocos Creator 3.8.8 / 手动发布，见 `CL-2026-0717-authority.md`）。D-01（玩法/产品目标）原为 `unassessed`。Decision Owner 现裁定核心玩法方向，使 `product-design` 与 `gameplay-systems` 两领域可进入 current。

## Decision

- **D-01 = 塔防（Tower Defense）**，核心参考《绿色循环圈》（War3 经典循环路径 TD）。
- 关键移植要素：环形路径、金/木双货币经济循环、单塔深度养成（"养塔"）、护甲克制多塔种、漏怪扣 Lives。
- 平台适配：微信小游戏触屏单指操作、3–5 分钟短局、跨局元进度 + 异步排行榜。
- 权威设计文档：`docs/design/GDD.md`（v0.1-draft），同时为 `product-design` 与 `gameplay-systems` 的 current 入口。

## Alternatives

- 放置/自走棋/弹幕：与"循环圈"参考不匹配，且塔防最贴合 Decision Owner 给出的参照。
- 纯直线 TD：放弃"循环"带来的多圈累计伤害与养成塔价值，削弱参考作精髓。

## Trade-offs

- 保留经济循环与养成（策略深度），牺牲 PC 端微操与多人实时合作（换零门槛与短局）。
- 塔种精简到 7 类，控首局复杂度，但可能损失硬核深度（后续可经元进度解锁补回）。

## Consequences

- `AUTHORITY_INDEX.md`：product-design、gameplay-systems 由 unassessed → current（指向 GDD）。
- 冻结锁追加 `docs/design/GDD.md` SHA。
- 后续首个工程任务须打通 `TEST_COMMAND`（Cocos 测试 / 微信开发者工具）并建立 `tools/validators`（Phase 5）。

## Migration

无（首版设计，无历史玩法需迁移）。

## Rollback/Exit

GDD 为独立文档；若玩法方向推翻，改 ADR 状态为 superseded 并新建 ADR，索引改指新文档。

## Review Trigger

首局试玩后、塔种数量调整、元进度资源模型变化、微信平台合规要求变化。

## Related Current Documents

- `docs/design/GDD.md`（current: product-design / gameplay-systems）
- `docs/governance/AUTHORITY_INDEX.md`
- `PROJECT_RULES.md`

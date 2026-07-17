# 系统策划案索引 (System Design Docs Index)

> 本目录为《塔防微信小游戏》**每个独立系统的策划案**，每份含 4 个强制章节：
> 1. 系统 UI 布局 · 2. 逻辑功能 · 3. 配置表设计 · 4. 美术资源需求
> 状态：v0.2-detailed（全部未提交） · 日期：2026-07-17
> 加深维度：功能逻辑全面 + 状态机/流程图 + 像素级 UI 线框 + 完整异常边界 + 分辨率自适应
> 关联：`SYSTEM_BREAKDOWN.md`（系统划分） · `GDD.md` · `FEATURE_SCOPE.md`
> v0.2 新增 S30–S33（属性/敌人/关卡配置/状态）四系统，补齐战斗基础配置+美术盲区。

---

## A 域 · 核心战斗域（MVP / P0–P1）

| 系统 | 文件 | 关联 F | 层级 |
|------|------|--------|------|
| S1 地图系统 | [S01_map.md](./S01_map.md) | F1 | MVP/P0 |
| S2 建筑（塔）系统 | [S02_building_tower.md](./S02_building_tower.md) | F2 F3 F4 | MVP/P0 |
| S3 经济系统 | [S03_economy.md](./S03_economy.md) | F5 | MVP/P0 |
| S4 波次系统 | [S04_wave.md](./S04_wave.md) | F6 | MVP/P0 |
| S5 战斗系统 | [S05_combat.md](./S05_combat.md) | F7 | MVP/P0 |
| S30 属性系统 | [S30_attribute.md](./S30_attribute.md) | （战斗基础） | MVP/P0 |
| S31 敌人系统 | [S31_enemy.md](./S31_enemy.md) | F6（敌人半边） | MVP/P0 |
| S32 关卡配置系统 | [S32_stage_config.md](./S32_stage_config.md) | F17（内容层） | MVP/P1 |
| S33 状态效果系统 | [S33_status_effect.md](./S33_status_effect.md) | F7（状态半边） | MVP/P0 |
| S28 技能系统 | [S28_skill_system.md](./S28_skill_system.md) | F4 F7 | MVP/P0 |
| S6 漏怪 / 生命系统 | [S06_leak_lives.md](./S06_leak_lives.md) | F8 | MVP/P0 |
| S7 HUD / 操控系统 | [S07_hud.md](./S07_hud.md) | F9 | MVP/P1 |
| S8 结算系统 | [S08_settlement.md](./S08_settlement.md) | F12 | MVP/P1 |

## B 域 · 元进度社交域（增强 / P2，S9/S10 为 MVP）

| 系统 | 文件 | 关联 F | 层级 |
|------|------|--------|------|
| S9 新手引导系统 | [S09_onboarding.md](./S09_onboarding.md) | F10 | MVP/P1 |
| S10 大厅系统 | [S10_hub.md](./S10_hub.md) | （导航） | MVP/P1 |
| S11 解锁 / 元进度系统 | [S11_meta_progression.md](./S11_meta_progression.md) | F13 F16 | 增强/P2 |
| S29 玩家等级系统 | [S29_level_system.md](./S29_level_system.md) | F45 | 增强/P2 |
| S12 签到系统 | [S12_checkin.md](./S12_checkin.md) | F14 | 增强/P2 |
| S13 排行榜系统 | [S13_leaderboard.md](./S13_leaderboard.md) | F15 | 增强/P2 |
| S14 关卡系统 | [S14_level.md](./S14_level.md) | F17 | 增强/P2 |
| S15 成就系统 | [S15_achievement.md](./S15_achievement.md) | F37 | 增强/P2 |
| S16 图鉴系统 | [S16_codex.md](./S16_codex.md) | F38 | 增强/P2 |
| S17 赛季系统 | [S17_season.md](./S17_season.md) | F21 | 探索/P3 |

## C 域 · 平台工程运营域

| 系统 | 文件 | 关联 F | 层级 |
|------|------|--------|------|
| S18 存档系统 | [S18_save.md](./S18_save.md) | F11 F32 | MVP/P1 |
| S19 分包 / 资源加载系统 | [S19_asset_subpackage.md](./S19_asset_subpackage.md) | F30 F34 F35 | MVP/P1 |
| S20 生命周期系统 | [S20_lifecycle.md](./S20_lifecycle.md) | F31 | MVP/P1 |
| S21 远程配置系统 | [S21_remote_config.md](./S21_remote_config.md) | F33 | 增强/P2 |
| S22 设置系统 | [S22_settings.md](./S22_settings.md) | F39 | MVP/P1 |
| S23 音频系统 | [S23_audio.md](./S23_audio.md) | F18 F35 | 增强/P2 |
| S24 防作弊系统 | [S24_anticheat.md](./S24_anticheat.md) | F43 | 增强/P2 |
| S25 数据分析系统 | [S25_analytics.md](./S25_analytics.md) | F26 F44 | 增强/P2 |
| S26 变现系统 | [S26_monetization.md](./S26_monetization.md) | F19 | 探索/P3 |
| S27 客服反馈系统 | [S27_feedback.md](./S27_feedback.md) | F41 | 增强/P2 |

---

## 配置表命名速查

| 配置表 | 系统 | 用途 |
|--------|------|------|
| map_config | S1 | 地图/路径/塔位 |
| tower_config / upgrade_config | S2 | 塔属性/升级 |
| economy_config | S3 | 双币/汇率/通胀 |
| wave_config | S4 | 波次/怪物 |
| combat_config | S5 | 克制/状态/弹道 |
| attribute_def / damage_armor_matrix / attr_composition | S30 | 属性架构/克制矩阵（唯一权威） |
| enemy_config / enemy_drop | S31 | 敌人实体/掉木（唯一权威） |
| stage_config | S32 | 关卡内容数据（唯一权威） |
| status_effect_config | S33 | 状态枚举/堆叠（唯一权威） |
| skill_config | S28 | 技能(主动/被动/CD/cost/解锁) |
| lives_config | S6 | 生命/漏怪 |
| hud_config | S7 | HUD 布局 |
| settlement_config | S8 | 结算产出 |
| tutorial_script | S9 | 引导剧本 |
| hub_config | S10 | 大厅入口 |
| meta_config | S11 | 元进度节点 |
| player_level_config | S29 | 玩家等级→加成(不累加) |
| unlock_config | S29 | 等级→功能解锁 |
| checkin_config | S12 | 签到奖励 |
| leaderboard_config | S13 | 榜单维度 |
| level_config | S14 | 关卡/解锁 |
| achievement_config | S15 | 成就条件 |
| codex_view_config | S16 | 图鉴展示 |
| season_config | S17 | 赛季周期 |
| save_schema | S18 | 存档结构 |
| subpackage_config | S19 | 分包规划 |
| lifecycle_config | S20 | 生命周期 |
| remote_config | S21 | 远端键值 |
| settings_config | S22 | 设置项 |
| audio_config | S23 | 音频/打击感 |
| anticheat_config | S24 | 防作弊阈值 |
| analytics_config | S25 | 埋点/阈值 |
| monetize_config | S26 | 变现开关/奖励 |
| feedback_config | S27 | 反馈表单 |

> 各表字段、类型、范围、默认值、说明与格式示例见对应系统文档 §3。
> 数值均为 `[PLACEHOLDER]` 或初值假设，需纸面模拟/playtest 后由 S21 热更调。

---

## v0.2 加深汇总（2026-07-17）

> **v0.2-rev（耦合重构，2026-07-17）**：按 DO 裁定新规统一落地——新增 **S28 技能系统**（每塔种 1 主动+2 被动）；木改 **session 货币**（仅怪掉 S04 + 受限应急兑换 S03，不持久化）；**移除木房、换新风种「风塔」(DO 已确认定稿)**；主动技手动+自动(S22 `auto_cast_active`)；S01/S02/S03/S04/S05/S18/S22 及 GDD/SYSTEM_BREAKDOWN/FEATURE_SCOPE 同步修订。全部数值 `[PLACEHOLDER]`。

- 由 3 个 `design-strategist` 并行加深（A: S1–S8 / B: S9–S17 / C: S18–S27），文件范围不重叠。
- 达成：每文档含 ①像素级 UI 线框(750×1334)+分辨率自适应 ②状态机+时序图+模块表+异常边界用例表 ③完整配置表字段 ④美术规格(帧数/分辨率/格式/切片)。
- 待 Decision Owner 裁定项：见各文档标注 + 下方「待裁定冲突」。
  - **C-1 通胀指标口径**：GDD §6 写"木头/活跃玩家/日"，SYSTEM_BREAKDOWN §S3/§S25 写"币/人/日"——以 GDD 为准统一。
  - **A-1 GDD §5.8 缺失**：S05/SYSTEM_BREAKDOWN/FEATURE_SCOPE 引用"GDD §5.8 战斗/状态"，但 GDD 只到 §5.7——需补 §5.8 或更正引用。
  - **B-2 S11↔S14 循环依赖**：SYSTEM_BREAKDOWN 描述循环，建议解耦（关卡解锁走 S14/S18，元进度走 S11）。
  - **NEW-1 新风种（风塔）已裁定（DO 确认）**：命名/定位/技能数值（击退控制）定稿，替换原木房；「待 DO 确认」标注已在 S02/S28/GDD §5.6/§5.8/SYSTEM_BREAKDOWN/FEATURE_SCOPE 全移除。见 S02/S28/GDD §5.6/§5.8。
  - **NEW-2 残留守档不一致（本轮已清理，2026-07-17）**：旧引用已回填——`GAME_FLOW.md`(木房→风塔、换木→应急兑换)、`S09_onboarding.md`(木房→风塔 / btn_exchange→应急兑换 / 木源统一怪掉)、`S16_codex.md`(t_wood→t_wind)、`S21_remote_config.md`(删除 orphan `wood_per_sec_base`)。
  - **NEW-3 A-1 已消解**：原"GDD §5.8 战斗/状态"所指 combat/status 现归属 S05；本重构新增 **§5.8 技能系统**，引用冲突据此消解。
  - **NEW-4 C-1 已统一**：通胀指标在 GDD §6 / S03 / SYSTEM_BREAKDOWN 均改为"木(session)产出/活跃玩家/日"。
  - **本轮回填（2026-07-17）：风塔定稿 + 守档清理**：①风塔/t_wind「待 DO 确认」标注已在 GDD/SYSTEM_BREAKDOWN/FEATURE_SCOPE/S02/S28 全移除（DO 已确认定稿）；②NEW-2 旧引用清理完成（GAME_FLOW 木房→风塔/换木→应急兑换、S09 木房→风塔 + btn_exchange→应急兑换 + 木源统一怪掉、S16 t_wood→t_wind、S21 删除 orphan `wood_per_sec_base`）；③术语统一「换木」→「应急兑换」已在 SYSTEM_BREAKDOWN(S3/S7/S9/S25/S26) 与 GAME_FLOW/S25_analytics 落地（机制保留，仅改词）。
  - **NEW-5 新增 S29 玩家等级系统（2026-07-17）**：玩家等级 = 跨局元进度（S18）；功能解锁统一由等级驱动（S11 原资源解锁树改为 `unlock_config.required_level` 门槛，资源货币 TBD）；每级提供全局塔基础属性增益（dmg/range/atk_speed 绝对值快照，**不累加**）；XP 来自 S08 结算。新建 `S29_level_system.md`（v0.2-detailed，四章齐全），并联动 GDD §5.9 / SYSTEM_BREAKDOWN(S29 小节 + 依赖矩阵) / S11(等级门槛) / S08(XP 产出) / S02+S05(战斗加成不累加) / FEATURE_SCOPE(F45) / systems_index。数值全 `[PLACEHOLDER]`。遗留：S18 `save_schema` 需补 `player_level`/`current_xp` 字段（不在本次交付清单，列为必跟）；S11 `meta_upgrade` 节点建议改主题为经济/容错类以免与 S29 加成双重计算。
- 治理提示：B agent 曾直接向 A/C agent 发协调消息（成员间直连），违反治理铁律，已确认无文件冲突；后续成员互通须经主理人中转。

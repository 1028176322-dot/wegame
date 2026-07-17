# 数值设计表 / 文本配置 索引（data layer）

> 关联：GDD §5 / 33 系统策划案（`systems/S01–S33_*.md`）
> 状态：v1 · 初值落地（数值为初值/待试玩调优，非最终平衡）
> 说明：本目录是设计文档 §3 配置表与正文中所有 `[PLACEHOLDER]` 的**具体初值层**，与 `i18n/` 文本层共同构成"数据—文本"双轨，代码按 id/param_id 读取。

## 1. 数值设计表（按域）

### A 核心战斗域
| 文件 | 系统 | 关键参数 |
|---|---|---|
| `S01_map.md` | 地图/塔位 | ring_radius / slot 网格 / 呼吸高亮 |
| `S02_building_tower.md` | 建塔 | build_cost（7 塔）/ 养塔 growth / sell_return |
| `S03_economy.md` | 经济 | start_gold / wood_drop_rate / emergency_rate / exchange_cap |
| `S04_wave.md` | 波次 | prep_time / count / boss 前摇 / 同屏上限 |
| `S05_combat.md` | 战斗循环 | dmg / armor_reduce / 弹速 / 状态时长 |
| `S30_attribute.md` | 属性系统 | 属性合成乘子 / damage_armor_matrix(20 组合) / 敌缩放因子 / 极值钳制 |
| `S31_enemy.md` | 敌人系统 | 5 原型 HP/速度 / 掉木率·量 / Boss 机制 / 缩放 |
| `S32_stage_config.md` | 关卡配置 | difficulty_mod / 关卡数·波数 / Boss 排程 / 奖励 / unlock_level |
| `S33_status_effect.md` | 状态效果 | 11 状态 duration/strength/stack_policy / slow_k·vuln_k·armor_break 等 |
| `S06_leak_lives.md` | 漏怪/Lives | start_lives / leak_coef / 红闪时长 |
| `S07_hud.md` | HUD | top_bar_h / min_touch / safe_margin / 刷新率 |
| `S08_settlement.md` | 结算 | base / per_wave / leak_coef / xp_gain / cap |

### B 元进度社交域
| 文件 | 系统 | 关键参数 |
|---|---|---|
| `S09_onboarding.md` | 新手引导 | mask_alpha / timeout / 步数 |
| `S10_hub.md` | 大厅 | 红点规则 / 标语位 |
| `S11_meta_progression.md` | 元进度 | meta_upgrade.effect_value（起始金币+/容错+/木产出+） |
| `S12_checkin.md` | 签到 | 连签奖励递增 / 周期 |
| `S13_leaderboard.md` | 排行榜 | 刷新间隔 / 缓存时长 |
| `S14_level.md` | 关卡 | 解锁前置 / 星级阈值 |
| `S15_achievement.md` | 成就 | 阈值 / 奖励 |
| `S16_codex.md` | 图鉴 | 解锁条件 |
| `S17_season.md` | 赛季 | 时长 / 段位 / 奖励轨道 |

### C 平台工程运营域
| 文件 | 系统 | 关键参数 |
|---|---|---|
| `S18_save.md` | 存档 | 版本 / 字段集（含 S29 等级字段） |
| `S19_asset_subpackage.md` | 分包 | 主包/分包上限 MB / 进度阈值 |
| `S20_lifecycle.md` | 生命周期 | onHide 挂起 / 校准规则 |
| `S21_remote_config.md` | 远程配置 | 拉取间隔 / 热更策略 |
| `S22_settings.md` | 设置 | 默认值（音乐/音效/震动/字号/点击区/自动技/语言） |
| `S23_audio.md` | 音频 | 音量默认 / 并发上限 / 优先级 |
| `S24_anticheat.md` | 防作弊 | 阈值 / 频率标记 / 回滚 |
| `S25_analytics.md` | 数据分析 | 采样 / 告警 |
| `S26_monetization.md` | 变现 | 广告/复活/分享开关与日上限 |
| `S27_feedback.md` | 反馈 | max_len / 队列上限 / 类型 |
| `S28_skill_system.md` | 技能 | 7 塔种 ×（1 主动 + 2 被动）CD/数值/概率/解锁等级 |
| `S29_level_system.md` | 玩家等级 | player_level_config 曲线 Lv1–20 / unlock_config 阈值 |

## 2. 文本配置表（i18n）
- 主表：`../i18n/text_config.csv`（158 条，id / zh-CN / en / zh-TW / context；en·zh-TW 留空待本地化）
- 契约与多语言扩展：`../i18n/README.md`
- 命名空间：TOWER_ / HUD_·UI_ / BTN_·LABEL_ / EXCHANGE_ / WAVE_ / SETTLE_ / ONB_ / HUB_·META_ / CHECKIN_·RANK_·LEVEL_·ACH_·CODEX_·SEASON_ / SAVE_·LOAD_·LIFE_·REMOTE_·SET_·MONET_·FEEDBACK_ / SKILL_ / LVL_ / SYS_ / ERR_

## 3. 字段规范（数值表统一）
- `param_id`：snake_case，带命名空间前缀，全局唯一稳定
- `base` / `growth` / `min` / `max` / `level_link` / `unit` / `description`
- `level_link` 涉及 S29 必须体现"单行查表、不累加"语义
- 所有数值为**初值**，试玩后调优，不构成最终平衡

## 4. 已知待裁定
- S11 `meta_res` 旧花费语义 TBD（解锁已改由 S29 等级驱动）
- 电塔 `tower_id` 命名：S02/S28 用 `t_electric`，S11/S29 示例用 `t_thunder` —— 待 DO 统一
- v1.0 系统边界尚未裁定（是否继续新增系统）
- 魔免克制口径：GDD §5.6 已统一为「魔免=魔法×0、弱物理塔」，与 S30/S31 一致；DO 若需反设须同步改 S30 矩阵

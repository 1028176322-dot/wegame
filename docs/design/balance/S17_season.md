# 数值设计表：S17 赛季

> 关联 F 码：F21 · GDD：—（SYSTEM_BREAKDOWN §S17）· 设计文档：systems/S17_season.md
> 说明：本表为该系统设计文档 §3 配置表（season_config / season_progress）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。
> 门控：依赖 S11/S13/S15 稳定后做，本期 enabled=false（入口隐藏）。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 season_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.xxx_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天 / 分）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| season_score_cap | (clamp, §2.4 E09) | 99999 | - | 0 | 999999 | 无 | 分 | 赛季积分上限钳制（§2.4 E09 `积分上限 [PLACEHOLDER]`）。防溢出；28 天 × max_per_day(200)≈5600 远在下界内，上限留足余量 |
| season_score_per_wave | season_config(score_rule.per_wave) | 10 | - | 0 | 1000 | 无 | 分/波 | 每撑过 1 波得 10 分（§3.1 JSON score_rule.per_wave [PLACEHOLDER]）。基础贡献，驱动「多打几波」 |
| season_score_win | season_config(score_rule.win) | 50 | - | 0 | 1000 | 无 | 分/胜 | 通关额外 +50 分（§3.1 JSON score_rule.win [PLACEHOLDER]） |
| season_score_max_per_day | season_config(score_rule.max_per_day) | 200 | - | 0 | 2000 | 无 | 分/天 | 每日积分获取上限（§3.1 JSON score_rule.max_per_day [PLACEHOLDER]）。防单日爆肝刷分破坏赛季节奏 |
| season_tier1_score_need | season_config(reward_track.T1) | 200 | - | 0 | 99999 | 无 | 分 | T1 段位门槛 200 分（§3.1 JSON tier1.score_need [PLACEHOLDER]）。低门槛即时奖，促活跃 |
| season_tier1_reward | season_config(reward_track.T1) | 50 | - | 0 | 9999 | 无 | meta_res | T1 奖励 50 meta_res（§3.1 JSON tier1.reward [PLACEHOLDER]） |
| season_tier5_score_need | season_config(reward_track.T5) | 1000 | - | 0 | 99999 | 无 | 分 | T5 段位门槛 1000 分（§3.1 JSON tier5.score_need [PLACEHOLDER]）。中期里程碑 |
| season_tier5_reward | season_config(reward_track.T5) | 200 | - | 0 | 9999 | 无 | meta_res | T5 奖励 200 meta_res（§3.1 JSON tier5.reward [PLACEHOLDER]） |
| season_tier8_score_need | season_config(reward_track.T8) | 2000 | - | 0 | 99999 | 无 | 分 | T8 段位门槛 2000 分（§3.1 JSON tier8.score_need [PLACEHOLDER]）。高阶，28 天内可达成 |
| season_tier8_reward | season_config(reward_track.T8) | 500 | - | 0 | 9999 | 无 | meta_res | T8 奖励 500 meta_res（§3.1 JSON tier8.reward [PLACEHOLDER]）。赛季顶档奖励 |

## 备注 / 待裁定
- 积分曲线校验：单日上限 200 分 → 28 天理论最大 ≈5600 分；T8 门槛 2000 分（≈10 天满勤或 20 天常规）可达，T1(200) 约 1–2 天可达，节奏合理。
- §3.1 其余字段：`remind_days=3`、`board_id="season_best"`、`theme_asset="season_s01"` 已给具体值；`start_time/end_time` 为日期（非数值 [PLACEHOLDER]）；`enabled=false`（门控），均未列。
- 奖励币种接 S11 `meta_res`（与签到/成就同源，非局内货币），避免经济失衡。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

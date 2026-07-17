# 数值设计表：S12 签到

> 关联 F 码：F14 · GDD：—（SYSTEM_BREAKDOWN §S12）· 设计文档：systems/S12_checkin.md
> 说明：本表为该系统设计文档 §3 配置表（checkin_config / checkin_reward_detail）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 chk_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.xxx_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| chk_day1_reward | checkin_reward_detail(D1) | 10 | - | 0 | 9999 | 无 | meta_res | 第 1 日签到元资源（§3.2 CSV D1 [PLACEHOLDER]）。低门槛日奖，培养首日回归习惯 |
| chk_day2_reward | checkin_reward_detail(D2) | 15 | - | 0 | 9999 | 无 | meta_res | 第 2 日（§3.2 CSV D2 [PLACEHOLDER]）。连签递增 +5 |
| chk_day3_reward | checkin_reward_detail(D3) | 20 | - | 0 | 9999 | 无 | meta_res | 第 3 日（§3.2 CSV D3 [PLACEHOLDER]） |
| chk_day4_reward | checkin_reward_detail(D4) | 25 | - | 0 | 9999 | 无 | meta_res | 第 4 日（§3.2 CSV D4 [PLACEHOLDER]） |
| chk_day5_reward | checkin_reward_detail(D5) | 30 | - | 0 | 9999 | 无 | meta_res | 第 5 日（§3.2 CSV D5 [PLACEHOLDER]） |
| chk_day6_reward | checkin_reward_detail(D6) | 40 | - | 0 | 9999 | 无 | meta_res | 第 6 日（§3.2 CSV D6 [PLACEHOLDER]）。临近大奖跳升 +10，强化第 7 日预期 |
| chk_day7_reward | checkin_reward_detail(D7) | 100 | - | 0 | 9999 | 无 | meta_res | 第 7 日大奖日元资源（§3.2 CSV D7 [PLACEHOLDER]，is_bonus=true）。7 日循环锚点奖励 |
| chk_day7_bonus | checkin_config(day7_bonus) | 100 | - | 0 | 9999 | 无 | meta_res | 第 7 日大奖额（§3.1 day7_bonus [PLACEHOLDER]、JSON day7_bonus [PLACEHOLDER]）。与 D7 一致（>日常），构成 7 日循环峰值激励 |
| chk_streak_cap | (clamp, §2.4 E09) | 999 | - | 1 | 9999 | 无 | 天 | 连续签到上限钳制（§2.4 E09 `streak 上限 [PLACEHOLDER]`）。防溢出，999 天远超现实周期（keep_best 已保留最高连） |

## 备注 / 待裁定
- §3.1 其余字段已给具体值：`cycle_days=7`、`keep_best=true`、`allow_makeup=false`（makeup_cost=null）、`reset_rule=cycle`、`reddot_on_newday=true`、`reward_type=meta_res`，无 [PLACEHOLDER]，未列。
- `day_reward` JSON 数组 7 元即上表 D1–D7；`day7_bonus` 与 D7 同值（设计上大奖日 = 第 7 日奖励），两处 [PLACEHOLDER] 已分别给同值初值。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

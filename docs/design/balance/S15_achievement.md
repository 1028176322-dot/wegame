# 数值设计表：S15 成就

> 关联 F 码：F37 · GDD：—（SYSTEM_BREAKDOWN §S15）· 设计文档：systems/S15_achievement.md
> 说明：本表为该系统设计文档 §3 配置表（achievement_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 ach_ 等），全局唯一、稳定，禁止中文
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
| ach_firstkill_target | achievement_config(a_firstkill) | 1 | - | 1 | 9999 | 无 | 只(击杀) | 初次击杀目标值（§3.1 target 默认值 [PLACEHOLDER]、CSV 1）。首杀即达成，零门槛入口成就 |
| ach_combo_target | achievement_config(a_combo) | 20 | - | 1 | 9999 | 无 | 次(连杀) | 单局连杀 20 目标（§3.1 CSV 20）。中等战斗技巧挑战 |
| ach_lv10_target | achievement_config(a_lv10) | 10 | - | 1 | 9999 | 无 | 级 | 养到 10 级塔目标（§3.1 CSV 10）。养成线中期里程碑 |
| ach_zeroleak_target | achievement_config(a_zeroleak) | 1 | - | 1 | 9999 | 无 | 次(通关) | 零漏通关 1 次目标（§3.1 CSV 1）。挑战类，鼓励无漏运营 |
| ach_towerclear_target | achievement_config(a_towerclear) | 7 | - | 1 | 9999 | 无 | 关 | 7 塔各通关目标（§3.1 CSV 7）。长线收集成就，覆盖全塔种 |
| ach_firstkill_reward | achievement_config(a_firstkill) | 10 | - | 0 | 9999 | 无 | meta_res | 初次击杀奖励（§3.1 reward 默认值 [PLACEHOLDER]、CSV [PLACEHOLDER]10） |
| ach_combo_reward | achievement_config(a_combo) | 50 | - | 0 | 9999 | 无 | meta_res | 连杀大师奖励（§3.1 CSV [PLACEHOLDER]50） |
| ach_lv10_reward | achievement_config(a_lv10) | 100 | - | 0 | 9999 | 无 | meta_res | 养成大师奖励（§3.1 CSV [PLACEHOLDER]100） |
| ach_zeroleak_reward | achievement_config(a_zeroleak) | 200 | - | 0 | 9999 | 无 | meta_res | 零漏通关奖励（§3.1 CSV [PLACEHOLDER]200） |
| ach_towerclear_reward | achievement_config(a_towerclear) | 300 | - | 0 | 9999 | 无 | meta_res | 全塔通关奖励（§3.1 CSV [PLACEHOLDER]300）。最高难度收集成就，奖励最高 |

## 备注 / 待裁定
- 奖励梯度（10→50→100→200→300）与成就难度正相关；最高项 a_towerclear 为长线收集，奖励最高但不破坏经济（meta_res 非局内货币）。
- §3.1 其余字段（multi_step=false 等）非数值 [PLACEHOLDER]，未列。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

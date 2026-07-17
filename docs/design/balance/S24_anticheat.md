# 数值设计表：S24 防作弊系统

> 关联 F 码：F43 · GDD：§6（经济可解性） · 设计文档：systems/S24_anticheat.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 ac_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（gold / wood / 分 / 波 / 毫秒 / 倍(0-1)）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| ac_gold_per_wave_max | anticheat_config | 500 | - | 200 | 5000 | 无 | gold | 单波金币上限。正常波收入基线约 100–300（rc_gold_per_wave_base=100 + S04 掉落），取 500 为宽松上限，首版仅标记(punish_mode=mark)。待 S25 观测峰值后收紧。 |
| ac_wood_per_wave_max | anticheat_config | 200 | - | 50 | 2000 | 无 | wood | 单波木头上限。木仅怪掉(S04)，正常波约 30–120，取 200 宽松上限。 |
| ac_score_jump_max | anticheat_config | 1000 | - | 100 | 50000 | 无 | 分 | 单局成绩较历史跳变上限（防刷分）。待 S25 观测分布裁定。 |
| ac_best_wave_jump_max | anticheat_config | 5 | - | 1 | 50 | 无 | 波 | 最佳波数单局跳变上限（防异常跳波）。 |
| ac_check_interval_ms | anticheat_config | 1000 | - | 100 | 5000 | 无 | 毫秒 | 采样校验间隔 1s，每 tick 比对基准曲线防内存改币（文档 E10）。 |
| ac_flag_rate_alert | anticheat_config | 0.05 | - | 0 | 1 | 无 | 倍(0-1) | 标记率告警线 5%。正常玩法标记率超此触发阈值复核（防过严误伤，文档 E5）。 |

## 备注 / 待裁定
- 文档 §3.1 其余字段（enable=true、punish_mode=mark 首版仅标记、checksum_algo=crc32、report_to=s25、whitelist=[]）为具体默认，**非 [PLACEHOLDER]**。
- 6 个 [PLACEHOLDER] 上限/阈值均已给初值（保守、首版仅标记，避免误伤）。实际阈值须由 S25 观测正常分布 + GDD §6 通胀检测裁定后收紧。
- 无 NEEDS-DESIGN 项。

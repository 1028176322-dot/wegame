# 数值设计表：S08 结算系统

> 关联 F 码：F12 · GDD：§5.7 · 设计文档：systems/S08_settlement.md
> 说明：本表为该系统设计文档 §3 配置表（settlement_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；塔属性前缀 t_<tower>_，系统参数前缀 sys_/econ_/wave_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.dmg_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| settle_win_base_gold | settlement_config | 100 | - | 10 | 500 | 无 | gold | 胜利基础金（通关激励），叠加 per_wave_gold×波数 |
| settle_win_base_wood | settlement_config | 50 | - | 10 | 500 | 无 | 木 | 胜利基础木（养塔来源，session 不持久化） |
| settle_per_wave_gold | settlement_config | 3 | - | 1 | 50 | 无 | gold/波 | 每撑过波奖励金，进度价值 |
| settle_leak_penalty | settlement_config | 0.3 | - | 0 | 1 | 无 | 系数 | 漏怪产出系数（少漏多奖）；产出 = base + per_wave×波×(1−leak_penalty×leak_norm)，钳制 [0,1] |
| settle_new_record_bonus | settlement_config | 20 | - | 0 | 100 | 无 | gold | 新纪录额外奖励（冲榜动力） |
| settle_xp_base | settlement_config | 50 | - | 0 | 500 | 无 | xp | 胜利基础 XP（S29 升级来源），产出 = xp_base + per_wave_xp×波×(1−leak_penalty×leak_norm) |
| settle_per_wave_xp | settlement_config | 2 | - | 1 | 50 | 无 | xp/波 | 每撑过波奖励 XP（S29 进度价值） |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- `fail_penalty=false`、`best_metric=wave` 等为 doc §3 已给默认，非 placeholder，本表不重复。
- 产出公式（doc §3）：`gold = win_base_gold + per_wave_gold × wave_reached × (1 − leak_penalty × leak_count_normalized)`；XP 公式同理（S29）。`leak_penalty` 已钳制 [0,1]（同 §2.4）。
- `settle_xp_*` 为 S29 等级系统的 XP 输入；XP 如何映射等级由 S29 `player_level_config.xp_required`（仍是 B 域 [PLACEHOLDER]）决定，本表不跨域改写。
- 本系统参数与玩家等级(S29)的 dmg/range/atk_speed 加成无关（XP 是产出而非战斗属性），level_link 全为“无”。

# 数值设计表：S03 经济系统

> 关联 F 码：F5 · GDD：§6 · 设计文档：systems/S03_economy.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| econ_start_gold | economy_config | 300 | - | 0 | 1000 | 无（可接 S29 unlock_gold 元进度永久加成：起始金 ×(1+effect%)，单层不累加） | gold | 开局金，参《绿色循环圈》直觉 300；金仅来自击杀/Boss/结算，木不互换(默认禁) |
| econ_exchange_rate | economy_config | 0.1 | - | 0.1 | 10 | 无 | 木/金 | 应急金→木汇率（木 += floor(金×rate)）。初值 0.1 即 10 金换 1 木，刻意劣于“纯怪掉”预期，防应急变木主源 |
| econ_emergency_max_per_session | economy_config | 3 | - | 0 | 10 | 无 | 次 | 每副本次应急兑换次数上限（非主源硬限）；初值 3，够兜底不破例 |
| econ_emergency_trigger_lives | economy_config | 5 | - | 1 | 50 | 无 | 条 | emergency_trigger.lives_below 阈值；Lives<5 才可应急兑换，仅作紧急兜底语义 |
| econ_kill_reward_gold | economy_config | 5 | - | 1 | 50 | 无 | gold | 击杀基础金（Lv1 波基准），随波次 HP 缩放另算；木主源为怪掉非金 |
| econ_boss_reward_gold | economy_config | 100 | - | 50 | 500 | 无 | gold | Boss 金，显著高于普通击杀以激励 Boss 波 |
| econ_inflation_threshold | economy_config | 1.5 | - | 0 | - | 无 | 倍 | 币/活跃人/日 告警线 1.5x，超阈触发 S21/S25 平衡 pass |
| econ_sell_refund_rate | economy_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 卖塔返还比例，与 S02 各塔 sell_refund_rate 一致（防卡死兜底） |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- `start_wood` 固定 0、`wood_persist=false`、`wood_to_gold_enabled=false`、`gold_cap/wood_cap=99999`、`exchange_min_gold=10`、`batch_options=[50,100,200]` 等为设计文档已给定结构值，本表不重复，但仍为 concrete（非 placeholder）。
- **S29 元进度联动**：`econ_start_gold` 可被 S29 `unlock_config[unlock_gold].effect_value`（永久升级·起始金币+%）放大，但该 effect_value 在 S29 中仍为 [PLACEHOLDER]（属 B 域待裁定项，不在本 8 系统范围）。本表仅标注联动方式，未改写其初值。
- 应急兑换 `exchange_rate=0.1` 为“较差汇率”初值，须劣于纯怪掉木预期；若试玩发现玩家仍依赖应急，下调该值或 `econ_emergency_max_per_session`。

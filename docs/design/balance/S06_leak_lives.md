# 数值设计表：S06 漏怪/生命系统

> 关联 F 码：F8 · GDD：§5.4 · 设计文档：systems/S06_leak_lives.md
> 说明：本表为该系统设计文档 §3 配置表（lives_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| sys_start_lives | lives_config | 20 | - | 1 | 50 | 无（可接 S29 unlock_lives 元进度永久 +Lives，单层不累加） | 条 | 初始命数，参《绿色循环圈》直觉 20；容错与压力平衡 |
| sys_normal_leak_cost | lives_config | 1 | - | 1 | 10 | 无 | 条 | 普通怪漏扣，初值 1（漏一只扣一条，压力温和） |
| sys_boss_leak_cost | lives_config | 5 | - | 1 | 20 | 无 | 条 | Boss 漏扣，初值 5（Boss 风险高，漏 Boss 近灭局） |
| sys_meta_lives_bonus | lives_config | 0 | - | 0 | 20 | 无（S29 unlock_lives 元进度提供，初始 0） | 条 | 元进度永久 +Lives（S11/S29），初值 0（无额外加成） |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- `tutorial_lock=true`、`fail_on_zero=true` 等为 doc §3 已给布尔默认，非 placeholder，本表不重复。
- **S29 元进度联动**：`sys_start_lives` 可被 S29 `unlock_config[unlock_lives].effect_value`（永久升级·漏怪容错+Lives）加成，但该 effect_value 在 S29 中仍为 [PLACEHOLDER]（属 B 域待裁定项，不在本 8 系统范围）。本表仅标注联动方式，未改写其初值 0。
- `sys_boss_leak_cost=5` 配合 `sys_start_lives=20`，意味着 Boss 漏怪约消耗 1/4 容错，凸显 Boss 风险而不至于一击崩盘。

# 数值设计表：S31 敌人系统 (Enemy / Monster System)

> 关联 F 码：F6 · GDD：§5.5 · 设计文档：systems/S31_enemy.md
> 说明：本表为该系统设计文档 §3 配置表（`enemy_config` 逐原型 + `enemy_drop` 逐敌）与正文中所有 `[PLACEHOLDER]` 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。
> **依赖说明**：armor_type 枚举、`magic_immune×0` 规则、缩放因子（关卡=S14 `diff_mult`、波次=S04 `wave_base_hp` growth）均已在设计文档 §0/§3/§5 标记；S30 属性系统 / S32 关卡系统 / S33 状态系统 三份被引用文档在仓库中**尚不存在**，本表缩放因子以"引用 S14/S04"或"S31 自定(待 S30 校准)"标注，详见设计文档 §5 冲突清单 B/C/D。

## 字段规范
- param_id：参数唯一标识（snake_case；敌属性前缀 `enemy_`，掉木前缀 `enemy_drop_`，Boss 机制前缀 `boss_`，缩放前缀 `enemy_`），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^波、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（"无" / "套用 S14_level.diff_mult(乘)" / "引用 S04 wave_base_hp growth(1.18^波)" / "引用 S14_level.diff_mult"）
- unit：单位（点 / px·s⁻¹ / % / 个 / 倍 / 倍·波 / 秒）
- description：含义与调优说明（含 armor_type 枚举字符串、weak_tower 映射、为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| enemy_hp_light | enemy_config | 30 | 1.18^波 | 1 | 1000000 | 套用 S14_level.diff_mult(乘) | 点 | 轻甲(light)普通敌基础HP；弱点 t_arrow(物理克轻甲)；第N波=30×1.18^(N-1)，再×关卡diff_mult；对齐 balance/S04 wave_base_hp |
| enemy_hp_heavy | enemy_config | 120 | 1.18^波 | 1 | 1000000 | 套用 S14_level.diff_mult(乘) | 点 | 重甲(heavy)基础HP；弱点 t_cannon/t_poison(炮溅射克重甲/毒克高HP)；对齐 S16_codex e_golem 示例 120 |
| enemy_hp_air | enemy_config | 70 | 1.18^波 | 1 | 1000000 | 套用 S14_level.diff_mult(乘) | 点 | 空军(air)基础HP；弱点 t_electric(electric_vs_air)；走上层z31；需对空/指定塔种 |
| enemy_hp_magic_immune | enemy_config | 90 | 1.18^波 | 1 | 1000000 | 套用 S14_level.diff_mult(乘) | 点 | 魔免(magic_immune)基础HP；**魔法伤害×0**，弱点 t_arrow/t_cannon(物理)；已修正"魔法克魔免"矛盾(设计文档冲突A) |
| enemy_hp_boss | enemy_config | 3000 | 1.12^波 | 1 | 1000000 | 套用 S14_level.diff_mult(乘) | 点 | Boss基础HP(高)；默认 heavy 护甲 + speedup 机制；Boss 波关键威胁 |
| enemy_speed_light | enemy_config | 70 | 1.0+0.005/波 | 10 | 300 | 套用 S14_level.diff_mult(乘) | px·s⁻¹ | 轻甲移动速度；被风塔击退延长在场(配合P4控制combo) |
| enemy_speed_heavy | enemy_config | 50 | 1.0+0.005/波 | 10 | 300 | 套用 S14_level.diff_mult(乘) | px·s⁻¹ | 重甲移动速度(慢) |
| enemy_speed_air | enemy_config | 80 | 1.0+0.005/波 | 10 | 300 | 套用 S14_level.diff_mult(乘) | px·s⁻¹ | 空军移动速度 |
| enemy_speed_magic_immune | enemy_config | 65 | 1.0+0.005/波 | 10 | 300 | 套用 S14_level.diff_mult(乘) | px·s⁻¹ | 魔免移动速度 |
| enemy_speed_boss | enemy_config | 40 | 1.0+0.003/波 | 10 | 300 | 套用 S14_level.diff_mult(乘) | px·s⁻¹ | Boss移动速度(慢但高HP)；可被 speedup 机制加速 |
| enemy_drop_rate_light | enemy_drop | 0.30 | 1.0+0.005/波 | 0 | 0.6 | 无 | % | 轻甲掉木概率；对齐 GDD§6 [P]0.3、balance/S04 上限0.6；session木主源(不持久化) |
| enemy_drop_min_light | enemy_drop | 1 | 1.0+0.05/波 | 1 | 999 | 无 | 个 | 轻甲掉木下限；对齐 GDD§6 量[P]2 |
| enemy_drop_max_light | enemy_drop | 3 | 1.0+0.1/波 | 1 | 999 | 无 | 个 | 轻甲掉木上限；对齐 balance/S04 amount 2→30 |
| enemy_drop_rate_heavy | enemy_drop | 0.25 | 1.0+0.005/波 | 0 | 0.6 | 无 | % | 重甲掉木概率(略低，肉但掉木少) |
| enemy_drop_min_heavy | enemy_drop | 1 | 1.0+0.05/波 | 1 | 999 | 无 | 个 | 重甲掉木下限 |
| enemy_drop_max_heavy | enemy_drop | 4 | 1.0+0.1/波 | 1 | 999 | 无 | 个 | 重甲掉木上限 |
| enemy_drop_rate_air | enemy_drop | 0.30 | 1.0+0.005/波 | 0 | 0.6 | 无 | % | 空军掉木概率；对齐 GDD§6 0.3 |
| enemy_drop_min_air | enemy_drop | 1 | 1.0+0.05/波 | 1 | 999 | 无 | 个 | 空军掉木下限 |
| enemy_drop_max_air | enemy_drop | 3 | 1.0+0.1/波 | 1 | 999 | 无 | 个 | 空军掉木上限 |
| enemy_drop_rate_magic_immune | enemy_drop | 0.30 | 1.0+0.005/波 | 0 | 0.6 | 无 | % | 魔免掉木概率；对齐 GDD§6 0.3 |
| enemy_drop_min_magic_immune | enemy_drop | 1 | 1.0+0.05/波 | 1 | 999 | 无 | 个 | 魔免掉木下限 |
| enemy_drop_max_magic_immune | enemy_drop | 3 | 1.0+0.1/波 | 1 | 999 | 无 | 个 | 魔免掉木上限 |
| enemy_drop_boss_rate | enemy_drop | 1.00 | - | 0 | 1 | 无 | % | Boss额外掉率(必掉)；Boss为养塔关键木点 |
| enemy_drop_boss_min | enemy_drop | 5 | 1.0+0.2/波 | 1 | 999 | 无 | 个 | Boss额外掉木下限 |
| enemy_drop_boss_max | enemy_drop | 15 | 1.0+0.5/波 | 1 | 999 | 无 | 个 | Boss额外掉木上限 |
| boss_speedup_mult | enemy_config(boss) | 1.30 | +0.02/秒 | 1.0 | 3.0 | 无 | 倍 | Boss加速机制倍率(speedup)；每 boss_speedup_interval 秒速度×该倍率 |
| boss_speedup_interval | enemy_config(boss) | 10 | - | 1 | 60 | 无 | 秒 | Boss每 N 秒触发一次加速(speedup 机制) |
| boss_heal_cut_rate | enemy_config(boss) | 0.50 | - | 0 | 1 | 无 | % | Boss减疗(heal_cut)：heal 行为受到的治疗 -50%；仅当 heal 行为存在时生效 |
| enemy_level_scale_factor | enemy_config | 1.00 | - | 0.5 | 3.0 | 引用 S14_level.diff_mult | 倍 | 关卡缩放因子(引用 S14_level.diff_mult，非 S32；S32 文档缺失)；effective=base×该因子 |
| enemy_wave_hp_growth | enemy_config | 1.18 | - | 1.0 | 10 | 引用 S04 wave_base_hp growth(1.18^波) | 倍/波 | 波次HP缩放因子(引用 S04，非 S30；S30 缺失) |
| enemy_wave_speed_growth | enemy_config | 1.005 | - | 1.0 | 2.0 | 无(S31定义,待S30校准) | 倍/波 | 波次速度缩放因子；速度随波次微增 |

## 备注 / 待裁定
- 本系统所有 `[PLACEHOLDER]` 均已给初值（共 31 条参数），无空白占位；armor_type 枚举字符串已写入 description（light/heavy/air/magic_immune/none/poison）。
- **HP/速度缩放模型**：`effective_hp = base_hp × enemy_level_scale_factor(S14) × 1.18^(wave-1)`；`effective_speed = base_move_speed × enemy_level_scale_factor(S14) × enemy_wave_speed_growth^(wave-1)`。玩家等级(S29)仅增益塔，不增益敌（故 level_link 对敌均为"无"或引用 S14/S04，无 S29 链接）。
- **木为 session**：所有 `enemy_drop_*` 产出为 session 木（S03 `wood_cap` 截断、不持久化、不带出副本）；Boss 额外掉木为养塔关键木点，受 S03 `inflation_threshold` 监控防"木无限养塔"。
- **冲突 A（已采用自洽规则）**：`magic_immune` 魔法伤害 ×0，弱点=物理塔(t_arrow/t_cannon)；GDD §5.6"魔法塔=魔免怪克星"与任务"魔法克魔免"措辞矛盾，建议 GDD 改为"物理克魔免"。
- **NEEDS-DESIGN**：S30 属性系统 / S32 关卡系统 / S33 状态系统 三份被引用文档缺失（仓库 systems/ 仅至 S29），缩放因子与枚举暂以 S04/S05/S14/GDD 兜底，待对应系统建立后回填对齐（见设计文档 §5 清单 B/C/D/E/F）。
- 掉木结算双 owner（S04 波级 `drop_wood_*` 与本系统逐敌 `enemy_drop`）按设计文档 §3 规则协调：S04 存在则优先，否则用 enemy_drop；建议 S04 后续委托本系统。

# 数值设计表：S05 战斗系统

> 关联 F 码：F7 · GDD：§5.7(+§5.8) · 设计文档：systems/S05_combat.md
> 说明：本表为该系统设计文档 §3 配置表（combat_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| combat_cm_arrow_vs_light | combat_config | 1.5 | - | 0.5 | 2.0 | 无 | 倍 | 克制系数：箭 vs 轻甲（轻甲易伤） |
| combat_cm_cannon_vs_heavy | combat_config | 1.5 | - | 0.5 | 2.0 | 无 | 倍 | 克制系数：炮 vs 重甲（重甲易伤） |
| combat_cm_ice_vs_none | combat_config | 1.0 | - | 0.5 | 2.0 | 无 | 倍 | 克制系数：冰 vs 无甲（设计文档已给常数 1.0，列此备查） |
| combat_cm_magic_vs_magic_immune | combat_config | 0.0 | - | 0.0 | 0.0 | 无 | 倍 | 克制系数：魔法 vs 魔免（魔免免疫魔法伤害=0.0，铁律见 S30；魔法塔非魔免克星，魔免弱物理塔） |
| combat_cm_poison_vs_heavy | combat_config | 1.3 | - | 0.5 | 2.0 | 无 | 倍 | 克制系数：毒 vs 重甲（越肉越赚） |
| combat_cm_electric_vs_air | combat_config | 1.5 | - | 0.5 | 2.0 | 无 | 倍 | 克制系数：电 vs 空军（对空主力） |
| combat_armor_none | combat_config | 0.0 | - | 0 | 0.9 | 无 | 减伤% | 无甲减伤 0% |
| combat_armor_light | combat_config | 0.1 | - | 0 | 0.9 | 无 | 减伤% | 轻甲减伤 10% |
| combat_armor_heavy | combat_config | 0.3 | - | 0 | 0.9 | 无 | 减伤% | 重甲减伤 30%（需炮/毒破） |
| combat_armor_magic_immune | combat_config | 0.0 | - | 0 | 0.0 | 无 | 减伤% | 魔免基础减伤 0%（魔免=免疫魔法×0，对物理塔无减免、反被克制；本行对应非魔法伤害兜底为0） |
| combat_projectile_speed | combat_config | 600 | - | 100 | 2000 | 无 | px/s | 弹速，初值 600 手感顺滑；钳制下限防弹道不达 |
| combat_splash_radius | combat_config | 80 | - | 0 | 200 | 无 | px | 炮溅射半径，初值 80 覆盖小群；钳制上限防 solo 全图 |
| combat_slow_factor | combat_config | 0.5 | - | 0.3 | 0.9 | 无 | 倍 | 冰减速比例（怪物速度 ×0.5），保命强度 |
| combat_slow_duration | combat_config | 2.0 | - | 0.5 | 5 | 无 | 秒 | 减速时长，与 slow_factor 共决控制链 |
| combat_poison_dps | combat_config | 15 | - | 1 | 100 | 无 | 点/秒 | 毒每秒伤害，越肉越赚 |
| combat_poison_duration | combat_config | 4.0 | - | 1 | 10 | 无 | 秒 | 毒时长，DOT 总量 = poison_dps×duration |
| combat_chain_count | combat_config | 3 | - | 0 | 10 | 无 | 跳 | 电连锁跳数，初值 3；钳制上限防 solo 全图 |
| combat_chain_range | combat_config | 150 | - | 50 | 400 | 无 | px | 电连锁半径，密集处理覆盖 |
| combat_dmg_round | combat_config | 0 | - | 0 | 3 | 无 | 位 | 伤害取整小数位（0=取整到整数，防浮点抖动与飘字一致）；effective_dmg 经 round() 后入 hp 扣减（见 S05 §2.5） |
| combat_electric_vs_air_override | combat_config | 1.5 | - | 0.5 | 2.0 | 无 | 倍 | 电塔对空克制覆盖系数：电塔 damage_type=physical 但 electric_vs_air=1.5（S28/S05 约定），覆盖通用 physical_air=0.5；解决 S30 C3「无 electric damage_type」缺口 |
| combat_crit_rate | combat_config | NEEDS-DESIGN | - | 0 | 1 | 无 | 率 | 暴击率（暴击机制当前未设计：S30/S28/S33 均无；若后续加入战斗管线再填初值，不进当前 effective_dmg 公式） |
| combat_crit_mult | combat_config | NEEDS-DESIGN | - | 1 | 5 | 无 | 倍 | 暴击伤害倍率（同 combat_crit_rate，未设计；设计后 effective_dmg 末尾乘 (1 + crit_rate×(crit_mult−1))） |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- `counter_matrix` / `armor_reduce` 原在 doc 中为单个 JSON [PLACEHOLDER]，本表已拆为逐键/逐甲的具体初值（counter 6 项含已给定的 ice_vs_none=1.0；armor 4 项对应 S04 armor_type 枚举 none/light/heavy/magic_immune/air；**原 `combat_armor_poison` 已按 N3 弃用删除**，poison 甲并入 air 甲），便于独立调参与钳制。
- **S29 等级加成消费**：本系统不持有等级加成参数——塔有效属性（dmg/range/atk_speed）已**在建塔时(S02)套用 S29 单行加成**，本系统仅按 `damage_formula = base×level_bonus×growth^养塔级×counter − armor` 消费该已修正属性（level_bonus 不累加）。故本表 level_link 全为“无”。
- 状态叠加默认 `status_stack_rule=refresh`（同类型刷新不叠层），已在 doc §3 给定，非 placeholder。
- `combat_splash_radius`/`combat_chain_count` 上限钳制呼应 doc §2.4 性能/防 solo 警告。
- **§2.5 战斗数值计算深化（S05 设计文档新增）引入的本系统新参数仅 2 项具体初值**：`combat_dmg_round`（伤害取整）+ `combat_electric_vs_air_override`（电塔对空覆盖）；另加 `combat_crit_rate`/`combat_crit_mult` 两项 **NEEDS-DESIGN 占位**（暴击机制未设计，不硬加初值，不进 effective_dmg 公式）。其余管线参数（克制矩阵/护甲减伤/状态强度/塔 base_dps/等级加成/击杀金木）均引用 S30/S33/S02/S03/S04/S08 既有字段，**不在此重定义**。击杀奖励公式（S05 §2.5.7）所用：`kill_reward_gold`/`boss_reward_gold`=S03`economy_config`；`reward_mult`=S04`wave_config.reward_mult`([P])；木=S04`drop_wood_*` 或 S31`enemy_drop.*`；XP 由 S08 结算 `xp_gain` 在局末按 `wave_reached` 计算（非逐杀）。

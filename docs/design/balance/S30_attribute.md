# 数值设计表：S30 属性系统 (Attribute / Stat System)

> 关联 F 码：F2 F3 F4 F6 F7 · GDD：§5.2/§5.6/§5.7/§5.9 · 设计文档：systems/S30_attribute.md
> 说明：本表为该系统设计文档 §3 配置表（`attribute_def` / `damage_armor_matrix` / `armor_type_def` / `attr_composition` / `enemy_attr_scaling`）与正文中所有 `[PLACEHOLDER]` 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。
> **本系统为全游戏属性唯一真理源**：S02/S04/S05/S28/S31/S32/S33 均引用本表，不得各自硬编码。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 `attr_`），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.dmg_mult(单行,不累加)" / "无" / "S32 关卡 level_scalar"）
- unit：单位（point / px / per_s / px_s / HP / 减伤% / 倍 / 级）
- description：含义与调优说明（含为何取此初值）

## 数值表

### A. 属性极值钳制（attribute_def · 非负铁律，越界走 S24）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_dmg_max | attribute_def | [P] | - | 0 | 99999 | 无 | point | 塔伤害上限钳制（初值调优[P]；硬上限结构值 99999） |
| attr_dmg_min | attribute_def | 0 | - | 0 | 0 | 无 | point | 塔伤害下限（非负铁律，负值钳 0） |
| attr_range_max | attribute_def | [P] | - | 0 | 99999 | 无 | px | 射程上限钳制 |
| attr_range_min | attribute_def | 0 | - | 0 | 0 | 无 | px | 射程下限（非负） |
| attr_atk_speed_max | attribute_def | [P] | - | 0.1 | 100 | 无 | per_s | 攻速上限（防除零/手感崩） |
| attr_atk_speed_min | attribute_def | 0.1 | - | 0.1 | 0.1 | 无 | per_s | 攻速下限（防 0 攻速） |
| attr_projectile_speed_max | attribute_def | [P] | - | 50 | 99999 | 无 | px_s | 弹速上限钳制 |
| attr_projectile_speed_min | attribute_def | 50 | - | 50 | 50 | 无 | px_s | 弹速下限（防弹道不达目标） |
| attr_hp_max | attribute_def | [P] | - | 1 | 9999999 | 无 | HP | 敌 HP 上限钳制 |
| attr_hp_min | attribute_def | 1 | - | 1 | 1 | 无 | HP | 敌 HP 下限（≤0 钳 1，正常死亡） |
| attr_move_speed_max | attribute_def | [P] | - | 20 | 99999 | 无 | px_s | 敌移速上限钳制 |
| attr_move_speed_min | attribute_def | 20 | - | 20 | 20 | 无 | px_s | 敌移速下限（防怪物不动） |

### B. 养塔成长系数（attr_composition 步骤2 · S02 消费，S30 定义）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_growth_base | attr_composition | 1.5 | - | 1.5 | 2.0 | 无 | 倍 | 养塔每级成长系数（指数 growth^level）；区间 1.5–2.0 初值，验证 P2 指数感 |

### C. 玩家等级加成（attr_composition 步骤3 · 单行查表，不累加 · 锚定 Lv1/Lv20）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_lvl_dmg_mult_lv1 | attr_composition | 1.0 | - | 1.0 | 1.5 | 套用S29 player_level_config.dmg_mult(单行,不累加) | 倍 | Lv1 全局塔伤害倍率（绝对值，无加成） |
| attr_lvl_dmg_mult_lv20 | attr_composition | 1.5 | - | 1.0 | 1.5 | 套用S29 player_level_config.dmg_mult(单行,不累加) | 倍 | Lv20 全局塔伤害倍率锚定初值（仅锚定，全曲线在 S29） |
| attr_lvl_range_mult_lv1 | attr_composition | 1.0 | - | 1.0 | 1.5 | 套用S29 player_level_config.range_mult(单行,不累加) | 倍 | Lv1 全局射程倍率 |
| attr_lvl_range_mult_lv20 | attr_composition | 1.5 | - | 1.0 | 1.5 | 套用S29 player_level_config.range_mult(单行,不累加) | 倍 | Lv20 全局射程倍率锚定初值 |
| attr_lvl_atkspd_mult_lv1 | attr_composition | 1.0 | - | 1.0 | 1.5 | 套用S29 player_level_config.atk_speed_mult(单行,不累加) | 倍 | Lv1 全局攻速倍率 |
| attr_lvl_atkspd_mult_lv20 | attr_composition | 1.5 | - | 1.0 | 1.5 | 套用S29 player_level_config.atk_speed_mult(单行,不累加) | 倍 | Lv20 全局攻速倍率锚定初值 |

> 注：上表仅锚定 Lv1 / Lv20 初值；完整 1–20 级曲线存于 S29 `player_level_config`（单行查表，绝不累加）。本系统不持有逐行数据，仅消费。

### D. 伤害×护甲克制矩阵（damage_armor_matrix · 全组合 4×5=20）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_cm_physical_none | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 物理 vs 无甲（中性真伤） |
| attr_cm_physical_light | damage_armor_matrix | 1.5 | - | 0 | 1.5 | 无 | 倍 | 物理 vs 轻甲（强克：箭塔克轻甲） |
| attr_cm_physical_heavy | damage_armor_matrix | 1.5 | - | 0 | 1.5 | 无 | 倍 | 物理 vs 重甲（强克：炮塔克重甲） |
| attr_cm_physical_magic_immune | damage_armor_matrix | 1.5 | - | 0 | 1.5 | 无 | 倍 | 物理 vs 魔免（强克：GDD §5.5「魔免需物理塔」） |
| attr_cm_physical_air | damage_armor_matrix | 0.5 | - | 0 | 1.5 | 无 | 倍 | 物理 vs 空军（弱抗：空军需专门对空塔） |
| attr_cm_magic_none | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 魔法 vs 无甲（真伤无视护甲） |
| attr_cm_magic_light | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 魔法 vs 轻甲（真伤无视护甲） |
| attr_cm_magic_heavy | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 魔法 vs 重甲（真伤无视护甲） |
| attr_cm_magic_magic_immune | damage_armor_matrix | 0.0 | - | 0 | 1.5 | 无 | 倍 | 魔法 vs 魔免（**免疫 ×0，铁律**；冲突见 doc §5 C1） |
| attr_cm_magic_air | damage_armor_matrix | 0.5 | - | 0 | 1.5 | 无 | 倍 | 魔法 vs 空军（弱抗） |
| attr_cm_poison_none | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 毒 vs 无甲（中性） |
| attr_cm_poison_light | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 毒 vs 轻甲（中性） |
| attr_cm_poison_heavy | damage_armor_matrix | 1.5 | - | 0 | 1.5 | 无 | 倍 | 毒 vs 重甲（强克：越肉越赚） |
| attr_cm_poison_magic_immune | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 毒 vs 魔免（有效，毒非魔法） |
| attr_cm_poison_air | damage_armor_matrix | 0.5 | - | 0 | 1.5 | 无 | 倍 | 毒 vs 空军（弱抗） |
| attr_cm_control_none | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 控制 vs 无甲（控制无伤，仅施加状态） |
| attr_cm_control_light | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 控制 vs 轻甲 |
| attr_cm_control_heavy | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 控制 vs 重甲 |
| attr_cm_control_magic_immune | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 控制 vs 魔免（控制非伤害，仍生效） |
| attr_cm_control_air | damage_armor_matrix | 1.0 | - | 0 | 1.5 | 无 | 倍 | 控制 vs 空军（冰/风对空仍生效） |

### E. 护甲类型减伤%（armor_type_def · 上限 0.9 防无敌）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_armor_none_reduce | armor_type_def | 0.0 | - | 0 | 0.9 | 无 | 减伤% | 无甲减伤 0% |
| attr_armor_light_reduce | armor_type_def | 0.10 | - | 0 | 0.9 | 无 | 减伤% | 轻甲减伤 10%（被物理强克） |
| attr_armor_heavy_reduce | armor_type_def | 0.30 | - | 0 | 0.9 | 无 | 减伤% | 重甲减伤 30%（需炮/毒破） |
| attr_armor_magic_immune_reduce | armor_type_def | 0.0 | - | 0 | 0.9 | 无 | 减伤% | 魔免减伤 0%（免疫由矩阵 magic×0 表达，避免双重惩罚） |
| attr_armor_air_reduce | armor_type_def | 0.0 | - | 0 | 0.9 | 无 | 减伤% | 空减伤 0%（弱抗由矩阵 ×0.5 表达） |

### F. 敌属性关卡/波次缩放因子（enemy_attr_scaling · S32/S04 提供）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_enemy_hp_level_scalar_lv1 | enemy_attr_scaling | 1.0 | 1.10/级 | 1.0 | [P] | S32 关卡 level_scalar(乘子) | 倍 | Lv1 敌 HP 关卡缩放基准 |
| attr_enemy_hp_level_scalar_lv20 | enemy_attr_scaling | [P] | 1.10/级 | 1.0 | [P] | S32 关卡 level_scalar(乘子) | 倍 | Lv20 敌 HP 关卡缩放锚定初值（≈3.0） |
| attr_enemy_hp_wave_scalar | enemy_attr_scaling | 1.0 | 1.06/波 | 1.0 | [P] | S04 波次 wave_scalar(乘子) | 倍 | 敌 HP 逐波缩放（每波 ×1.06） |
| attr_enemy_speed_level_scalar_lv1 | enemy_attr_scaling | 1.0 | 1.03/级 | 1.0 | [P] | S32 关卡 level_scalar(乘子) | 倍 | Lv1 敌移速关卡缩放基准 |
| attr_enemy_speed_level_scalar_lv20 | enemy_attr_scaling | [P] | 1.03/级 | 1.0 | [P] | S32 关卡 level_scalar(乘子) | 倍 | Lv20 敌移速关卡缩放锚定初值（≈1.5） |
| attr_enemy_speed_wave_scalar | enemy_attr_scaling | 1.0 | 1.02/波 | 1.0 | [P] | S04 波次 wave_scalar(乘子) | 倍 | 敌移速逐波缩放（每波 ×1.02） |

### G. 技能/状态乘子默认值（attr_composition 步骤4/5 · S28/S33 提供）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| attr_skill_mod_default | attr_composition | 1.0 | - | 0.1 | 5.0 | S28 技能乘子(可叠加,默认1.0) | 倍 | 技能修正默认乘子（破甲/冰封易伤/导电/腐蚀/逆风等；具体见 S28） |
| attr_buff_mod_default | attr_composition | 1.0 | - | 0.1 | 5.0 | S33 状态乘子(占位默认1.0;S33未设计) | 倍 | 状态修正默认乘子（S33 状态系统尚未设计，暂占位 1.0） |

## 备注 / 待裁定

- 本系统共 **52 条**数值参数（钳制 12 + 成长 1 + 等级锚 6 + 克制矩阵 20 + 护甲减伤 5 + 敌缩放 6 + 技能/状态 2）。
- 所有 `[PLACEHOLDER]` 为初值，须经试玩调优；`attr_dmg_max` 等上限区间已给结构硬上限（99999/9999999）防溢出，初值填实后不得超硬上限。
- **克制矩阵权威值**已对齐 GDD §5.6/§5.7/§5.5：物理克轻/重/魔免(×1.5)、魔法无视护甲但**对魔免 ×0**（冲突 C1 见 doc §5）、毒克重甲(×1.5)、控制全克无伤(×1.0)。
- **`armor_type` 枚举**本表采用 S30 权威值 none/light/heavy/magic_immune/**air**（替换 S04 旧 `poison`），冲突 C2 待 S04 修订。
- **等级加成**仅锚定 Lv1/Lv20，全曲线在 S29 `player_level_config`（单行不累加），本表 `level_link` 已声明消费方式。
- **electric 对空**：S30 仅 4 damage_type（无 electric），`electric_vs_air=1.5` 由 S02 逐塔克制覆盖实现（冲突 C3 / ND-4）。
- **依赖未设计系统**：S33（buff_mod 占位 1.0，ND-2）、S32（敌关卡缩放因子初值，ND-3）落地后须回填真值。
- **S24 防作弊**：所有钳制越界（NaN/Inf/负值/超上限）均对 S24 报可疑，兜底钳制后再交付战斗（见 doc §2.4 异常边界表）。
- 无 NEEDS-DESIGN 阻断项导致数值空白；ND 项均为"待相关系统回填真值/枚举修订"，不影响本表初值落地。

# 数值设计表：S33 状态效果系统

> 关联 F 码：F7 · GDD：§5.7（战斗/状态）· 设计文档：systems/S33_status_effect.md
> 说明：本表为 S33 设计文档 §2.5/§2.6/§2.7/§3 中**所有状态参数**的具体初值。S33 是 FEATURE_SCOPE F7 状态半边的权威定义源；本表初值**已与 `balance/S05_combat.md`（slow 0.5/slow_dur 2.0/poison_dps 15/poison_dur 4.0/chain_count 3）及 `balance/S28_skill_system.md`（破甲20%/易伤20%/导电20%/逆风15%cap3/腐蚀cap5/传染半径120/燃烧30/击退120+定身1/剧毒40）对齐**，避免跨文档分叉。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 `st_`），全局唯一、稳定，禁止中文
- module：所属配置表/模块（status_effect_config / UI）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（状态强度默认不随等级成长；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式——状态数值不随 S29 玩家等级缩放（S29 仅修正塔基础 dmg/range/atk_speed）；是否随 source 塔养塔等级缩放见设计文档 §5 #6 待裁定
- unit：单位（倍(0-1) / % / 秒 / px / 跳 / 层 / 伤害·s⁻¹ / 个）
- description：含义与调优说明（含为何取此初值、跨文档对齐来源）

## 数值表

### 全局 / UI
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_ui_max_slots | status_effect_config/UI | 6 | - | 1 | 12 | 无 | 个 | 单单位状态图标栏最大槽位数（超出折叠为 +N）；初始 6 兼顾可读性与 P3 一指可玩。 |

### 1. slow 减速（move_speed ×k）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_slow_k | status_effect_config | 0.50 | - | 0.10 | 0.95 | 无 | 倍(0-1) | 减速速度乘子（move_speed ×0.5）。对齐 `balance/S05_combat.md` combat_slow_factor=0.5；min=0.1 防 move_speed 归零（见文档 §2.4）。 |
| st_slow_duration | status_effect_config | 2.0 | - | 0.5 | 5.0 | 无 | 秒 | 减速时长。对齐 combat_slow_duration=2.0；与 slow_k 共决控制链。 |

### 2. knockback 击退（位移 + 定身）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_knockback_kb_dist | status_effect_config | 120 | - | 10 | 300 | 无 | px | 沿路径后退距离。对齐 `balance/S28` skill_wind_active_kb_dist=120；钳至路径最近点防越界。 |
| st_knockback_stun | status_effect_config | 1.0 | - | 0.5 | 5.0 | 无 | 秒 | 击退伴随定身时长。对齐 skill_wind_active_stun_dur=1.0；用 move_locked 非 0 速。 |

### 3. poison_dot 中毒（持续 HP 伤害）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_poison_dps | status_effect_config | 15 | - | 1 | 200 | 无 | 伤害·s⁻¹ | 每秒毒伤。对齐 combat_poison_dps=15（越肉越赚）；refresh 取 max 防无限叠加。 |
| st_poison_duration | status_effect_config | 4.0 | - | 0.5 | 10.0 | 无 | 秒 | 毒持续时长。对齐 combat_poison_duration=4.0 / skill_poison_active_dot_dur=4.0。 |

### 4. burn 燃烧（持续伤害 + 溅射）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_burn_dps | status_effect_config | 30 | - | 1 | 200 | 无 | 伤害·s⁻¹ | 灼烧每秒伤害。对齐 skill_cannon_p1_dot=30（燃烧溅射被动）。 |
| st_burn_splash | status_effect_config | 80 | - | 10 | 200 | 无 | px | 燃烧溅射半径。派生（文档未显式 [P]），取 80 与炮塔 splash 量级一致；钳[10,200] 防 solo。 |
| st_burn_duration | status_effect_config | 3.0 | - | 0.5 | 10.0 | 无 | 秒 | 燃烧时长。对齐 skill_cannon_p1_dot_dur=3.0。 |

### 5. chain 连锁（伤害跳数，结算时）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_chain_count | status_effect_config | 3 | - | 0 | 10 | 无 | 跳 | 连锁跳数。对齐 combat_chain_count=3；S28 过载被动 +2 跳另算（不在此）。钳[0,10] 防 solo 全图。 |
| st_chain_range | status_effect_config | 150 | - | 50 | 400 | 无 | px | 连锁半径。派生（文档范围 50–400），取 150 覆盖密集怪群；钳[50,400]。 |

### 6. armor_break 破甲（敌 armor 削减）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_armor_break_val | status_effect_config | 20 | - | 0 | 90 | 无 | % | 护甲减免 −20%。对齐 skill_arrow_p1_armor_reduct=20；refresh 取 max，eff_armor 取最强削减。 |
| st_armor_break_duration | status_effect_config | 3.0 | - | 0.5 | 10.0 | 无 | 秒 | 破甲持续。对齐 skill_arrow_p1_dur=3.0。 |

### 7. vulnerable 易伤（受伤害 ×k）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_vuln_k | status_effect_config | 20 | - | 1 | 100 | 无 | % | 受伤 +20%。对齐 skill_ice_p2_vuln=20；与 conductive 异类乘算（见文档 §2.6）。 |
| st_vuln_duration | status_effect_config | 3.0 | - | 0.5 | 10.0 | 无 | 秒 | 易伤持续（默认独立 3.0s；是否绑定 slow 存在期见文档 §5 #7）。 |

### 8. conductive 导电（受伤害 ×k，combo 放大）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_conductive_k | status_effect_config | 20 | - | 1 | 100 | 无 | % | 受伤 +20%（被电塔命中）。对齐 skill_electric_p2_vuln=20；与 vulnerable 乘算。 |
| st_conductive_duration | status_effect_config | 3.0 | - | 0.5 | 10.0 | 无 | 秒 | 导电持续。派生（文档未显式 [P]），取 3.0 与多数减益一致。 |

### 9. corrosion 腐蚀（护甲持续削减，叠层）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_corrosion_val | status_effect_config | 15 | - | 0 | 90 | 无 | %/层 | 每层护甲减免 −15%。⚠️ 与 S28 定义分歧：S28 写「腐蚀=DoT 可叠 N 层」，本系统按任务 brief 实现为护甲持续削减（见设计文档 §5 #5 待裁定）。 |
| st_corrosion_duration | status_effect_config | 4.0 | - | 0.5 | 10.0 | 无 | 秒 | 腐蚀持续。派生，取 4.0。 |
| st_corrosion_max_stack | status_effect_config | 5 | - | 1 | 20 | 无 | 层 | 叠层上限。对齐 skill_poison_p1_max_stack=5；stack_cap_5 防无限。 |

### 10. infect 传染（DoT 扩散，触发型）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_infect_radius | status_effect_config | 120 | - | 10 | 400 | 无 | px | 中毒怪死亡爆毒半径。对齐 skill_poison_p2_spread_radius=120。 |
| st_infect_dot_dps | status_effect_config | 15 | - | 1 | 200 | 无 | 伤害·s⁻¹ | 传染毒伤（继承 poison_dot 基础）。取 15 与 st_poison_dps 一致。 |
| st_infect_dot_dur | status_effect_config | 3.0 | - | 0.5 | 10.0 | 无 | 秒 | 传染毒持续。派生，取 3.0。 |

### 11. headwind 逆风惩罚（移速惩罚，叠层）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_headwind_slow | status_effect_config | 15 | - | 1 | 100 | 无 | %/层 | 每层移速 −15%。对齐 skill_wind_p2_slow=15；stack_cap_3 相乘。 |
| st_headwind_duration | status_effect_config | 5.0 | - | 0.5 | 15.0 | 无 | 秒 | 逆风持续。派生，取 5.0（较其他长，放大全场 DPS）。 |
| st_headwind_max_stack | status_effect_config | 3 | - | 1 | 10 | 无 | 层 | 叠层上限。对齐 skill_wind_p2_max_stack=3；stack_cap_3 防无限。 |

## 备注 / 待裁定

### NEEDS-DESIGN（待 DO 裁定）
1. **S30 属性合成（含 `buff_mod(S33)`）未建**：设计文档 §2.7 已定义乘子契约与伤害公式；S30 须实现并消费本表数值。数值本身已 concretized，不阻塞本系统。
2. **S31 敌人（状态叠加层美术位）未建**：设计文档 §4 已定义图标位/tint/粒子规格；S31 须消费。美术参数（颜色/帧数）已在本表/设计文档给定。
3. **`corrosion` 语义分歧**：任务 brief 定义 `corrosion=护甲持续削减`，而 S28 原文 `腐蚀=DoT 可叠 N 层`。本表按 brief 实现（st_corrosion_val 为护甲削减/层，stack_cap_5），与 S28 冲突——需 DO 裁定统一（要么改 S28 文案，要么 S33 改为 DoT 叠层语义）。当前以 brief 为准。
4. **S05 `combat_config` 状态字段重定向**：S05 的 slow/poison/chain/status_stack_rule 应改引本表（初值已对齐）；不修改 S05，仅标注（见设计文档 §3）。
5. **状态强度是否随养塔等级缩放**：当前 `level_link=无`，状态强度取固定 base；若需随 source 塔 cultivate_lv 缩放（`strength = base × growth^lv`），待 S05 对齐裁定（见设计文档 §5 #6）。
6. **`vulnerable` 与减速绑定**：默认独立 3.0s；是否严格绑定 slow 存在期（slow 消失则易伤提前结束）待裁定（设计文档 §5 #7）。

### 已给初值说明
- 本表共 **27 行**（1 全局 UI + 26 状态参数），全部 `[PLACEHOLDER]` 已填实，`growth` 统一 `-`（状态强度不随等级成长），`level_link` 统一「无」。
- 跨文档对齐来源：S05 平衡（slow 0.5/2.0、poison 15/4.0、chain 3）+ S28 平衡（破甲20%/3s、易伤20%/3s、导电20%/3s、逆风15%cap3、腐蚀cap5、传染120、燃烧30/3s、击退120/定身1、剧毒40/4s）。
- 钳制区间覆盖设计文档 §2.4 异常边界：`slow_k` min 0.1（防速度归零）、`incoming_dmg_mult` 上限 3.0（防秒杀）、`armor_reduce` [0,0.9]（防免疫）、`chain_count` [0,10]（防 solo 全图）、`stack_cap`（corrosion 5 / headwind 3，防无限叠加）。
- 无其它 NEEDS-DESIGN 项：S33 状态全枚举（11 个）数值均已给初值。

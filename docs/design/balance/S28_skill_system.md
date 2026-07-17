# 数值设计表：S28 技能系统

> 关联 F 码：F2 F3 F4 F7 · GDD：§5.8（技能系统） · 设计文档：systems/S28_skill_system.md
> 说明：本表为该系统设计文档 §2.6 每塔技能定义与 §3 `skill_config` 中**所有 [PLACEHOLDER] 数值参数**的具体初值（7 塔种 × 1 主动 + 2 被动）。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 skill_<tower>_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（skill_config / 技能效果派生）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（技能数值不随等级单独变化；S29 全局倍率经 S02/S05 统一修正塔基础属性）
- unit：单位（秒 / 次 / 层 / 跳 / px / % / 倍 / 倍(0-1) / 伤害/s）
- description：含义与调优说明（含为何取此初值）

## 数值表

### 通用 / 全局
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_cd_min_clamp | skill_config | 1 | - | 1 | - | 无 | 秒 | cd≤0 钳制最小 1s（文档 §2.4 数值极值），并报 S25。防配置错误致技能常驻。 |
| skill_active_cost | skill_config | 0 | - | 0 | 0 | 无 | wood | 主动技木消耗，默认 0（纯 CD 触发，R2/R3 不争养塔木）。全 7 塔一致。 |

### 箭塔 t_arrow（物理单攻·克轻甲）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_arrow_active_cd | skill_config | 12 | - | 1 | 120 | 无 | 秒 | 主动技「精准齐射」冷却 12s（快速单体爆发，低 CD）。 |
| skill_arrow_active_shots | skill_config | 5 | - | 1 | 20 | 无 | 次 | 精准齐射连射次数 N=5（文档 §2.6 [P]）。 |
| skill_arrow_active_burst_mult | skill_config | 2.0 | - | 1.0 | 10 | 无 | 倍 | 精准齐射每发伤害倍率 2.0×（文档 §2.6 [P]「[P]× 爆发伤害」）。5×2=10× 单体瞬时，专秒脆皮。 |
| skill_arrow_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「破甲」解锁所需养塔等级（建议 3）。 |
| skill_arrow_p1_proc | skill_config | 30 | - | 0 | 100 | 无 | % | 破甲触发概率 30%（文档 §2.6 [P]）。 |
| skill_arrow_p1_armor_reduct | skill_config | 20 | - | 0 | 100 | 无 | % | 破甲使目标护甲减免 −20%，持续（文档 §2.6 [P]）。协同克制链。 |
| skill_arrow_p1_dur | skill_config | 3 | - | 0.5 | 10 | 无 | 秒 | 破甲持续 3s（文档 §2.6 [P]）。 |
| skill_arrow_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「连射」解锁所需养塔等级（建议 5）。 |
| skill_arrow_p2_interval | skill_config | 4 | - | 2 | 20 | 无 | 次 | 每第 4 次攻击后触发（文档 §2.6 [P]）。 |
| skill_arrow_p2_atkspd | skill_config | 30 | - | 1 | 200 | 无 | % | 连射攻速 +30%（文档 §2.6 [P]）。 |
| skill_arrow_p2_dur | skill_config | 3 | - | 0.5 | 10 | 无 | 秒 | 连射持续 3s（文档 §2.6 [P]）。 |

### 炮塔 t_cannon（物理溅射·克集群/重甲）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_cannon_active_cd | skill_config | 18 | - | 1 | 120 | 无 | 秒 | 主动技「饱和轰炸」冷却 18s（大范围 AOE，中 CD）。 |
| skill_cannon_active_aoe_mult | skill_config | 1.5 | - | 1.0 | 10 | 无 | 倍 | 饱和轰炸 AOE 伤害倍率 1.5×（派生：文档只标慢速 [P]，伤害取塔溅射 1.5×）。 |
| skill_cannon_active_slow_dur | skill_config | 2 | - | 0.5 | 10 | 无 | 秒 | 饱和轰炸短减速持续 2s（文档 §2.6 [P]）。 |
| skill_cannon_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「燃烧溅射」解锁养塔等级（建议 3）。 |
| skill_cannon_p1_dot | skill_config | 30 | - | 1 | 200 | 无 | 伤害/s | 燃烧溅射灼烧 DoT 30/s（文档 §2.6 [P]）。 |
| skill_cannon_p1_dot_dur | skill_config | 3 | - | 0.5 | 10 | 无 | 秒 | 灼烧持续 3s（文档 §2.6 [P]）。 |
| skill_cannon_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「重创」解锁养塔等级（建议 5）。 |
| skill_cannon_p2_heavy | skill_config | 50 | - | 1 | 200 | 无 | % | 对重甲目标额外伤害 +50%（文档 §2.6 [P]，强化克制 P4）。 |

### 冰塔 t_ice（控制减速·克所有）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_ice_active_cd | skill_config | 25 | - | 1 | 120 | 无 | 秒 | 主动技「极寒领域」冷却 25s（强控，高 CD，Boss 波救命）。 |
| skill_ice_active_freeze_dur | skill_config | 2 | - | 0.5 | 10 | 无 | 秒 | 冻结定身 2s（文档 §2.6 [P]）。 |
| skill_ice_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「霜冻蔓延」解锁养塔等级（建议 3）。 |
| skill_ice_p1_spread_chance | skill_config | 25 | - | 0 | 100 | 无 | % | 减速结束蔓延概率 25%（文档 §2.6 [P]）。 |
| skill_ice_p1_spread_count | skill_config | 3 | - | 1 | 20 | 无 | 个 | 蔓延至附近 3 个怪（文档 §2.6 [P]）。 |
| skill_ice_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「冰封易伤」解锁养塔等级（建议 5）。 |
| skill_ice_p2_vuln | skill_config | 20 | - | 1 | 100 | 无 | % | 被减速/冻结怪受他塔伤害 +20%（文档 §2.6 [P]，支援型放大组合 P4）。 |

### 风塔 t_wind（击退控制·DO 已确认）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_wind_active_cd | skill_config | 15 | - | 1 | 120 | 无 | 秒 | 主动技「飓风之眼」冷却 15s（位移控制，中低 CD）。 |
| skill_wind_active_kb_dist | skill_config | 120 | - | 10 | 300 | 无 | px | 击退距离 120px（沿路径后退，文档 §2.6 [P]）。 |
| skill_wind_active_stun_dur | skill_config | 1 | - | 0.5 | 10 | 无 | 秒 | 定身 1s（文档 §2.6 [P]）。 |
| skill_wind_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「持续气流」解锁养塔等级（建议 3）。 |
| skill_wind_p1_proc | skill_config | 20 | - | 0 | 100 | 无 | % | 每次攻击附加小幅击退概率 20%（文档 §2.6 [P]）。 |
| skill_wind_p1_kb_dist | skill_config | 30 | - | 10 | 300 | 无 | px | 小幅击退距离 30px（派生：文档「小幅击退」无 [P]，取 30px 延长怪在射程内时间）。 |
| skill_wind_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「逆风惩罚」解锁养塔等级（建议 5）。 |
| skill_wind_p2_slow | skill_config | 15 | - | 1 | 100 | 无 | % | 被击退怪移速 −15%（文档 §2.6 [P]）。 |
| skill_wind_p2_max_stack | skill_config | 3 | - | 1 | 10 | 无 | 层 | 逆风惩罚叠加上限 3 层（文档 §2.6 [P]）。 |

### 魔法塔 t_magic（真伤·魔免克星）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_magic_active_cd | skill_config | 20 | - | 1 | 120 | 无 | 秒 | 主动技「奥术爆发」冷却 20s（单体真伤+净化，中 CD）。 |
| skill_magic_active_truedmg_mult | skill_config | 3.0 | - | 1.0 | 10 | 无 | 倍 | 奥术爆发真伤倍率 3.0×（派生：文档只标 CD，伤害取 3× 塔基础，无视护甲+清增益/护盾）。 |
| skill_magic_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「奥术穿透」解锁养塔等级（建议 3）。 |
| skill_magic_p1_armor_pen | skill_config | 30 | - | 0 | 100 | 无 | % | 攻击无视 30% 护甲减免（文档 §2.6 [P]，强化真伤定位）。 |
| skill_magic_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「法力充能」解锁养塔等级（建议 5）。 |
| skill_magic_p2_cd_reduce | skill_config | 1.0 | - | 0.1 | 10 | 无 | 秒 | 每次击杀缩短主动技 CD 1s（文档 §2.6 [P]，击杀流循环）。 |

### 毒塔 t_poison（持续 DoT·克高 HP）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_poison_active_cd | skill_config | 16 | - | 1 | 120 | 无 | 秒 | 主动技「剧毒新星」冷却 16s（范围毒云，中低 CD）。 |
| skill_poison_active_dot | skill_config | 40 | - | 1 | 200 | 无 | 伤害/s | 剧毒新星 DoT 40/s（文档 §2.6 [P]）。 |
| skill_poison_active_dot_dur | skill_config | 4 | - | 0.5 | 10 | 无 | 秒 | 剧毒新星 DoT 持续 4s（文档 §2.6 [P]）+ 微减速。 |
| skill_poison_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「腐蚀」解锁养塔等级（建议 3）。 |
| skill_poison_p1_max_stack | skill_config | 5 | - | 1 | 20 | 无 | 层 | DoT 可叠 5 层（文档 §2.6 [P]，越肉掉血越快）。 |
| skill_poison_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「毒性传染」解锁养塔等级（建议 5）。 |
| skill_poison_p2_spread_radius | skill_config | 120 | - | 10 | 400 | 无 | px | 中毒怪死亡爆毒传染范围 120px（文档 §2.6 [P]）。 |

### 电塔 t_electric（连锁·克密集）
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| skill_electric_active_cd | skill_config | 14 | - | 1 | 120 | 无 | 秒 | 主动技「雷暴」冷却 14s（全场连锁，低 CD）。 |
| skill_electric_active_strikes | skill_config | 6 | - | 1 | 30 | 无 | 次 | 雷暴落雷次数 6（文档 §2.6 [P]）。 |
| skill_electric_passive1_lv | skill_config | 3 | - | 1 | 10 | 无 | 级 | 被动①「过载」解锁养塔等级（建议 3）。 |
| skill_electric_p1_jump_bonus | skill_config | 2 | - | 1 | 10 | 无 | 跳 | 连锁跳数 +2（文档 §2.6 [P]）。 |
| skill_electric_p1_recast_dmg | skill_config | 30 | - | 1 | 200 | 无 | % | 对同目标二次命中增伤 +30%（文档 §2.6 [P]）。 |
| skill_electric_passive2_lv | skill_config | 5 | - | 1 | 10 | 无 | 级 | 被动②「导电」解锁养塔等级（建议 5）。 |
| skill_electric_p2_vuln | skill_config | 20 | - | 1 | 100 | 无 | % | 被电塔命中的怪受他塔伤害 +20%（文档 §2.6 [P]，combo 放大 P4）。 |

## 备注 / 待裁定
- 养塔等级上限（passive1_lv/passive2_lv 的 max=10）取自本表假定塔最高等级 10，待与 S02 `tower_config` 对齐校准（max_level 字段以 S02 为准）。
- 派生数值（skill_*_active_aoe_mult / skill_magic_active_truedmg_mult / skill_wind_p1_kb_dist 等文档未显式 [P] 的主动伤害/小幅击退）已合理初填并标注「派生」，待试玩调优。
- **设计红线自检**：7 塔技能互补（单体/AOE/控/真伤/DoT/连锁/位移），无单一技能碾压；主动 cost=0 不争木；每塔仅 1 主动+2 被动，无主导策略/经济失衡/认知过载。
- 无 NEEDS-DESIGN 项：所有 [PLACEHOLDER]（§2.6 效果数值 + §3 表 active_cd/passive1_lv/passive2_lv + §2.4 cd 钳制）均已给初值。

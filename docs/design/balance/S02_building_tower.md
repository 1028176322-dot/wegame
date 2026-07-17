# 数值设计表：S02 建筑（塔）系统

> 关联 F 码：F2 F3 F4 · GDD：§5.1/§5.2/§5.7 · 设计文档：systems/S02_building_tower.md
> 说明：本表为该系统设计文档 §3 配置表（tower_config / upgrade_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| t_arrow_build_cost | tower_config | 100 | - | 10 | 500 | 无 | gold | 箭塔建造成本（首发，单体高频廉价） |
| t_arrow_max_level | tower_config | 15 | - | 1 | 30 | 无 | 级 | 箭塔软封顶等级（养塔 session 上限） |
| t_arrow_base_dps | tower_config | 30 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 箭塔 1 级 DPS，建塔时按 S29 当前等级单行加成 |
| t_arrow_growth | tower_config | 1.15 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.15^养塔级），参《绿色循环圈》养塔直觉 |
| t_arrow_range | tower_config | 140 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 箭塔射程，建塔时套 S29 range_mult |
| t_arrow_attack_speed | tower_config | 1.5 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 箭塔攻速，建塔时套 S29 atk_speed_mult |
| t_arrow_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 箭塔卖塔返还比例（与 S03 econ_sell_refund_rate 一致） |
| t_cannon_build_cost | tower_config | 160 | - | 10 | 500 | 无 | gold | 炮塔建造成本（首发，AOE 溅射） |
| t_cannon_max_level | tower_config | 15 | - | 1 | 30 | 无 | 级 | 炮塔软封顶等级 |
| t_cannon_base_dps | tower_config | 45 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 炮塔 1 级 DPS（溅射伤害另见 S05 combat_splash_radius） |
| t_cannon_growth | tower_config | 1.18 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.18^养塔级） |
| t_cannon_range | tower_config | 130 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 炮塔射程 |
| t_cannon_attack_speed | tower_config | 0.8 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 炮塔攻速（低频高伤） |
| t_cannon_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 炮塔卖塔返还比例 |
| t_ice_build_cost | tower_config | 120 | - | 10 | 500 | 无 | gold | 冰塔建造成本（首发，减速控制） |
| t_ice_max_level | tower_config | 12 | - | 1 | 30 | 无 | 级 | 冰塔软封顶等级（控制向，养成浅） |
| t_ice_base_dps | tower_config | 18 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 冰塔 1 级 DPS（减速见 S05 combat_slow_*） |
| t_ice_growth | tower_config | 1.15 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.15^养塔级） |
| t_ice_range | tower_config | 120 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 冰塔射程 |
| t_ice_attack_speed | tower_config | 1.0 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 冰塔攻速 |
| t_ice_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 冰塔卖塔返还比例 |
| t_wind_build_cost | tower_config | 140 | - | 10 | 500 | 无 | gold | 风塔建造成本（首发·DO 定稿，击退控制） |
| t_wind_max_level | tower_config | 12 | - | 1 | 30 | 无 | 级 | 风塔软封顶等级 |
| t_wind_base_dps | tower_config | 22 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 风塔 1 级 DPS（击退见 S28 技能/status_effect=knockback） |
| t_wind_growth | tower_config | 1.16 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.16^养塔级） |
| t_wind_range | tower_config | 110 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 风塔射程（近程控制） |
| t_wind_attack_speed | tower_config | 1.2 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 风塔攻速 |
| t_wind_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 风塔卖塔返还比例 |
| t_magic_build_cost | tower_config | 200 | - | 10 | 500 | 无 | gold | 魔法塔建造成本（解锁·S11/unlock_magic，破魔免） |
| t_magic_max_level | tower_config | 18 | - | 1 | 30 | 无 | 级 | 魔法塔软封顶等级（高阶主 DPS） |
| t_magic_base_dps | tower_config | 60 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 魔法塔 1 级 DPS（克制 magic_immune） |
| t_magic_growth | tower_config | 1.20 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.20^养塔级，高阶塔更强指数） |
| t_magic_range | tower_config | 150 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 魔法塔射程（远程） |
| t_magic_attack_speed | tower_config | 1.0 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 魔法塔攻速 |
| t_magic_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 魔法塔卖塔返还比例 |
| t_poison_build_cost | tower_config | 180 | - | 10 | 500 | 无 | gold | 毒塔建造成本（解锁·unlock_poison，DOT） |
| t_poison_max_level | tower_config | 15 | - | 1 | 30 | 无 | 级 | 毒塔软封顶等级 |
| t_poison_base_dps | tower_config | 25 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 毒塔 1 级 DPS（DOT 见 S05 combat_poison_*） |
| t_poison_growth | tower_config | 1.17 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.17^养塔级） |
| t_poison_range | tower_config | 120 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 毒塔射程 |
| t_poison_attack_speed | tower_config | 1.0 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 毒塔攻速 |
| t_poison_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 毒塔卖塔返还比例 |
| t_electric_build_cost | tower_config | 220 | - | 10 | 500 | 无 | gold | 电塔建造成本（解锁·unlock_thunder，连锁） |
| t_electric_max_level | tower_config | 18 | - | 1 | 30 | 无 | 级 | 电塔软封顶等级 |
| t_electric_base_dps | tower_config | 35 | - | 1 | 1000 | 套用 player_level_config[session_player_level].dmg_mult（单行查表,不累加） | 点 | 电塔 1 级 DPS（连锁见 S05 combat_chain_*） |
| t_electric_growth | tower_config | 1.19 | - | 1.1 | 3.0 | 无 | 倍/级 | 养塔指数（1.19^养塔级） |
| t_electric_range | tower_config | 140 | - | 50 | 400 | 套用 player_level_config[session_player_level].range_mult（单行查表,不累加） | px | 电塔射程 |
| t_electric_attack_speed | tower_config | 1.3 | - | 0.2 | 5 | 套用 player_level_config[session_player_level].atk_speed_mult（单行查表,不累加） | 次/秒 | 电塔攻速（高频连锁） |
| t_electric_sell_refund_rate | tower_config | 0.70 | - | 0.3 | 0.9 | 无 | % | 电塔卖塔返还比例 |
| t_wood_cost | upgrade_config | 20 | 线性 +10/级 | 5 | 999 | 无 | 木 | 养塔每级喂木量（session，每局重来）；首级 20，每级 +10，封顶 999；dps_mult 公式兜底 = growth^养塔级 |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- **S29 等级加成（要求 #4）**：塔的 `base_dps / range / attack_speed` 三项的 level_link 已明确为「套用 player_level_config[session_player_level].{dmg_mult|range_mult|atk_speed_mult}（单行查表,不累加）」——即仅取当前玩家等级那一行绝对值，绝不把 1..N 级求和（非 Σ/Π）。建塔时应用一次，玩家零操作。养塔 `growth` 与玩家等级无关（level_link=无），二者独立叠加：有效属性 = base × S29单行加成 × growth^养塔级。
- 7 塔 `growth` 取 1.15–1.20，贴近用户所给《绿色循环圈》养塔直觉 1.15^level，并让高阶解锁塔(魔法/电)成长略高形成长线差异。doc §3 建议 1.5–2.0x 仅作参考上界，初值偏保守，待试玩上调。
- 养塔 `t_wood_cost` 为全局统一曲线（养塔不区分塔种），与 `dps_mult=growth^养塔级` 共同决定 session 内强度。
- 各塔 `sell_refund_rate` 统一 0.70，与 S03 `econ_sell_refund_rate` 保持一致（防两表漂移）。

# 数值设计表：S29 玩家等级系统

> 关联 F 码：F45 · GDD：§5.9（玩家等级系统） · 设计文档：systems/S29_level_system.md
> 说明：本表为该系统设计文档 §3 `player_level_config` 与 `unlock_config` 中**所有 [PLACEHOLDER] 数值参数**的具体初值。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 plv_ / unlock_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（player_level_config / unlock_config）
- base：基础值（Lv1 / 初始状态）；曲线表每行为该等级快照
- growth：成长系数（等级曲线为非线性平滑，非每级累加；详情见曲线表）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式——本表自身即等级查表，**单行查表、不累加**；战斗内套用 `player_level_config[当前等级]` 那一行，历史行不参与计算
- unit：单位（级 / gold / 倍 / % / 条(Lives) / XP）
- description：含义与调优说明（含为何取此初值）

## 数值表 · 一、`player_level_config`（等级曲线 Lv1–Lv20，原子化 per-cell param_id）

> 每行原为行级 param_id（plv.L1…plv.L20），已按 DO 终审方案(b)原子展开为独立 per-cell param_id（`plv.L<n>.<field>`），**共 80 行**。战斗有效属性 = `tower_base × player_level_config[level].mult`，仅取当前等级一行。**单行查表、不累加**。

### xp_required（累计 XP 阈值，严格递增）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| plv.L1.xp_required | player_level_config | 0 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 本表自身查表(单行,不累加)；战斗内 `level = max{L \| xp_required[L] ≤ current_xp}` | XP | Lv1 累计 XP 阈值（起始 0） |
| plv.L2.xp_required | player_level_config | 100 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv2 累计 XP 阈值（100，级差 100） |
| plv.L3.xp_required | player_level_config | 250 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv3 累计 XP 阈值（250，级差 150） |
| plv.L4.xp_required | player_level_config | 450 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv4 累计 XP 阈值（450，级差 200） |
| plv.L5.xp_required | player_level_config | 700 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv5 累计 XP 阈值（700，级差 250） |
| plv.L6.xp_required | player_level_config | 1000 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv6 累计 XP 阈值（1000，级差 300） |
| plv.L7.xp_required | player_level_config | 1350 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv7 累计 XP 阈值（1350，级差 350） |
| plv.L8.xp_required | player_level_config | 1750 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv8 累计 XP 阈值（1750，级差 400） |
| plv.L9.xp_required | player_level_config | 2200 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv9 累计 XP 阈值（2200，级差 450） |
| plv.L10.xp_required | player_level_config | 2700 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv10 累计 XP 阈值（2700，级差 500） |
| plv.L11.xp_required | player_level_config | 3300 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv11 累计 XP 阈值（3300，级差 600） |
| plv.L12.xp_required | player_level_config | 4000 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv12 累计 XP 阈值（4000，级差 700） |
| plv.L13.xp_required | player_level_config | 4800 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv13 累计 XP 阈值（4800，级差 800） |
| plv.L14.xp_required | player_level_config | 5700 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv14 累计 XP 阈值（5700，级差 900） |
| plv.L15.xp_required | player_level_config | 6700 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv15 累计 XP 阈值（6700，级差 1000） |
| plv.L16.xp_required | player_level_config | 7800 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv16 累计 XP 阈值（7800，级差 1100） |
| plv.L17.xp_required | player_level_config | 9000 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv17 累计 XP 阈值（9000，级差 1200） |
| plv.L18.xp_required | player_level_config | 10300 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv18 累计 XP 阈值（10300，级差 1300） |
| plv.L19.xp_required | player_level_config | 11700 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv19 累计 XP 阈值（11700，级差 1400） |
| plv.L20.xp_required | player_level_config | 13200 | 非线性平滑(级差递增100→1700，累计阈值) | 0 | 13200 | 同上 | XP | Lv20 累计 XP 阈值（13200，级差 1500，封顶） |

### dmg_mult（全局塔伤害倍率，绝对值快照、不累加）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| plv.L1.dmg_mult | player_level_config | 1.00 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 本表自身查表(单行,不累加)；战斗内 `tower_eff.dps = tower_base × player_level_config[level].dmg_mult` | 倍 | Lv1 全局塔伤害倍率（绝对值快照，不累加） |
| plv.L2.dmg_mult | player_level_config | 1.04 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv2 全局塔伤害倍率 |
| plv.L3.dmg_mult | player_level_config | 1.07 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv3 全局塔伤害倍率 |
| plv.L4.dmg_mult | player_level_config | 1.10 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv4 全局塔伤害倍率 |
| plv.L5.dmg_mult | player_level_config | 1.13 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv5 全局塔伤害倍率 |
| plv.L6.dmg_mult | player_level_config | 1.16 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv6 全局塔伤害倍率 |
| plv.L7.dmg_mult | player_level_config | 1.19 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv7 全局塔伤害倍率 |
| plv.L8.dmg_mult | player_level_config | 1.22 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv8 全局塔伤害倍率 |
| plv.L9.dmg_mult | player_level_config | 1.25 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv9 全局塔伤害倍率 |
| plv.L10.dmg_mult | player_level_config | 1.28 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv10 全局塔伤害倍率 |
| plv.L11.dmg_mult | player_level_config | 1.31 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv11 全局塔伤害倍率 |
| plv.L12.dmg_mult | player_level_config | 1.34 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv12 全局塔伤害倍率 |
| plv.L13.dmg_mult | player_level_config | 1.36 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv13 全局塔伤害倍率 |
| plv.L14.dmg_mult | player_level_config | 1.39 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv14 全局塔伤害倍率 |
| plv.L15.dmg_mult | player_level_config | 1.41 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv15 全局塔伤害倍率 |
| plv.L16.dmg_mult | player_level_config | 1.43 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv16 全局塔伤害倍率 |
| plv.L17.dmg_mult | player_level_config | 1.45 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv17 全局塔伤害倍率 |
| plv.L18.dmg_mult | player_level_config | 1.47 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv18 全局塔伤害倍率 |
| plv.L19.dmg_mult | player_level_config | 1.49 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv19 全局塔伤害倍率 |
| plv.L20.dmg_mult | player_level_config | 1.50 | 非线性平滑(L1=1.0→L20=1.50，前载明显) | 1.0 | 1.5 | 同上 | 倍 | Lv20 全局塔伤害倍率（封顶 1.5，落在文档范围 1.0–5.0 内） |

### range_mult（全局射程倍率，绝对值快照、不累加）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| plv.L1.range_mult | player_level_config | 1.00 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 本表自身查表(单行,不累加) | 倍 | Lv1 全局射程倍率（绝对值快照，不累加） |
| plv.L2.range_mult | player_level_config | 1.02 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv2 全局射程倍率 |
| plv.L3.range_mult | player_level_config | 1.04 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv3 全局射程倍率 |
| plv.L4.range_mult | player_level_config | 1.06 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv4 全局射程倍率 |
| plv.L5.range_mult | player_level_config | 1.08 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv5 全局射程倍率 |
| plv.L6.range_mult | player_level_config | 1.10 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv6 全局射程倍率 |
| plv.L7.range_mult | player_level_config | 1.12 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv7 全局射程倍率 |
| plv.L8.range_mult | player_level_config | 1.14 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv8 全局射程倍率 |
| plv.L9.range_mult | player_level_config | 1.16 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv9 全局射程倍率 |
| plv.L10.range_mult | player_level_config | 1.17 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv10 全局射程倍率 |
| plv.L11.range_mult | player_level_config | 1.19 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv11 全局射程倍率 |
| plv.L12.range_mult | player_level_config | 1.20 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv12 全局射程倍率 |
| plv.L13.range_mult | player_level_config | 1.22 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv13 全局射程倍率 |
| plv.L14.range_mult | player_level_config | 1.23 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv14 全局射程倍率 |
| plv.L15.range_mult | player_level_config | 1.25 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv15 全局射程倍率 |
| plv.L16.range_mult | player_level_config | 1.26 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv16 全局射程倍率 |
| plv.L17.range_mult | player_level_config | 1.27 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv17 全局射程倍率 |
| plv.L18.range_mult | player_level_config | 1.28 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv18 全局射程倍率 |
| plv.L19.range_mult | player_level_config | 1.29 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv19 全局射程倍率 |
| plv.L20.range_mult | player_level_config | 1.30 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv20 全局射程倍率（封顶 1.3，落在文档范围 1.0–3.0 内） |

### atk_speed_mult（全局攻速倍率，绝对值快照、不累加）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| plv.L1.atk_speed_mult | player_level_config | 1.00 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 本表自身查表(单行,不累加) | 倍 | Lv1 全局攻速倍率（绝对值快照，不累加） |
| plv.L2.atk_speed_mult | player_level_config | 1.02 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv2 全局攻速倍率 |
| plv.L3.atk_speed_mult | player_level_config | 1.04 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv3 全局攻速倍率 |
| plv.L4.atk_speed_mult | player_level_config | 1.06 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv4 全局攻速倍率 |
| plv.L5.atk_speed_mult | player_level_config | 1.08 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv5 全局攻速倍率 |
| plv.L6.atk_speed_mult | player_level_config | 1.10 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv6 全局攻速倍率 |
| plv.L7.atk_speed_mult | player_level_config | 1.11 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv7 全局攻速倍率 |
| plv.L8.atk_speed_mult | player_level_config | 1.13 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv8 全局攻速倍率 |
| plv.L9.atk_speed_mult | player_level_config | 1.15 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv9 全局攻速倍率 |
| plv.L10.atk_speed_mult | player_level_config | 1.16 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv10 全局攻速倍率 |
| plv.L11.atk_speed_mult | player_level_config | 1.18 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv11 全局攻速倍率 |
| plv.L12.atk_speed_mult | player_level_config | 1.19 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv12 全局攻速倍率 |
| plv.L13.atk_speed_mult | player_level_config | 1.21 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv13 全局攻速倍率 |
| plv.L14.atk_speed_mult | player_level_config | 1.22 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv14 全局攻速倍率 |
| plv.L15.atk_speed_mult | player_level_config | 1.24 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv15 全局攻速倍率 |
| plv.L16.atk_speed_mult | player_level_config | 1.25 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv16 全局攻速倍率 |
| plv.L17.atk_speed_mult | player_level_config | 1.26 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv17 全局攻速倍率 |
| plv.L18.atk_speed_mult | player_level_config | 1.27 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv18 全局攻速倍率 |
| plv.L19.atk_speed_mult | player_level_config | 1.29 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv19 全局攻速倍率 |
| plv.L20.atk_speed_mult | player_level_config | 1.30 | 非线性平滑(L1=1.0→L20=1.30) | 1.0 | 1.3 | 同上 | 倍 | Lv20 全局攻速倍率（封顶 1.3，落在文档范围 1.0–3.0 内） |

> `xp_required`：累计阈值，每级严格递增（L1=0→L20=13200，级差从100→1500，平滑升曲线）。
> `dmg_mult`：L1=1.0→L20=1.50（前载明显，前期手感强）；`range_mult`/`atk_speed_mult`：L1=1.0→L20=1.30。全部落在文档范围（dmg 1.0–5.0、range/atk_speed 1.0–3.0）。值以各 atomic param_id 为准。

## 数值表 · 二、`unlock_config`（解锁门槛 + meta_upgrade 效果）

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| plv_max_level | player_level_config | 20 | - | 1 | 20 | 无 | 级 | 玩家等级上限（文档 §3.1 `level 1–[PLACEHOLDER]`），曲线覆盖 Lv1–Lv20。 |
| unlock_magic_required_level | unlock_config | 3 | - | 1 | 20 | 无 | 级 | 魔法塔(t_magic)解锁所需玩家等级。权威阈值，B 域 S11 旧节点对齐。 |
| unlock_poison_required_level | unlock_config | 6 | - | 1 | 20 | 无 | 级 | 毒塔(t_poison)解锁所需玩家等级。 |
| unlock_electric_required_level | unlock_config | 10 | - | 1 | 20 | 无 | 级 | 电塔解锁所需玩家等级。⚠️ target_ref 采用 **t_electric**（S02/S28 权威命名），非 S29 文档示例的 t_thunder，见备注。 |
| unlock_gold_required_level | unlock_config | 2 | - | 1 | 20 | 无 | 级 | 永久升级·起始金币+% 解锁等级。 |
| unlock_lives_required_level | unlock_config | 4 | - | 1 | 20 | 无 | 级 | 永久升级·漏怪容错+Lives 解锁等级。 |
| unlock_wood_required_level | unlock_config | 8 | - | 1 | 20 | 无 | 级 | 永久升级·木头产出+% 解锁等级。 |
| unlock_leaderboard_required_level | unlock_config | 12 | - | 1 | 20 | 无 | 级 | 解锁排行榜(S13)所需等级。 |
| unlock_levels_required_level | unlock_config | 5 | - | 1 | 20 | 无 | 级 | 解锁多关卡(S14)所需等级。 |
| unlock_gold_effect_value | unlock_config | 20 | - | 0 | 100 | 无 | % | 永久升级·起始金币 +20%（start_gold_mult）。经济类，避开 dmg/range/atk_speed 防双重计算。 |
| unlock_lives_effect_value | unlock_config | 2 | - | 1 | 10 | 无 | 条(Lives) | 永久升级·漏怪容错 +2 Lives（leak_tolerance）。 |
| unlock_wood_effect_value | unlock_config | 20 | - | 0 | 100 | 无 | % | 永久升级·木头产出 +20%（wood_gain_mult）。 |

## 备注 / 待裁定

### NEEDS-DESIGN（待 DO 裁定）
1. **电塔 tower_id 命名不一致**：S02/S28 定义电塔为 `t_electric`，而 S11 与 S29 §3.2 示例用 `t_thunder`。本表 `unlock_electric_required_level` 的 target_ref 采用 **t_electric**（塔权威命名），但需在全局统一电塔 id，否则解锁写 S2 可建列表时会查不到。**建议 DO 裁定统一为 t_electric 或 t_thunder。**
2. **xp_gain 归属**：S29 文档 §0/§2 提及 `xp_gain（[PLACEHOLDER]）` 为每局结算产出，但该字段属 **S08 结算系统**，本表未含；其初值由 S08 裁定（建议 S08 平衡表补充）。
3. **S18 存档 schema 补字段**：`player_level`/`current_xp`/解锁态集合需在 S18 `save_schema` 落实（S29 §5.3 已列必做），否则跨局持久化无法落地。

### 已给初值说明
- 8 个 `required_level`（魔3/毒6/电10/金2/容错4/木8/排行12/多关5）+ 3 个 `effect_value`（金+20%/容错+2Lives/木+20%）+ `plv_max_level=20` 均已按任务指令填初值。
- 等级曲线 20 级 × 4 字段 = **80 个原子 param_id**（`plv.L<n>.xp_required` / `.dmg_mult` / `.range_mult` / `.atk_speed_mult`），`xp_required` 严格递增、倍率为绝对值快照，L20=1.5/1.3/1.3，体现**单行查表、不累加**。
- meta_upgrade 三类（start_gold/leak_tolerance/wood_gain）刻意避开 dmg/range/atk_speed，与 §3.1 等级加成从语义上避免双重计算。
- 无其它 NEEDS-DESIGN 项：所有 [PLACEHOLDER] 均已给初值。

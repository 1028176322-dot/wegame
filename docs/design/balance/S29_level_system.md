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
- unit：单位（级 / gold / 倍 / % / 条(Lives)）
- description：含义与调优说明（含为何取此初值）

## 数值表 · 一、`player_level_config`（等级曲线 Lv1–Lv20，单行查表、不累加）

> 每行 `dmg_mult/range_mult/atk_speed_mult` 为该等级的**绝对值快照**（非增量）。战斗有效属性 = `tower_base × player_level_config[level].mult`，仅取当前等级一行。
> 全局映射：module=player_level_config；base=L1(0 / 1.0 / 1.0 / 1.0)；growth=非线性平滑(锚点见下表)；min=1.0(倍率下限，钳制)；max=L20(13200 / 1.5 / 1.3 / 1.3)；level_link=本表自身查表(单行,不累加)；unit=级/gold/倍。

| param_id | level | xp_required(累计,严格递增) | dmg_mult | range_mult | atk_speed_mult |
|---|---|---|---|---|---|
| plv.L1 | 1 | 0 | 1.00 | 1.00 | 1.00 |
| plv.L2 | 2 | 100 | 1.04 | 1.02 | 1.02 |
| plv.L3 | 3 | 250 | 1.07 | 1.04 | 1.04 |
| plv.L4 | 4 | 450 | 1.10 | 1.06 | 1.06 |
| plv.L5 | 5 | 700 | 1.13 | 1.08 | 1.08 |
| plv.L6 | 6 | 1000 | 1.16 | 1.10 | 1.10 |
| plv.L7 | 7 | 1350 | 1.19 | 1.12 | 1.11 |
| plv.L8 | 8 | 1750 | 1.22 | 1.14 | 1.13 |
| plv.L9 | 9 | 2200 | 1.25 | 1.16 | 1.15 |
| plv.L10 | 10 | 2700 | 1.28 | 1.17 | 1.16 |
| plv.L11 | 11 | 3300 | 1.31 | 1.19 | 1.18 |
| plv.L12 | 12 | 4000 | 1.34 | 1.20 | 1.19 |
| plv.L13 | 13 | 4800 | 1.36 | 1.22 | 1.21 |
| plv.L14 | 14 | 5700 | 1.39 | 1.23 | 1.22 |
| plv.L15 | 15 | 6700 | 1.41 | 1.25 | 1.24 |
| plv.L16 | 16 | 7800 | 1.43 | 1.26 | 1.25 |
| plv.L17 | 17 | 9000 | 1.45 | 1.27 | 1.26 |
| plv.L18 | 18 | 10300 | 1.47 | 1.28 | 1.27 |
| plv.L19 | 19 | 11700 | 1.49 | 1.29 | 1.29 |
| plv.L20 | 20 | 13200 | 1.50 | 1.30 | 1.30 |

- `xp_required`：累计阈值，每级严格递增（L1=0 起步，级差随等级放大 100→1700，平滑升曲线）。
- `dmg_mult`：L1=1.0 → L20=1.50（前载更明显，前期手感强）；`range_mult`/`atk_speed_mult`：L1=1.0 → L20=1.30。全部落在文档范围（dmg 1.0–5.0、range/atk_speed 1.0–3.0）。

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
- 等级曲线 20 行 `xp_required` 严格递增、`dmg/range/atk_speed_mult` 为绝对值快照，L20=1.5/1.3/1.3，体现**单行查表、不累加**。
- meta_upgrade 三类（start_gold/leak_tolerance/wood_gain）刻意避开 dmg/range/atk_speed，与 §3.1 等级加成从语义上避免双重计算。
- 无其它 NEEDS-DESIGN 项：所有 [PLACEHOLDER] 均已给初值。

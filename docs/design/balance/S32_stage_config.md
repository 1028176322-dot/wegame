# 数值设计表：S32 关卡内容配置系统

> 关联 F 码：F17（续 S14）· GDD：§5.5/§5.6 · 设计文档：systems/S32_stage_config.md
> 说明：本表为该系统设计文档 §3 配置表（stage_config）与正文中所有 `[PLACEHOLDER]` 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 stg_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（首关 / 初始状态）
- growth：成长系数（如 growth^关、+x%/关、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 S14.diff_mult 乘算(运营粗调)" / "套用 S29 player_level 门槛" / "无"）
- unit：单位（关 / 波 / 倍 / 个 / gold / meta_res / 级）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| stg_total_count | stage_config(global) | 12 | - | 10 | 20 | 无 | 关 | 首版关卡总数（10–20 区间初值，可微调）。非 NEEDS-DESIGN，已给初值 |
| stg_wave_count | stage_config(stage) | 8 | 线性 +2/关 | 8 | 50 | 无 | 波 | 每关波数 = 8 + 2×(N-1)，封顶 S4 wave_total_waves=50。首关低压教学 8 波→末关 30 波 |
| stg_hp_scale | stage_config(stage) | 1.0 | 1.05^(关-1) | 1.0 | 3.0 | 套用 S14.diff_mult 乘算(运营粗调) | 倍 | 敌血缩放基线。首关 1.00(低压教学)→末关 1.71(高难)。最终 = hp_scale × S14.diff_mult |
| stg_speed_scale | stage_config(stage) | 1.0 | 1.02^(关-1) | 1.0 | 2.0 | 套用 S14.diff_mult 乘算(运营粗调) | 倍 | 敌速缩放基线。首关 1.00→末关 1.24。最终 = speed_scale × S14.diff_mult |
| stg_boss_every | stage_config(global) | 10 | - | 5 | 20 | 无 | 波 | Boss 间隔（同 S4 boss_every=10）；且每关末波恒为 Boss(高潮)。调优杆 |
| stg_boss_count | stage_config(stage) | 1 | 派生 floor((waves-1)/10)+1 | 1 | - | 无 | 个 | 每关 Boss 数 = floor((waves-1)/10)+1（含末波）。随波数增长 1→3 |
| stg_reward_gold_clear | stage_config(stage) | 50 | 线性 +10/关 | 0 | 9999 | 无 | gold | 清场一次性 session 金（结算入元进度）。第 N 关 = 50+10×(N-1)。与 S4 击杀金互不重叠 |
| stg_reward_meta_first | stage_config(stage) | 100 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | 首通元进度（对齐 S14 level_reward）。第 N 关 = 100+50×(N-1)。首通/重复≈1/5 防刷主导策略 |
| stg_reward_meta_repeat | stage_config(stage) | 20 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | 重复通关元进度。第 N 关 = 20+10×(N-1)。远低于首通，抑制刷资源 |
| stg_unlock_level | stage_config(stage) | 1 | +1/每3关 | 1 | S29.max_level | 套用 S29 player_level 门槛 | 级 | 进关所需 S29 等级（与 S14.pre_level 串行解锁叠加为双闸门）。第 N 关 = 1+floor((N-1)/3)，初值 1/1/1/2/2/2/3/3/3/4/4/4 |

## 逐关派生汇总表（12 关，依据上方 base+growth 公式展开；全部为可推导初值）

| stage_id | waves | hp_scale | speed_scale | boss_count | reward_gold | meta_first | meta_repeat | unlock_level |
|---|---|---|---|---|---|---|---|---|
| st_01 | 8 | 1.00 | 1.00 | 1 | 50 | 100 | 20 | 1 |
| st_02 | 10 | 1.05 | 1.02 | 1 | 60 | 150 | 30 | 1 |
| st_03 | 12 | 1.10 | 1.04 | 2 | 70 | 200 | 40 | 1 |
| st_04 | 14 | 1.16 | 1.06 | 2 | 80 | 250 | 50 | 2 |
| st_05 | 16 | 1.22 | 1.08 | 2 | 90 | 300 | 60 | 2 |
| st_06 | 18 | 1.28 | 1.10 | 2 | 100 | 350 | 70 | 2 |
| st_07 | 20 | 1.34 | 1.13 | 2 | 110 | 400 | 80 | 3 |
| st_08 | 22 | 1.41 | 1.15 | 3 | 120 | 450 | 90 | 3 |
| st_09 | 24 | 1.48 | 1.17 | 3 | 130 | 500 | 100 | 3 |
| st_10 | 26 | 1.55 | 1.20 | 3 | 140 | 550 | 110 | 4 |
| st_11 | 28 | 1.63 | 1.22 | 3 | 150 | 600 | 120 | 4 |
| st_12 | 30 | 1.71 | 1.24 | 3 | 160 | 650 | 130 | 4 |

> 公式速查：`waves=8+2×(N-1)`；`hp_scale=1.05^(N-1)`；`speed_scale=1.02^(N-1)`；`boss_count=floor((waves-1)/10)+1`；`reward_gold=50+10×(N-1)`；`meta_first=100+50×(N-1)`；`meta_repeat=20+10×(N-1)`；`unlock_level=1+floor((N-1)/3)`。

## 无尽模式（Endless Mode）数值表

> 对应设计文档 §3.1 `endless_config`。无尽模式为独立生存模式（stage_type=endless），不引用预置 wave_table，敌群由 S04 按 wave 序号代入下方公式程序化生成（接 S31 enemy_id）。所有数值为初值/待试玩调优。

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| stg_endless_k_hp | endless_config | 0.05 | - | 0.01 | 0.30 | 无 | 倍/波 | 无尽敌血每波线性增量 k_hp：hp_scale = 1 + (wave-1)×k_hp。初值 0.05 → 波50 约 3.45×；乘 S14.diff_mult；上限钳 3.0 防失控（同 stg_hp_scale） |
| stg_endless_k_speed | endless_config | 0.02 | - | 0.005 | 0.20 | 无 | 倍/波 | 无尽敌速每波线性增量 k_speed：speed_scale = 1 + (wave-1)×k_speed。初值 0.02 → 波50 约 1.98×；钳 2.0 |
| stg_endless_boss_every | endless_config | 10 | - | 5 | 20 | 无 | 波 | 无尽 Boss 周期：每 N 波出 Boss（同 stg_boss_every / S4 boss_every）。初值 10 |
| stg_endless_score_wave | endless_config | 100 | - | 1 | 100000 | 无 | 分/波 | 计分权重 w_wave：score += wave_reached × w_wave。初值 100（波权重远高于击杀，鼓励撑更久而非刷杀） |
| stg_endless_score_kill | endless_config | 5 | - | 1 | 1000 | 无 | 分/杀 | 计分权重 w_kill：score += total_kills × w_kill。初值 5 |
| stg_endless_reward_gold | endless_config | 10 | - | 0 | 9999 | 无 | gold/波 | 每波结算金：gold_total = per_wave × wave_reached → 元进度(S11/S08)。初值 10 |
| stg_endless_reward_wood | endless_config | 2 | - | 0 | 9999 | 无 | wood/波 | 每波结算木：wood_total = per_wave × wave_reached → session 木(S03)。初值 2（接 S03 铁律：session，非持久化；见一致性提示） |
| stg_endless_unlock_level | endless_config | 1 | - | 1 | S29.max_level | 套用 S29 player_level 门槛 | 级 | 进入无尽所需 S29 等级（与 S14 入口解锁叠加双闸门）。初值 1（全员可进，降低门槛鼓励尝试） |
| stg_endless_max_wave_cap | endless_config | 0 | - | 0 | 100000 | 无 | 波 | 无尽封顶波数；0=无上限(真无限)。初值 0。结构封顶另由 S4 wave_total_waves 上限兜底防溢出 |

> 无尽地图复用标准地图变体（`endless_config.map_variant` 固定 "map_01"，非调优参数，不入本数值表）。计分公式：`score = wave_reached × stg_endless_score_wave + total_kills × stg_endless_score_kill`。

## 备注 / 待裁定 / NEEDS-DESIGN

- **本系统唯一硬 NEEDS-DESIGN：S31 敌群原型系统未建**。`enemy_composition`/`boss_schedule` 引用的 `enemy_id` 目录为 **provisional 契约**，待 S31 定稿冻结。provisional 目录（供美术占位资产与 E04 兜底参考）：
  - 常规敌（接 GDD §5.6 克制）：`e_goblin`(none) / `e_light`(light) / `e_heavy`(heavy) / `e_poison`(poison) / `e_magic_immune`(magic_immune) / `e_air`(air,需对空塔)
  - Boss（接 S4 boss_mechanic）：`b_goblin_king`(heavy+speedup) / `b_lich`(magic_immune+heal_cut) / `b_lava_demon`(heavy+heal_cut) / `b_wyrm`(air+heavy+speedup)
  - **须先建 S31 并冻结上述 enemy_id 目录，S32 的 E04（敌 id 非法兜底）方可关闭**。
- `unlock_level` 初值依赖 S29 `player_level` 可达性；S29 `xp_required`/max_level 仍为 `[PLACEHOLDER]`，故 unlock_level 为**暂定初值（已填实，待 S29 调优后校验）**，非 NEEDS-DESIGN。
- `stg_total_count=12` 为 10–20 区间内初值，可微调；调增需同步扩写 §4 美术资产清单与 S19 分包。
- 难度缩放与 S14 `diff_mult`/`reward_mult` **乘算**（非叠加定义），钳制 hp∈[1.0,3.0]、speed∈[1.0,2.0]，防失控（见设计文档 §5.3-2）。
- `reward` **不含木头**（木为 session，S03 铁律），仅 meta_first/meta_repeat(元进度) + gold_clear(session 金，结算入 meta)。
- 本系统所有 `[PLACEHOLDER]` 均已给初值（公式派生或固定），无遗漏 `[PLACEHOLDER]`；唯一 NEEDS-DESIGN 为 S31 enemy_id 目录（外部系统依赖）。
- **无尽模式（endless_config）已补数值**（见上「无尽模式数值表」）：k_hp/k_speed/boss_every/score_weights/reward_per_wave/unlock_level/max_wave_cap 均已给初值；其数值的**单一真理源在 `endless_config`**（balance `stg_endless_*`），S04 生成侧 `endless_*` 仅为镜像引用（见 balance/S04_wave.md），避免双重定义。无尽 `reward_per_wave.wood` 为 DO 裁定例外（结算发 session 木），与 S03 铁律的一致性以设计文档 §3.1 提示为准。

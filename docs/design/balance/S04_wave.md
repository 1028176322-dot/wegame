# 数值设计表：S04 波次系统

> 关联 F 码：F6 · GDD：§5.5 · 设计文档：systems/S04_wave.md
> 说明：本表为该系统设计文档 §3 配置表（wave_config 逐波 + 全局波数参数）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| wave_count | wave_config | 8 | 线性 +4/波 | 1 | 200 | 无 | 只 | 每波怪物数量，第 N 波 = 8 + 4×(N-1)，封顶 200（同屏上限另钳） |
| wave_spawn_interval | wave_config | 1.2 | 线性 -0.03/波 | 0.1 | 10 | 无 | 秒 | 出场间隔，第 N 波 = max(0.4, 1.2-0.03×(N-1))，后期更密 |
| wave_base_hp | wave_config | 30 | 1.18^波 | 1 | 100000 | 无 | 点 | 本波怪物基础血量，第 N 波 = 30×1.18^(N-1)，指数难度 |
| wave_prep_time | wave_config | 8 | 线性 -0.1/波 | 0 | 30 | 无 | 秒 | 准备期，第 N 波 = max(3, 8-0.1×(N-1))，末段留最少决策窗口 |
| wave_reward_mult | wave_config | 1.0 | 线性 +0.04/波 | 0.5 | 5 | 无 | 倍 | 本波奖励倍率(金)，第 N 波 = min(3, 1.0+0.04×(N-1)) |
| wave_drop_wood_chance | wave_config | 0.15 | 线性 +0.005/波 | 0 | 1 | 无 | % | 每只怪掉木概率，第 N 波 = min(0.6, 0.15+0.005×(N-1))；木主源(session) |
| wave_drop_wood_amount | wave_config | 2 | 线性 +0.15/波 | 1 | 999 | 无 | 木 | 命中掉木量，第 N 波 = min(30, 2+0.15×(N-1)) |
| wave_spawn_loops | wave_config | 2 | - | 1 | 2 | 无 | 圈 | 本波怪绕圈数，须 ≤ sys_loop_count(=2)，初值等同地图 loop_count |
| wave_total_waves | wave_global | 50 | - | 10 | 100 | 无 | 波 | 单局总波数，参 GDD 直觉 50；P5 时长硬约束 |
| wave_boss_every | wave_global | 10 | - | 5 | 20 | 无 | 波 | 每 N 波一个 Boss，参 GDD 直觉 10；情绪高点 |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- 逐波参数以「base + 随波次 growth」模型给出，第 N 波值 = base + growth×(N-1)（指数项按 1.18^波）。具体每波行可在 `wave_config` 按此公式展开；引擎也可在运行时按公式推导以减少配置行。
- `wave_spawn_loops` 上限锁为 `sys_loop_count=2`（见 S01），避免“绕圈数 > 地图圈数”的非法配置。
- 木供给（drop_wood_chance/amount）为 session 木主源，Boss 波可在具体行上配更高掉率作为养塔关键木点（初值未单列 Boss 行，待试玩补）。
- 本系统参数与玩家等级(S29)无关，level_link 全为"无"。

## 无尽生成参数（Endless Generation · 接 S32.endless_config）

> 对应 S04 §2.5 无尽波次生成。无尽缩放系数与 Boss 周期的**单一真理源在 `S32.endless_config`**（balance `stg_endless_*`）。本表 `endless_*` 为 S04 生成侧的**镜像引用**（base 列填与 S32 相同初值，仅用于 S04 代码侧读取，不独立调优，避免双重定义）。

| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| endless_hp_k | endless_gen | 0.05 | - | 0.01 | 0.30 | 无 | 倍/波 | = S32.endless_config.stg_endless_k_hp（镜像）。无尽敌血每波增量 k_hp；S04 生成时读取，不独立调优 |
| endless_speed_k | endless_gen | 0.02 | - | 0.005 | 0.20 | 无 | 倍/波 | = S32.endless_config.stg_endless_k_speed（镜像）。无尽敌速每波增量 k_speed |
| endless_boss_n | endless_gen | 10 | - | 5 | 20 | 无 | 波 | = S32.endless_config.stg_endless_boss_every（镜像）。无尽 Boss 周期（每 N 波） |

> 单一真理源声明：`endless_hp_k`/`endless_speed_k`/`endless_boss_n` 的权威值与调优均在 `balance/S32_stage_config.md` 的 `stg_endless_*`；本表仅作 S04 生成模块的消费引用。若二者出现分歧，以 S32 为准。

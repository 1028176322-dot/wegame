<!-- 编码: UTF-8 -->
# 系统策划案：S4 波次系统 (Wave System)

> 归属域：A 核心战斗域 · 层级/优先级：MVP / P0 · 关联 F 码：F6 · 关联：GDD §5.5；SYSTEM_BREAKDOWN §S4
> 状态：v0.2-detailed · 日期 2026-07-17
> 版本说明：在 v0.1-draft 基础上补全 像素级 UI 线框 / 状态机 / 时序图 / 异常边界用例 / 完整配置字段与多行示例 / 美术资源帧数·分辨率·格式·切片。
> **v0.2-rev（耦合重构）：** 按 DO 新规——**木 = session 货币，主源 = 怪物概率掉落**。新增 `wave_config.drop_wood_chance` / `drop_wood_amount`（每波配置，全 `[PLACEHOLDER]`），命中则在怪死亡时向 S03 累加 session 木（接 S28 木掉落实时指示）。木不再有木房产木/通关木奖励来源。
> 平衡数值（单局波数、Boss 频率、每波数量/间隔/准备期/奖励倍率/怪物血量、掉木率/掉木量等）保持 `[PLACEHOLDER]`，仅标注"调优杆"，禁止硬编码。

---

## 1. 系统 UI 布局

### 1.1 布局层级（z 轴，HUD 内）

| 层级 z | 名称 | 说明 |
|---|---|---|
| 45 | 波次指示 | 顶部中："第 X / Y 波" + 进度条 |
| 46 | 准备期倒计时 / 敌预览 | 出怪前显示 |
| 60 | Boss 预警 | 全屏闪，Boss 波前 2s |

### 1.2 像素级线框（750 × 1334）

```
  (0,0)┌─────────────────────────────────────────── 750 ──┐
       │ 顶栏 z45 [金] [第 X / Y 波 ▓▓▓░░] [木] [♥]       │ y=20..90
       │                                                │
       │ 准备期: [准备 8s ▓▓▓▓▓░░] (z46)                  │ y=120
       │ 敌预览: [🐉轻甲][🛡重甲][✨魔免] (z46)            │ y=160
       │        （战场：怪物沿路径出怪）                   │
       │                                                │
       │  ┌── BOSS 来袭!! ──┐  (z60 全屏红闪 2s)         │
       │  │      ⚠ BOSS ⚠    │                            │
       │  └─────────────────┘                            │
       └──────────────────────────────────────────── 1334 ┘
```

### 1.3 组件表（x,y 左上角；w×h；z）

| 组件 | 坐标(x,y) | 尺寸(w×h) | z | 响应行为 |
|---|---|---|---|---|
| 波次文本 | (375,40) 居中 | 文本 28px | 45 | 静态刷新 |
| 波次进度条 | (225,70) 居中 | 300×16 | 45 | 本波进度动画 |
| 准备倒计时 | (225,120) | 300×24 | 46 | 倒计时动画 |
| 敌预览条 | (75,160) | 600×64 | 46 | 展示本波怪图标+护甲色 |
| Boss 预警 | 全屏居中 (375,667) | 大字 64px + 屏闪 | 60 | 2s 后消失，不可点 |

### 1.4 交互流程图（mermaid flowchart）

```mermaid
flowchart TD
    A[开局/上波清空] --> B{还有下一波?}
    B -->|否| C[胜利 S8]
    B -->|是| D{下一波=Boss?}
    D -->|是| E[Boss预警 2s z60]
    D -->|否| F[准备期 显示敌预览]
    E --> F
    F --> G[倒计时归零 → 出怪 S5沿S1]
    G --> H{本波清完?}
    H -->|否| G
    H -->|是| A
```

---

## 2. 逻辑功能

### 2.1 功能模块表（触发 / 处理 / 输出）

| 模块 | 触发条件 | 处理流程（正常） | 输出 |
|---|---|---|---|
| 波次调度 | 上一波清空/超时 | 取 `wave_config[next]` → 进入准备期 → 倒计时 → 出怪 | 怪物生成指令(S5) |
| 怪物生成 | 出怪期 | 按 count/interval 沿 S1 路径产怪，赋 armor/type | 战场怪物流 |
| 护甲/克制 | 怪物生成 | 赋 `armor_type` → S5 按塔 type 算克制系数 | 伤害差异 |
| 类型波 | 特定 wave | 空军(上层z)/魔免(需物理)/重甲(需魔法) 标记 | 决策压力 |
| Boss 波 | 到 Boss 节点 | 生成 Boss（高血+特殊）→ 触发预警 | 高难威胁 |
| 掉木产出 | 怪死亡(S5 回调) | 按 `drop_wood_chance` 掷骰命中 → 向 S03 累加 `drop_wood_amount`(session 木) | 木主源（接 S03/S28 飘字） |
| 波间节奏 | 每波结束 | 切准备期，开放建/养窗口 | 决策窗口 |
| 无尽生成 | 无尽模式每波 | 读 S32.endless_config → 按 wave 序号代入难度公式 + 选 S31 `enemy_id` 组成敌群（普通波/Boss波）；不查 `wave_table` | 无尽敌群 |

### 2.2 状态机（mermaid stateDiagram-v2 — 波次状态）

```mermaid
stateDiagram-v2
    [*] --> PrepPhase
    PrepPhase --> BossWarning : 下一波是Boss
    PrepPhase --> SpawnPhase : 倒计时结束(普通波)
    BossWarning --> SpawnPhase : 2s预警后
    SpawnPhase --> ClearCheck : 本波生成完毕
    ClearCheck --> PrepPhase : 清完 且 非末波
    ClearCheck --> Victory : 清完 且 末波→S8
    SpawnPhase --> Paused : onHide S20
    Paused --> SpawnPhase : onShow S20
```

> **无尽模式变体（stage_type=endless）**：无 `Victory` 终态。波次状态机退化为 `PrepPhase ⇄ SpawnPhase ⇄ ClearCheck` 的**无限循环**，仅 `SpawnPhase → Lives=0 → FailSettle` 一条退出路径（漏光 Lives 即结束）。`boss_every_n_waves` 周期在 `PrepPhase` 前插入 `BossWarning`。详见 §2.5。

### 2.3 时序流程图（mermaid sequenceDiagram — 一波生命周期）

```mermaid
sequenceDiagram
    participant S4 as 波次系统
    participant S7 as HUD
    participant S5 as 战斗系统
    participant S1 as 地图系统
    participant S6 as 漏怪系统
    S4->>S7: 进入准备期(敌预览+倒计时)
    S7-->>S4: 倒计时归零
    S4->>S5: 生成怪物(count/interval/armor)
    S5->>S1: 沿 path_points 布怪
    loop 每怪
        S1->>S6: 到终点→漏怪回调
        S5->>S4: 击杀/存活计数
    end
    S4->>S4: 本波清空判定
    alt 末波
        S4->>S8: 胜利结算
    else 非末波
        S4->>S7: 下一波准备期
    end
```

### 2.4 异常与边界用例表

| 场景 | 触发条件 | 处理流程 | 输出 / 兜底 |
|---|---|---|---|
| 网络中断 | S21 远程波表拉取失败 | 用本地默认 10 波 | 不阻塞 |
| 切后台（S20） | `onHide` | 生成计时挂起；恢复续发 | 无重复/漏发 |
| 数据损坏（S18） | `wave_config` 损坏 | 用内置默认 10 波 + 记 S25 | 可玩 |
| 并发操作 | 加速(S7 2x) + 暂停 | 统一 `game_speed` 乘子，暂停优先 | 计时一致 |
| 数值极值 | `count` 极大 | 限制同屏上限（如 ≤60），分批生成 | 防卡顿 |
| 数值极值 | `spawn_interval`=0 | 整波同时出，受同屏上限钳制 | 不崩 |
| 数值极值 | `prep_time`=0 | 直接出怪（无准备期） | 仍可玩 |
| 数值极值 | 怪物 `hp` 异常(≤0) | 钳制最小 1 | 正常死亡 |
| 配置缺失 | 波表越界/缺失 | 内置默认 10 波 | 不阻塞 |
| 配置缺失 | Boss 配置缺失 | 跳过 Boss，普通波收尾 | 可结算 |
| 类型波重叠 | 空地同时来 / Boss+类型波 | 空军走上层 z、地面走路径；Boss 优先演出 | 分轨不混 |
| 加速致资源不及 | 2x 下玩家来不及布塔 | 纯表现倍速，不跳波，玩家自担 | 设计预期 |
| 无尽生成失败 | `endless_config` 缺失/公式非法 | 回退默认敌群（e_light_01 × base count）+ 记 S25，不崩 | 可战(降级) |
| 无尽敌 id 非法 | 生成的 `enemy_id` 不在 S31 原型表 | 替换默认 `e_light_01` + 记 S25 | 可战 |
| 无尽公式 NaN | k_hp/k_speed 缺失/越界 | 钳制 k 到默认(0.05/0.02)；hp/speed 缩放下限 1.0 | 不崩 |
| 无尽波数溢出 | wave_reached > max_wave_cap(>0) | 达 cap 即强制结束（视作"结束"，仍按 S8 失败结算口径） | 防溢出 |

---

## 2.5 无尽波次生成（Endless Wave Generation · 接 S32.endless_config）

> 无尽模式（stage_type=endless）**不引用任何预置 `wave_table`**。每波敌群由本系统在运行时**按 wave 序号程序化生成**：读取 `S32.endless_config` 的难度公式与排程，从 **S31 `enemy_id` 原型池**选取敌种、按波次推导数量/护甲/缩放，再交给 S5/S1 生成。standard 模式仍走 `wave_table` 预置路径，二者不混。

**1. 普通波生成规则（wave w，w 不为 Boss 波）**
- **敌种分级（composition by tier）**：按 wave 区间从 S31 原型池选取（引用 S31 `enemy_id`；S31 为敌人实体唯一定义源，其 `enemy_id` 目录见 S31 §3 示例）：
  - `w ≤ 5`：`e_light_01`（轻甲，弱 arrow）
  - `6 ≤ w ≤ 15`：+ `e_heavy_01`（重甲，弱 cannon/poison）
  - `16 ≤ w ≤ 30`：+ `e_air_01`（空军，弱 electric/对空）
  - `31 ≤ w ≤ 50`：+ `e_magic_immune_01`（魔免，弱物理）
  - `w > 50`：全类型混编 + `e_poison_01`（毒甲肉盾，弱 poison）
  - 每波从当前已解锁区间**随机抽 1–2 种**组合（保证 P4 取舍，避免单一解）。
- **数量**：`count = min(200, 8 + 4×(w-1))`（复用 `wave_count` 公式；同屏上限 60 分批）。
- **间隔/准备期**：`spawn_interval = max(0.4, 1.2 − 0.03×(w-1))`、`prep_time = max(3, 8 − 0.1×(w-1))`（复用 S04 全局公式）。
- **缩放（核心难度曲线）**：
  - `enemy_eff.hp = S31.base_hp × [1 + (w−1) × k_hp] × S14.diff_mult`
  - `enemy_eff.speed = S31.base_move_speed × [1 + (w−1) × k_speed] × S14.diff_mult`
  - `k_hp`/`k_speed` 单一真理源 = `S32.endless_config`（`stg_endless_k_hp`/`stg_endless_k_speed`，见 balance）。
  - 护甲 `armor_type`/特殊行为 `special_behavior` 直接取 S31 原型值（不随波变）。
- **掉木**：沿用 S31 `enemy_drop`（逐敌 session 木主源）；Boss 波额外掉木（见 S31）。

**2. Boss 排程（每 N 波）**
- 当 `w % boss_every_n_waves == 0` → Boss 波：生成 `e_boss_01`（S31 Boss 原型，heavy + speedup/heal_cut 轮换机制），触发 `BossWarning`（2s 全屏预警，接 `HUD_BOSS_WARN`/同 `ENDLESS_BOSS_INCOMING`）。
- Boss 波**不叠加**普通波（独占该波），保证情绪高点。

**3. 难度曲线说明**
- 难度随波**单调递增**：hp 线性×(1+k_hp·(w−1))、speed 线性×(1+k_speed·(w−1))，叠加 S14 `diff_mult` 运营粗调。
- 无"末波"概念，理论上无限（真无限由 `max_wave_cap=0` 表示）；结构封顶由 S4 `wave_total_waves` 上限兜底防数值溢出。
- 敌种随波**逐步解锁更硬护甲**（轻→重→空→魔免→毒），逼迫玩家随进度补对应克制塔（P4 取舍延续）。

**4. 异常边界（生成失败回退）**
- `endless_config` 缺失/公式非法 → 回退默认敌群（e_light_01 × base count）+ 记 S25。
- 生成的 `enemy_id` 不在 S31 原型表 → 替换默认 `e_light_01` + 记 S25。
- `k_hp`/`k_speed` 缺失/越界 → 钳制到默认(0.05/0.02)，hp/speed 缩放下限 1.0。
- `boss_every_n_waves` 非法(≤0/越界) → 默认 10。
- `wave_reached > max_wave_cap(>0)` → 达 cap 即强制结束（按 S8 失败结算口径，记 S25）。
- 同屏敌超限 → 对象池 + 同屏上限 60 分批（同 standard）。

---

## 3. 配置表设计

**表名：`wave_config`（波次配置，按关卡）**

| 字段 | 类型 | 取值范围 | 默认值 | 说明 |
|---|---|---|---|---|
| wave_id | string | 唯一 | — | 波主键 |
| level_id | string | 关联 S14 | "lv_01" | 所属关卡 |
| wave_index | int | 1–N | — | 第几波（N=单局波数） |
| enemy_type | enum | normal/air/boss/special | "normal" | 怪物类型 |
| count | int | 1–200 | `[PLACEHOLDER]` | 数量。**调优杆**：压力曲线 |
| spawn_interval | float | 0.1–10 | `[PLACEHOLDER]` | 出场间隔(s)。**调优杆**：节奏 |
| base_hp | int | 1–100000 | `[PLACEHOLDER]` | 本波怪物基础血量（随波缩放）。**调优杆**：难度 |
| armor_type | enum | none/light/heavy/magic_immune/poison | none | 护甲（决定克制） |
| is_boss | bool | true/false | false | 是否 Boss 波 |
| boss_mechanic | enum | null/speedup/heal_cut | null | Boss 特殊机制 |
| prep_time | float | 0–30 | `[PLACEHOLDER]` | 准备期(s)。**调优杆**：决策窗口 |
| reward_mult | float | 0.5–5 | `[PLACEHOLDER]` | 本波奖励倍率（金，非木）。**调优杆**：金产出 |
| drop_wood_chance | float | 0–1 | `[PLACEHOLDER]` | 本波每只怪掉木概率（session 木主源）。**调优杆**：养塔木供给节奏 |
| drop_wood_amount | int | 1–999 | `[PLACEHOLDER]` | 命中掉木量（session）。**调优杆**：单次掉木强度 |
| spawn_loops | int | 1–loop_count | `[PLACEHOLDER]` | 本波怪绕圈数（接 S1） |

**全局波数参数（单例，非逐波）**

| 字段 | 类型 | 取值范围 | 默认值 | 说明 |
|---|---|---|---|---|
| total_waves | int | 10–100 | `[PLACEHOLDER]` | 单局总波数（GDD：`[PLACEHOLDER]` 50）。**调优杆**：P5 时长硬约束 |
| boss_every | int | 5–20 | `[PLACEHOLDER]` | 每 N 波一个 Boss（GDD：每 `[PLACEHOLDER]` 10 波）。**调优杆**：情绪高点 |

**多行示例数据（CSV；数值列 `[PLACEHOLDER]` 为待调优占位）**

```csv
wave_id,level_id,wave_index,enemy_type,count,spawn_interval,base_hp,armor_type,is_boss,boss_mechanic,prep_time,reward_mult,drop_wood_chance,drop_wood_amount,spawn_loops
w_lv01_01,lv_01,1,normal,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],none,false,null,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER]
w_lv01_03,lv_01,3,normal,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],light,false,null,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER]
w_lv01_05,lv_01,5,air,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],none,false,null,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER]
w_lv01_10,lv_01,10,boss,1,[PLACEHOLDER],[PLACEHOLDER],heavy,true,speedup,[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER],[PLACEHOLDER]
```

> 掉木说明：`drop_wood_chance`/`drop_wood_amount` 为 session 木主源（替代原木房产木/通关木奖励）；Boss 波可配更高掉率作为养塔关键木点。所有值 `[PLACEHOLDER]` 待调优。

> 无尽模式（stage_type=endless）**不使用本表 `wave_config` 逐波行**：其敌群由 §2.5 程序化生成，缩放系数 `k_hp`/`k_speed` 与 Boss 周期见 `balance/S04_wave.md` 的 `endless_*` 参数（单一真理源在 `S32.endless_config`，见 balance/S32 `stg_endless_*`）。无尽复用本表 `wave_count`/`wave_spawn_interval`/`wave_prep_time` 的**随波次公式**推导数量/间隔/准备期。

---

## 4. 美术资源需求

| 资源 | 帧数 | 分辨率 | 格式 | 切片要求 |
|---|---|---|---|---|
| 怪物立绘（按 enemy_type） | 行走 4–6 帧 | 64×64 | Atlas | 单格切片，锚点中心 |
| 怪物护甲标识 | 1（静态，按 armor 着色环） | 24×24 | Atlas | 套怪物头顶 |
| Boss 立绘 / 模型 | idle 4 + 攻击 4 | 128×128+ | Atlas / Skeleton | 专属骨骼 |
| 波次进度条 | 1（静态，九宫） | 300×16 | PNG | 九宫 |
| Boss 预警字 | 红闪 2 帧 | 文本 64px | 引擎文本+特效 | 屏闪 2s |
| 敌预览图标 | 1（静态） | 64×64 | Atlas | 单格切片 |

> 怪物动作与受击特效见 S23；Boss 专属演出 F40 暂不做。

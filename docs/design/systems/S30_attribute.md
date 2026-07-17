<!-- 编码: UTF-8 -->
# 系统策划案：S30 属性系统 (Attribute / Stat System)

> 归属域：A 核心战斗域 · 层级/优先级：基础设施 / P0（**全游戏属性的唯一真理源 single source of truth**）· 关联 F 码：F2 F3 F4 F6 F7（属性被建/养/战/波/技能全局引用）· 关联：GDD §5.2(养塔)/§5.6(塔种)/§5.7(克制)/§5.9(等级)；SYSTEM_BREAKDOWN §S30
> 状态：v0.2-detailed · 日期 2026-07-17
> 版本说明：本系统为**新增基础设施系统**，是塔/敌全部属性（dmg/range/atk_speed/armor_type/projectile_speed/hp/move_speed/special_behavior）与伤害类型、护甲类型、克制矩阵、属性合成公式、极值钳制的**唯一权威定义源**。S02（建塔）/S04（波次）/S05（战斗）/S28（技能）/S31（敌人）/S32（关卡）/S33（状态）均须引用本系统，不得各自硬编码属性参数。
> **本系统核心铁律（务必实现正确）**：
> 1. `tower_effective = base × growth(养塔) × player_level_mult(等级,单行不累加) × skill_mod(技能) × buff_mod(状态)`
> 2. 伤害类型枚举 = `physical / magic / poison / control`；护甲类型枚举 = `none / light / heavy / magic_immune / air`
> 3. 所有属性非负、上限钳制；异常一律走 **S24 防作弊校验**兜底。
> 平衡数值（克制系数、等级加成曲线、养塔成长、敌缩放因子、钳制阈值）保持 `[PLACEHOLDER]` 初值，标注「调优杆」，禁止硬编码。

---

## 0. 设计定位与权威边界

- **为什么需要 S30**：原 29 系统中，塔/敌属性（dmg/range/atk_speed/armor/HP）散落在 S02/S04/S05，无统一属性模型，导致 (a) 数值表不知要填哪些属性参数；(b) 美术不知属性图标/伤害飘字颜色/图鉴属性展示怎么做。S30 收口为**唯一真理源**。
- **引用关系（强制）**：
  - S02 建塔：塔基础属性取 S30 `attribute_def` + 养塔 `growth`（S30 定义、S02 消费）
  - S29 等级：`player_level_mult` 单行不累加，由 S30 公式引用、S02 套用
  - S28 技能：`skill_mod` 各被动/主动乘子，由 S30 公式引用
  - S33 状态：`buff_mod` 状态乘子，由 S30 公式引用（**S33 尚未设计，见 §2.3 / NEEDS-DESIGN**）
  - S04 波次 / S31 敌人 / S32 关卡：敌属性（`hp/armor_type/move_speed/special_behavior`）+ 关卡/波次缩放因子，字段由 S30 定义
  - S05 战斗：伤害结算消费 S30 合成后的 `tower_effective` + 查 S30 `damage_armor_matrix`
  - S16 图鉴：属性展示卡消费 S30 `attribute_def`（图标/名称/单位/描述）
  - S07 HUD / S24 防作弊：钳制阈值与异常上报
- **设计红线**：无主导策略（克制矩阵 4×5 互有长短）、无认知过载（属性展示克制色板固定）、无支柱漂移（服务 P2 养成爽感 + P4 每局取舍）、无经济失衡（属性系统不引入新货币）。

---

## 1. 系统 UI 布局

> S30 本身无独立菜单页，其 UI 是**散落在各系统内的属性展示组件**。本章列出 S30 负责的属性相关 UI 组件规范（图鉴属性卡 / 塔信息卡属性行 / 伤害飘字 / 状态图标位），供 S16/S02/S05 直接套用。

### 1.1 布局层级（z 轴，属性相关组件贴合既有层级）

| 层级 z | 名称 | 说明 |
|---|---|---|
| 35 | 伤害飘字 / 状态图标位 | 怪物头顶（接 S5）；颜色按伤害类型（S30 定义） |
| 50 | 塔信息卡属性行 | 选中塔信息卡内属性展示行（接 S2） |
| 70 | 图鉴属性展示卡 | 图鉴(S16)内单属性说明卡 |
| 80 | 属性说明弹层 | 长按属性图标 → 描述（接 S16） |

### 1.2 像素级线框（750 × 1334 设计基准）

**视图 A：塔信息卡属性行（嵌入 S02 信息卡，卡体 300×260 @ y≈700）**
```
  (0,0)┌─────────────────────────────────────────── 750 ──┐
       │        （战场：路径+塔位，见 S1）                   │
       │  ┌── 塔信息卡 z50 (S2，S30 注入属性行) ────────┐   │ y=700
       │  │ [图标]箭塔 Lv.3                        [✕]   │   │ y=712
       │  │ ── 属性行 (S30 规范) ─────────────────────  │   │
       │  │ 🗡伤害 [P]   🎯范围 [P]px  ⚡攻速 [P]/s    │   │ y=752
       │  │ 💨弹速 [P]px/s  ☠伤害类型:物理(红)          │   │ y=784
       │  │ 🛡护甲类型:无(灰)   下一养级预览 ▸          │   │ y=816
       │  │ [养塔 木×N] [卖塔] [索敌]                   │   │ y=900
       │  │ ── 技能区 z51 (S28) ────────────────────   │   │
       │  └──────────────────────────────────────────┘   │
       └──────────────────────────────────────────── 1334 ┘
```

**视图 B：伤害飘字 + 状态图标位（怪物头顶，z35，世界空间）**
```
        （怪物沿路径行进 z30，64×64）
              🐉(64×64)
              | -[红]23  ← physical 伤害飘字(红白)
              | -[蓝]18  ← magic 伤害飘字(蓝紫)
              | -[绿]5/s ← poison DoT 飘字(绿，持续)
              | ❄(青) 💀(绿) ⚡(黄)  ← 状态图标位 24×24 横排
              ↓ 弹道(按 damage_type 着色, z30→35)
            🏹塔(已占 z30)
```

**视图 C：图鉴属性展示卡（S16 图鉴内，z70）**
```
  ┌── 图鉴属性卡 z70 (长按属性图标弹出) ──────┐  (195,560) 360×240
  │ [🗡] 伤害 (dmg)                           │
  │ 单位: 点/次   范围: [min]–[max]            │
  │ 说明: 塔单次攻击基础伤害，经 S30 合成公式  │
  │ 套用养塔/等级/技能/状态乘子后为有效伤害。  │
  │ 克制: 见伤害类型色板 →                     │
  └──────────────────────────────────────────┘
```

### 1.3 组件表（x,y 左上角；w×h；z；分辨率自适应说明）

| 组件 | 坐标(x,y) | 尺寸(w×h) | z | 响应 | 自适应 |
|---|---|---|---|---|---|
| 塔信息卡·属性行容器 | (245,748)（信息卡内） | 260×120 | 50 | 无（展示） | 锚定信息卡内相对定位；九宫拉伸 |
| 属性图标(伤害/范围/攻速/弹速) | 行内 (245,752) 起横排 | 24×24 + 文本 | 50 | 长按→图鉴卡(S16) | 相对比例 `×safe_scale` |
| 伤害类型徽标 | (245,784) | 文本 20px 着色 | 50 | 无 | 锚定信息卡内 |
| 护甲类型徽标 | (245,816) | 文本 20px 着色 | 50 | 无 | 锚定信息卡内 |
| 伤害飘字 | 怪物头顶动态 | 文本 18–32px 着色 | 35 | 无 | 字号随伤缩放；世界空间 |
| 状态图标位 | 怪物身上动态 | 24×24 ×N 横排 | 35 | 无 | 世界空间；超出合并 |
| 图鉴属性卡 | (195,560) 居中 | 360×240 | 70 | 长按属性图标弹/收 | 锚定 center，letterbox 居中 |
| 属性说明弹层 | 同图鉴卡 | 360×240 | 80 | 松手收起 | 锚定 center |

**分辨率自适应策略（强制，对齐 S01/S28）**
- **设计基准** 750×1334（@1x 逻辑）。所有坐标以上表为准。
- **锚点**：塔信息卡属性行锚定"信息卡内相对 + 安全区"；图鉴属性卡锚定 Center；伤害飘字/状态图标为世界空间动态。
- **九宫格**：属性行容器、图鉴卡均九宫（边 16px 圆角 12），拉伸不变形。
- **相对比例**：`safe_scale = min(screen_w/750, screen_h/1334)`；属性图标/飘字尺寸 = 基准 × safe_scale。
- **安全区**：可点组件内缩 `top≥状态栏+20, bottom≥手势条+20`；属性图标最小可点区 ≥ 44×44（P3）。
- **Letterbox**：渲染分辨率 ≠ 基准时按 **contain** 留黑边；HUD/卡相对基准定位后整体缩放。
- **DPR**：美术资源出 @2x/@3x（见 §4），引擎 `cc.view` 设 `resolutionPolicy = FIT`。

### 1.4 交互流程图（mermaid flowchart — 属性查看）

```mermaid
flowchart TD
    A[选中塔 S1/S2] --> B[塔信息卡 z50 + 属性行(S30)]
    B --> C[展示 dmg/range/atk_speed/projectile_speed/damage_type/armor_type]
    C --> D{长按属性图标?}
    D -->|是| E[图鉴属性卡 z70(S16) 弹层]
    E --> F[显 单位/范围/说明/克制色板]
    F --> G[松手收起]
    D -->|否| H[仅看数值]
    I[命中怪物 S5] --> J[伤害飘字 z35 按 damage_type 着色]
    J --> K[状态图标位 z35 挂 slow/poison/chain]
```

---

## 2. 逻辑功能

### 2.1 功能模块表（触发 / 处理 / 输出）

| 模块 | 触发条件 | 处理流程（正常） | 输出 |
|---|---|---|---|
| 属性定义加载 | 进局/读档 | 读 `attribute_def` → 建塔/敌属性 schema（id/type/unit/min/max） | 属性容器就绪 |
| 塔有效属性合成 | 建塔(S02)/养塔升级(S02)/等级变更(S29)/技能生效(S28)/状态变更(S33) | `tower_effective = base × growth^level × player_level_mult(单行) × skill_mod × buff_mod` → 钳制(min/max) | 已修正塔有效属性 |
| 敌属性派生 | 波次出怪(S04) | `enemy_eff.hp = base_hp × level_scalar(S32) × wave_scalar(S04)`；`move_speed` 同理；赋 `armor_type`/`special_behavior` | 战场敌属性 |
| 克制系数查询 | 命中结算(S05) | 查 `damage_armor_matrix[tower.damage_type][enemy.armor_type]` | 系数(0/0.5/1/1.5) |
| 护甲减伤查询 | 命中结算(S05) | 查 `armor_type_def[enemy.armor_type].reduce` | 减伤%(0–0.9) |
| 极值钳制 | 每属性写入 | `clamp(v, min, max)`；越界对 S24 报可疑 | 合规属性值 |
| 异常兜底 | NaN/Inf/缺配置 | 默认值(1.0/0/物理) + S25 告警 + S24 校验 | 不崩 |

### 2.2 属性数据结构（TypeScript 接口草案 · 数据驱动）

```ts
// ===== S30 属性模型（全游戏唯一真理源） =====
enum DamageType { physical = 'physical', magic = 'magic', poison = 'poison', control = 'control' }
enum ArmorType   { none = 'none', light = 'light', heavy = 'heavy', magic_immune = 'magic_immune', air = 'air' }
enum SpecialBehavior { none = 'none', air = 'air', heal_cut = 'heal_cut', speedup = 'speedup', boss = 'boss', special = 'special' }

interface TowerAttr {
  tower_id: string;
  damage_type: DamageType;     // 由 S02 tower.type 映射（箭/炮=physical, 魔=magic, 毒=poison, 冰/风=control）
  dmg: number;                 // 基础伤害（Lv1，S02 tower_config.base_dps）
  range: number;               // 射程 px
  atk_speed: number;           // 攻速 次/s
  projectile_speed: number;    // 弹速 px/s
  armor_type: ArmorType;       // 保留字段，TD 中敌不攻击塔，恒 = none（见 NEEDS-DESIGN-1）
}

interface EnemyAttr {
  enemy_id: string;
  hp: number;                  // 派生：base_hp × level_scalar × wave_scalar
  armor_type: ArmorType;       // 决定克制（S04 wave_config.armor_type）
  move_speed: number;          // 派生：base_speed × level_scalar × wave_scalar
  special_behavior: SpecialBehavior; // 特殊行为（S04 boss_mechanic / enemy_type 映射）
}

// 合成结果
interface EffectiveTowerAttr {
  dmg: number; atk_speed: number; range: number; projectile_speed: number;
  damage_type: DamageType;
}
```

### 2.3 属性合成结算流程（mermaid sequenceDiagram — 铁律公式）

```mermaid
sequenceDiagram
    participant S2 as 建筑(塔)
    participant S29 as 等级系统
    participant S28 as 技能系统
    participant S33 as 状态系统
    participant S30 as 属性系统(S30)
    participant S5 as 战斗系统
    participant S24 as 防作弊
    S2->>S30: 建塔/养塔 → base_attr + level(养塔级)
    S29->>S30: player_level_mult = player_level_config[session_level].bonus(单行,不累加)
    S28->>S30: skill_mod(被动破甲/冰封易伤/导电/腐蚀/逆风…)
    S33->>S30: buff_mod(状态乘子, 默认1.0; S33未设计→占位)
    S30->>S30: effective = base × growth^level × player_level_mult × skill_mod × buff_mod
    S30->>S30: clamp(effective, min, max)
    alt 越界(NaN/Inf/>max/<min)
        S30->>S24: 报可疑(钳制后值)
    end
    S30-->>S5: EffectiveTowerAttr(已合成+钳制)
    Note over S5,S30: 命中时
    S5->>S30: 查 damage_armor_matrix[damage_type][enemy.armor_type]
    S30-->>S5: 克制系数(0/0.5/1/1.5)
    S5->>S30: 查 armor_type_def[enemy.armor_type].reduce
    S30-->>S5: 减伤%
    S5->>S5: dmg_eff = effective.dmg × counter × (1 − reduce) × status_mod
```

> **公式语义（铁律重申）**：
> - `base`：S02 `tower_config` 基础值（Lv1）。
> - `growth^level`：养塔指数（S02 消费，S30 定义 `attr_growth_base` 与区间 1.5–2.0）。
> - `player_level_mult`：**单行查表、不累加**（S29 `player_level_config[level].bonus`，非 Σ/Π）。
> - `skill_mod`：S28 各被动/主动的数值乘子（如破甲降减免、冰封易伤 +伤、导电 +伤），默认 1.0。
> - `buff_mod`：S33 状态系统乘子（如风塔逆风惩罚移速下降、冰减速），**S33 尚未设计，占位默认 1.0**（见 NEEDS-DESIGN-2）。
> - 顺序固定，禁止在任一乘子内再嵌套累加语义。

### 2.4 异常与边界用例表（12 类）

| 用例ID | 异常类型 | 触发条件 | 预期处理流程 | 输出 / 兜底 | 涉及系统 |
|---|---|---|---|---|---|
| E01 | 属性为负 | 养塔/技能算出负 dmg | `clamp(v, 0, max)`，负值置 0 | 合规正属性 | S24 |
| E02 | 属性溢出 | dmg 超 `attr_dmg_max` | 钳制上限；对 S24 报可疑 | 不溢出 | S24 |
| E03 | 除零 | `armor_reduce` 作分母 / 0 减伤公式 | 分母保护默认 1.0（无减伤） | 不崩 | S24 |
| E04 | 矩阵缺键 | `damage_armor_matrix[type][armor]` 缺 | 系数默认 1.0 + S25 告警 | 可战 | S25 |
| E05 | 护甲类型未知 | `armor_type` 不在枚举 | 降级 `none`（无减免） | 可战 | S25 |
| E06 | 伤害类型未知 | `damage_type` 不在枚举 | 降级 `physical` | 可战 | S25 |
| E07 | 等级加成缺失 | `player_level_config[level]` 缺 | 用 level=1 行（倍率 1.0，无加成） | 安全降级 | S29/S24 |
| E08 | 等级加成越界 | `bonus` ≤0 / >max | 钳制合法区间；S24 报可疑 | 塔可战 | S24 |
| E09 | skill_mod 缺失 | 技能未解锁/配置缺 | `skill_mod = 1.0`（无修正） | 降级不崩 | S28 |
| E10 | buff_mod 缺失 | S33 未接入/状态缺 | `buff_mod = 1.0`（无修正） | 降级不崩 | S33 |
| E11 | 敌 HP 异常 | 派生 HP ≤0 | 钳制最小 `attr_hp_min`(=1) | 正常死亡 | S04/S24 |
| E12 | NaN/Inf | 任何乘子算出 NaN/Inf | 钳制到 [min,max]；S24 报可疑 | 不崩 | S24 |

> 设计红线检查：无主导策略（矩阵 4×5 互有长短，无单一 ×∞）；无认知过载（属性展示固定色板，玩家零学习）；无支柱漂移（服务 P2 养成 + P4 取舍）。

---

## 3. 配置表设计

### 3.1 表 `attribute_def`（属性定义，唯一真理源）

| 字段 | 类型 | 取值/范围 | 默认值 | 说明 |
|---|---|---|---|---|
| attr_id | string | 唯一(snake_case) | — | 属性主键（dmg/range/atk_speed/projectile_speed/hp/move_speed） |
| display_name | string | 非空 | — | 展示名（图鉴 S16） |
| data_type | enum | int/float/enum | float | 数值类型 |
| unit | enum | point/px/per_s/HP/级 | point | 单位（飘字/图鉴用） |
| min | float | ≥0 | 0 | 下限（钳制，非负铁律） |
| max | float | >min | `[PLACEHOLDER]` | 上限（钳制） |
| default | float | [min,max] | 0 | 缺省值 |
| owner | enum | tower/enemy | tower | 归属（塔/敌） |
| icon_ref | string | 资源 id | — | 属性图标（见 §4） |

**多行示例（CSV；数值列 `[PLACEHOLDER]` 为初值待调优）**

```csv
attr_id,display_name,data_type,unit,min,max,default,owner,icon_ref
dmg,伤害,float,point,0,[PLACEHOLDER],0,tower,icon_attr_dmg
range,范围,float,px,0,[PLACEHOLDER],0,tower,icon_attr_range
atk_speed,攻速,float,per_s,0.1,[PLACEHOLDER],0,tower,icon_attr_atkspd
projectile_speed,弹速,float,px_s,50,[PLACEHOLDER],0,tower,icon_attr_proj
hp,生命,float,HP,1,[PLACEHOLDER],1,enemy,icon_attr_hp
move_speed,移速,float,px_s,20,[PLACEHOLDER],0,enemy,icon_attr_movespd
```

### 3.2 表 `damage_armor_matrix`（伤害类型 × 护甲类型 克制矩阵 · 全组合 4×5=20）

| 字段 | 类型 | 取值 | 说明 |
|---|---|---|---|
| damage_type | enum | physical/magic/poison/control | 攻击方伤害类型 |
| armor_type | enum | none/light/heavy/magic_immune/air | 防守方护甲类型 |
| coefficient | float | {0.0, 0.5, 1.0, 1.5} | 克制系数：×0 免疫 / ×0.5 弱抗 / ×1 真伤·中性 / ×1.5 强克 |

**初始矩阵（权威值；冲突标注见 §5）**

| damage_type \ armor_type | none | light | heavy | magic_immune | air |
|---|---|---|---|---|---|
| **physical**（箭/炮） | 1.0 | **1.5** | **1.5** | **1.5** | 0.5 |
| **magic**（魔法塔） | 1.0 | 1.0 | 1.0 | **0.0** | 0.5 |
| **poison**（毒塔） | 1.0 | 1.0 | **1.5** | 1.0 | 0.5 |
| **control**（冰/风） | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

> 取值依据（对齐 GDD §5.6/§5.7/§5.5）：
> - 物理克轻甲(箭)、克重甲(炮) → ×1.5；物理克魔免(§5.5「魔免需物理塔」) → ×1.5；物理对空弱 → ×0.5。
> - 魔法无视护甲(真伤) → ×1.0；**魔法对魔免 = ×0（魔免免疫魔法，铁律，见 §5 冲突-1）**。
> - 毒克高 HP/重甲(越肉越赚) → ×1.5；毒对空弱 → ×0.5；毒对魔免有效(非魔法) → ×1.0。
> - 控制全克但无伤(control 本身 0 伤害，仅施加状态)；对魔免/空均生效(控制非伤害) → ×1.0。

**CSV（初值）**
```csv
damage_type,armor_type,coefficient
physical,none,1.0
physical,light,1.5
physical,heavy,1.5
physical,magic_immune,1.5
physical,air,0.5
magic,none,1.0
magic,light,1.0
magic,heavy,1.0
magic,magic_immune,0.0
magic,air,0.5
poison,none,1.0
poison,light,1.0
poison,heavy,1.5
poison,magic_immune,1.0
poison,air,0.5
control,none,1.0
control,light,1.0
control,heavy,1.0
control,magic_immune,1.0
control,air,1.0
```

### 3.3 表 `armor_type_def`（护甲类型定义 + 减伤%）

| 字段 | 类型 | 取值 | 说明 |
|---|---|---|---|
| armor_type | enum | none/light/heavy/magic_immune/air | 护甲主键 |
| reduce | float | 0–0.9 | 减伤%（magic_immune 仅对物理/毒生效，魔法经矩阵已 ×0，故魔免 reduce=0 避免双重惩罚） |
| color_ref | string | 色板 id | 护甲标识着色（图鉴/敌头顶环） |

**CSV（初值）**
```csv
armor_type,reduce,color_ref
none,0.0,armor_none_gray
light,0.10,armor_light_green
heavy,0.30,armor_heavy_orange
magic_immune,0.0,armor_magicimmune_purple
air,0.0,armor_air_cyan
```

### 3.4 表 `attr_composition`（合成乘子来源映射 · 铁律公式落表）

| 字段 | 类型 | 说明 |
|---|---|---|
| step | int | 合成顺序 1–5 |
| mult_name | string | 乘子名（base/growth/player_level_mult/skill_mod/buff_mod） |
| source_system | string | 提供系统（S02/S29/S28/S33/S30） |
| formula | string | 该乘子计算式 |
| stack_semantic | string | 叠加语义（growth=指数, level=单行不累加, skill/buff=可叠加倍率） |

**CSV**
```csv
step,mult_name,source_system,formula,stack_semantic
1,base,S02,tower_config.base_attr,基础值(单行)
2,growth,S02,growth^养塔level,指数(可超过1)
3,player_level_mult,S29,player_level_config[level].bonus,单行查表,不累加
4,skill_mod,S28,Π(已解锁被动/主动乘子),可叠加倍率(默认1.0)
5,buff_mod,S33,Π(生效状态乘子),可叠加倍率(默认1.0;S33未设计)
```

### 3.5 表 `enemy_attr_scaling`（敌属性关卡/波次缩放因子）

| 字段 | 类型 | 取值 | 说明 |
|---|---|---|---|
| scale_dim | enum | level/wave | 缩放维度（S32 关卡 / S04 波次） |
| target_attr | enum | hp/move_speed | 作用属性 |
| base | float | 1.0 | Lv1/首波基准 |
| per_step_growth | float | >1 | 每级/每波乘子 |
| max | float | — | 上限钳制 |
| source_ref | string | 提供系统 | S32(关卡) / S04(波次) |

**CSV（初值）**
```csv
scale_dim,target_attr,base,per_step_growth,max,source_ref
level,hp,1.0,1.10,[PLACEHOLDER],S32
level,move_speed,1.0,1.03,[PLACEHOLDER],S32
wave,hp,1.0,1.06,[PLACEHOLDER],S04
wave,move_speed,1.0,1.02,[PLACEHOLDER],S04
```

> 说明：`enemy_eff.hp = base_hp(S04) × level_scalar(S32) × wave_scalar(S04)`，S32 关卡系统尚未设计（见 NEEDS-DESIGN-3）。`special_behavior` 枚举对齐 S04 `boss_mechanic`(null/speedup/heal_cut) + `enemy_type`(normal/air/boss/special)。

---

## 4. 美术资源需求

| 资源 | 帧数 | 分辨率(@1x) | 格式 | 切片要求 |
|---|---|---|---|---|
| 属性图标·伤害 | 静态+禁用 | 48×48 | Atlas | 单格；红白描边 |
| 属性图标·范围 | 静态 | 48×48 | Atlas | 单格 |
| 属性图标·攻速 | 静态 | 48×48 | Atlas | 单格 |
| 属性图标·弹速 | 静态 | 48×48 | Atlas | 单格 |
| 属性图标·生命(敌) | 静态 | 48×48 | Atlas | 单格 |
| 属性图标·移速(敌) | 静态 | 48×48 | Atlas | 单格 |
| 护甲标识·5 型 | 静态(按 armor 着色环) | 24×24 | Atlas | 套敌头顶（接 S4） |
| 伤害类型徽标·4 型 | 静态(物理/魔法/毒/控制) | 24×24 | Atlas | 塔信息卡/图鉴用 |
| 图鉴属性卡底 | 静态九宫 | 360×240 | PNG | 3×3 切片 |
| 伤害飘字（按类型着色） | 文本动画 | 文本 18–32px | 引擎 SDF 文本 | 0.5s 上浮，配色见下表 |
| 状态图标位·4 型 | 循环 2–4 帧 | 24×24 | Atlas | slow/poison/chain/control（接 S5/S28） |

**伤害飘字颜色规范（按 damage_type，S30 唯一权威）**

| damage_type | 主色(HEX) | 描边 | 说明 |
|---|---|---|---|
| physical | `#FF4444` 红 | `#FFFFFF` | 物理伤害（箭/炮） |
| magic | `#9B59FF` 紫 | `#E8D6FF` | 魔法真伤 |
| poison | `#3ED16B` 绿 | `#DFFBE8` | 毒 DoT（持续小字 /s） |
| control | `#37C0FF` 青 | `#D6F4FF` | 控制（减速/击退，0 伤害仅状态提示） |

> 配色与 GDD §5.6 塔种调性对齐（箭炮=红、魔=紫、毒=绿、冰风=青），供美术与 S05 飘字统一。资源经 S19 分包；@2x/@3x 由引擎按 DPR 选档。

---

## 5. 依赖 / 边界 / 冲突说明（务必关注）

### 5.1 依赖
- **S02 建塔**：消费 `attribute_def` + `growth` + 套用 `player_level_mult`(单行)。
- **S29 等级**：提供 `player_level_mult` 单行查表值（不累加）。
- **S28 技能**：提供 `skill_mod` 各乘子。
- **S33 状态**（**未设计**）：提供 `buff_mod`，当前占位默认 1.0。
- **S04 波次 / S31 敌人 / S32 关卡**（S32 **未设计**）：提供敌属性与缩放因子。
- **S05 战斗**：消费合成后 `tower_effective` + 查 `damage_armor_matrix`/`armor_type_def`。
- **S16 图鉴 / S07 HUD**：消费属性展示与飘字色板。
- **S24 防作弊**：所有极值/异常兜底。

### 5.2 冲突与一致性（已识别，需主理人裁定收口）

| # | 冲突点 | 现状 | S30 裁定 | 需修订方 |
|---|---|---|---|---|
| C1 | `magic_vs_magic_immune` 系数 | GDD §5.6 称魔法塔「魔免克星」；`balance/S05_combat.md` 已写 `=1.5` | **=0.0（魔免免疫魔法，铁律）**，与 GDD §5.5「魔免需物理塔」一致 | 改 GDD §5.6 魔法塔描述为「无视护甲真伤塔（不克魔免）」；改 `balance/S05_combat.md` 该值为 0.0 |
| C2 | `armor_type` 枚举 | S04 `wave_config.armor_type` = none/light/heavy/magic_immune/**poison**；S30 要求 = none/light/heavy/magic_immune/**air** | S30 权威枚举含 **air**（替换 poison）；poison 降为 damage_type/status，非护甲类 | 改 S04 枚举；`balance/S05_combat.md` 的 `combat_armor_poison` 删除或改 air |
| C3 | electric 对空克制 | S28/S05 有 `electric_vs_air=1.5`；S30 仅 4 damage_type（无 electric） | electric 归类 `physical`（造成伤害）；对空 ×1.5 由 **S02 逐塔克制覆盖** `t_electric_vs_air` 实现，不进通用矩阵 | S02 增加逐塔克制覆盖字段；或扩展 damage_type 枚举（需主理人定） |
| C4 | 塔 `armor_type` 语义 | 任务列塔属性含 `armor_type` | TD 中敌不攻击塔，塔 `armor_type` 恒 = none（保留字段）；战斗用 `tower.damage_type` 查矩阵 | 澄清（见 NEEDS-DESIGN-1） |

### 5.3 NEEDS-DESIGN 项（本系统未决，待主理人/相关系统裁定）

1. **ND-1（塔 armor_type 语义）**：任务将 `armor_type` 列入塔属性，但本 TD 敌不攻击塔。建议塔 `armor_type` 保留为保留字段恒 = none，战斗使用 `tower.damage_type` 查矩阵。需确认是否仍要该字段或改名 `damage_type`。
2. **ND-2（S33 状态系统未设计）**：`buff_mod` 乘子来源系统 S33 尚未存在。当前占位默认 1.0；S33 设计后须回写乘子接口与可叠加语义（避免与 skill_mod 双重叠加）。
3. **ND-3（S32 关卡系统未设计）**：敌属性 `level_scalar` 由 S32 提供，当前仅定义缩放字段与初值，S32 落地后须回填 `per_step_growth`/`max` 真值。
4. **ND-4（electric 对空归类，见 C3）**：在 S02 加逐塔克制覆盖，或扩展 damage_type 枚举含 electric，二选一。
5. **ND-5（钳制上限初值 `[PLACEHOLDER]`）**：`attribute_def.max` 各属性上限需试玩调优后填实（见 `balance/S30_attribute.md` 已给建议区间）。

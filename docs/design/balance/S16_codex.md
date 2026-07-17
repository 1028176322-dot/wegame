# 数值设计表：S16 图鉴

> 关联 F 码：F38 · GDD：—（SYSTEM_BREAKDOWN §S16）· 设计文档：systems/S16_codex.md
> 说明：本表为该系统设计文档 §3 配置表（消费契约 tower_config / enemy_config，来自 S2/S4）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。
> ⚠️ 本系统**无独立写配置**（§0/§3 明确只读 S2/S4）；下方 [PLACEHOLDER] 仅出现在消费契约示例行，数值须与 **A 域权威表一致**。已对齐 S02 塔表与 S04 波表基准，避免跨域漂移。

## 字段规范
- param_id：参数唯一标识（snake_case；消费契约来源前缀 cdx_src_，标明源自 S2/S4 只读契约），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 消费契约表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.xxx_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天 / 点 / HP）
- description：含义与调优说明（含为何取此初值；标注权威来源）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| cdx_src_t_arrow_base_dps | tower_config(S2,消费) | 30 | - | 1 | 1000 | 套用 player_level_config[level].dmg_mult（单行,不累加,见 S02/S29） | 点 | 箭塔基础 DPS；**对齐 A 域 S02 权威值 30**（doc §3.2 示例 "10" 仅为占位，以 S02 为准） |
| cdx_src_t_arrow_base_range | tower_config(S2,消费) | 140 | - | 50 | 400 | 套用 player_level_config[level].range_mult（单行,不累加） | px | 箭塔射程；对齐 S02 140 |
| cdx_src_t_magic_base_dps | tower_config(S2,消费) | 60 | - | 1 | 1000 | 套用 player_level_config[level].dmg_mult（单行,不累加） | 点 | 魔法塔基础 DPS；**对齐 S02 权威值 60**（doc §3.2 示例 "12" 仅为占位，以 S02 为准） |
| cdx_src_t_magic_base_range | tower_config(S2,消费) | 150 | - | 50 | 400 | 套用 player_level_config[level].range_mult（单行,不累加） | px | 魔法塔射程；对齐 S02 150 |
| cdx_src_t_wind_base_dps | tower_config(S2,消费) | 22 | - | 1 | 1000 | 套用 player_level_config[level].dmg_mult（单行,不累加） | 点 | 风塔基础 DPS；对齐 S02 22（控制向低伤） |
| cdx_src_t_wind_base_range | tower_config(S2,消费) | 110 | - | 50 | 400 | 套用 player_level_config[level].range_mult（单行,不累加） | px | 风塔射程；对齐 S02 110 |
| cdx_src_t_wind_growth | tower_config(S2,消费) | 1.16 | - | 1.1 | 3.0 | 无 | 倍/级 | 风塔养塔指数；对齐 S02 1.16（doc §3.2 为 [PLACEHOLDER]，取 S02 权威值） |
| cdx_src_e_slime_base_hp | enemy_config(S4,消费) | 30 | - | 1 | 9999 | 无（随波缩放见 S04 wave_base_hp=30×1.18^(N-1)） | HP | 史莱姆基础 HP；对齐 S04 早期基准 30（light_armor，弱 t_arrow） |
| cdx_src_e_golem_base_hp | enemy_config(S4,消费) | 120 | - | 1 | 9999 | 无 | HP | 石巨人基础 HP（heavy_armor，约 4× slime，弱 t_cannon） |
| cdx_src_e_wraith_base_hp | enemy_config(S4,消费) | 80 | - | 1 | 9999 | 无 | HP | 幽灵基础 HP（immune_magic，中阶，弱 t_arrow） |

## 备注 / 待裁定
- §1.2 线框 DetailPanel「DPS:[PLACEHOLDER] 范围:[PLACEHOLDER]」即读上述 `cdx_src_t_*_base_dps / base_range`（已覆盖），无独立新增参数。
- §3.1 `codex_view_config`（本系统唯一写表：show_locked_as_silhouette/ grid_cols=5/ icon_size=96 等）均给具体值，**无 [PLACEHOLDER]**，未列。
- **一致性对齐**：doc §3.2 示例行中的塔数值（t_arrow "10/120"、t_magic "12/110"、t_wind 全空）为占位 stub，与 A 域 S02 塔表权威值（dps 30/60/22、range 140/150/110、growth 1.16）不符；本表以 S02 为准填初值，消除跨域漂移。cannon/ice/poison/electric 三属性同由 S02 权威定义，S16 仅采样 3 塔，其余 4 塔图鉴展示值直接复用 S02，无新增 [PLACEHOLDER]。
- **轻量 NEEDS-DESIGN（跨域对齐）**：enemy_config 的 `e_slime/e_golem/e_wraith base_hp` 权威值建议在 S4 敌表平衡文件中定稿（A 域）。本表初值基于 S04 `wave_base_hp=30` 基准与护甲梯度（heavy≈4×、immune_mid≈2.7×）给出合理初值，待 S4 敌表定稿后回写对齐。
- 本系统全部 [PLACEHOLDER] 均已给初值（来源对齐 A 域），无 B 域内部 NEEDS-DESIGN。

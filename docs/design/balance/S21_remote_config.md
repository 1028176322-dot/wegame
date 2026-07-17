# 数值设计表：S21 远程配置系统

> 关联 F 码：F33 · GDD：§6（通胀检测） · 设计文档：systems/S21_remote_config.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 rc_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天 / MB / 倍）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| rc_exchange_rate | remote_config | 1.0 | - | 0.1 | 10 | 无 | 倍(木/金) | 金→木应急兑换汇率（每 1 金可兑木数）。初值 1.0 中性；木应稀缺，试玩后或下调至 0.5 以压低非主源产出。 |
| rc_wave_diff_mult | remote_config | 1.0 | - | 0.5 | 3 | 无 | 倍 | 波表难度倍率，初值 1.0（不改变预设难度曲线），留作热更调难调易杆。 |
| rc_drop_mult | remote_config | 1.0 | - | 0.5 | 3 | 无 | 倍 | 掉落倍率，初值 1.0（不改变预设掉率），协同 S04 调优。 |
| rc_gold_per_wave_base | remote_config | 100 | - | 1 | 1000 | 无 | gold | 单波基础金（S03 经济锚点）。初值 100，待经济闭环试玩后依通胀线(GDD §6)裁定。 |
| rc_fetch_interval | remote_config | 300 | - | 60 | 3600 | 无 | 秒 | 远程配置拉取间隔，初值 300s（5 分钟），限频防耗流（文档 E6）。 |
| rc_inflation_threshold | remote_config | 1.5 | - | 0.1 | 10 | 无 | 倍 | 通胀线（复用 S3/GDD §6）：单局经济产出超基线 1.5× 触发告警。⚠️ 应与 S25.an_inflation_threshold 共用 GDD §6 单一真值（见备注，待裁定）。 |

## 备注 / 待裁定
- `flag_monetize`/`flag_season`/`show_reload_toast` 在 §3.1 已为具体布尔值（default off / off / off），**非 [PLACEHOLDER]**，不列入本表。
- **单一来源待裁定（NEEDS-DESIGN）**：`inflation_threshold` 在 S21 与 S25 各持一份，语义同为 GDD §6 通胀线。建议以 GDD §6 为唯一真值，S21（客户端热更）与 S25（服务端看板）均引用同一值，避免双定义漂移。本表两处均暂置 1.5。
- 无其它 NEEDS-DESIGN 项：6 个 [PLACEHOLDER] 均已给初值。

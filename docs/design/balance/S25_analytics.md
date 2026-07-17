# 数值设计表：S25 数据分析系统

> 关联 F 码：F26 F44 · GDD：§6（通胀检测） · 设计文档：systems/S25_analytics.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 an_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（倍(0.01-1) / 倍 / 秒 / 条）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| an_sample_rate | analytics_config | 1.0 | - | 0.01 | 1 | 无 | 倍(0.01-1) | 采样率 1.0（首发全量采集），量级上升后下调控成本（文档 E4）。初值 1.0 保数据完整。 |
| an_inflation_threshold | analytics_config | 1.5 | - | 0.1 | 10 | 无 | 倍 | 通胀线（复用 S3/GDD §6）：单局经济产出超基线 1.5× 触发告警。⚠️ 应与 S21.rc_inflation_threshold 共用 GDD §6 单一真值（见备注，待裁定）。 |
| an_report_interval | analytics_config | 300 | - | 60 | 3600 | 无 | 秒 | 上报间隔 300s（5 分钟），定时/缓冲满触发脱敏上报。 |
| an_buffer_max | analytics_config | 1000 | - | 100 | 10000 | 无 | 条 | 本地缓冲上限 1000 条，满则环形覆盖最旧（文档 E6）。 |

## 备注 / 待裁定
- 文档 §3.1 其余字段（enable=true、retain_events、privacy_filter）为具体默认，**非 [PLACEHOLDER]**。
- **单一来源待裁定（NEEDS-DESIGN）**：`inflation_threshold` 在 S25 与 S21 各持一份，语义同为 GDD §6 通胀线。建议以 GDD §6 为唯一真值，避免双定义漂移。本表与 S21 均暂置 1.5。
- 4 个 [PLACEHOLDER]（采样率/通胀线/上报间隔/缓冲上限）均已给初值。
- 无其它 NEEDS-DESIGN 项。

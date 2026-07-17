# 数值设计表：S26 变现系统

> 关联 F 码：F19 · GDD：§8（合规）/ FEATURE_SCOPE §7#1 · 设计文档：systems/S26_monetization.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 mon_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（次/天 / wood / 条(Lives) / 秒）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| mon_ad_daily_limit | monetize_config | 5 | - | 1 | 20 | 无 | 次/天 | 每日广告上限 5 次，达上限入口灰显（防刷，协同 S24）。初值 5 控频。 |
| mon_ad_wood_reward | monetize_config | 20 | - | 1 | 200 | 无 | wood | 看广告得木 20。须确保开关 on 时通胀仍在 GDD §6 阈值内（协同 S21.rc_inflation_threshold）。初值 20。 |
| mon_revive_lives_gain | monetize_config | 2 | - | 1 | 10 | 无 | 条(Lives) | 复活回补 Lives +2（S8 内续命，不重复结算）。 |
| mon_share_reward | monetize_config | 10 | - | 0 | 200 | 无 | wood | 分享得奖 10 木。 |
| mon_min_session | monetize_config | 60 | - | 0 | 300 | 无 | 秒 | 最短局 60s 后才显广告入口（防速刷，合规）。初值 60s。 |
| mon_ad_cooldown | monetize_config | 120 | - | 0 | 600 | 无 | 秒 | 两次广告间隔 120s（防高频点）。初值 120s。 |

## 备注 / 待裁定
- 文档 §3.1 其余字段（enabled=false default off、revive_enabled=false、position=ingame）为具体默认，**非 [PLACEHOLDER]**。
- **硬隔离铁律不变**：`enabled=false`（首发必为关）时 S3 不接收任何外部产出，经济零破环。本表上限/奖励均为占位填充，实际值经合规 + S25 观测裁定。
- 6 个 [PLACEHOLDER]（广告上限/木奖/复活Lives/分享奖/最短局/广告冷却）均已给初值。
- 无 NEEDS-DESIGN 项。

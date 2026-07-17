# 数值设计表：S13 排行榜

> 关联 F 码：F15 · GDD：—（SYSTEM_BREAKDOWN §S13）· 设计文档：systems/S13_leaderboard.md
> 说明：本表为该系统设计文档 §3 配置表（leaderboard_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 ldb_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.xxx_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| ldb_fetch_timeout | leaderboard_config(fetch_timeout) | 5 | - | 1 | 10 | 无 | 秒 | 远端榜单拉取超时（§3.1 fetch_timeout 默认值 5、§2.4 E04 `fetch_timeout [PLACEHOLDER]`）。超时即回落本地榜并标「未同步」，绝不阻塞 UI；5s 兼顾弱网体验与等待忍耐 |

## 备注 / 待裁定
- §3.1 其余字段已给具体值：`top_n=50`、`min_score=1`、`sort_order=desc`、`tie_breaker=timestamp`、`only_increase=true`、`scope=friend`、`cycle=none`，无 [PLACEHOLDER]，未列。
- §2.4 E09 成绩钳制区间 `[0, max_wave]` 中的 `max_wave` 为 S14/S4 运行期变量（非固定 [PLACEHOLDER]），不单列参数。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

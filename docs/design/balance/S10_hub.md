# 数值设计表：S10 大厅

> 关联 F 码：—（导航中枢）· GDD：—（SYSTEM_BREAKDOWN §S10）· 设计文档：systems/S10_hub.md
> 说明：本表为该系统设计文档 §3 配置表（hub_config / reddot_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 hub_/sys_ 等），全局唯一、稳定，禁止中文
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
| hub_status_meta_res_display | hub_config(status_fields) | 0 | - | 0 | 999999 | 无 | meta_res | §1.2 线框 StatusBar「元资源:[PLACEHOLDER]」为运行期实时显示槽，读 S11/S18 当前 `meta_res`，新档初始 0。**非调优量**（UI 显示槽），仅作占位说明；非配置可调初值 |

## 备注 / 待裁定
- 本系统 §3.1 `hub_config` 与 §3.2 `reddot_config` 配置表**无 [PLACEHOLDER] 调优量**：`max_click_interval=0.5`、`default_level="lv_01"`、`show_reddot=true`、`bg_theme="lobby_1"`、`show_season_cd=true` 等均已给具体值，故未列入数值表。
- 设计文档中唯一 [PLACEHOLDER] 出现在 §1.2 线框的「元资源:[PLACEHOLDER]」显示槽（上表 `hub_status_meta_res_display`），属运行期实时值，无独立初值可调。
- 本系统所有 [PLACEHOLDER] 均已说明，无 NEEDS-DESIGN（唯一项为非调优显示槽）。

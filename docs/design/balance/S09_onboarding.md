# 数值设计表：S09 新手引导

> 关联 F 码：F10 · GDD：§7（SYSTEM_BREAKDOWN §S9）· 设计文档：systems/S09_onboarding.md
> 说明：本表为该系统设计文档 §3 配置表（onboarding_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 onb_/sys_ 等），全局唯一、稳定，禁止中文
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
| onb_mask_alpha | onboarding_config | 0.6 | - | 0.3 | 0.85 | 无 | 透明度 | 引导遮罩层透明度（见 §3.1 mask_alpha，默认值 0.6；§1.3 组件表 `alpha [PLACEHOLDER]0.6` 同参）。压暗非聚焦区的同时保证聚光挖空区可见，0.6 兼顾聚焦与可读性 |
| onb_lives_lock | onboarding_config | 99 | - | 1 | 999 | 无 | 条(Lives) | 引导局锁定 Lives 值（§3.1 lives_lock_value，默认值 99）。远大于正常漏怪容错，确保「本局不会失败」保送体验，消除新玩家首局挫败 |
| onb_tutorial_wave_count | onboarding_config | 8 | - | 1 | 20 | 无 | 波 | 引导局保送波数（§3.1 tutorial_wave_count，默认值 8）。8 波足以走完 6 步教学（建箭/首杀/风塔/兑换/养塔/冰塔）并给正反馈，又不冗长 |

## 备注 / 待裁定
- 本系统 §3.1 其余字段（enable_tutorial/default_timeout=30/focus_w=120/focus_h=120 等）均已给具体默认值，无 [PLACEHOLDER]，故未列。
- §1.3 组件表 `alpha [PLACEHOLDER]0.6` 与 §3.1 `mask_alpha` 为同一参数，已合并为 `onb_mask_alpha`，无重复。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

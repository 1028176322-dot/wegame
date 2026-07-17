# 数值设计表：S14 关卡

> 关联 F 码：F17 · GDD：—（SYSTEM_BREAKDOWN §S14）· 设计文档：systems/S14_level.md
> 说明：本表为该系统设计文档 §3 配置表（level_config / level_reward）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 lvl_ 等），全局唯一、稳定，禁止中文
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
| lvl_ring_count_lv01 | level_config(lv_01) | 3 | 阶梯 +1/每2关 | 1 | 12 | 无 | 圈 | lv_01 圈数（§3.1 CSV [PLACEHOLDER]3）。首发关简单 3 圈 |
| lvl_ring_count_lv02 | level_config(lv_02) | 3 | 阶梯 +1/每2关 | 1 | 12 | 无 | 圈 | lv_02 圈数（§3.1 CSV [PLACEHOLDER]3） |
| lvl_ring_count_lv03 | level_config(lv_03) | 4 | 阶梯 +1/每2关 | 1 | 12 | 无 | 圈 | lv_03 圈数（§3.1 CSV [PLACEHOLDER]4） |
| lvl_ring_count_lv04 | level_config(lv_04) | 4 | 阶梯 +1/每2关 | 1 | 12 | 无 | 圈 | lv_04 圈数（§3.1 CSV [PLACEHOLDER]4） |
| lvl_ring_count_lv05 | level_config(lv_05) | 5 | 阶梯 +1/每2关 | 1 | 12 | 无 | 圈 | lv_05 圈数（§3.1 CSV [PLACEHOLDER]5）。高难关 5 圈 |
| lvl_tower_slots_lv01 | level_config(lv_01) | 12 | 线性 +2/关 | 1 | 40 | 无 | 个 | lv_01 塔位数（§3.1 CSV [PLACEHOLDER]12）。首发 12 格宽松 |
| lvl_tower_slots_lv02 | level_config(lv_02) | 14 | 线性 +2/关 | 1 | 40 | 无 | 个 | lv_02 塔位数（§3.1 CSV [PLACEHOLDER]14） |
| lvl_tower_slots_lv03 | level_config(lv_03) | 16 | 线性 +2/关 | 1 | 40 | 无 | 个 | lv_03 塔位数（§3.1 CSV [PLACEHOLDER]16） |
| lvl_tower_slots_lv04 | level_config(lv_04) | 18 | 线性 +2/关 | 1 | 40 | 无 | 个 | lv_04 塔位数（§3.1 CSV [PLACEHOLDER]18） |
| lvl_tower_slots_lv05 | level_config(lv_05) | 20 | 线性 +2/关 | 1 | 40 | 无 | 个 | lv_05 塔位数（§3.1 CSV [PLACEHOLDER]20）。高难关 20 格 |
| lvl_first_clear_meta_lv01 | level_reward(lv_01) | 100 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | lv_01 首通元资源（§3.2 字段 [PLACEHOLDER]；CSV 示例 100）。首通主激励 |
| lvl_first_clear_meta_lv02 | level_reward(lv_02) | 150 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | lv_02 首通元资源（CSV 示例 150） |
| lvl_first_clear_meta_lv03 | level_reward(lv_03) | 200 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | lv_03 首通元资源（CSV 示例 200） |
| lvl_first_clear_meta_lv04 | level_reward(lv_04) | 250 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | lv_04 首通元资源（doc 示例未列，按 +50/关外推） |
| lvl_first_clear_meta_lv05 | level_reward(lv_05) | 300 | 线性 +50/关 | 0 | 9999 | 无 | meta_res | lv_05 首通元资源（按 +50/关外推） |
| lvl_repeat_meta_lv01 | level_reward(lv_01) | 20 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | lv_01 重复通关元资源（§3.2 字段 [PLACEHOLDER]；CSV 示例 20）。防刷：首通 1/5 |
| lvl_repeat_meta_lv02 | level_reward(lv_02) | 30 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | lv_02 重复通关元资源（CSV 示例 30） |
| lvl_repeat_meta_lv03 | level_reward(lv_03) | 40 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | lv_03 重复通关元资源（CSV 示例 40） |
| lvl_repeat_meta_lv04 | level_reward(lv_04) | 50 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | lv_04 重复通关元资源（按 +10/关外推） |
| lvl_repeat_meta_lv05 | level_reward(lv_05) | 60 | 线性 +10/关 | 0 | 9999 | 无 | meta_res | lv_05 重复通关元资源（按 +10/关外推） |

## 备注 / 待裁定
- §3.1 `diff_mult`/`reward_mult` 在 CSV 中已给具体值（1.0–2.2，随关递增），非 [PLACEHOLDER]，故未列；二者为关卡内波表/奖励缩放系数，与上方 per-level 静态配置独立。
- `first_clear_meta`/`repeat_meta` 的「重复 / 首通」比值约 1/5，抑制通关刷资源（防主导策略）。
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。

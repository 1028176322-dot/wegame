# 数值设计表：S11 元进度（解锁/元进度）

> 关联 F 码：F13 F16 · GDD：—（SYSTEM_BREAKDOWN §S11）· 设计文档：systems/S11_meta_progression.md
> 说明：本表为该系统设计文档 §3 配置表（meta_config）与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。
> v0.2 修订：解锁门槛改由 **S29 玩家等级**驱动（unlock_config.required_level 属 C 域 S29，本 B 域不填）；原 `cost` 资源花费解锁已废弃（meta_res 旧语义 TBD）。本表按任务要求仅填 `meta_upgrade` 的 `effect_value` 初值 + S11 自有数值。

## 字段规范
- param_id：参数唯一标识（snake_case；系统参数前缀 meta_ 等），全局唯一、稳定，禁止中文
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
| meta_upgrade_start_gold_effect | meta_config(n_gold1) | 0.20 | - | 0 | 2.0 | 无（达 unlock_config.required_level 后永久生效；门槛由 S29 填） | % | 永久升级·起始金币 +20%（effect_value，§3.1 CSV n_gold1）。经济类加成，刻意避开 S29 的 dmg/range/atk_speed 以免双重计算 |
| meta_upgrade_leak_tolerance_effect | meta_config(n_lives1) | 2 | - | 0 | 10 | 无（达 unlock_config.required_level 后永久生效；门槛由 S29 填） | 条(Lives) | 永久升级·漏怪容错 +2 Lives（effect_value，§3.1 CSV n_lives1）。容错类，非战斗基础属性 |
| meta_upgrade_wood_gain_effect | meta_config(n_wood1) | 0.20 | - | 0 | 2.0 | 无（达 unlock_config.required_level 后永久生效；门槛由 S29 填） | % | 永久升级·木头产出 +20%（effect_value，§3.1 CSV n_wood1）。经济类，与 S03 局内 wood 解耦、长线增益 |
| meta_node_grid_spacing | meta_config(TreeView) | 140 | - | 80 | 240 | 无 | px | 元进度解锁树节点网格间距（§1.3 组件表 `间距 [PLACEHOLDER]140`）。120×120 节点 + 140 间距保证三态可读、不拥挤 |
| meta_res_cap | (clamp, §2.4 E09) | 999999 | - | 0 | 999999 | 无 | meta_res | 元资源上限钳制（§2.4 E09 `meta_res 上限 [PLACEHOLDER]`）。防溢出/显示异常；长线多源累积（结算/签到/成就）的安全上界 |
| meta_display_meta_res | meta_config(MetaBar) | 0 | - | 0 | 999999 | 无 | meta_res | §1.2 线框「元资源:[PLACEHOLDER]」为运行期实时值（读 S18 当前 meta_res），新档初始 0。**非调优量**（UI 显示槽），仅作占位说明 |

## 备注 / 待裁定
- **NEEDS-DESIGN（跨域·S29 裁定）`meta_required_level`**：6 个节点（n_magic/n_poison/n_thunder/n_gold1/n_lives1/n_wood1）的 `required_level` 及 §3.1 字段上限 `1–[PLACEHOLDER]` 中的上限，归属 C 域 S29 `unlock_config.required_level`（任务 #4 明确「由 S29 数值表填，本域 S11 只填 meta_upgrade 的 effect_value 初值」）。本表**不填**，建议暂定值供 S29 采纳：n_magic=L2、n_poison=L4、n_thunder=L6、n_gold1=L3、n_lives1=L5、n_wood1=L7（渐进、与 S29 unlock_config feature 一一对应）；§3.1 字段上限建议 = S29 `player_level_config` 的 max_level。
- **NEEDS-DESIGN（DO 裁定）`meta_cost`**：原 6 节点 `cost`（解锁花费元资源）随 v0.2 改为 S29 等级门槛而废弃，doc 多处标 [OBSOLETE-待定]、meta_res 旧花费语义 TBD。本表**不填**；待 DO 裁定 meta_res 最终用途（纯展示 / 未来系统）。
- §3.1 `effect_value` 字段默认值 0.1 为全局示例，本表以各 meta_upgrade 节点实际初值覆盖（见上表 3 行）。
- 本系统已给初值的 [PLACEHOLDER] 全部完成；剩余 [PLACEHOLDER]（required_level / cost）按任务范围标 NEEDS-DESIGN，不属 B 域 S11 填值职责。

# 数值设计表：S07 HUD/操控系统

> 关联 F 码：F9 · GDD：§9（适配 §8） · 设计文档：systems/S07_hud.md
> 说明：本系统为 UX/布局层，设计文档 §3（hud_config）**无 [PLACEHOLDER]**，全部为已定 UX 默认结构值。下列为这些默认值的统一登记（base = 已给默认，min/max 取 §2.4 钳制区间），列此备查与跨系统一致性核对。所有数值为**已定默认 / 待异形屏实测微调**，非平衡 placeholder。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；塔属性前缀 t_<tower>_，系统参数前缀 sys_/econ_/wave_ 等），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.dmg_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| hud_top_bar_h | hud_config | 70 | - | 50 | 120 | 无 | px | 顶条高（设计基准），已定默认；钳制 [50,120] 同 §2.4 |
| hud_min_touch | hud_config | 96 | - | 64 | 120 | 无 | px | 最小点击区边长，无障碍调优杆(接 S22)；钳制最小 64 同 §2.4 |
| hud_safe_margin | hud_config | 20 | - | 0 | 40 | 无 | px | 安全边距（距屏边），已定默认；钳制 ≥0 |
| hud_design_width | hud_config | 750 | - | - | - | 无 | px | 设计基准宽（适配用），结构值非调优 |
| hud_design_height | hud_config | 1334 | - | - | - | 无 | px | 设计基准高（适配用），结构值非调优 |
| hud_speed_2x_free | hud_config | true | - | - | - | 无 | bool | 加速免费（建议免费，防刷经济） |
| hud_show_lives_in_top | hud_config | true | - | - | - | 无 | bool | Lives 进顶条 |
| hud_speed_levels | hud_config | [1,2] | - | - | - | 无 | json | 倍速档（增强可 [1,2,3]） |
| hud_pause_confirm | hud_config | false | - | - | - | 无 | bool | 暂停免确认（防误触） |
| hud_vibrate_on_leak | hud_config | true | - | - | - | 无 | bool | 漏怪震动（接 S22/S23） |

## 备注 / 待裁定
- 本系统 §3 原无 [PLACEHOLDER]，故无 NEEDS-DESIGN；上表为已定 UX 默认值登记，便于跨系统一致性核对（如 S07 只引用 S03/S04/S06 的展示值，不持有独立数值）。
- 唯一“调优杆”性质的参数是 `hud_min_touch`（无障碍/误触，接 S22），已给 96、钳制最小 64；后续按实机单指可达性微调。
- 本系统与玩家等级(S29)无关，level_link 全为“无”。
- 若后续引入 3x 加速档，仅需把 `hud_speed_levels` 改为 [1,2,3]，不影响本表其他项。

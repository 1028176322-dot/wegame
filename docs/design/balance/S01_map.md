# 数值设计表：S01 地图/塔位系统

> 关联 F 码：F1 · GDD：§4 · 设计文档：systems/S01_map.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

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
| sys_ring_count | map_config | 3 | - | 1 | 6 | 无 | 圈 | 环形路径圈数。初值 3（内/中/外三环），决定怪物被多塔命中次数与单局时长；钳制区间 [1,6] 同 §2.4 异常边界，越界回退默认 |
| sys_ring_radius | map_config | 110,170,230 | - | 40 | 300 | 无 | px | 每圈半径(px，设计基准)，数组长度须 = sys_ring_count(3)。内110/中170/外230，外圈直径460 落于 75..675 路径框内不越界、不压顶栏 |
| sys_loop_count | map_config | 2 | - | 1 | 6 | 无 | 圈 | 怪物需绕满圈数才抵达终点。初值 2，与单局波数共决时长；过大拖节奏、过小难形成“循环圈”体验 |
| sys_slot_inner_count | map_config | 6 | - | 0 | 200 | 无 | 个 | 内环塔位数。初值 6，影响内圈 DPS 利用率；与 sys_slot_outer_count 合计 16 个可用塔位 |
| sys_slot_outer_count | map_config | 10 | - | 0 | 200 | 无 | 个 | 外环塔位数（贵但覆盖长）。初值 10，合计 16 塔位，贴近《绿色循环圈》有限塔位的策略密度 |
| sys_move_speed | map_config | 100 | - | 20 | 200 | 无 | px/s | 怪物基础移动速度。初值 100px/s：外环单圈周长≈2π×230≈1445px，loop_count=2 时单怪暴露≈29s，给足塔输出窗口；钳制下限 20 同 §2.4 |

## 备注 / 待裁定
- 本系统所有 [PLACEHOLDER] 均已给初值，无 NEEDS-DESIGN。
- `sys_ring_radius` 为数组（逗号分隔），引擎须校验 `length == sys_ring_count`；若不等须回退 map_default 并告警 S25。
- 地图类参数与玩家等级(S29)无关，level_link 统一为“无”。
- `slot_size`(80)、`ring_count`/`move_speed` 的钳制下限等结构值已在设计文档给定，本表不重复。

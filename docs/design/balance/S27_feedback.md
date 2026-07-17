# 数值设计表：S27 客服反馈系统

> 关联 F 码：F41 · GDD：§8（适配） · 设计文档：systems/S27_feedback.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 fb_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（字 / KB / px(边长) / 秒 / 条）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| fb_max_len | feedback_config | 500 | - | 100 | 2000 | 无 | 字 | 反馈文本上限 500 字，超长截断提示剩余（文档 E4）。初值 500。 |
| fb_screenshot_max_kb | feedback_config | 500 | - | 50 | 2000 | 无 | KB | 截图体积上限 500KB，超则压缩到上限或提示重选（文档 E3）。初值 500。 |
| fb_screenshot_size | feedback_config | 600 | - | 200 | 1000 | 无 | px(边长) | 截图边长上限 600px，压缩后附缩略。初值 600。 |
| fb_submit_cooldown | feedback_config | 10 | - | 0 | 60 | 无 | 秒 | 提交冷却 10s，防连点重复建单（文档 E6）。初值 10。 |
| fb_pending_max | feedback_config | 20 | - | 1 | 50 | 无 | 条 | 待补报队列上限 20 条，满则环形覆盖最旧（文档 E10）。初值 20。 |

## 备注 / 待裁定
- 文档 §3.1 其余字段（enable=true、types、attach_screenshot=true、attach_context=true、report_target=ops）为具体默认，**非 [PLACEHOLDER]**。
- 5 个 [PLACEHOLDER]（文本上限/截图KB/截图边长/提交冷却/待补报上限）均已给初值。
- 无 NEEDS-DESIGN 项。

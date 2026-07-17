# 数值设计表：S20 生命周期系统

> 关联 F 码：F31 · GDD：§8（适配） · 设计文档：systems/S20_lifecycle.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 lc_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（bool / 毫秒 / 秒 等）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| lc_auto_pause_on_hide | lifecycle_config | true | - | - | - | 无 | bool | 切后台自动暂停（文档 §3.1 默认 true）。 |
| lc_save_on_hide | lifecycle_config | true | - | - | - | 无 | bool | 切后台存档（默认 true）。 |
| lc_resume_confirm | lifecycle_config | true | - | - | - | 无 | bool | 回前台确认再续（防误触，默认 true）。弱网容错预设可设 false。 |
| lc_bg_no_tick | lifecycle_config | true | - | - | - | 无 | bool | 后台无产出（防作弊/合规，默认 true）。挂起期间所有 ticker/产出停。 |
| lc_pause_bgm_on_hide | lifecycle_config | true | - | - | - | 无 | bool | 切后台停 BGM（交 S23，默认 true）。 |
| lc_max_resume_lock_ms | lifecycle_config | 300 | - | 100 | 2000 | 无 | 毫秒 | 恢复竞态锁时长，防快速切前台导致恢复 broadcast 重入（文档 §3.1 范围 100–2000，默认 300）。初值 300ms。 |
| lc_save_retry_queue | lifecycle_config | true | - | - | - | 无 | bool | 存失败进补存队列（默认 true），onShow 补存不阻切后台。 |

## 备注 / 待裁定
- **S20 设计文档无 [PLACEHOLDER] 标记**（行为型系统，无平衡数值）。本表依据 §3.1 `lifecycle_config` 默认值生成工程配置初值，作为完整数据层参考。
- `max_resume_lock_ms` 为唯一数值调优杆，其余为布尔行为开关。
- 无 NEEDS-DESIGN 项。

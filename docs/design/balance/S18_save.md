# 数值设计表：S18 存档系统

> 关联 F 码：F11 F32 · GDD：§8（适配） · 设计文档：systems/S18_save.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 save_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（如 growth^level、+x%/级、线性 +x；无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（如 "套用 player_level_config.dmg_mult(单行,不累加)" / "无" / "公式: ..."）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天 / MB）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| save_storage_limit | save_schema | 10 | - | - | 10 | 无 | MB | 微信本地 storage 配额硬上限约 10MB（文档 E3 即引用此值）。超出触发清理非关键缓存(日志/临时)+压缩后重试，仍败则告警"存储空间不足"并保活关键档。初值对齐微信平台规范。 |
| save_backup_count | save_schema | 1 | - | 1 | 5 | 无 | 份 | 保留最近 1 份 rollback 备份（save_backup），每次成功写后复制当前档。初值 1 份（默认），多份提升回退容错但增存储占用。 |
| save_checksum_algo | save_schema | crc32 | - | - | - | 无 | 算法 | 完整性校验算法（本地基础校验，防离线篡改）。与 S24 anticheat_config.checksum_algo 对齐为 crc32；深防作弊见 S24。初值取 crc32（轻量、够用）。 |

## 备注 / 待裁定
- S18 设计文档 §3.1 `save_schema` 其余字段（schema_version=1、meta_res=0、best_wave=0 等）均为具体默认值，**非 [PLACEHOLDER]**，不属本表填值范围；其完整契约见原文档。
- 木(wood) 明确**不写入** `save_schema`（session 货币，每局归零）——属 v0.2-rev 设计红线，本表无需为 wood 设参数。
- 无 NEEDS-DESIGN 项：`[PLACEHOLDER]` 存储上限 / 备份份数 / 校验算法均已给初值。

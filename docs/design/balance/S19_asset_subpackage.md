# 数值设计表：S19 资源分包系统

> 关联 F 码：F30 F34 F35 · GDD：§8（适配） · 设计文档：systems/S19_asset_subpackage.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 sub_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（gold / wood / % / px / 秒 / 级 / 次 / 条 / 天 / MB / KB）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| sub_download_timeout_s | subpackage_config | 30 | - | 5 | 120 | 无 | 秒 | 单包下载无进度超过 30s 判超时（文档 E3），转重试逻辑（防卡死）。初值 30s 平衡弱网容忍与卡死风险。 |
| sub_total_pkg_limit_mb | subpackage_config | 20 | - | - | 20 | 无 | MB | 微信小游戏总包（主包+分包）上限约 20MB（文档 §3.1 注「总包分档随平台更新」）。单包 4MB 见 sub_size_limit_kb。初值对齐微信平台规范。 |
| sub_size_limit_kb | subpackage_config | 4096 | - | 512 | 4096 | 无 | KB | 单包体积上限 4MB（微信规范），主包同档。文档 §3.1 `size_limit` 默认值即 4096，构建期校验超则拒过审。 |
| sub_retry_max | subpackage_config | 3 | - | 1 | 10 | 无 | 次 | 分包下载失败自动重试上限（文档状态机「重试次数<3」）。≥3 弹 z=85 失败层（防无限转圈）。初值 3 次。 |

## 备注 / 待裁定
- 文档 §3.1 `subpackage_config` 其余字段（preload=false、preload_wifi_only=true、priority=5 等）为具体默认，**非 [PLACEHOLDER]**。
- `size_limit` 在文档表中已给默认值 4096(KB)，本表将其单列 `sub_size_limit_kb` 以补全数据层；其 `priority`/`md5` 等为调度/完整性用途，非数值调优杆。
- 无 NEEDS-DESIGN 项：`[PLACEHOLDER]` 下载超时 / 总包上限均已给初值（重试次数原硬编码 3，已显式化）。

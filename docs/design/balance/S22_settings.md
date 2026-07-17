# 数值设计表：S22 设置系统

> 关联 F 码：F39 · GDD：§7（无障碍） · 设计文档：systems/S22_settings.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 st_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（bool / enum 等）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| st_bgm | settings_config | true | - | - | - | 无 | bool | BGM 开关（交 S23）。默认开。 |
| st_sfx | settings_config | true | - | - | - | 无 | bool | 音效开关（交 S23）。默认开。 |
| st_shake | settings_config | true | - | - | - | 无 | bool | 震动开关（wx.vibrateShort）。默认开。 |
| st_font_size | settings_config | medium | - | - | - | 无 | enum | 字号 small/medium/large，默认 medium（影响 S7）。 |
| st_tap_scale | settings_config | normal | - | - | - | 无 | enum | 点击区缩放 normal/large（无障碍，影响 S7），默认 normal。 |
| st_auto_cast_active | settings_config | false | - | - | - | 无 | bool | 主动技自动释放开关（交 S28）。默认关（手动优先，玩家主动开启自动释放）。 |
| st_language | settings_config | zh-CN | - | - | - | 无 | enum | 语言，首批仅 zh-CN（预留多语钩子）。 |

## 备注 / 待裁定
- **S22 设计文档无 [PLACEHOLDER] 标记**。本表依据 §3.1 `settings_config` 默认值生成数据层初值。
- 具体音量（bgm_volume/sfx_volume）由 S23 `audio_config` 持有，本系统只管开关与偏好（见 S23 平衡表）。
- 无 NEEDS-DESIGN 项。

# 数值设计表：S23 音频系统

> 关联 F 码：F18 F35 · GDD：§2（Fun Hypothesis 放大器） · 设计文档：systems/S23_audio.md
> 说明：本表为该系统设计文档 §3 配置表与正文中所有 [PLACEHOLDER] 数值参数的**具体初值**。所有数值为**初值 / 待试玩调优**，非最终平衡。字段命名见下方规范。

## 字段规范
- param_id：参数唯一标识（snake_case；前缀 audio_），全局唯一、稳定，禁止中文
- module：所属配置表/模块（对应设计文档 §3 表名）
- base：基础值（Lv1 / 初始状态）
- growth：成长系数（无则填 -）
- min / max：下限 / 上限（钳制区间；无界填 -）
- level_link：与玩家等级(S29)关联方式（本系统无关填 "无"）
- unit：单位（倍(0-1) / 个 / 倍(0.1-1) 等）
- description：含义与调优说明（含为何取此初值）

## 数值表
| param_id | module | base | growth | min | max | level_link | unit | description |
|---|---|---|---|---|---|---|---|---|
| audio_bgm_volume | audio_config | 0.6 | - | 0 | 1 | 无 | 倍(0-1) | BGM 音量 60%。0=静音不崩，1=不破音(限幅)。初值 0.6 留余量防爆音。 |
| audio_sfx_volume | audio_config | 0.8 | - | 0 | 1 | 无 | 倍(0-1) | 音效音量 80%。音效较 BGM 更突出以强化打击感。 |
| audio_max_sfx_concurrent | audio_config | 16 | - | 4 | 32 | 无 | 个 | 音效并发上限 16。超则按 sfx_priority 丢低优先(如 hit)，保 boss/upgrade（文档 E1）。初值 16 平衡听感与性能。 |
| audio_shake_intensity | audio_config | 0.5 | - | 0.1 | 1 | 无 | 倍(0.1-1) | 震屏强度 0.5（相机位移比例），不超安全区（文档 E8）。初值 0.5 中强反馈。 |

## 备注 / 待裁定
- 文档 §3.1 其余字段（bgm_enabled/sfx_enabled 镜像 S22、shake_on_kill=true、hit_fx_level=mid、sfx_priority json）为具体默认，**非 [PLACEHOLDER]**。
- 4 个 [PLACEHOLDER]（音量×2 / 并发上限 / 震屏强度）均已给初值，均为试听调优杆。
- 无 NEEDS-DESIGN 项。

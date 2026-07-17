<!-- 编码: UTF-8 -->
# TECH_ARCHITECTURE.md — 技术架构（current）

> 领域：tech-architecture（方案 §3）
> Baseline Date: 2026-07-17 ｜ Owner: Decision Owner ｜ Review Trigger: 引擎升级/技术栈变更/首个工程任务落地

## 已裁定技术变量（Decision Owner 2026-07-17）

| 变量 | 值 | 说明 |
|---|---|---|
| 引擎 | **Cocos Creator 3.8.8** | 固定主版本；升级需独立 ADR + 影响分析 |
| 开发语言 | TypeScript（Cocos 3.x 默认） | 除非首个工程任务裁定改用 JS |
| 包管理器 | npm | 用于第三方模块 / Cocos 扩展；引擎本体由编辑器管理 |
| 构建目标 | 微信小游戏 | 经 Cocos Creator「构建发布」→ 微信小游戏 |
| 源码根 `PRIMARY_PRODUCT_ROOT` | `unassessed` | 待首个工程任务创建 Cocos 工程目录后裁定并冻结 |

## 约束
- 引擎主版本（3.8.x）冻结；跨大版本升级属 C3 变更，须独立 ADR 与回归验证（方案 §18）。
- 技术栈相关决策以本文件为唯一 current 入口；与 product-design / gameplay-systems 冲突时按 §3 冲突协议升级裁决。
- 首个工程任务须创建实际 Cocos 工程并回填 `PRIMARY_PRODUCT_ROOT` 与对应冻结 SHA。

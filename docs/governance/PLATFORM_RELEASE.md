<!-- 编码: UTF-8 -->
# PLATFORM_RELEASE.md — 平台与发布（current）

> 领域：platform-release（方案 §3）
> Baseline Date: 2026-07-17 ｜ Owner: Decision Owner ｜ Review Trigger: 发布平台变更/微信政策变化/接入新渠道

## 已裁定平台/发布变量（Decision Owner 2026-07-17）

| 变量 | 值 | 说明 |
|---|---|---|
| 主平台 `PRIMARY_PLATFORM` | **微信小游戏（WeChat Mini Game）** | 单一平台优先；多端扩展属后续决策 |
| 运行环境 | 微信小游戏运行时（JS / Cocos Creator runtime） | |
| 发布模式 | **微信小游戏发布（manual）** | 经微信平台审核后上线，非自动发布 |
| 构建产物 | Cocos Creator 构建输出 → 微信开发者工具预览/上传 | |
| 合规要求 | 需微信 appid、用户隐私合规（`wx.login` / 用户信息授权等） | 首个接入工程须落实；详见 SECURITY_RULES.md |

## 约束
- 当前为手动发布（manual），不启用自动 CD；发布门禁与回滚策略见方案 §18，首个发布任务前须完成发布演练。
- 接入微信账号体系 / 网络 / 存储时，秘密与用户数据处置按 SECURITY_RULES.md 与安全域 current 执行。
- 平台变更（如新增 H5 / 抖音小游戏）须独立 ADR，不得在本文件顺手扩展。

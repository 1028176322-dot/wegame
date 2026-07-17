<!-- 编码: UTF-8 -->
# Authority Index — 领域权威索引

> 每个领域最多一个 current 入口（方案 §3）。两个同级 current 冲突时停止该决策分支并申请裁决，禁止按日期/文件名自动选赢家。
> Baseline Date: 2026-07-17 ｜ Owner 缺省为 Decision Owner（用户本人）。

| Domain | Current | Supporting | Superseded | Status | Owner | Baseline Date | Review Trigger |
|---|---|---|---|---|---|---|---|
| ai-governance | `docs/governance/通用AI项目管理方案.md` | 本索引、各治理规则 | — | current | Decision Owner | 2026-07-17 | 方法论章节或模板变化 |
| product-design | `docs/design/GDD.md` | 本索引、ADR-0002 | — | current | Decision Owner | 2026-07-17 | 玩法大改/平台合规变化 |
| tech-architecture | `docs/governance/TECH_ARCHITECTURE.md` | 方案 §14 | — | current | Decision Owner | 2026-07-17 | 引擎升级/首个工程任务 |
| data-config | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 引入配置/存档结构 |
| ux-content-assets | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 引入美术/音频/文案资产 |
| gameplay-systems | `docs/design/GDD.md` | 本索引、ADR-0002 | — | current | Decision Owner | 2026-07-17 | 塔种调整/核心机制变更 |
| test-quality | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 建立测试框架 |
| platform-release | `docs/governance/PLATFORM_RELEASE.md` | 方案 §18 | — | current | Decision Owner | 2026-07-17 | 发布平台变更/微信政策变化 |
| security-compliance | `docs/governance/SECURITY_RULES.md` | 方案 §15、§16 | — | current | Decision Owner | 2026-07-17 | 引入密钥/用户数据/合规要求 |
| progress | `docs/progress/_index.md` | 方案 §7 | — | current | Decision Owner | 2026-07-17 | 新增任务或状态迁移 |

## 冻结锁

| 对象 | SHA-256 |
|---|---|
| `docs/governance/通用AI项目管理方案.md` | `0bb4b00bfb0a433be144b0b636cf071af2f4ba689f536d8453a631d898ee298e` |
| `docs/governance/TECH_ARCHITECTURE.md` | `3ed1a6acbf1a4647eae639e69bfd1d8e3f07e64e90d41b88a94094e30a78eafc` |
| `docs/governance/PLATFORM_RELEASE.md` | `2ecc88addbb901c8f8b168c470fa4ed282746c73d6533cd30f218ce6d9936207` |
| `docs/design/GDD.md` | `2adaef2ff6fab1ed8379c5683936a52244df331f0309dd9aa6dd6af2a039d30f` |

> 注：tech-architecture、platform-release、product-design、gameplay-systems 均已由 Decision Owner 裁定 current 入口（2026-07-17；D-01 玩法=塔防，参考《绿色循环圈》，见 ADR-0002 与 `docs/design/GDD.md`）。剩余 `unassessed`：data-config、ux-content-assets、test-quality，须在对应首个工程/决策任务中裁定。

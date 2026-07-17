<!-- 编码: UTF-8 -->
# Authority Index — 领域权威索引

> 每个领域最多一个 current 入口（方案 §3）。两个同级 current 冲突时停止该决策分支并申请裁决，禁止按日期/文件名自动选赢家。
> Baseline Date: 2026-07-17 ｜ Owner 缺省为 Decision Owner（用户本人）。

| Domain | Current | Supporting | Superseded | Status | Owner | Baseline Date | Review Trigger |
|---|---|---|---|---|---|---|---|
| ai-governance | `docs/governance/通用AI项目管理方案.md` | 本索引、各治理规则 | — | current | Decision Owner | 2026-07-17 | 方法论章节或模板变化 |
| product-design | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 确定游戏玩法/目标 |
| tech-architecture | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 引擎/技术栈选型 |
| data-config | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 引入配置/存档结构 |
| ux-content-assets | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 引入美术/音频/文案资产 |
| gameplay-systems | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 确定核心系统/关卡 |
| test-quality | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 建立测试框架 |
| platform-release | `unassessed` | — | — | unassessed | Decision Owner | 2026-07-17 | 确定发布平台/商店 |
| security-compliance | `docs/governance/SECURITY_RULES.md` | 方案 §15、§16 | — | current | Decision Owner | 2026-07-17 | 引入密钥/用户数据/合规要求 |
| progress | `docs/progress/_index.md` | 方案 §7 | — | current | Decision Owner | 2026-07-17 | 新增任务或状态迁移 |

## 冻结锁

| 对象 | SHA-256 |
|---|---|
| `docs/governance/通用AI项目管理方案.md` | `0bb4b00bfb0a433be144b0b636cf071af2f4ba689f536d8453a631d898ee298e` |

> 注：游戏相关领域（product/tech/gameplay/ux/platform）当前均为 `unassessed`，须在对应首个决策任务中由 Decision Owner 裁定 current 入口后更新本表。

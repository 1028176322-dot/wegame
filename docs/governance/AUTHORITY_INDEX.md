<!-- 编码: UTF-8 -->
# Authority Index — 领域权威索引

> 每个领域最多一个 current 入口（方案 §3）。两个同级 current 冲突时停止该决策分支并申请裁决，禁止按日期/文件名自动选赢家。
> Baseline Date: 2026-07-17 ｜ Owner 缺省为 Decision Owner（用户本人）。

| Domain | Current | Supporting | Superseded | Status | Owner | Baseline Date | Review Trigger |
|---|---|---|---|---|---|---|---|
| ai-governance | `docs/governance/通用AI项目管理方案.md` | 本索引、各治理规则 | — | current | Decision Owner | 2026-07-17 | 方法论章节或模板变化 |
| product-design | `docs/design/GDD.md` | 本索引、ADR-0002 | — | current | Decision Owner | 2026-07-17 | 玩法大改/平台合规变化 |
| tech-architecture | `docs/governance/TECH_ARCHITECTURE.md` | 方案 §14 | — | current | Decision Owner | 2026-07-17 | 引擎升级/首个工程任务 |
| data-config | `data/README.md` | `docs/design/SPEC_STANDARD.md` | — | current | Decision Owner | 2026-07-17 | 引入配置/存档结构 |
| ux-content-assets | `docs/design/UX_CONTENT_BASELINE.md` | — | — | current | Decision Owner | 2026-07-17 | 引入美术/音频/文案资产 |
| gameplay-systems | `docs/design/GDD.md` | 本索引、ADR-0002 | — | current | Decision Owner | 2026-07-17 | 塔种调整/核心机制变更 |
| system-design | `docs/design/SYSTEM_BREAKDOWN.md` | GDD/FEATURE_SCOPE/GAME_FLOW/`docs/design/systems/` | — | current | Decision Owner | 2026-07-17 | 新系统增删/系统边界变更/塔种扩展 |
| test-quality | `docs/decisions/ADR-0004-test-quality-baseline.md` | — | — | current | Decision Owner | 2026-07-17 | 建立测试框架 |
| platform-release | `docs/governance/PLATFORM_RELEASE.md` | 方案 §18 | — | current | Decision Owner | 2026-07-17 | 发布平台变更/微信政策变化 |
| security-compliance | `docs/governance/SECURITY_RULES.md` | 方案 §15、§16 | — | current | Decision Owner | 2026-07-17 | 引入密钥/用户数据/合规要求 |
| progress | `docs/progress/_index.md` | 方案 §7 | — | current | Decision Owner | 2026-07-17 | 新增任务或状态迁移 |

## 冻结锁

| 对象 | SHA-256 |
|---|---|
| `docs/governance/通用AI项目管理方案.md` | `0bb4b00bfb0a433be144b0b636cf071af2f4ba689f536d8453a631d898ee298e` |
| `docs/governance/TECH_ARCHITECTURE.md` | `3ed1a6acbf1a4647eae639e69bfd1d8e3f07e64e90d41b88a94094e30a78eafc` |
| `docs/governance/PLATFORM_RELEASE.md` | `2ecc88addbb901c8f8b168c470fa4ed282746c73d6533cd30f218ce6d9936207` |
| `docs/design/GDD.md` | `724a46cc9e1cbdd399e2fc26a506abd60082dc01d822ea112cc380d16d432779` |
| `docs/design/SYSTEM_BREAKDOWN.md` | `319e0de6eff836b80a24bc941fba098aef0f49c09d085f4e953616ee0ad1449c` |
| `docs/design/FEATURE_SCOPE.md` | `ea5c6051fbef773e801ad32adab26380d72d915736aa468849a80a10fada9489` |
| `docs/design/GAME_FLOW.md` | `d185e92b442447fa0c24d121cf254475428fa36ac66b36833a0c20f03869ca34` |
| `data/README.md` | `b8056e0d27bd451c6cbde5287b8e56bc4c57ccf4802f2bb89bf54803db2946d8` |
| `docs/design/UX_CONTENT_BASELINE.md` | `488102b9321e7cc22b7113427f0b41a4bf59b9ac934450629b77d386cecf074f` |
| `docs/decisions/ADR-0004-test-quality-baseline.md` | `080d309b5dd6e7aaf17e8f69937febbcdce68d2ac59f9791e82baec10bc4dd3a` |

> 注：全部 11 个领域均已由 Decision Owner 裁定 current 入口（2026-07-17；D-01 玩法=塔防见 ADR-0002；D-03 引擎=Cocos Creator 3.8.8；D-08 裁定 ux-content-assets=`docs/design/UX_CONTENT_BASELINE.md`、test-quality=`docs/decisions/ADR-0004-test-quality-baseline.md`）。冻结锁覆盖 10 个 current 文档（canonical + 9 业务/治理 current）；memory/skills 等运行态目录不纳入冻结锁。

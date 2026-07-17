<!-- 编码: UTF-8 -->
# CHANGE LIST — CL-2026-0717-authority

Status: execution_authorized
Risk: C2
Authorization mode: Decision Owner 直接裁定（chat 2026-07-17）
Task-card SHA: AUTHORITY_INDEX.md 预编辑 `81b0e116…6a0264`

## Decisions
- D-02 主平台：裁定为 **微信小游戏（WeChat Mini Game）**
- D-03 引擎/技术栈：裁定为 **Cocos Creator 3.8.8**（语言默认 TypeScript，包管理 npm）
- D-05 发布模式：裁定为 **微信小游戏发布**（微信平台审核，manual）
- D-01 玩法/产品目标：仍 **待定（unassessed）**，由 Decision Owner 后续裁定
- 项目类型：由泛"游戏开发"收敛为 **微信小游戏**

## NEW
- `docs/governance/TECH_ARCHITECTURE.md`（tech-architecture 领域 current 入口）
- `docs/governance/PLATFORM_RELEASE.md`（platform-release 领域 current 入口）

## MOD
- `PROJECT_RULES.md` §1 初始化变量：PROJECT_NAME 描述、PRIMARY_PLATFORM、PACKAGE_MANAGER、运行环境、发布模式
- `docs/governance/AUTHORITY_INDEX.md`：tech-architecture / platform-release 状态 unassessed→current；末注更新；冻结锁补两张新 current 文档 SHA
- `docs/governance/PROJECT_MANAGEMENT.md` §关键裁剪决定 #1：注明 tech-architecture 与 platform-release 已 current

## VERIFY / NOCHG
- product-design / gameplay-systems / data-config / ux-content-assets / test-quality：保持 unassessed（玩法待定，无对应资产/测试）
- 冻结锁中 `通用AI项目管理方案.md` SHA 不变

## DELETE / MOVE / RENAME
- 无

## Forbidden Scope
- 不得修改方法论 canonical 文档正文
- 不得在此变更中顺手降低治理要求或改写其他 current 文档
- 不得 commit / push（推送需 Decision Owner 单独授权）

## Baseline SHA-256（预编辑）
| 文件 | SHA-256 |
|---|---|
| `docs/governance/AUTHORITY_INDEX.md` | `81b0e11639afe61e1578ab7126409705afbb9697a0495f9b51f2906dde6a0264` |
| `PROJECT_RULES.md` | `6c049189ba91cb2a91c4f2de6c4e7e69f9f301a7066ef516d0612cbae82affbc` |
| `docs/governance/PROJECT_MANAGEMENT.md` | `a9332487cd535760fb45604db00800e1f2fbb4c0f0cc2f708c44c2ec38b16c4a` |

## Exact Instructions
1. 新建两张 current 文档，内容仅记录已裁定变量，不扩展未裁定范围
2. 编辑 PROJECT_RULES.md 与 AUTHORITY_INDEX.md，保持表格结构
3. 新建文档写入后计算 SHA 追加至冻结锁
4. `git add` 指定文件，`git commit`（本地，不推送）

## Validation
- [ ] 两张 current 文档存在且 owner=Decision Owner
- [ ] AUTHORITY_INDEX 中 tech-architecture / platform-release 行 status=current 且 Current 列指向新文档
- [ ] PROJECT_RULES 初始化变量与裁定一致
- [ ] 冻结锁含两张新文档 SHA；方法论 SHA 未变
- [ ] 未触发 forbidden scope

## Rollback
- `git revert <commit>` 回退本次提交；或直接 restore 三个被改文件至上表 baseline SHA

## Authorization Invalidators
- Decision Owner 撤回上述裁定
- 微信小游戏平台政策重大变化导致发布模式改变

## DoD
- 权威索引反映已裁定变量，未裁定项仍显式 unassessed；冻结锁与新文档 SHA 一致。

<!-- Change List 正文不自写自身最终 SHA；外部授权回执提供冻结锁。 -->

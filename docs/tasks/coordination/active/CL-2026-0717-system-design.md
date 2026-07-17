<!-- 编码: UTF-8 -->
# CHANGE LIST — CL-2026-0717-system-design

Status: execution_authorized
Risk: C2
Authorization mode: Decision Owner 直接裁定（chat 2026-07-17，q-1「清理+本地提交(推荐)」）
Task-card SHA: `docs/governance/AUTHORITY_INDEX.md`（本次编辑后提交态）= `fac7fb824332e2e0f1bde411434e54814e7a70d210e33a2e39e4ef0eab24410f`

## Decisions
- D-06 设计 corpus 落地裁定：`docs/design/` 全量（GDD v0.2-rev + SYSTEM_BREAKDOWN + FEATURE_SCOPE + GAME_FLOW + 29 份系统策划案 v0.2-detailed）作为 `system-design` 领域 current 入口。
- 解锁阈值策略：`unlock_config.required_level` 全部保持 `[PLACEHOLDER]`，由后续**数值设计表**驱动（DO 裁定，chat 2026-07-17；不在本次写死）。

## NEW
- `docs/design/SYSTEM_BREAKDOWN.md`（system-design 当前入口）
- `docs/design/FEATURE_SCOPE.md`
- `docs/design/GAME_FLOW.md`
- `docs/design/systems/` S01–S29 共 29 份系统策划案（v0.2-detailed）+ `_index.md`
- `docs/design/systems/S28_skill_system.md`、`S29_level_system.md`（本批新增系统）

## MOD
- `docs/design/GDD.md`：v0.2-rev（S28 技能系统 + S29 玩家等级系统）；§5.8 技能系统 / §5.9 玩家等级系统；修正 S28 对 GDD 章节引用（技能系统 §5.8）
- `docs/governance/AUTHORITY_INDEX.md`：新增 `system-design` 行（current）；冻结锁刷新 GDD、新增 SYSTEM_BREAKDOWN/FEATURE_SCOPE/GAME_FLOW
- 残留一致性清理（design-strategist-cleanup 汇报）：S18 补 player_level/current_xp/unlocked_features 字段；S05 接 S29 引用；GAME_FLOW §2.5 改等级驱动解锁；S11 旧 meta_res 扣费路径标 OBSOLETE/TBD；S03「应急换木」→「应急兑换」；SYSTEM_BREAKDOWN:189 / FEATURE_SCOPE:39「§5.9 胜负」→「§5.7 胜负」

## VERIFY / NOCHG
- product-design / gameplay-systems 仍指向 GDD（未改指向）
- 冻结锁中 methodology / tech-architecture / platform-release SHA 未变
- 木(wood) 仍为 session 货币，不写入 S18 存档（见 S03/S04）

## DELETE / MOVE / RENAME
- 无

## Forbidden Scope
- 不得修改 methodology canonical 文档正文
- 不得 commit / push 到远程（推送需 Decision Owner 单独授权）
- 不得写死任何数值调优量（保持 `[PLACEHOLDER]`）

## Baseline SHA-256（pre-edit）
| 文件 | SHA-256 |
|---|---|
| `docs/design/GDD.md`（旧冻结锁） | `2adaef2ff6fab1ed8379c5683936a52244df331f0309dd9aa6dd6af2a039d30f` |
| 其余 3 顶层文档 / systems/ 为 NEW（无 baseline） | — |

## 冻结锁 SHA-256（提交态）
| 文件 | SHA-256 |
|---|---|
| `docs/design/GDD.md` | `fed0c67ee285d5a1d301b27c555f0294c407974c02fb5dc724ef02eaa988b372` |
| `docs/design/SYSTEM_BREAKDOWN.md` | `c19299c1acfe8db4c8a2694467e8289470b5db35d614e54de2e12f9504f4827c` |
| `docs/design/FEATURE_SCOPE.md` | `5f226cbd819383944657ac7f551003eb2fac495c11216e31107236e4b8d368ef` |
| `docs/design/GAME_FLOW.md` | `d185e92b442447fa0c24d121cf254475428fa36ac66b36833a0c20f03869ca34` |

## Exact Instructions
1. 清理残留（design-strategist-cleanup 已完成）
2. 编辑 AUTHORITY_INDEX.md 增加 `system-design` 行与冻结锁
3. `git add docs/design/ docs/governance/AUTHORITY_INDEX.md docs/tasks/coordination/active/CL-2026-0717-system-design.md`
4. `git commit`（本地，不推送）

## Validation
- [ ] `system-design` 行 status=current 且 Current 指向 SYSTEM_BREAKDOWN.md
- [ ] 冻结锁含 4 顶层文档 SHA，与提交态一致
- [ ] 设计 corpus 全部入版本库（29 系统 + 4 顶层 + _index + S28/S29）
- [ ] 未触碰 forbidden scope

## Rollback
- `git revert <commit>` 回退本次提交；或 `git restore` 上述文件至 baseline SHA。

## Authorization Invalidators
- Decision Owner 撤回设计 corpus current 裁定
- v1.0 系统边界重大调整导致 `system-design` 重新 open

## DoD
- 设计 corpus 作为单一事实源入版本库；AUTHORITY_INDEX 反映 `system-design` current；冻结锁与外部可核对；解锁阈值留待数值设计表。

<!-- Change List 正文不自写自身最终 SHA；冻结锁以提交态 SHA 记录。 -->

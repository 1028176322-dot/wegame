<!-- 编码: UTF-8 -->
# DOCUMENT_RULES.md — 文档管理规则（current）

> 依据方案 §11。本文件记录本项目强制执行的文档规则。

## 文档类型（方案 §11.1）

current / target / migration / supporting / report / historical / deprecated。

## 强制规则（方案 §11.2）

1. 同一领域最多一个 current 入口；current 变化必须同步 `AUTHORITY_INDEX.md`。
2. 被替代文档写明 `superseded_by`，不删除掩盖历史。
3. 文档链接使用相对路径，须可存在性检查。
4. 示例占位符不得残留在正式 current 区段。
5. 报告不得自升为 accepted。
6. 根目录不新增 md（方案根允许清单）；方法论 canonical 副本唯一，勿在根另建。

## current 文档元数据（方案 §3.3）

每份 current 文档建议包含：`doc_status / view_type / scope / owner / baseline_date / evidence_level / supersedes / superseded_by / review_trigger`。`mixed` 文档必须在正文区分"当前/目标/迁移中"。

## 创建文档前

按方案 §4.4 决策树与 §11.4 先确认：类型、领域、读者、Owner、是否已有 canonical 入口、维护触发器、退出路径。NEW 文档必须在 Change List 声明并说明是否同步权威索引（方案 §4.5）。
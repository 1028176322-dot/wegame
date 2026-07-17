<!-- 编码: UTF-8 -->
# MEMORY_SCHEMA.md — 项目记忆规范（current）

> 依据方案 §12。本目录是本项目**唯一活动记忆根**，不得存在竞争副本。

## 分层（方案 §12.1）

| 层级 | 内容 | 写权限 | 位置 |
|---|---|---|---|
| G0 索引 | 稳定规则入口与主题路由 | Curator | 本文件 |
| G1 主题 | 长期有效决定与约束 | Curator 合并 | `topics/` |
| G2 Inbox | 带任务ID的候选补丁 | Executor 可新增 | `inbox/` |
| G3 日志 | 临时执行记录 | 对应任务 | 见 WorkBuddy `.workbuddy/memory/`（工作区日志） |

## 条目 schema（方案 §12.5）

```text
id:
topic:
kind: fact / decision / constraint / preference / lesson
statement:
source:
evidence_level:
owner:
created_at:
last_validated:
review_after:
invalidated_by:
sensitivity:
supersedes:
```

## 准入与禁止（方案 §12.2）

- 每条长期记忆须含上述完整字段；statement 原子化，一条只表达一个可验证事实/决定。
- 禁止写入：密钥、个人隐私、无来源推测、实时任务进度、机器绝对路径、过期平台口径、大段聊天记录。

## Inbox 状态机（方案 §12.7）

`proposed → validated → merged`，另有 `rejected / conflict / expired`。仅 Curator（Decision Owner）在冻结窗口合并。

## 主题清单

暂无长期记忆条目。首个业务决策产生后，由 Executor 提交 `inbox/` 补丁，Curator 合并入 `topics/`。

<!-- 编码: UTF-8 -->
# wegame

游戏开发项目。本仓库已按《通用 AI 项目管理方案》(Standard 规模) 建立治理体系。

## 从这里开始

- **唯一启动入口**：[`PROJECT_RULES.md`](PROJECT_RULES.md) — 所有执行者（人工/AI）动手前必读。
- **方法论全文**：[`docs/governance/通用AI项目管理方案.md`](docs/governance/通用AI项目管理方案.md)
- **领域权威索引**：[`docs/governance/AUTHORITY_INDEX.md`](docs/governance/AUTHORITY_INDEX.md)
- **进度总索引**：[`docs/progress/_index.md`](docs/progress/_index.md)

## 目录结构

```text
PROJECT_RULES.md          # 唯一启动入口
docs/
  governance/             # 方法论 + 权威索引 + 治理规则
  decisions/              # ADR 决策记录
  progress/               # 进度索引
  tasks/                  # 任务卡、Change List、协调、报告、模板
memory/                   # 项目记忆（唯一活动根）
skills/                   # Skill 注册表与安装锁
tools/                    # validators / maintenance / generators
config/                   # 根允许清单、文件放置规则
archive/ deprecated/ experimental/
```

## 当前状态

- 生命周期：prototype ｜ 团队模式：human-AI ｜ 采用规模：Standard
- 多数产品变量为 `unassessed`，将随首个工程任务逐步裁定（见 `PROJECT_RULES.md §1`）。

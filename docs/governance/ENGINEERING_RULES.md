<!-- 编码: UTF-8 -->
# ENGINEERING_RULES.md — 工程实现与代码审查规则（current）

> 依据方案 §14、§17。游戏项目引入引擎/技术栈后，须补充领域附录（资产管线、场景、序列化、平台）。

## 变更风险与证据（方案 §6）

- 变更风险：C0（自检）/ C1（目标测试）/ C2（影响图+独立审查+全量回归）/ C3（冻结授权+独立审查+回滚+最终冻结验证）。
- 证据等级：E0 推测 / E1 存在 / E2 人工检查 / E3 自动测试 / E4 真实环境或业务验收。声明必须写明证据等级。

## 实现前契约（方案 §14.1）

C2/C3 工程任务先明确：问题与最小复现、接口定义方、唯一实现、composition root、全部消费方、测试 fixture 与负向测试、配置/数据/存档/API 兼容、性能/安全/确定性/平台影响。

## 测试纪律（方案 §14.4）

- 禁止 skip/only、删除失败测试、放宽关键断言、无原因类型抑制。
- 先失败后修复；共同根因不得拆成多个局部 mock 掩盖。
- 真实编译/lint/测试/静态门禁分别记录；占位命令不是 PASS。

## 状态词（方案 §17.3）

`PASS / FAIL / NOT_RUN / NOT_IMPLEMENTED / BLOCKED`。`TEST_COMMAND` = `python tools/validators/run_tests.py`；`VALIDATE_COMMAND` = `python tools/validators/run_validators.py`（命令定义见 `config/commands.json`）。已落地（证据 E3：13 项负向 fixture 自测全 PASS；当前仓库全量门禁 0 ERROR）。

## 基线失败规则（方案 §17.2）

新增失败必须修复；失败数不变仅说明"未引入新失败"；不得通过改测试/忽略/关门禁降低失败数。

## Impact Map（方案 §14.6）

C2/C3 必须产出影响图，每项标 `affected / not affected / unassessed` 及依据。

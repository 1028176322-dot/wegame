<!-- 编码: UTF-8 -->
# experimental/

## Purpose
一次性实验代码/原型，隔离于生产入口（方案 §4.10）。

## Owner
Executor（每个子目录归属对应任务）

## Allowed Contents
`experimental/<TASK-ID>/` 下的实验产物。

## Forbidden Contents
被生产入口默认引用的代码；无 Owner/到期日的长期内容。

## Retention/Cleanup
每个子目录有 Owner、到期日与转正规则。转正须重走审查/测试/放置/注册流程，不能直接移动后宣称完成。

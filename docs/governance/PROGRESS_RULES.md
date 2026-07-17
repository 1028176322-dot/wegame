<!-- 编码: UTF-8 -->
# PROGRESS_RULES.md — 进度管理规则（current）

> 依据方案 §7。

## 七值进度状态（方案 §7.1）

`unassessed / not_started / in_progress / blocked / verification_pending / verified / deprecated`。

> `completed` 不作为进度状态；最终接受用独立 `accepted` 验收记录。

## 状态迁移（方案 §7.7）

```text
unassessed → not_started → in_progress → verification_pending → verified
                     ↘ blocked ↗
任意非终态 → deprecated
```

- 无实际写入/执行证据不得进入 in_progress。
- 无完整实施回执不得进入 verification_pending。
- 无规定证据不得进入 verified；verified 后目标/输入变化必须重新评估。

## 进度文件最小字段（方案 §7.2）

`Status / Owner / Scope / Evidence / Last Verified / Not Completed Items / Block Reason / Unblock Condition / Next Review Trigger`。

## 索引一致性

进度总索引 `docs/progress/_index.md` 必须由个体进度文件生成或校验，不得维护两套独立状态。

<!-- 编码: UTF-8 -->
# UX / 内容资产基线规范（ux-content-assets current）

> 领域：ux-content-assets｜Owner：Decision Owner｜Baseline：2026-07-17
> Status：current（基线 v0.1，待 DO 终审）｜依据方案 §4、SECURITY_RULES §16.3

本文件为 UX / 美术 / 音频 / 文案资产的统一基线。后续细化只扩展子章节，不改变本文件职责边界。

## 1. 资产分类与管线
- 美术：角色 / 场景 / UI / 特效 / 图标，经 `assets/source/`（只读来源）→ `assets/processed/`（处理后，记录输入 hash 与工具版本）。
- 音频：BGM / SFX / 语音，统一格式与采样率（**NEEDS-DESIGN**，待 DO 裁定）。
- 文案：全部走 `data/i18n/` 多语言文本表，代码按 id 读取不硬编码；命名空间见 `docs/design/i18n/text_config.csv`。

## 2. 命名与放置
- 资产命名遵循双轨制命名债 N1–N6（param_id 前缀白名单、枚举对齐 S30 等）。
- 禁止 `new/ final/ temp/ misc/ others/` 目录与 `*_new.*` / `*_final.*` / `*_copy.*` / `*_backup*.*` 命名（root_allowlist）。
- 本地化文本 key 全局唯一；缺失回退 zh-CN（运行时落点 `assets/config/i18n/`）。

## 3. 合规
- 资产不含硬编码密钥；外部资源记录来源与许可（放 `data/raw` 或 `assets/source`）。
- 跨平台：注意大小写、路径分隔符、保留名、最大长度（SECURITY_RULES §16.3）。

## 4. 待裁定（NEEDS-DESIGN，owner=Decision Owner）
- 美术风格指南（塔防主题视觉语言）。
- 音频格式 / 采样率 / 压缩策略。
- 资产 LOD / 图集 / 分包策略（关联 S19 资产分包）。

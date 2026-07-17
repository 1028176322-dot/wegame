<!-- 编码: UTF-8 -->
# tools/validators — Phase 5 工程/安全/门禁检查器

> 默认只读，返回明确退出码。依据 `docs/governance/ENGINEERING_RULES.md` §17.3。
> 命令定义见 `config/commands.json`。

## 检查器

| 脚本 | 职责 | 退出码 |
|---|---|---|
| `file_placement_validator.py` | 根 allowlist + 子目录模式校验；全局禁名/禁目录 | 0=无ERROR / 1=ERROR / 2=运行错误 |
| `secret_validator.py` | 秘密扫描（AWS/私钥/GitHub/Slack/Google/OpenAI/JWT/赋值高熵）；输出脱敏 | 0=0命中 / 1=命中 / 2=运行错误 |
| `gate_validator.py` | 冻结锁 SHA 一致性 + 进度七值/五状态词合法性 | 0=无ERROR / 1=ERROR / 2=运行错误 |

## 入口

- `VALIDATE_COMMAND` = `python tools/validators/run_validators.py`（聚合三检查器）
- `TEST_COMMAND` = `python tools/validators/run_tests.py`（负向 fixture 自测）

命令以仓库相对路径执行；运行器按脚本位置推导 `REPO_ROOT = parents[2]`，
扫描范围仅 `git ls-files` 跟踪文件，不修改任何文件。

> 秘密扫描跳过已知测试/夹具路径（`tools/validators/`、`/tests/`、`fixtures`），
> 因其含合成密钥仅供自测；此为透明可审计的跳过，不掩盖真实凭据。

## 证据等级

- `run_tests.py` 全 PASS → 检查器行为有负向 fixture 证明（E3）。
- `run_validators.py` 对当前仓库 0 ERROR → 当前事实状态（E3）。
- 冻结锁 SHA 漂移属治理红线，gate_validator 必报 ERROR。

## 扩展

新增检查器：在 `tools/validators/` 下追加 `*.py`（main 返回 0/1/2），
并加入 `run_validators.py` 的 `VALIDATORS` 列表。

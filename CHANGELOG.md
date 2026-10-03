# 更新日志

本文件记录 `funui` 的重要变更，版本按时间倒序排列。

## [未发布]

### 修复

- 修正 `pyproject.toml` 的 `[project.urls] Issues` 误指向 `farfarfun/todo-list`，
  改回本仓库 `farfarfun/funui/issues`。
- `.gitignore` 补齐 `*.db`、`*.rar`、`.run/`、`logs/`、`.vscode/`，并取消 `.idea/` 的注释，
  覆盖 SPEC.md §10 要求的数据库、压缩包、运行时文件、日志、IDE 配置规则。

## [1.0.4] - 2026-09-20

### 变更

- 将项目说明和元数据改为如实描述当前的预留命名空间状态。
- 移除未打包、未维护且与 `funui` 命名空间无关的聊天 Demo。

### 修复

- 删除 Demo 中提交的示例密码和硬编码会话密钥。
- 补充 MIT 协议信息和组织介绍。

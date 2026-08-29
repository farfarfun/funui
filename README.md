# funui

## 说明

这个仓库的实际代码和 `funui` 这个名字对不上：

- 仓库里唯一有内容的代码是根目录下的 `main.py` + `frontend.py`：基于 [NiceGUI](https://nicegui.io/) + FastAPI 写的一个一次性聊天/社交 Demo（页面里自称 "Zwitter"，标题为 `Welcome to Zwitter!!`，页脚署名 `Made with ❤️ by tr1x_em`），包含注册（`register`）、登录（`login`/`try_login`，密码明文存在 `logins.json` 里）、在线用户列表（`update_user`）、实时聊天（`chat_messages`/`send`）等页面，可以用 `run.sh dev`/`run.sh prod` 本地跑起来，也带了 `vercel.json` 用于部署到 Vercel。
- `pyproject.toml` 里声明的 Python 包 `src/funui/`（含 `funui/__init__.py`、`funui/module/__init__.py`、`funui/page/__init__.py`）全部是空文件，没有任何实现，也没有被 `main.py`/`frontend.py` 引用。

也就是说，`funui` 目前不是一个可用的 UI 组件库/工具包，仓库里真正在跑的是一个跟包名无关、未维护的聊天 Demo 一次性脚本。

## 安装

`funui` 已发布到 PyPI（当前版本 1.0.3），但对应的 `src/funui` 包内容为空，`pip install funui` 之后拿到的是一个没有任何可用 API 的空包，因此这里不给出安装/引用示例。

## 运行 Demo（Zwitter 聊天页面）

Demo 的真实依赖（fastapi/nicegui/uvicorn/starlette 等）已迁移进 `pyproject.toml` 的
`[dependency-groups] demo`，由 `uv.lock` 统一管理和自动升级；根目录
`requirements.txt` 现在是 `uv export --group demo` 自动生成的产物，不再手工维护。

```bash
uv sync --group demo
./run.sh dev   # 或 ./run.sh prod
```

或者仍然用 `pip install -r requirements.txt`（该文件由 uv 自动生成，效果等价）。

默认监听 `127.0.0.1:8080`，依次访问 `/`（首页）、`/register`（注册）、`/login`（登录，默认账号见 `logins.json`）、`/chat`（聊天室）。

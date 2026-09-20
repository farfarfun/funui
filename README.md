# funui

## 说明

`funui` 是 farfarfun 预留的 Python UI 命名空间。目前只保证包可安装、可导入，
不提供可调用的公开 API。

仓库曾附带一套与包名无关的 NiceGUI 聊天 Demo。该 Demo 没有进入发布产物，且包含不安全的示例凭据，已在 `1.0.4` 中移除。

## 安装

```bash
pip install funui
```

## 最小示例

```python
import funui
```

## 开发

```bash
uv sync
uv run pytest
uv build
```

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。

"""funui 包的基础冒烟测试。"""


def test_import_funui() -> None:
    """顶层命名空间应可正常导入。"""
    import funui

    assert funui is not None

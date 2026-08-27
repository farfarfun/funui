"""Lightweight smoke tests for the published ``funui`` package.

IMPORTANT CONTEXT (read before extending this file):

The ``funui`` PyPI distribution's actual source lives under ``src/funui`` in
this repository. As of this writing, ``src/funui/__init__.py``,
``src/funui/module/__init__.py`` and ``src/funui/page/__init__.py`` are all
completely empty files. The package therefore currently exposes *no* public
classes, functions, or constants at all -- it is importable, and that is
the full extent of its functionality.

Separately, the repository ROOT contains an unrelated NiceGUI + FastAPI chat
demo application (``main.py``, ``frontend.py``, etc.). That code is NOT part
of the ``funui`` distribution (it is not under ``src/funui`` and is not
packaged/shipped to PyPI), so it is intentionally NOT exercised by these
tests -- testing it here would be testing a different, unrelated app under
the ``funui`` package's name.

Because of this, the only thing that can honestly be smoke-tested today is
that the package and its submodules import cleanly. When real functionality
is added to ``src/funui``, this file should grow real tests alongside it.
"""


def test_import_funui():
    """The top-level package must import without error."""
    import funui

    assert funui is not None


def test_import_funui_module_submodule():
    """The ``funui.module`` submodule must import without error."""
    import funui.module

    assert funui.module is not None


def test_import_funui_page_submodule():
    """The ``funui.page`` submodule must import without error."""
    import funui.page

    assert funui.page is not None


def test_funui_has_no_public_api_yet():
    """Document the current (stub) state of the package explicitly.

    src/funui/__init__.py is empty today, so it defines no functions,
    classes, or constants of its own. This test pins that fact down: if
    someone adds real exports to funui/__init__.py, this test will start
    failing and should be updated (or removed) alongside real functionality
    tests for the new API.

    Note: ``dir(funui)`` may additionally list submodules such as
    ``module``/``page`` simply because importing them elsewhere in this
    process attaches them as attributes of the ``funui`` package -- that is
    a Python import mechanic, not something ``funui/__init__.py`` itself
    defines, so submodule attributes are excluded from this check.
    """
    import types

    import funui

    own_public_names = [
        name
        for name in dir(funui)
        if not name.startswith("_") and not isinstance(getattr(funui, name), types.ModuleType)
    ]
    assert own_public_names == []

from __future__ import annotations

import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
EXAMPLES = (
    "calls.py",
    "commands.py",
    "dialogs.py",
    "echo.py",
    "files.py",
    "gifts.py",
    "groups.py",
    "json_output.py",
    "login.py",
    "messages.py",
    "updates.py",
)


@pytest.mark.parametrize("filename", EXAMPLES)
def test_examples_are_short_and_valid(filename: str) -> None:
    source = (ROOT / "examples" / filename).read_text(encoding="utf-8")
    ast.parse(source, filename=filename)
    assert len(source.splitlines()) <= 20
    assert "argparse" not in source


def test_examples_use_a_simple_named_session() -> None:
    for path in (ROOT / "examples").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name) and node.func.id == "Client":
                assert len(node.args) == 1
                assert isinstance(node.args[0], ast.Constant)
                assert node.args[0].value == "my_account"

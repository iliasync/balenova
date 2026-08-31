from __future__ import annotations

import ast
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
EXAMPLES = (
    "calls.py",
    "commands.py",
    "dialogs.py",
    "dialogs_by_type.py",
    "echo.py",
    "files.py",
    "filter_messages.py",
    "gifts.py",
    "groups.py",
    "json_output.py",
    "login.py",
    "messages.py",
    "updates.py",
)


@pytest.mark.parametrize("filename", EXAMPLES)
def test_example_cli_help(filename: str) -> None:
    env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
    completed = subprocess.run(
        [sys.executable, str(ROOT / "examples" / filename), "--help"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr


def test_examples_do_not_pass_a_phone_to_client_constructor() -> None:
    for path in (ROOT / "examples").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name) and node.func.id == "Client":
                assert not node.args, f"{path.name} passes a positional credential"

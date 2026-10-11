"""Text formatting helpers for Bale Markdown."""

from __future__ import annotations

import re


def bold(text: str) -> str:
    """Format text as bold for Bale messenger (* text *).

    According to Bale specifications, asterisks must have spaces around text
    or standalone boundaries.
    """
    return f"*{text}*"


def italic(text: str) -> str:
    """Format text as italic for Bale messenger (_ text _)."""
    return f"_{text}_"


def link(text: str, url: str) -> str:
    """Format inline hyperlink for Bale messenger ([text](url))."""
    return f"[{text}]({url})"


def spoiler(text: str, description: str = "") -> str:
    """Format instant view / spoiler explanation (```[text]description```)."""
    if description:
        return f"```[{text}]{description}```"
    return f"```[{text}]```"


def code(text: str) -> str:
    """Format inline monospace code (`text`)."""
    return f"`{text}`"


def code_block(text: str, language: str = "") -> str:
    """Format a multi-line code block with optional syntax language.

    Format:
    ```language
    line1
    line2
    ```
    """
    clean_lang = language.strip()
    clean_text = text.rstrip("\n")
    if clean_lang:
        return f"```{clean_lang}\n{clean_text}\n```"
    return f"```\n{clean_text}\n```"


pre = code_block


def escape_markdown(text: str) -> str:
    """Escape Bale Markdown special characters."""
    return re.sub(r"([*_`\[\]()])", r"\\\1", text)

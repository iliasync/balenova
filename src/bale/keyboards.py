"""Keyboard and markup builders for Bale messages, inspired by aiogram."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class InlineKeyboardButton:
    """A button in an inline keyboard."""

    text: str
    callback_data: str | None = None
    url: str | None = None
    web_app_url: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"text": self.text}
        if self.callback_data is not None:
            data["callback_data"] = {"value": self.callback_data}
        if self.url is not None:
            data["url"] = {"value": self.url}
        if self.web_app_url is not None:
            data["web_app"] = {"url": self.web_app_url}
        return data

    def __repr__(self) -> str:
        attrs = [f"text={self.text!r}"]
        if self.callback_data is not None:
            attrs.append(f"callback_data={self.callback_data!r}")
        if self.url is not None:
            attrs.append(f"url={self.url!r}")
        if self.web_app_url is not None:
            attrs.append(f"web_app_url={self.web_app_url!r}")
        return f"InlineKeyboardButton({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class InlineKeyboardMarkup:
    """An inline keyboard with rows of buttons displayed attached to a message."""

    inline_keyboard: list[list[InlineKeyboardButton]] = field(default_factory=list)

    def add(self, *buttons: InlineKeyboardButton) -> InlineKeyboardMarkup:
        """Add buttons to the keyboard in a single row."""
        self.inline_keyboard.append(list(buttons))
        return self

    def row(self, *buttons: InlineKeyboardButton) -> InlineKeyboardMarkup:
        """Add a full row of buttons."""
        return self.add(*buttons)

    def to_dict(self) -> dict[str, Any]:
        return {
            "inline_keyboard_markup": {
                "list_of_inline_list": [
                    {"inline_list": [btn.to_dict() for btn in row_btns]}
                    for row_btns in self.inline_keyboard
                ]
            }
        }

    def __repr__(self) -> str:
        return f"InlineKeyboardMarkup({self.inline_keyboard!r})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class KeyboardButton:
    """A button in a custom reply keyboard."""

    text: str
    request_contact: bool = False
    request_location: bool = False

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"text": self.text}
        if self.request_contact:
            data["request_contact"] = {"value": True}
        if self.request_location:
            data["request_location"] = {"value": True}
        return data

    def __repr__(self) -> str:
        attrs = [f"text={self.text!r}"]
        if self.request_contact:
            attrs.append("request_contact=True")
        if self.request_location:
            attrs.append("request_location=True")
        return f"KeyboardButton({', '.join(attrs)})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class ReplyKeyboardMarkup:
    """A custom keyboard with reply buttons displayed below the input field."""

    keyboard: list[list[KeyboardButton]] = field(default_factory=list)
    resize_keyboard: bool = True
    one_time_keyboard: bool = False

    def add(self, *buttons: KeyboardButton) -> ReplyKeyboardMarkup:
        """Add buttons in a single row."""
        self.keyboard.append(list(buttons))
        return self

    def row(self, *buttons: KeyboardButton) -> ReplyKeyboardMarkup:
        """Add a full row of buttons."""
        return self.add(*buttons)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reply_keyboard_markup": {
                "list_of_keyboard_list": [
                    {"keyboard_list": [btn.to_dict() for btn in row_btns]}
                    for row_btns in self.keyboard
                ]
            }
        }

    def __repr__(self) -> str:
        return f"ReplyKeyboardMarkup({self.keyboard!r})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(slots=True)
class ReplyKeyboardRemove:
    """Instruction to remove any active custom reply keyboard."""

    remove_keyboard: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {"reply_keyboard_remove": {"remove_keyboard": self.remove_keyboard}}

    def __repr__(self) -> str:
        return "ReplyKeyboardRemove()"

    def __str__(self) -> str:
        return repr(self)

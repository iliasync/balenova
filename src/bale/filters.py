"""Composable filters for incoming user-session messages."""

from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bale.client import Client
    from bale.models import Message

Predicate = Callable[["Client", "Message"], bool | Awaitable[bool]]


@dataclass(frozen=True, slots=True)
class Filter:
    """An async-aware predicate composable with ``&``, ``|`` and ``~``."""

    predicate: Predicate
    name: str = "filter"

    async def check(self, client: Client, message: Message) -> bool:
        result = self.predicate(client, message)
        if inspect.isawaitable(result):
            result = await result
        return bool(result)

    def __and__(self, other: Filter) -> Filter:
        async def combined(client: Client, message: Message) -> bool:
            return await self.check(client, message) and await other.check(
                client, message
            )

        return Filter(combined, f"({self.name} & {other.name})")

    def __or__(self, other: Filter) -> Filter:
        async def combined(client: Client, message: Message) -> bool:
            return await self.check(client, message) or await other.check(
                client, message
            )

        return Filter(combined, f"({self.name} | {other.name})")

    def __invert__(self) -> Filter:
        async def inverted(client: Client, message: Message) -> bool:
            return not await self.check(client, message)

        return Filter(inverted, f"~{self.name}")


def create(predicate: Predicate, name: str = "custom") -> Filter:
    return Filter(predicate, name)


def all_of(*items: Filter) -> Filter:
    async def predicate(client: Client, message: Message) -> bool:
        for item in items:
            if not await item.check(client, message):
                return False
        return True

    return Filter(predicate, "all")


def any_of(*items: Filter) -> Filter:
    async def predicate(client: Client, message: Message) -> bool:
        for item in items:
            if await item.check(client, message):
                return True
        return False

    return Filter(predicate, "any")


text = Filter(lambda _client, message: bool(message.text), "text")
content = Filter(lambda _client, message: bool(message.content), "content")
gift = Filter(lambda _client, message: message.gift is not None, "gift")
private = Filter(
    lambda _client, message: message.chat.type.value == "private", "private"
)
group = Filter(
    lambda _client, message: message.chat.type.value in {"group", "supergroup"},
    "group",
)
channel = Filter(
    lambda _client, message: message.chat.type.value == "channel", "channel"
)


def command(
    name: str,
    prefix: str = "/",
    min_args: int | None = None,
    max_args: int | None = None,
) -> Filter:
    expected = f"{prefix}{name}".casefold()

    def predicate(_client: Client, message: Message) -> bool:
        if not message.text:
            return False
        parts = message.text.strip().split()
        count = len(parts) - 1
        return bool(parts) and (
            parts[0].casefold() == expected
            and (min_args is None or count >= min_args)
            and (max_args is None or count <= max_args)
        )

    return Filter(predicate, f"command({name})")


# Names familiar to balejs users.
all = all_of
any = any_of


def not_(item: Filter) -> Filter:
    return ~item

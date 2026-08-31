"""Message and lifecycle event dispatcher."""

from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal

from bale.filters import Filter

if TYPE_CHECKING:
    from bale.client import Client
    from bale.models import Message

MessageHandler = Callable[["Message", "Client"], object | Awaitable[object]]
UpdateHandler = Callable[[dict[str, Any], "Client"], object | Awaitable[object]]
ErrorHandler = Callable[[BaseException, "Client"], object | Awaitable[object]]
LifecycleHandler = Callable[["Client"], object | Awaitable[object]]
LifecycleEvent = Literal["connect", "disconnect", "initialize", "shutdown"]


@dataclass(frozen=True, slots=True)
class _MessageRegistration:
    callback: MessageHandler
    filter: Filter | None


class Dispatcher:
    def __init__(self) -> None:
        self._message_handlers: list[_MessageRegistration] = []
        self._update_handlers: list[UpdateHandler] = []
        self._error_handlers: list[ErrorHandler] = []
        self._lifecycle_handlers: dict[LifecycleEvent, list[LifecycleHandler]] = {
            "connect": [],
            "disconnect": [],
            "initialize": [],
            "shutdown": [],
        }

    def add_message_handler(
        self, callback: MessageHandler, filter_: Filter | None = None
    ) -> MessageHandler:
        self._message_handlers.append(_MessageRegistration(callback, filter_))
        return callback

    def add_error_handler(self, callback: ErrorHandler) -> ErrorHandler:
        self._error_handlers.append(callback)
        return callback

    def add_update_handler(self, callback: UpdateHandler) -> UpdateHandler:
        self._update_handlers.append(callback)
        return callback

    def add_lifecycle_handler(
        self, event: LifecycleEvent, callback: LifecycleHandler
    ) -> LifecycleHandler:
        self._lifecycle_handlers[event].append(callback)
        return callback

    async def dispatch_message(self, client: Client, message: Message) -> None:
        for handler in tuple(self._message_handlers):
            try:
                if handler.filter and not await handler.filter.check(client, message):
                    continue
                await _maybe_await(handler.callback(message, client))
            except Exception as error:
                await self.dispatch_error(client, error)

    async def dispatch_update(self, client: Client, update: dict[str, Any]) -> None:
        for handler in tuple(self._update_handlers):
            try:
                await _maybe_await(handler(update, client))
            except Exception as error:
                await self.dispatch_error(client, error)

    async def dispatch_error(self, client: Client, error: BaseException) -> None:
        if not self._error_handlers:
            raise error
        for handler in tuple(self._error_handlers):
            await _maybe_await(handler(error, client))

    async def dispatch_lifecycle(self, event: LifecycleEvent, client: Client) -> None:
        for handler in tuple(self._lifecycle_handlers[event]):
            await _maybe_await(handler(client))


async def _maybe_await(value: object | Awaitable[object]) -> object:
    if inspect.isawaitable(value):
        return await value
    return value

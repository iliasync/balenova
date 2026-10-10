"""Finite State Machine (FSM) support for Bale accounts, inspired by aiogram."""

from __future__ import annotations

import asyncio
from typing import Any


class State:
    """Represents a state in the finite state machine."""

    def __init__(self, state_name: str | None = None) -> None:
        self._state_name = state_name

    def __set_name__(self, owner: type[StatesGroup], name: str) -> None:
        if self._state_name is None:
            self._state_name = f"{owner.__name__}:{name}"

    @property
    def state(self) -> str:
        return self._state_name or "unknown_state"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, State):
            return self.state == other.state
        if isinstance(other, str):
            return self.state == other
        return False

    def __hash__(self) -> int:
        return hash(self.state)

    def __repr__(self) -> str:
        return f"<State '{self.state}'>"


class StatesGroup:
    """Base class to group states together."""

    @classmethod
    def all_states(cls) -> list[State]:
        return [
            getattr(cls, attr)
            for attr in dir(cls)
            if isinstance(getattr(cls, attr), State)
        ]


class MemoryStorage:
    """In-memory state and data storage for conversations."""

    def __init__(self) -> None:
        self._states: dict[tuple[int | str, int | str], str | None] = {}
        self._data: dict[tuple[int | str, int | str], dict[str, Any]] = {}
        self._lock = asyncio.Lock()

    async def set_state(
        self, chat_id: int | str, user_id: int | str, state: State | str | None
    ) -> None:
        async with self._lock:
            key = (str(chat_id), str(user_id))
            if state is None:
                self._states.pop(key, None)
            else:
                self._states[key] = (
                    state.state if isinstance(state, State) else str(state)
                )

    async def get_state(self, chat_id: int | str, user_id: int | str) -> str | None:
        async with self._lock:
            return self._states.get((str(chat_id), str(user_id)))

    async def set_data(
        self, chat_id: int | str, user_id: int | str, data: dict[str, Any]
    ) -> None:
        async with self._lock:
            self._data[(str(chat_id), str(user_id))] = dict(data)

    async def get_data(self, chat_id: int | str, user_id: int | str) -> dict[str, Any]:
        async with self._lock:
            return dict(self._data.get((str(chat_id), str(user_id)), {}))

    async def update_data(
        self, chat_id: int | str, user_id: int | str, **kwargs: Any
    ) -> dict[str, Any]:
        async with self._lock:
            key = (str(chat_id), str(user_id))
            current = self._data.get(key, {})
            current.update(kwargs)
            self._data[key] = current
            return dict(current)

    async def finish(self, chat_id: int | str, user_id: int | str) -> None:
        async with self._lock:
            key = (str(chat_id), str(user_id))
            self._states.pop(key, None)
            self._data.pop(key, None)


class FSMContext:
    """State context bound to a particular user and chat."""

    def __init__(
        self,
        storage: MemoryStorage,
        chat_id: int | str,
        user_id: int | str,
    ) -> None:
        self.storage = storage
        self.chat_id = chat_id
        self.user_id = user_id

    async def set_state(self, state: State | str | None) -> None:
        await self.storage.set_state(self.chat_id, self.user_id, state)

    async def get_state(self) -> str | None:
        return await self.storage.get_state(self.chat_id, self.user_id)

    async def set_data(self, data: dict[str, Any]) -> None:
        await self.storage.set_data(self.chat_id, self.user_id, data)

    async def get_data(self) -> dict[str, Any]:
        return await self.storage.get_data(self.chat_id, self.user_id)

    async def update_data(self, **kwargs: Any) -> dict[str, Any]:
        return await self.storage.update_data(self.chat_id, self.user_id, **kwargs)

    async def clear(self) -> None:
        await self.storage.finish(self.chat_id, self.user_id)

    finish = clear

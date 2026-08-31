"""High-level asynchronous Bale user-session client."""

from __future__ import annotations

import asyncio
import inspect
import re
import time
from collections.abc import Awaitable, Callable, Iterable, Mapping
from pathlib import Path
from typing import Any, TypeVar, overload

from bale.dispatcher import (
    Dispatcher,
    ErrorHandler,
    LifecycleEvent,
    LifecycleHandler,
    MessageHandler,
)
from bale.errors import AuthenticationError, BaleRpcError, ClientStateError
from bale.filters import Filter, command
from bale.models import (
    Chat,
    DefaultResponse,
    Message,
    OtherMessage,
    PeerSource,
    ReportKind,
    User,
    wrap_default,
    wrap_group,
    wrap_message,
    wrap_user,
)
from bale.protocol import ProtocolRecorder
from bale.session import Session, SessionStorage
from bale.transports import GrpcTransport, WebSocketTransport

ResponseT = TypeVar("ResponseT", bound=dict[str, Any])
Prompt = Callable[[str], str | Awaitable[str]]
ClientTask = Callable[["Client"], object | Awaitable[object]]

_PEER_PATTERN = re.compile(r"^(?P<id>\d+)\|(?P<type>\d+)$")
_MESSAGE_PATTERN = re.compile(r"^(?P<rid>\d+)\|(?P<date>\d+)$")
_API_KEY = "C28D46DC4C3A7A26564BFCC48B929086A95C93C98E789A19847BEE8627DE4E7D"


class Client:
    """An async client for real Bale user sessions.

    ``credential`` may be an international phone number or an exported
    ``<user_id>:<jwt>`` session string. Phone authentication is performed only
    when no reusable session is available.
    """

    def __init__(
        self,
        credential: str,
        *,
        session_dir: str | Path = ".",
        session_name: str | None = None,
        update_concurrency: int = 16,
        code_prompt: Prompt | None = None,
        password_prompt: Prompt | None = None,
        signup_name_prompt: Prompt | None = None,
        grpc: GrpcTransport | None = None,
        websocket_options: Mapping[str, Any] | None = None,
        recorder: ProtocolRecorder | None = None,
    ) -> None:
        if not credential.strip():
            raise AuthenticationError("A phone number or Bale session is required")
        self.credential = credential.strip()
        self.dispatcher = Dispatcher()
        self.user: User | None = None
        self._session = (
            Session.parse(self.credential) if _is_session(self.credential) else None
        )
        storage_name = session_name or self.credential
        self._storage = SessionStorage(session_dir, storage_name)
        self._recorder = recorder
        self._grpc = grpc or GrpcTransport(recorder=recorder)
        self._websocket_options = dict(websocket_options or {})
        self._websocket: WebSocketTransport | None = None
        self._code_prompt = code_prompt or _terminal_prompt
        self._password_prompt = password_prompt or _terminal_prompt
        self._signup_name_prompt = signup_name_prompt or _terminal_prompt
        self._update_semaphore = asyncio.Semaphore(max(1, update_concurrency))
        self._update_tasks: set[asyncio.Task[None]] = set()
        self._peer_cache: dict[str, User | Chat] = {}
        self._chat_cache: dict[str, Chat] = {}
        self._author_cache: dict[int, User] = {}
        self._stop_event = asyncio.Event()
        self._running = False
        self._closed = False

    @property
    def connected(self) -> bool:
        return self._websocket is not None and self._websocket.connected

    @property
    def session(self) -> str | None:
        return str(self._session) if self._session else None

    @overload
    def on_message(self, callback: MessageHandler) -> MessageHandler: ...

    @overload
    def on_message(
        self, callback: Filter | None = None
    ) -> Callable[[MessageHandler], MessageHandler]: ...

    def on_message(
        self, callback: MessageHandler | Filter | None = None
    ) -> MessageHandler | Callable[[MessageHandler], MessageHandler]:
        if callable(callback) and not isinstance(callback, Filter):
            return self.dispatcher.add_message_handler(callback)

        def decorator(handler: MessageHandler) -> MessageHandler:
            return self.dispatcher.add_message_handler(handler, callback)

        return decorator

    def on_command(
        self, name: str, filter_: Filter | None = None
    ) -> Callable[[MessageHandler], MessageHandler]:
        combined = command(name) if filter_ is None else command(name) & filter_

        def decorator(handler: MessageHandler) -> MessageHandler:
            return self.dispatcher.add_message_handler(handler, combined)

        return decorator

    def on_error(self, callback: ErrorHandler) -> ErrorHandler:
        return self.dispatcher.add_error_handler(callback)

    def _lifecycle_decorator(
        self, event: LifecycleEvent, callback: LifecycleHandler
    ) -> LifecycleHandler:
        return self.dispatcher.add_lifecycle_handler(event, callback)

    def on_connect(self, callback: LifecycleHandler) -> LifecycleHandler:
        return self._lifecycle_decorator("connect", callback)

    def on_disconnect(self, callback: LifecycleHandler) -> LifecycleHandler:
        return self._lifecycle_decorator("disconnect", callback)

    def on_initialize(self, callback: LifecycleHandler) -> LifecycleHandler:
        return self._lifecycle_decorator("initialize", callback)

    def on_shutdown(self, callback: LifecycleHandler) -> LifecycleHandler:
        return self._lifecycle_decorator("shutdown", callback)

    async def __aenter__(self) -> Client:
        await self.connect()
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.stop()

    async def connect(self) -> None:
        if self.connected:
            return
        if self._closed:
            raise ClientStateError("This client has already been closed")
        self._session = self._session or await self._storage.load()
        if self._session is None:
            self._session = await self._authenticate()
            await self._storage.save(self._session)
        websocket = WebSocketTransport(
            self._session.jwt,
            recorder=self._recorder,
            **self._websocket_options,
        )
        websocket.add_update_handler(self._enqueue_update)
        await websocket.connect()
        self._websocket = websocket
        try:
            self.user = await self.get_me()
        except BaseException:
            self._websocket = None
            await websocket.close()
            raise

    async def disconnect(self) -> None:
        websocket, self._websocket = self._websocket, None
        if websocket is not None:
            await websocket.close()
        if self._update_tasks:
            await asyncio.gather(*tuple(self._update_tasks), return_exceptions=True)

    async def run(self, task: ClientTask | None = None) -> None:
        if self._running:
            raise ClientStateError("Client is already running")
        self._running = True
        self._stop_event.clear()
        try:
            await self.connect()
            await self.dispatcher.dispatch_lifecycle("connect", self)
            await self.dispatcher.dispatch_lifecycle("initialize", self)
            if task is None:
                await self._stop_event.wait()
            else:
                value = task(self)
                if inspect.isawaitable(value):
                    await value
        except asyncio.CancelledError:
            raise
        except Exception as error:
            await self.dispatcher.dispatch_error(self, error)
        finally:
            await self.stop()

    async def stop(self) -> None:
        was_active = self._running or self.connected
        self._running = False
        self._stop_event.set()
        if was_active:
            await self.dispatcher.dispatch_lifecycle("shutdown", self)
        await self.disconnect()

    async def close(self) -> None:
        if self._closed:
            return
        await self.stop()
        await self._grpc.close()
        self._closed = True

    async def export_session(self) -> str:
        if self._session is None:
            self._session = await self._storage.load()
        if self._session is None:
            raise AuthenticationError("No authenticated session is available")
        return str(self._session)

    async def start_phone_auth(self, phone_number: str) -> dict[str, Any]:
        normalized = re.sub(r"\D", "", phone_number)
        if not normalized:
            raise AuthenticationError("The phone number contains no digits")
        return await self._grpc.request(
            "bale.auth.v1.Auth",
            "StartPhoneAuth",
            "request.StartPhoneAuth",
            "response.StartPhoneAuth",
            {
                "phone_number": int(normalized),
                "app_id": 4,
                "api_key": _API_KEY,
                "device_hash": "ce5ced83-a9ab-47fa-80c8-ed425eeb2ace",
                "device_title": "Chrome_138.0.0.0, Python async client",
                "send_code_type": 1,
                "options": b"\x00\x01",
            },
        )

    async def validate_code(self, transaction_hash: str, code: str) -> dict[str, Any]:
        return await self._grpc.request(
            "bale.auth.v1.Auth",
            "ValidateCode",
            "request.ValidateCode",
            "response.Auth",
            {
                "transaction_hash": transaction_hash,
                "code": code,
                "is_jwt": {"value": True},
            },
        )

    async def validate_password(
        self, transaction_hash: str, password: str
    ) -> dict[str, Any]:
        return await self._grpc.request(
            "bale.auth.v1.Auth",
            "ValidatePassword",
            "request.ValidatePassword",
            "response.Auth",
            {
                "transaction_hash": transaction_hash,
                "password": password,
                "is_jwt": {"value": True},
            },
        )

    async def sign_up(
        self, transaction_hash: str, name: str, password: str | None = None
    ) -> dict[str, Any]:
        return await self._grpc.request(
            "bale.auth.v1.Auth",
            "SignUp",
            "request.SignUp",
            "response.Auth",
            {
                "transaction_hash": transaction_hash,
                "name": name,
                "password": {"value": password} if password else None,
            },
        )

    async def sign_out(self) -> DefaultResponse:
        response = await self.post(
            "bale.auth.v1.Auth",
            "SignOut",
            "request.SignOut",
            "response.DefaultResponse",
            {},
        )
        await self.stop()
        await self._storage.delete()
        self._session = None
        self.user = None
        self._peer_cache.clear()
        return wrap_default(response)

    async def invoke(
        self,
        service: str,
        method: str,
        request_type: str,
        response_type: str,
        payload: Mapping[str, Any],
    ) -> dict[str, Any]:
        if self._websocket is not None:
            return await self._websocket.request(
                service, method, request_type, payload, response_type
            )
        return await self.post(service, method, request_type, response_type, payload)

    async def post(
        self,
        service: str,
        method: str,
        request_type: str,
        response_type: str,
        payload: Mapping[str, Any],
    ) -> dict[str, Any]:
        session = self._session or await self._storage.load()
        return await self._grpc.request(
            service,
            method,
            request_type,
            response_type,
            payload,
            access_token=session.jwt if session else None,
        )

    async def edit_name(self, name: str) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditName",
                "request.EditName",
                "response.DefaultResponse",
                {"name": name},
            )
        )

    async def edit_nickname(self, nickname: str | None = None) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditNickName",
                "request.EditNickName",
                "response.DefaultResponse",
                {"nick_name": {"value": nickname} if nickname else None},
            )
        )

    async def edit_about(self, about: str | None = None) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditAbout",
                "request.EditAbout",
                "response.DefaultResponse",
                {"about": {"value": about} if about else None},
            )
        )

    async def check_nickname(self, nickname: str) -> bool:
        response = await self.invoke(
            "bale.users.v1.Users",
            "CheckNickName",
            "request.CheckNickName",
            "response.CheckNickName",
            {"nick_name": nickname},
        )
        return bool(response.get("available"))

    async def get_me(self) -> User:
        session = self._session or await self._storage.load()
        if session is None:
            raise AuthenticationError("No Bale session is available")
        user = await self.get_chat(f"{session.user_id}|1")
        if not isinstance(user, User):
            raise ClientStateError("Could not load the Bale user profile")
        return user

    async def get_chat(self, chat_id: str) -> User | Chat | None:
        cached = self._peer_cache.get(chat_id)
        if cached:
            return cached
        peer = _parse_peer(chat_id)
        if peer:
            return await self._load_peer(*peer)
        normalized = _normalize_query(chat_id)
        response = await self.search_contacts(normalized)
        users = response.get("users") or []
        groups = response.get("groups") or []
        return users[0] if users else groups[0] if groups else None

    async def load_users(self, users: Iterable[int | str]) -> list[User]:
        response = await self.invoke(
            "bale.users.v1.Users",
            "LoadUsers",
            "request.LoadUsers",
            "response.LoadUsers",
            {"user_peers": [_user_peer(value) for value in users]},
        )
        result = [wrap_user(raw).bind(self) for raw in response.get("users", [])]
        for user in result:
            self._peer_cache[f"{user.id}|1"] = user
            if user.is_bot:
                self._peer_cache[f"{user.id}|4"] = user
        return result

    async def load_full_users(self, users: Iterable[int | str]) -> list[dict[str, Any]]:
        response = await self.invoke(
            "bale.users.v1.Users",
            "LoadFullUsers",
            "request.LoadFullUsers",
            "response.LoadFullUsers",
            {"user_peers": [_user_peer(value) for value in users]},
        )
        return list(response.get("full_users", []))

    async def search_contacts(self, query: str) -> dict[str, Any]:
        response = await self.invoke(
            "bale.users.v1.Users",
            "SearchContacts",
            "request.SearchContacts",
            "response.SearchContacts",
            {"request": _normalize_query(query)},
        )
        users = [wrap_user(raw).bind(self) for raw in response.get("users", [])]
        groups = [wrap_group(raw).bind(self) for raw in response.get("groups", [])]
        for user in users:
            self._peer_cache[f"{user.id}|1"] = user
        for group in groups:
            self._peer_cache[group.id] = group
        return {**response, "users": users, "groups": groups}

    async def search_username(self, query: str) -> User | Chat | None:
        result = await self.search_contacts(query)
        users = result.get("users") or []
        groups = result.get("groups") or []
        return users[0] if users else groups[0] if groups else None

    async def create_group(
        self,
        title: str,
        username: str | None = None,
        users: Iterable[int | str] = (),
        *,
        group_type: int = 0,
    ) -> Chat:
        normalized_username = username.strip() if username else None
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "CreateGroup",
            "request.CreateGroup",
            "response.CreateGroup",
            {
                "random_id": _milliseconds(),
                "title": title,
                "users": [_user_peer(user) for user in users],
                "group_type": group_type,
                "username": (
                    {"value": normalized_username} if normalized_username else None
                ),
                "restriction": int(bool(normalized_username)),
            },
        )
        raw = response.get("group")
        if not isinstance(raw, dict):
            raise ClientStateError("Bale did not return the created group")
        # The compact Group response doesn't expose group_type.
        raw.setdefault("group_type", group_type)
        chat = wrap_group(raw).bind(self)
        self._peer_cache[chat.id] = chat
        return chat

    async def create_channel(
        self,
        title: str,
        username: str | None = None,
        users: Iterable[int | str] = (),
    ) -> Chat:
        return await self.create_group(title, username, users, group_type=1)

    async def get_full_group(self, chat_id: str) -> dict[str, Any] | None:
        peer_id, _peer_type = _require_peer_tuple(chat_id)
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetFullGroup",
            "request.GetFullGroup",
            "response.GetFullGroup",
            {"peer": {"group_id": peer_id, "access_hash": 1}},
        )
        value = response.get("full_group")
        return value if isinstance(value, dict) else None

    async def join_chat(self, token_or_url: str) -> Chat:
        token = token_or_url.removeprefix("https://ble.ir/join/").removeprefix(
            "ble.ir/join/"
        )
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "JoinGroup",
            "request.JoinGroup",
            "response.JoinGroup",
            {"token": token},
        )
        return self._cache_group_response(response)

    join_group = join_chat

    async def join_public_chat(self, chat_id: str) -> Chat:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "JoinPublicGroup",
            "request.JoinPublicGroup",
            "response.JoinPublicGroup",
            {"peer": _require_peer(chat_id)},
        )
        return self._cache_group_response(response)

    join_public_group = join_public_chat

    async def leave_chat(self, chat_id: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "LeaveGroup",
            "request.LeaveGroup",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "rid": WebSocketTransport.create_rid(),
                "make_orphan": False,
            },
        )
        self._peer_cache.pop(chat_id, None)
        return wrap_default(response)

    leave_group = leave_chat

    async def get_group_link(self, chat_id: str) -> str | None:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetGroupInviteURL",
            "request.GetGroupInviteUrl",
            "response.GetGroupInviteUrl",
            {"group_peer": _group_peer(chat_id)},
        )
        value = response.get("url")
        return value if isinstance(value, str) else None

    get_group_invite_url = get_group_link

    async def revoke_group_link(self, chat_id: str) -> str | None:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RevokeInviteURL",
            "request.RevokeInviteUrl",
            "response.RevokeInviteUrl",
            {"group_peer": _group_peer(chat_id)},
        )
        value = response.get("url")
        return value if isinstance(value, str) else None

    revoke_invite_url = revoke_group_link

    async def invite_users(
        self, chat_id: str, user_ids: Iterable[int | str]
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.groups.v1.Groups",
            "InviteUsers",
            "request.InviteUsers",
            "response.InviteUsers",
            {
                "group_peer": _group_peer(chat_id),
                "rid": WebSocketTransport.create_rid(),
                "users": [_user_peer(user) for user in user_ids],
            },
        )

    async def kick_user(self, chat_id: str, user_id: int | str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "KickUser",
            "request.KickUser",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "user": _user_peer(user_id),
                "rid": WebSocketTransport.create_rid(),
            },
        )
        return wrap_default(response)

    async def unban_user(self, chat_id: str, user_id: int | str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "UnBanUser",
            "request.UnBanUser",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "user": _user_peer(user_id),
            },
        )
        return wrap_default(response)

    async def set_member_permissions(
        self,
        chat_id: str,
        user_id: int | str,
        permissions: Mapping[str, bool],
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "SetMemberPermissions",
            "request.SetMemberPermissions",
            "response.DefaultResponse",
            {
                "group": _group_peer(chat_id),
                "user": _user_peer(user_id),
                "permissions": dict(permissions),
            },
        )
        return wrap_default(response)

    async def edit_group_title(self, chat_id: str, title: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "EditGroupTitle",
            "request.EditGroupTitle",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "title": title,
                "rid": WebSocketTransport.create_rid(),
            },
        )
        return wrap_default(response)

    async def edit_group_about(self, chat_id: str, about: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "EditGroupAbout",
            "request.EditGroupAbout",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "about": about,
                "rid": WebSocketTransport.create_rid(),
            },
        )
        return wrap_default(response)

    async def load_members(
        self, chat_id: str, limit: int = 50, next_: str | int | None = None
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.groups.v1.Groups",
            "LoadMembers",
            "request.LoadMembers",
            "response.LoadMembers",
            {
                "group": _group_peer(chat_id),
                "limit": limit,
                "next": {"value": str(next_)} if next_ is not None else None,
            },
        )

    async def get_group_members_count(self, chat_id: str) -> int:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetGroupMembersCount",
            "request.GetGroupMembersCount",
            "response.GetGroupMembersCount",
            {"group": _group_peer(chat_id)},
        )
        return int(response.get("members_count", 0))

    async def load_full_chat(self, chat_id: str) -> dict[str, Any] | None:
        peer_id, peer_type = _require_peer_tuple(chat_id)
        if peer_type in (1, 4):
            users = await self.load_full_users([peer_id])
            return users[0] if users else None
        return await self.get_full_group(chat_id)

    async def get_parameters(self) -> list[dict[str, str]]:
        response = await self.invoke(
            "bale.v1.Configs",
            "GetParameters",
            "request.GetParameters",
            "response.GetParameters",
            {},
        )
        return [
            {"key": str(item.get("key", "")), "value": str(item.get("value", ""))}
            for item in response.get("params", [])
        ]

    async def edit_parameter(
        self, key: str, value: str | None = None
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.v1.Configs",
            "EditParameter",
            "request.EditParameter",
            "response.DefaultResponse",
            {"key": key, "value": {"value": value} if value is not None else None},
        )
        return wrap_default(response)

    async def load_history(
        self, chat_id: str, from_date: int = -1, limit: int = 20
    ) -> list[Message]:
        peer = _require_peer(chat_id)
        response = await self._load_history(peer, from_date, limit)
        result = []
        for item in response.get("history", []):
            message = self._wrap_message({**item, "peer": peer})
            if int(message.rid) != 0:
                result.append(message)
        return result

    async def load_dialogs(
        self, limit: int = 40, min_date: int = -1, exclude_pinned: bool = False
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.messaging.v2.Messaging",
            "LoadDialogs",
            "request.LoadDialogs",
            "response.LoadDialogs",
            {
                "min_date": min_date,
                "limit": limit,
                "exclude_pinned_dialogs": exclude_pinned,
            },
        )

    async def send_message(
        self, chat_id: str, text: str, reply_to: Message | None = None
    ) -> Message:
        peer = _require_peer(chat_id)
        rid = WebSocketTransport.create_rid()
        message_payload = {"text_message": {"text": text}}
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "SendMessage",
            "request.SendMessage",
            "response.DefaultResponse",
            {
                "peer": peer,
                "rid": rid,
                "message": message_payload,
                "reply_to": _info_message(reply_to) if reply_to else None,
                "ex_peer": peer,
            },
        )
        return self._wrap_message(
            {
                "peer": peer,
                "sender_uid": self.user.id if self.user else 0,
                "date": response.get("date", 0),
                "rid": rid,
                "message": message_payload,
            }
        )

    async def clear_chat(self, chat_id: str) -> DefaultResponse:
        return await self._simple_peer_call("ClearChat", "ClearChat", chat_id)

    async def delete_chat(self, chat_id: str) -> DefaultResponse:
        return await self._simple_peer_call("DeleteChat", "DeleteChat", chat_id)

    async def message_read(
        self, chat_id: str, date: int | None = None
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "MessageRead",
            "request.MessageRead",
            "response.DefaultResponse",
            {"peer": _require_peer(chat_id), "date": date or _milliseconds()},
        )
        return wrap_default(response)

    seen_chat = message_read

    async def set_online(self, is_online: bool, duration: int = 30) -> DefaultResponse:
        response = await self.invoke(
            "bale.presence.v1.Presence",
            "SetOnline",
            "request.SetOnline",
            "response.DefaultResponse",
            {"is_online": int(is_online), "duration": duration},
        )
        return wrap_default(response)

    async def typing(self, chat_id: str, typing_type: int = 1) -> DefaultResponse:
        response = await self.invoke(
            "bale.presence.v1.Presence",
            "Typing",
            "request.Typing",
            "response.DefaultResponse",
            {"peer": _out_peer(chat_id), "typing_type": typing_type},
        )
        return wrap_default(response)

    start_typing = typing

    async def stop_typing(self, chat_id: str, typing_type: int = 1) -> DefaultResponse:
        response = await self.invoke(
            "bale.presence.v1.Presence",
            "StopTyping",
            "request.StopTyping",
            "response.DefaultResponse",
            {"peer": _require_peer(chat_id), "typing_type": typing_type},
        )
        return wrap_default(response)

    async def message_set_reaction(
        self, chat_id: str, message_id: str, code: str
    ) -> dict[str, Any]:
        rid, date = _require_message_id(message_id)
        return await self.invoke(
            "bale.abacus.v1.Abacus",
            "MessageSetReaction",
            "request.MessageSetReaction",
            "response.MessageSetReaction",
            {
                "peer": _require_peer(chat_id),
                "rid": rid,
                "code": code,
                "date": date,
            },
        )

    async def delete_message(
        self, chat_id: str, message_id: str, just_me: bool = False
    ) -> DefaultResponse:
        rid, date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "DeleteMessage",
            "request.DeleteMessage",
            "response.DefaultResponse",
            {
                "peer": _require_peer(chat_id),
                "rids": [rid],
                "dates": {"dates": [date]},
                "just_mine": {"value": int(just_me)},
            },
        )
        return wrap_default(response)

    async def load_pinned_messages(self, chat_id: str) -> list[Message]:
        peer = _out_peer(chat_id)
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "LoadPinnedMessages",
            "request.LoadPinnedMessages",
            "response.LoadPinnedMessages",
            {"peer": peer},
        )
        return [
            self._wrap_message({**item, "peer": peer})
            for item in response.get("pinned_messages", [])
        ]

    async def pin_message(
        self, chat_id: str, message_id: str, just_mine: bool = False
    ) -> DefaultResponse:
        rid, date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "PinMessage",
            "request.PinMessages",
            "response.DefaultResponse",
            {
                "peer": _require_peer(chat_id),
                "message_id": {"rid": rid, "date": date},
                "just_mine": just_mine,
            },
        )
        return wrap_default(response)

    async def unpin_messages(
        self, chat_id: str, message_ids: Iterable[str] = (), *, all_: bool = False
    ) -> DefaultResponse:
        identifiers = []
        for message_id in message_ids:
            rid, date = _require_message_id(message_id)
            identifiers.append({"rid": rid, "date": date})
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "UnPinMessages",
            "request.UnPinMessages",
            "response.DefaultResponse",
            {
                "peer": _out_peer(chat_id),
                "message_ids": identifiers,
                "all": all_,
            },
        )
        return wrap_default(response)

    async def unpin_message(self, chat_id: str, message_id: str) -> DefaultResponse:
        return await self.unpin_messages(chat_id, [message_id])

    async def unpin_all(self, chat_id: str) -> DefaultResponse:
        return await self.unpin_messages(chat_id, all_=True)

    async def edit_message_text(
        self, chat_id: str, message_id: str, text: str
    ) -> DefaultResponse:
        rid, _date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "UpdateMessage",
            "request.UpdateMessage",
            "response.DefaultResponse",
            {
                "peer": _require_peer(chat_id),
                "rid": rid,
                "updated_message": {"text_message": {"text": text}},
            },
        )
        return wrap_default(response)

    edit_message = edit_message_text

    async def forward_message(
        self, chat_id: str, from_chat_id: str, message_id: str
    ) -> DefaultResponse:
        rid, date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "ForwardMessages",
            "request.ForwardMessages",
            "response.DefaultResponse",
            {
                "peer": _require_peer(chat_id),
                "rid": [WebSocketTransport.create_rid()],
                "forwarded_messages": [
                    {
                        "peer": _require_peer(from_chat_id),
                        "random_id": rid,
                        "date": {"value": date},
                    }
                ],
            },
        )
        return wrap_default(response)

    async def copy_message(
        self, chat_id: str, from_chat_id: str, message_id: str
    ) -> Message:
        rid, date = _require_message_id(message_id)
        history = await self._load_history(_require_peer(from_chat_id), date, 20)
        source = next(
            (item for item in history.get("history", []) if int(item["rid"]) == rid),
            None,
        )
        if source is None:
            raise ClientStateError(f"Could not load source message {message_id}")
        peer = _require_peer(chat_id)
        new_rid = WebSocketTransport.create_rid()
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "SendMessage",
            "request.SendMessage",
            "response.DefaultResponse",
            {
                "peer": peer,
                "rid": new_rid,
                "message": source["message"],
                "ex_peer": peer,
            },
        )
        return self._wrap_message(
            {
                "peer": peer,
                "sender_uid": self.user.id if self.user else 0,
                "date": response.get("date", 0),
                "rid": new_rid,
                "message": source["message"],
            }
        )

    async def report_chat(
        self,
        chat_id: str,
        reason: str | None = None,
        kind: ReportKind = ReportKind.SPAM,
        source: PeerSource = PeerSource.DIALOGS,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.report.v1.Report",
            "ReportInappropriateContent",
            "request.ReportInappropriateContent",
            "response.DefaultResponse",
            {
                "report_body": {
                    "kind": int(kind),
                    "description": reason,
                    "peer_report": {
                        "source": int(source),
                        "peer": _require_peer(chat_id),
                    },
                }
            },
        )
        return wrap_default(response)

    async def report_message(
        self,
        chat_id: str,
        message: Message | OtherMessage,
        reason: str | None = None,
        kind: ReportKind = ReportKind.SPAM,
    ) -> DefaultResponse:
        return await self.report_messages(chat_id, [message], reason, kind)

    async def report_messages(
        self,
        chat_id: str,
        messages: Iterable[Message | OtherMessage],
        reason: str | None = None,
        kind: ReportKind = ReportKind.SPAM,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.report.v1.Report",
            "ReportInappropriateContent",
            "request.ReportInappropriateContent",
            "response.DefaultResponse",
            {
                "report_body": {
                    "kind": int(kind),
                    "description": reason,
                    "message_report": {
                        "peer": _require_peer(chat_id),
                        "messages": [_other_message(item) for item in messages],
                    },
                }
            },
        )
        return wrap_default(response)

    async def _authenticate(self) -> Session:
        try:
            sent = await self.start_phone_auth(self.credential)
        except BaleRpcError as error:
            if error.message == "PHONE_NUMBER_INVALID":
                raise AuthenticationError(
                    "Bale rejected the phone number. Use international format, "
                    "for example +989121234567."
                ) from error
            raise
        transaction_hash = str(sent.get("transaction_hash", ""))
        if not transaction_hash:
            raise AuthenticationError("Phone authentication response is incomplete")
        while True:
            code = (
                await _resolve_prompt(self._code_prompt, "Enter phone code: ")
            ).strip()
            try:
                return _parse_auth(await self.validate_code(transaction_hash, code))
            except BaleRpcError as error:
                if error.message == "PHONE_CODE_INVALID":
                    continue
                if error.message == "PHONE_NUMBER_UNOCCUPIED":
                    name = await _resolve_prompt(
                        self._signup_name_prompt, "Enter account name: "
                    )
                    return _parse_auth(
                        await self.sign_up(transaction_hash, name.strip())
                    )
                if not error.message or "password" in error.message.casefold():
                    password = await _resolve_prompt(
                        self._password_prompt, "Enter password: "
                    )
                    return _parse_auth(
                        await self.validate_password(transaction_hash, password.strip())
                    )
                raise

    async def _load_peer(self, peer_id: int, peer_type: int) -> User | Chat | None:
        if peer_type in (1, 4):
            users = await self.load_users([peer_id])
            return users[0] if users else None
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetFullGroup",
            "request.GetFullGroup",
            "response.GetFullGroup",
            {"peer": {"group_id": peer_id, "access_hash": 1}},
        )
        raw = response.get("full_group")
        if not isinstance(raw, dict):
            return None
        chat = wrap_group(raw).bind(self)
        self._peer_cache[f"{peer_id}|{peer_type}"] = chat
        self._peer_cache[chat.id] = chat
        return chat

    async def _load_history(
        self, peer: dict[str, int], date: int, limit: int
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.messaging.v2.Messaging",
            "LoadHistory",
            "request.LoadHistory",
            "response.LoadHistory",
            {"peer": peer, "date": date, "load_mode": 2, "limit": limit},
        )

    async def _simple_peer_call(
        self, method: str, request_name: str, chat_id: str
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            method,
            f"request.{request_name}",
            "response.DefaultResponse",
            {"peer": _require_peer(chat_id)},
        )
        return wrap_default(response)

    def _enqueue_update(self, update: dict[str, Any]) -> None:
        task = asyncio.create_task(self._process_update(update), name="bale-update")
        self._update_tasks.add(task)
        task.add_done_callback(self._update_tasks.discard)

    async def _process_update(self, update: dict[str, Any]) -> None:
        async with self._update_semaphore:
            raw = (update.get("update") or {}).get("composed_update", {}).get("message")
            if not isinstance(raw, dict) or int(raw.get("rid", 0)) == 0:
                return
            try:
                await self.dispatcher.dispatch_message(self, self._wrap_message(raw))
            except Exception as error:
                await self.dispatcher.dispatch_error(self, error)

    def _wrap_message(self, raw: dict[str, Any]) -> Message:
        peer = raw.get("peer") or {}
        peer_id, peer_type = int(peer.get("id", 0)), int(peer.get("type", 0))
        key = f"{peer_id}|{peer_type}"
        chat = self._chat_cache.get(key)
        if chat is None:
            chat = Chat(peer_id, peer_type).bind(self)
            self._chat_cache[key] = chat
        author_id = int(raw.get("sender_uid", 0))
        author = self._author_cache.get(author_id)
        if author is None:
            author = User(author_id).bind(self)
            self._author_cache[author_id] = author
        return wrap_message(raw, chat=chat, author=author).bind(self)

    def _cache_group_response(self, response: dict[str, Any]) -> Chat:
        raw = response.get("group")
        if not isinstance(raw, dict):
            raise ClientStateError("Bale did not return the requested group")
        chat = wrap_group(raw).bind(self)
        self._peer_cache[chat.id] = chat
        return chat


def _is_session(value: str) -> bool:
    return re.fullmatch(r"\d+:.+", value, re.DOTALL) is not None


def _parse_peer(value: str) -> tuple[int, int] | None:
    match = _PEER_PATTERN.fullmatch(value.strip())
    if match is None:
        return None
    return int(match.group("id")), int(match.group("type"))


def _require_peer(value: str) -> dict[str, int]:
    parsed = _parse_peer(value)
    if parsed is None:
        raise ValueError(f"Expected a Bale peer like '123|1', received {value!r}")
    return {"id": parsed[0], "type": parsed[1]}


def _require_peer_tuple(value: str) -> tuple[int, int]:
    parsed = _parse_peer(value)
    if parsed is None:
        raise ValueError(f"Expected a Bale peer like '123|1', received {value!r}")
    return parsed


def _group_peer(value: str) -> dict[str, int]:
    peer_id, _peer_type = _require_peer_tuple(value)
    return {"group_id": peer_id, "access_hash": 1}


def _out_peer(value: str) -> dict[str, int]:
    return {**_require_peer(value), "access_hash": 1}


def _user_peer(value: int | str) -> dict[str, int]:
    if isinstance(value, int):
        return {"uid": value, "access_hash": 1}
    parsed = _parse_peer(value)
    user_id = parsed[0] if parsed else int(value)
    return {"uid": user_id, "access_hash": 1}


def _require_message_id(value: str) -> tuple[int, int]:
    match = _MESSAGE_PATTERN.fullmatch(value.strip())
    if match is None:
        raise ValueError(f"Expected a message id like '123|1700000000', got {value!r}")
    return int(match.group("rid")), int(match.group("date"))


def _info_message(message: Message) -> dict[str, Any]:
    return {
        "peer": _require_peer(message.chat.id),
        "message_id": int(message.message_id),
        "date": message.date,
    }


def _other_message(message: Message | OtherMessage) -> dict[str, Any]:
    if isinstance(message, Message):
        return {"date": message.date, "message_id": int(message.message_id)}
    return {
        "date": message.date,
        "message_id": int(message.message_id),
        "seq": {"value": message.seq} if message.seq is not None else None,
    }


def _normalize_query(value: str) -> str:
    value = value.removeprefix("@").removeprefix("+")
    return value.removeprefix("https://ble.ir/").removeprefix("ble.ir/")


def _parse_auth(response: dict[str, Any]) -> Session:
    user = response.get("user") or {}
    jwt = response.get("jwt") or {}
    user_id, token = int(user.get("id", 0)), jwt.get("value")
    if not user_id or not isinstance(token, str) or not token:
        raise AuthenticationError("Bale authentication response is incomplete")
    return Session(user_id, token)


async def _terminal_prompt(text: str) -> str:
    return await asyncio.to_thread(input, text)


async def _resolve_prompt(prompt: Prompt, text: str) -> str:
    value = prompt(text)
    if inspect.isawaitable(value):
        value = await value
    return value


def _milliseconds() -> int:
    return int(time.time() * 1000)

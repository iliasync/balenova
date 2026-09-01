"""High-level asynchronous Bale user-session client."""

from __future__ import annotations

import asyncio
import contextlib
import getpass
import inspect
import json
import mimetypes
import os
import re
import sys
import time
from collections.abc import AsyncIterator, Awaitable, Callable, Iterable, Mapping
from io import BufferedIOBase
from pathlib import Path
from typing import Any, BinaryIO, TypedDict, TypeVar, overload
from urllib.parse import urlsplit

from google.protobuf.message import Message as ProtobufMessage

from bale.api import ProtocolAPI
from bale.dispatcher import (
    Dispatcher,
    ErrorHandler,
    LifecycleEvent,
    LifecycleHandler,
    MessageHandler,
    RawUpdateHandler,
    UpdateHandler,
)
from bale.errors import AuthenticationError, BaleRpcError, ClientStateError
from bale.events import MessageEdited, NewMessage, Update, build_updates
from bale.filters import Filter, command
from bale.models import (
    CallMode,
    CallRecordQuality,
    Chat,
    ChatType,
    DefaultResponse,
    GivingType,
    Message,
    OtherMessage,
    PacketResponse,
    PeerSource,
    PrivacyStatus,
    PrivacyType,
    ReportKind,
    User,
    WalletResponse,
    wrap_default,
    wrap_group,
    wrap_message,
    wrap_packet_response,
    wrap_user,
    wrap_wallet_response,
)
from bale.proto import schema as pb
from bale.protocol import ProtocolRecorder
from bale.recovered import RecoveredAPI
from bale.rtc import CallRtcConnection, call_rtc_connection_from_group_call
from bale.session import Session, SessionStorage
from bale.transports import GrpcTransport, WebSocketTransport

ResponseT = TypeVar("ResponseT", bound=dict[str, Any])
Prompt = Callable[[str], str | Awaitable[str]]
ClientTask = Callable[["Client"], object | Awaitable[object]]
MediaInput = bytes | bytearray | memoryview | str | Path | BinaryIO


class DialogBuckets(TypedDict):
    """Dialog entities grouped by account-session peer kind."""

    groups: list[Chat]
    channels: list[Chat]
    private_chats: list[User]
    bots: list[User]


_PEER_PATTERN = re.compile(r"^(?P<id>\d+)\|(?P<type>\d+)$")
_MESSAGE_PATTERN = re.compile(r"^(?P<rid>-?\d+)\|(?P<date>\d+)$")
_API_KEY = "C28D46DC4C3A7A26564BFCC48B929086A95C93C98E789A19847BEE8627DE4E7D"


def _color_enabled() -> bool:
    """Return whether interactive status output should use ANSI colors."""
    setting = os.environ.get("BALE_COLOR", "auto").strip().casefold()
    if setting in {"0", "false", "never", "no"} or "NO_COLOR" in os.environ:
        return False
    return setting in {"1", "true", "always", "yes"} or sys.stdout.isatty()


def _colorize(text: str, code: int) -> str:
    return f"\033[{code}m{text}\033[0m" if _color_enabled() else text


def _status(text: str, *, error: bool = False) -> None:
    """Print a short colored login/session status without exposing secrets."""
    print(_colorize(text, 31 if error else 36))


def _fanoos_value(value: Any) -> dict[str, Any]:
    """Convert a JSON-like Python value to Bale's analytics ``WebValue``."""
    if isinstance(value, str):
        return {"stringValue": value}
    if isinstance(value, bool):
        return {"booleanValue": value}
    if isinstance(value, int):
        if not -(1 << 63) <= value < (1 << 63):
            raise ValueError("Fanoos integer values must fit in signed int64")
        return {"int64Value": value}
    if isinstance(value, float):
        return {"doubleValue": value}
    if isinstance(value, (list, tuple)):
        return {
            "arrayValue": {"array": [_fanoos_value(item) for item in value]}
        }
    raise TypeError(
        "Fanoos values must be str, bool, int, float, list, or tuple; "
        f"got {type(value).__name__}"
    )


class Client:
    """An async client for real Bale user sessions.

    By default the client loads a named session. If it is missing or expired,
    interactive phone authentication is started in the terminal. ``credential``
    remains optional for backwards compatibility and may be a phone number or
    an exported ``<user_id>:<jwt>`` session string.
    """

    def __init__(
        self,
        credential: str | None = None,
        *,
        session_dir: str | Path = "sessions",
        session_name: str | None = None,
        update_concurrency: int = 16,
        phone_prompt: Prompt | None = None,
        code_prompt: Prompt | None = None,
        password_prompt: Prompt | None = None,
        signup_name_prompt: Prompt | None = None,
        grpc: GrpcTransport | None = None,
        websocket_options: Mapping[str, Any] | None = None,
        recorder: ProtocolRecorder | None = None,
    ) -> None:
        normalized_credential = credential.strip() if credential else None
        if credential is not None and not normalized_credential:
            raise AuthenticationError("The supplied Bale credential is empty")
        if (
            normalized_credential
            and session_name is None
            and not _is_session(normalized_credential)
            and not _looks_like_phone(normalized_credential)
        ):
            session_name = normalized_credential
            normalized_credential = None
        self.credential = normalized_credential
        self._phone_number = (
            normalized_credential
            if normalized_credential and not _is_session(normalized_credential)
            else None
        )
        self.dispatcher = Dispatcher()
        self.user: User | None = None
        self._session = (
            Session.parse(normalized_credential)
            if normalized_credential and _is_session(normalized_credential)
            else None
        )
        storage_name = session_name or self._phone_number or "bale"
        self._storage = SessionStorage(session_dir, storage_name)
        self._recorder = recorder
        self._grpc = grpc or GrpcTransport(recorder=recorder)
        self._websocket_options = dict(websocket_options or {})
        self._websocket: WebSocketTransport | None = None
        self._phone_prompt = phone_prompt or _terminal_prompt
        self._code_prompt = code_prompt or _terminal_prompt
        self._password_prompt = password_prompt or _terminal_password_prompt
        self._signup_name_prompt = signup_name_prompt or _terminal_prompt
        self._update_semaphore = asyncio.Semaphore(max(1, update_concurrency))
        self._update_tasks: set[asyncio.Task[None]] = set()
        self._event_queue: asyncio.Queue[Update] = asyncio.Queue()
        self._seen_messages: dict[tuple[str, str], str] = {}
        self._peer_cache: dict[str, User | Chat] = {}
        self._chat_cache: dict[str, Chat] = {}
        self._author_cache: dict[int, User] = {}
        self._wallet_cache: tuple[float, WalletResponse] | None = None
        self._wallet_lock = asyncio.Lock()
        self._stop_event = asyncio.Event()
        self._running = False
        self._closed = False
        self.api = ProtocolAPI(self)
        self.recovered = RecoveredAPI(self)
        for service_name in self.api.services:
            setattr(self, service_name, getattr(self.api, service_name))

    @property
    def connected(self) -> bool:
        return self._websocket is not None and self._websocket.connected

    @property
    def session(self) -> str | None:
        return str(self._session) if self._session else None

    @overload
    def on_message(
        self, callback: Filter | None = None
    ) -> Callable[[MessageHandler], MessageHandler]: ...

    @overload
    def on_message(self, callback: MessageHandler) -> MessageHandler: ...

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

    def on(
        self,
        event_type: type[Update] = Update,
        filter_: Filter | None = None,
    ) -> Callable[[UpdateHandler], UpdateHandler]:
        """Register a handler for one class of update."""

        def decorator(callback: UpdateHandler) -> UpdateHandler:
            return self.dispatcher.add_update_handler(callback, event_type, filter_)

        return decorator

    def on_update(self, callback: UpdateHandler) -> UpdateHandler:
        """Register a handler for every class-based update."""
        return self.dispatcher.add_update_handler(callback, Update)

    def on_raw_update(self, callback: RawUpdateHandler) -> RawUpdateHandler:
        """Register a compatibility handler for the original update dictionary."""
        return self.dispatcher.add_raw_update_handler(callback)

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
        loaded_existing_session = self._session is not None
        session_from_storage = False
        if self._session is None:
            try:
                self._session = await self._storage.load()
            except AuthenticationError:
                await self._storage.delete()
            loaded_existing_session = self._session is not None
            session_from_storage = loaded_existing_session
        if self._session is None:
            self._session = await self._authenticate()
            await self._storage.save(self._session)
        try:
            await self._connect_session(self._session)
        except BaseException as error:
            if not loaded_existing_session or not _is_authentication_failure(error):
                raise
            if session_from_storage:
                await self._storage.delete()
            self._session = None
            self.user = None
            self._peer_cache.clear()
            self._phone_number = None
            _status(
                "Existing Bale session is invalid or expired; logging in again.",
                error=True,
            )
            self._session = await self._authenticate()
            await self._storage.save(self._session)
            await self._connect_session(self._session)

    async def _connect_session(self, session: Session) -> None:
        websocket = WebSocketTransport(
            session.jwt,
            recorder=self._recorder,
            **self._websocket_options,
        )
        websocket.add_update_handler(self._enqueue_update)
        try:
            await websocket.connect()
            self._websocket = websocket
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

    async def start(self) -> Client:
        """Connect and return this client for convenient interactive use."""
        await self.connect()
        return self

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

    def run_forever(self) -> None:
        """Run the client until interrupted, without requiring asyncio setup."""
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            with contextlib.suppress(KeyboardInterrupt):
                asyncio.run(self._run_and_close())
            return
        raise ClientStateError("Use 'await client.run()' inside async code")

    def run_task(self, task: ClientTask) -> None:
        """Connect, run one async function, and close without asyncio setup."""
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            with contextlib.suppress(KeyboardInterrupt):
                asyncio.run(self._run_and_close(task))
            return
        raise ClientStateError("Use 'await client.run(task)' inside async code")

    async def _run_and_close(self, task: ClientTask | None = None) -> None:
        try:
            await self.run(task)
        finally:
            await self.close()

    async def next_update(self, timeout: float | None = None) -> Update:
        """Wait for and return the next class-based update."""
        if timeout is None:
            return await self._event_queue.get()
        return await asyncio.wait_for(self._event_queue.get(), timeout)

    async def iter_updates(self) -> AsyncIterator[Update]:
        """Yield class-based updates as they arrive."""
        while True:
            yield await self.next_update()

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

    async def terminate_all_sessions(self) -> DefaultResponse:
        """Invalidate all other authenticated Bale sessions."""
        response = await self.post(
            "bale.auth.v1.Auth",
            "TerminateAllSessions",
            "request.TerminateAllSessions",
            "response.DefaultResponse",
            {},
        )
        return wrap_default(response)

    async def get_auth_sessions(self) -> list[dict[str, Any]]:
        """List active account authorizations shown by Bale Web."""
        response = await self.post(
            "bale.auth.v1.Auth",
            "GetAuthSessions",
            "request.GetAuthSessions",
            "response.GetAuthSessions",
            {},
        )
        sessions = response.get("sessions") or []
        return [dict(item) for item in sessions if isinstance(item, Mapping)]

    async def terminate_session(
        self, user_id: int, ex_info: Mapping[str, Any] | None = None
    ) -> DefaultResponse:
        """Terminate one authorization session from the current account."""
        response = await self.post(
            "bale.auth.v1.Auth",
            "TerminateSession",
            "request.TerminateSession",
            "response.DefaultResponse",
            {"uid": user_id, "ex_info": dict(ex_info) if ex_info else None},
        )
        return wrap_default(response)

    async def refresh_token(self) -> str:
        """Refresh the current JWT and persist it for future connections."""
        session = self._session or await self._storage.load()
        if session is None:
            raise AuthenticationError("No Bale session is available")
        response = await self.post(
            "bale.auth.v1.Auth",
            "GetJWTToken",
            "request.GetJWTToken",
            "response.GetJWTToken",
            {},
        )
        jwt_value = response.get("jwt")
        jwt = jwt_value.get("value") if isinstance(jwt_value, Mapping) else jwt_value
        if not isinstance(jwt, str) or not jwt.strip():
            raise AuthenticationError("Bale did not return a refreshed JWT")
        self._session = Session(session.user_id, jwt.strip())
        await self._storage.save(self._session)
        return self._session.jwt

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

    async def invoke_raw(self, service: str, method: str, payload: bytes) -> bytes:
        """Invoke a captured RPC before its protobuf schema is bundled.

        ``payload`` is the nested protobuf message, not a transport envelope.
        """
        if self._websocket is not None:
            return await self._websocket.request_raw(service, method, payload)
        return await self.post_raw(service, method, payload)

    async def invoke_protobuf_bytes(
        self,
        service: str,
        method: str,
        payload: bytes,
        *,
        response_type: type[ProtobufMessage] | None = None,
    ) -> ProtobufMessage | bytes:
        """Invoke an RPC using the complete generated protocol surface."""
        raw = await self.invoke_raw(service, method, payload)
        if response_type is None:
            return raw
        response = response_type()
        response.ParseFromString(raw)
        return response

    async def invoke_protobuf(
        self,
        service: str,
        method: str,
        request: ProtobufMessage,
        *,
        response_type: type[ProtobufMessage] | None = None,
    ) -> ProtobufMessage | bytes:
        """Serialize a generated request and decode its generated response."""
        if not isinstance(request, ProtobufMessage):
            raise TypeError("request must be a protobuf Message")
        return await self.invoke_protobuf_bytes(
            service,
            method,
            request.SerializeToString(),
            response_type=response_type,
        )

    async def stream_protobuf(
        self,
        service: str,
        method: str,
        request: ProtobufMessage,
        *,
        response_type: type[ProtobufMessage],
        timeout: float | None = None,
    ) -> AsyncIterator[ProtobufMessage]:
        """Yield decoded messages from a generated server-streaming RPC."""
        if not isinstance(request, ProtobufMessage):
            raise TypeError("request must be a protobuf Message")
        session = self._session or await self._storage.load()
        async for raw in self._grpc.stream_raw(
            service,
            method,
            request.SerializeToString(),
            access_token=session.jwt if session else None,
            timeout=timeout,
        ):
            response = response_type()
            response.ParseFromString(raw)
            yield response

    async def call(
        self,
        service: str,
        method: str,
        request: ProtobufMessage | None = None,
        *,
        request_bytes: bytes | None = None,
        response_type: type[ProtobufMessage] | None = None,
        timeout: float = 10.0,
    ) -> ProtobufMessage | bytes:
        """Call any recovered unary RPC using its generated protobuf types."""
        if request is not None and request_bytes is not None:
            raise ValueError("pass either request or request_bytes, not both")
        if response_type is None:
            from bale.methods import METHODS

            pair = METHODS.get((service, method))
            if pair is not None:
                response_type = pair[1]
        if request is not None:
            operation = self.invoke_protobuf(
                service,
                method,
                request,
                response_type=response_type,
            )
        elif request_bytes is not None:
            operation = self.invoke_protobuf_bytes(
                service,
                method,
                request_bytes,
                response_type=response_type,
            )
        else:
            raise ValueError("either request or request_bytes is required")
        return await asyncio.wait_for(operation, timeout=timeout)

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

    async def post_raw(self, service: str, method: str, payload: bytes) -> bytes:
        """Invoke an untyped unary gRPC-web method using the current session."""
        session = self._session or await self._storage.load()
        return await self._grpc.request_raw(
            service,
            method,
            payload,
            access_token=session.jwt if session else None,
        )

    async def edit_name(self, name: str) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditName",
                "request.EditName",
                "response.SequenceResponse",
                {"name": name},
            )
        )

    async def edit_nickname(self, nickname: str | None = None) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditNickName",
                "request.EditNickName",
                "response.SequenceResponse",
                {"nick_name": {"value": nickname} if nickname else None},
            )
        )

    async def edit_about(self, about: str | None = None) -> DefaultResponse:
        return wrap_default(
            await self.invoke(
                "bale.users.v1.Users",
                "EditAbout",
                "request.EditAbout",
                "response.SequenceResponse",
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
        return bool(response.get("value", response.get("available")))

    async def edit_sex(self, sex: int) -> DefaultResponse:
        """Update the authenticated account's profile sex enum."""
        await self.invoke(
            "bale.users.v1.Users",
            "EditSex",
            "request.EditSex",
            "response.EmptyResponse",
            {"sex": int(sex)},
        )
        return DefaultResponse()

    async def edit_birth_date(self, date: int) -> DefaultResponse:
        """Update the account birth date using Bale's int64 representation."""
        await self.invoke(
            "bale.users.v1.Users",
            "EditBirthDate",
            "request.EditBirthDate",
            "response.EmptyResponse",
            {"date": _signed_int64(date, field_name="date")},
        )
        return DefaultResponse()

    async def edit_avatar(
        self,
        file_id: int | str,
        access_hash: int,
        file_storage_version: int,
    ) -> dict[str, Any]:
        """Set a profile avatar from an already uploaded Bale file."""
        return await self.invoke(
            "bale.users.v1.Users",
            "EditAvatar",
            "request.EditAvatar",
            "response.EditAvatar",
            {
                "file_location": _file_location(
                    file_id, access_hash, file_storage_version
                )
            },
        )

    async def remove_avatar(self, avatar_id: int) -> DefaultResponse:
        """Remove one profile avatar by its signed int64 avatar ID."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "RemoveAvatar",
            "request.RemoveAvatar",
            "response.SequenceResponse",
            {"avater_id": {"value": _signed_int64(avatar_id, field_name="avatar_id")}},
        )
        return wrap_default(response)

    async def edit_time_zone(self, time_zone: str) -> DefaultResponse:
        """Update the account time-zone identifier."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "EditMyTimeZone",
            "request.EditMyTimeZone",
            "response.SequenceResponse",
            {"tz": time_zone},
        )
        return wrap_default(response)

    edit_timezone = edit_time_zone

    async def edit_preferred_languages(
        self, languages: Iterable[str]
    ) -> DefaultResponse:
        """Replace the account's preferred language list."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "EditMyPreferredLanguages",
            "request.EditMyPreferredLanguages",
            "response.SequenceResponse",
            {"preferred_languages": [str(language) for language in languages]},
        )
        return wrap_default(response)

    async def edit_user_local_name(
        self, user: int | str, name: str, *, access_hash: int = 1
    ) -> DefaultResponse:
        """Set this account's local display name for another user."""
        peer = _user_peer(user, access_hash=access_hash)
        response = await self.invoke(
            "bale.users.v1.Users",
            "EditUserLocalName",
            "request.EditUserLocalName",
            "response.SequenceResponse",
            {**peer, "name": name},
        )
        return wrap_default(response)

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

    get_entity = get_chat

    async def resolve_peer_id(self, chat_id: int | str | User | Chat) -> int | str:
        """Resolve a Bale peer object, numeric id, or username to its id."""
        if isinstance(chat_id, (User, Chat)):
            return chat_id.id
        if isinstance(chat_id, int):
            return chat_id
        if chat_id.isnumeric():
            return int(chat_id)
        parsed = _parse_peer(chat_id)
        if parsed is not None:
            return parsed[0]
        peer = await self.get_chat(chat_id)
        if peer is None:
            raise ClientStateError(f"Could not resolve Bale peer {chat_id!r}")
        return peer.id

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

    async def get_full_user(
        self, user: int | str, *, access_hash: int = 1
    ) -> dict[str, Any] | None:
        """Load the current Web client's combined profile for one user."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "GetFullUser",
            "request.GetFullUser",
            "response.GetFullUser",
            {"peer": _user_peer(user, access_hash=access_hash)},
        )
        profile = response.get("full_user")
        return dict(profile) if isinstance(profile, Mapping) else None

    async def load_full_users_sequentially(
        self, users: Iterable[int | str]
    ) -> list[dict[str, Any]]:
        """Load full-user records through Bale's sequential RPC variant."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "LoadFullUsersSequentially",
            "request.LoadFullUsersSequentially",
            "response.LoadFullUsers",
            {"user_peers": [_user_peer(value) for value in users]},
        )
        return list(response.get("full_users", []))

    async def load_user_avatars(
        self, user: int | str, *, access_hash: int = 1
    ) -> list[dict[str, Any]]:
        """Load all known avatars for one Bale user."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "LoadAvatars",
            "request.LoadAvatars",
            "response.LoadAvatars",
            {"peer": _user_peer(user, access_hash=access_hash)},
        )
        avatars = response.get("avatars")
        if not isinstance(avatars, Mapping):
            return []
        values = avatars.get("avatars")
        if not isinstance(values, list):
            return []
        return [dict(value) for value in values if isinstance(value, Mapping)]

    load_avatars = load_user_avatars

    async def block_user(
        self, user: int | str, *, access_hash: int = 1
    ) -> DefaultResponse:
        """Block a Bale user for the authenticated account."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "BlockUser",
            "request.BlockUser",
            "response.SequenceResponse",
            {"peer": _user_peer(user, access_hash=access_hash)},
        )
        return wrap_default(response)

    async def unblock_user(
        self, user: int | str, *, access_hash: int = 1
    ) -> DefaultResponse:
        """Unblock a Bale user for the authenticated account."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "UnblockUser",
            "request.UnblockUser",
            "response.SequenceResponse",
            {"peer": _user_peer(user, access_hash=access_hash)},
        )
        return wrap_default(response)

    async def load_blocked_users(self) -> list[dict[str, Any]]:
        """Return the blocked-user peer records visible to this account."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "LoadBlockedUsers",
            "request.LoadBlockedUsers",
            "response.LoadBlockedUsers",
            {},
        )
        return [
            dict(peer)
            for peer in response.get("user_peers", [])
            if isinstance(peer, Mapping)
        ]

    async def get_contacts(
        self, contacts_hash: str = "", optimizations: Iterable[int] = ()
    ) -> dict[str, Any]:
        """Load account contacts, optionally using Bale's unchanged hash."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "GetContacts",
            "request.GetContacts",
            "response.GetContacts",
            {
                "contacts_hash": contacts_hash,
                "optimizations": [int(value) for value in optimizations],
            },
        )
        users = [wrap_user(raw).bind(self) for raw in response.get("users", [])]
        for user in users:
            self._peer_cache[f"{user.id}|1"] = user
            if user.is_bot:
                self._peer_cache[f"{user.id}|4"] = user
        return {**response, "users": users}

    async def add_contact(
        self, user: int | str, *, access_hash: int = 1
    ) -> DefaultResponse:
        """Add one Bale user to the account contacts."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "AddContact",
            "request.AddContact",
            "response.SequenceResponse",
            _user_peer(user, access_hash=access_hash),
        )
        return wrap_default(response)

    async def remove_contact(
        self, user: int | str, *, access_hash: int = 1
    ) -> DefaultResponse:
        """Remove one Bale user from the account contacts."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "RemoveContact",
            "request.RemoveContact",
            "response.SequenceResponse",
            _user_peer(user, access_hash=access_hash),
        )
        return wrap_default(response)

    async def get_user_privacy_status(
        self, user_id: int, privacy_type: int | PrivacyType
    ) -> PrivacyStatus:
        """Return one integer privacy status for a Bale user."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "GetUserPrivacyStatus",
            "request.GetUserPrivacyStatus",
            "response.GetUserPrivacyStatus",
            {"user_id": _user_id(user_id), "type": int(privacy_type)},
        )
        return PrivacyStatus(int(response.get("status", 0)))

    async def set_user_privacy_status(
        self,
        user_id: int,
        privacy_type: int | PrivacyType,
        status: int | PrivacyStatus,
    ) -> DefaultResponse:
        """Set one integer privacy status for a Bale user."""
        await self.invoke(
            "bale.users.v1.Users",
            "SetUserPrivacyStatus",
            "request.SetUserPrivacyStatus",
            "response.EmptyResponse",
            {
                "user_id": _user_id(user_id),
                "type": int(privacy_type),
                "status": int(status),
            },
        )
        return DefaultResponse()

    async def get_user_full_privacy(self, user_id: int) -> dict[str, Any] | None:
        """Load the invite, presence, and money-transfer privacy tuple."""
        response = await self.invoke(
            "bale.users.v1.Users",
            "GetUserFullPrivacy",
            "request.GetUserFullPrivacy",
            "response.GetUserFullPrivacy",
            {"user_id": _user_id(user_id)},
        )
        privacy = response.get("privacy")
        return dict(privacy) if isinstance(privacy, Mapping) else None

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
        title = title.strip()
        if not title:
            raise ValueError("Group title cannot be empty")
        if len(title) > 30:
            raise ValueError("Group title cannot be longer than 30 characters")
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

    async def get_my_group_peers(
        self,
        *,
        mode: int = 0,
        is_owner: bool = False,
        filters: Iterable[Mapping[str, Any]] = (),
    ) -> list[dict[str, Any]]:
        """Return all groups known to the account without scanning dialogs."""
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetMyGroups",
            "request.GetMyGroups",
            "response.GetMyGroups",
            {
                "mode": mode,
                "is_owner": is_owner,
                "filters": [dict(item) for item in filters],
            },
        )
        return [
            dict(item)
            for item in response.get("groups", [])
            if isinstance(item, Mapping) and item.get("group_id") is not None
        ]

    async def load_groups(
        self, peers: Iterable[Mapping[str, Any] | Chat | str]
    ) -> list[Chat]:
        """Resolve group peers in one RPC and retain their access hashes."""
        normalized: list[dict[str, int]] = []
        for value in peers:
            if isinstance(value, Chat):
                normalized.append(
                    {"group_id": value.peer_id, "access_hash": value.access_hash or 1}
                )
            elif isinstance(value, str):
                peer_id, _peer_type = _require_peer_tuple(value)
                normalized.append({"group_id": peer_id, "access_hash": 1})
            elif isinstance(value, Mapping) and value.get("group_id") is not None:
                normalized.append(
                    {
                        "group_id": int(value["group_id"]),
                        "access_hash": int(value.get("access_hash", 1)),
                    }
                )
            else:
                raise TypeError("group peer must be a chat id, Chat, or mapping")
        if not normalized:
            return []
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "LoadGroups",
            "request.LoadGroups",
            "response.LoadGroups",
            {"peers": normalized},
        )
        result: list[Chat] = []
        for item in response.get("groups", []):
            if not isinstance(item, Mapping):
                continue
            chat = wrap_group(dict(item)).bind(self)
            self._peer_cache[chat.id] = chat
            result.append(chat)
        return result

    async def get_my_groups(
        self,
        *,
        mode: int = 0,
        is_owner: bool = False,
        filters: Iterable[Mapping[str, Any]] = (),
    ) -> list[Chat]:
        peers = await self.get_my_group_peers(
            mode=mode, is_owner=is_owner, filters=filters
        )
        return await self.load_groups(peers)

    async def get_member_permissions(
        self, chat_id: str, user_id: int | str
    ) -> dict[str, Any]:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetMemberPermissions",
            "request.GetMemberPermissions",
            "response.GetMemberPermissions",
            {"group": _group_peer(chat_id), "user": _user_peer(user_id)},
        )
        permissions = response.get("permissions")
        return dict(permissions) if isinstance(permissions, Mapping) else {}

    async def get_can_see_messages(self, chat_id: str, user_id: int) -> bool:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetCanSeeMessages",
            "request.GetCanSeeMessages",
            "response.GetCanSeeMessages",
            {"group_peer": _group_peer(chat_id), "user_id": user_id},
        )
        return bool(response.get("can_see_messages", False))

    async def fetch_group_admins(self, chat_id: str) -> dict[str, Any]:
        return await self.invoke(
            "bale.groups.v1.Groups",
            "FetchGroupAdmins",
            "request.FetchGroupAdmins",
            "response.FetchGroupAdmins",
            {"group_out_peer": _group_peer(chat_id)},
        )

    async def get_banned_users(self, chat_id: str) -> list[dict[str, Any]]:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetBannedUsers",
            "request.GetBannedUsers",
            "response.GetBannedUsers",
            {"group": _group_peer(chat_id)},
        )
        return [dict(item) for item in response.get("banned_users", [])]

    async def get_mutual_groups(self, user_id: int | str) -> list[dict[str, Any]]:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetMutualGroups",
            "request.GetMutualGroups",
            "response.GetMutualGroups",
            {"peer": _user_peer(user_id)},
        )
        return [dict(item) for item in response.get("groups", [])]

    async def get_group_preview(self, token_or_url: str) -> dict[str, Any] | None:
        """Load a group preview without joining it."""
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "GetGroupPreview",
            "request.GetGroupPreview",
            "response.GetGroupPreview",
            {"token": _group_token(token_or_url)},
        )
        return dict(response) if isinstance(response.get("group"), Mapping) else None

    get_chat_preview = get_group_preview

    async def join_chat(self, token_or_url: str) -> Chat:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "JoinGroup",
            "request.JoinGroup",
            "response.JoinGroup",
            {"token": _group_token(token_or_url)},
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
            "GetGroupInviteUrl",
            "request.GetGroupInviteUrl",
            "response.GetGroupInviteUrl",
            {"group_peer": _group_peer(chat_id)},
        )
        value = response.get("url")
        return value if isinstance(value, str) else None

    get_group_invite_url = get_group_link
    export_chat_invite_link = get_group_link

    async def revoke_group_link(self, chat_id: str) -> str | None:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RevokeInviteUrl",
            "request.RevokeInviteUrl",
            "response.RevokeInviteUrl",
            {"group_peer": _group_peer(chat_id)},
        )
        value = response.get("url")
        return value if isinstance(value, str) else None

    revoke_invite_url = revoke_group_link
    revoke_chat_invite_link = revoke_group_link

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

    async def invite_user(self, chat_id: str, user_id: int | str) -> dict[str, Any]:
        """Invite one user through the account-session RPC."""
        return await self.invite_users(chat_id, [user_id])

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

    ban_chat_member = kick_user

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

    unban_chat_member = unban_user

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

    async def promote_chat_member(
        self,
        chat_id: str,
        user_id: int | str,
        permissions: Mapping[str, bool] | None = None,
        **permission_flags: bool | None,
    ) -> DefaultResponse:
        """Set account-session member permissions using either mapping or flags."""
        normalized = dict(permissions or {})
        for name, value in permission_flags.items():
            if value is None:
                continue
            key = name.removeprefix("can_")
            normalized[key] = bool(value)
        return await self.set_member_permissions(chat_id, user_id, normalized)

    async def restrict_chat_member(
        self,
        chat_id: str,
        user_id: int | str,
        permissions: Mapping[str, bool] | None = None,
    ) -> DefaultResponse:
        """Remove administrator status for an account-session member."""
        del permissions
        return await self.remove_user_admin(chat_id, user_id)

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

    set_chat_title = edit_group_title

    async def edit_group_about(self, chat_id: str, about: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "EditGroupAbout",
            "request.EditGroupAbout",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "about": {"value": about},
                "rid": WebSocketTransport.create_rid(),
            },
        )
        return wrap_default(response)

    set_chat_description = edit_group_about

    async def remove_user_admin(
        self, chat_id: str, user_id: int | str
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RemoveUserAdmin",
            "request.RemoveUserAdmin",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "user_peer": _user_peer(user_id),
            },
        )
        return wrap_default(response)

    async def edit_group_avatar(
        self, chat_id: str, file: Mapping[str, Any]
    ) -> dict[str, Any]:
        file_id = _unsigned_int64(file["file_id"], field_name="file_id")
        access_hash = int(file["access_hash"])
        storage_version = file.get("file_storage_version")
        return await self.invoke(
            "bale.groups.v1.Groups",
            "EditGroupAvatar",
            "request.EditGroupAvatar",
            "response.EditGroupAvatar",
            {
                "group_peer": _group_peer(chat_id),
                "file_location": {
                    "file_id": file_id,
                    "access_hash": access_hash,
                    "file_storage_version": (
                        {"value": int(storage_version)}
                        if storage_version is not None
                        else None
                    ),
                },
                "rid": WebSocketTransport.create_rid(),
                "optimizations": [],
            },
        )

    async def set_chat_photo(self, chat_id: str, photo: MediaInput) -> dict[str, Any]:
        """Upload and set a group's avatar using account-session RPCs."""
        owner_id = self.user.id if self.user else None
        if owner_id is None and self._session is not None:
            owner_id = self._session.user_id
        if owner_id is None:
            raise AuthenticationError("Connect before setting a chat photo")
        uploaded = await self.upload_file(f"{owner_id}|1", photo, send_type=1)
        return await self.edit_group_avatar(chat_id, uploaded)

    async def load_group_avatars(self, chat_id: str) -> list[dict[str, Any]]:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "LoadGroupAvatars",
            "request.LoadGroupAvatars",
            "response.LoadGroupAvatars",
            {"peer": _group_peer(chat_id)},
        )
        avatars = response.get("avatars") or {}
        return list(avatars.get("avatars", []))

    async def remove_group_avatar(
        self, chat_id: str, avatar_id: int | None = None
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RemoveGroupAvatar",
            "request.RemoveGroupAvatar",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "rid": WebSocketTransport.create_rid(),
                "optimizations": [],
                "avatar_id": {"value": avatar_id} if avatar_id is not None else None,
            },
        )
        return wrap_default(response)

    async def delete_chat_photo(self, chat_id: str) -> DefaultResponse:
        """Remove the newest group avatar."""
        avatars = await self.load_group_avatars(chat_id)
        if not avatars:
            return wrap_default({})
        avatar_id = avatars[0].get("id") if isinstance(avatars[0], Mapping) else None
        if isinstance(avatar_id, Mapping):
            avatar_id = avatar_id.get("value")
        return await self.remove_group_avatar(
            chat_id,
            int(avatar_id) if avatar_id is not None else None,
        )

    async def load_members(
        self,
        chat_id: str,
        limit: int = 50,
        next_: str | int | None = None,
        *,
        excepted_permissions: bool = False,
        contacts: bool = False,
        query: str | None = None,
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
                "condition": {
                    "excepted_permissions": excepted_permissions,
                    "contacts": contacts,
                    "query": query or "",
                },
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

    get_chat_members_count = get_group_members_count

    async def get_chat_members(
        self,
        chat_id: str,
        limit: int = 200,
        next_: bytes | str | int | None = None,
        *,
        excepted_permissions: bool = False,
        contacts: bool = False,
        query: str | None = None,
    ) -> dict[str, Any]:
        """Load a page of group members."""
        if isinstance(next_, bytes):
            try:
                next_ = next_.decode("utf-8")
            except UnicodeDecodeError as error:
                raise ValueError("next_ must be valid UTF-8 bytes") from error
        return await self.load_members(
            chat_id,
            limit=limit,
            next_=next_,
            excepted_permissions=excepted_permissions,
            contacts=contacts,
            query=query,
        )

    async def get_chat_administrators(
        self,
        chat_id: str,
        limit: int = 200,
        next_: bytes | str | int | None = None,
    ) -> list[dict[str, Any]]:
        """Return members marked as administrators by the account RPC."""
        result = await self.get_chat_members(chat_id, limit=limit, next_=next_)
        return [
            dict(member)
            for member in result.get("members", [])
            if isinstance(member, Mapping) and _member_is_admin(member)
        ]

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
        # ``parameters`` is the current Web schema.  ``params`` was emitted
        # by older captures and is retained as a read-only compatibility
        # fallback for callers replaying those captures.
        raw_parameters = response.get("parameters", response.get("params", []))
        return [
            {"key": str(item.get("key", "")), "value": str(item.get("value", ""))}
            for item in raw_parameters
            if isinstance(item, Mapping)
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

    async def iter_messages(
        self,
        chat_id: str,
        *,
        limit: int | None = None,
        batch_size: int = 50,
    ) -> AsyncIterator[Message]:
        """Yield message history without making the caller handle pages."""
        if limit is not None and limit < 0:
            raise ValueError("limit cannot be negative")
        if batch_size < 1:
            raise ValueError("batch_size must be positive")
        remaining = limit
        from_date = -1
        seen: set[str] = set()
        while remaining is None or remaining > 0:
            page_size = batch_size if remaining is None else min(batch_size, remaining)
            page = await self.load_history(chat_id, from_date, page_size)
            fresh = [message for message in page if message.id not in seen]
            if not fresh:
                break
            for message in fresh:
                seen.add(message.id)
                yield message
                if remaining is not None:
                    remaining -= 1
                    if remaining == 0:
                        return
            next_date = min(message.date for message in fresh)
            if next_date == from_date:
                break
            from_date = next_date

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

    async def get_dialogs_by_type(
        self,
        limit: int = 40,
        min_date: int = -1,
        *,
        resolve_entities: bool = True,
    ) -> DialogBuckets:
        """Return account dialogs split into groups, channels, users, and bots.

        Some Web responses contain full ``users``/``groups`` objects while
        others contain only ``user_peers``/``group_peers``.  When
        ``resolve_entities`` is true (the default), the latter are resolved
        through the read-only Users/Groups RPCs so channel and bot types are
        not guessed from peer ids.
        """
        response = await self.load_dialogs(limit=limit, min_date=min_date)
        return await self._bucket_dialog_response(response, resolve_entities)

    async def _bucket_dialog_response(
        self, response: Mapping[str, Any], resolve_entities: bool
    ) -> DialogBuckets:
        groups: list[Chat] = []
        channels: list[Chat] = []
        users: list[User] = []
        bots: list[User] = []

        for raw_group in response.get("groups", []):
            if not isinstance(raw_group, Mapping) or "id" not in raw_group:
                continue
            group = wrap_group(dict(raw_group)).bind(self)
            self._peer_cache[group.id] = group
            if group.type is ChatType.CHANNEL:
                channels.append(group)
            else:
                groups.append(group)

        for raw_user in response.get("users", []):
            if not isinstance(raw_user, Mapping) or "id" not in raw_user:
                continue
            user = wrap_user(dict(raw_user)).bind(self)
            self._peer_cache[f"{user.id}|1"] = user
            (bots if user.is_bot else users).append(user)

        if resolve_entities:
            user_peers = response.get("user_peers", [])
            known_user_ids = {user.id for user in users + bots}
            ids = [
                int(peer["uid"])
                for peer in user_peers
                if isinstance(peer, Mapping)
                and peer.get("uid") is not None
                and int(peer["uid"]) not in known_user_ids
            ]
            if ids:
                loaded_users = await self.load_users(ids)
                for user in loaded_users:
                    (bots if user.is_bot else users).append(user)

        if resolve_entities:
            group_peers = response.get("group_peers", [])
            known_group_ids = {group.peer_id for group in groups + channels}
            for peer in group_peers:
                if not isinstance(peer, Mapping) or peer.get("group_id") is None:
                    continue
                if int(peer["group_id"]) in known_group_ids:
                    continue
                try:
                    entity = await self._load_peer(int(peer["group_id"]), 2)
                except Exception:
                    continue
                if not isinstance(entity, Chat):
                    continue
                known_group_ids.add(entity.peer_id)
                if entity.type is ChatType.CHANNEL:
                    channels.append(entity)
                else:
                    groups.append(entity)

        # Recent Web responses may contain only dialogs plus peer ids.  The
        # peer type is authoritative for counting and avoids one RPC per
        # group/channel just to produce a typed list.
        if not groups and not channels and not users and not bots:
            seen: set[tuple[int, int]] = set()
            for dialog in response.get("dialogs", []):
                if not isinstance(dialog, Mapping):
                    continue
                peer = dialog.get("peer") or {}
                if not isinstance(peer, Mapping):
                    continue
                peer_id = int(peer.get("id", 0))
                peer_type = int(peer.get("type", 0))
                marker = (peer_id, peer_type)
                if peer_id <= 0 or marker in seen:
                    continue
                seen.add(marker)
                if peer_type == 1:
                    users.append(User(peer_id).bind(self))
                elif peer_type == 4:
                    bots.append(User(peer_id, is_bot=True).bind(self))
                elif peer_type in (2, 5):
                    groups.append(Chat(peer_id, peer_type).bind(self))
                elif peer_type == 3:
                    channels.append(Chat(peer_id, peer_type).bind(self))

        return {
            "groups": groups,
            "channels": channels,
            "private_chats": users,
            "bots": bots,
        }

    async def get_all_dialogs_by_type(
        self,
        page_size: int = 100,
        max_pages: int = 100,
        *,
        resolve_entities: bool = True,
    ) -> DialogBuckets:
        """Load and classify all available account dialogs across pages.

        Set ``resolve_entities=False`` for a fast peer-type count.  The default
        resolves entities so channels, groups, and bots are classified using
        server metadata rather than guessed from peer ids.
        """
        if page_size <= 0:
            raise ValueError("page_size must be positive")
        if max_pages <= 0:
            raise ValueError("max_pages must be positive")
        min_date = -1
        merged: dict[str, Any] = {
            "dialogs": [],
            "users": [],
            "groups": [],
            "user_peers": [],
            "group_peers": [],
        }
        seen_peers: set[tuple[int, int]] = set()
        seen_users: set[int] = set()
        seen_groups: set[int] = set()
        for _ in range(max_pages):
            response = await self.load_dialogs(limit=page_size, min_date=min_date)
            dialogs = response.get("dialogs", [])
            if not isinstance(dialogs, list) or not dialogs:
                break
            for key in ("dialogs", "users", "groups", "user_peers", "group_peers"):
                values = response.get(key, [])
                if not isinstance(values, list):
                    continue
                for value in values:
                    if key == "dialogs" and isinstance(value, Mapping):
                        peer = value.get("peer") or {}
                        peer_marker = (int(peer.get("id", 0)), int(peer.get("type", 0)))
                        if peer_marker in seen_peers:
                            continue
                        seen_peers.add(peer_marker)
                    elif key in {"users", "user_peers"} and isinstance(value, Mapping):
                        if key == "user_peers":
                            user_marker = int(value.get("uid", 0))
                        else:
                            user_marker = int(value.get("id", 0))
                        if user_marker in seen_users:
                            continue
                        seen_users.add(user_marker)
                    elif key in {"groups", "group_peers"} and isinstance(
                        value, Mapping
                    ):
                        if key == "group_peers":
                            group_marker = int(value.get("group_id", 0))
                        else:
                            group_marker = int(value.get("id", 0))
                        if group_marker in seen_groups:
                            continue
                        seen_groups.add(group_marker)
                    merged[key].append(value)
            dates = [
                int(item.get("sort_date", item.get("date", 0)))
                for item in dialogs
                if isinstance(item, Mapping)
            ]
            if len(dialogs) < page_size or not dates:
                break
            next_date = min(dates)
            if next_date >= min_date and min_date != -1:
                break
            min_date = next_date
        return await self._bucket_dialog_response(merged, resolve_entities)

    async def get_groups(self, limit: int | None = None) -> list[Chat]:
        """Return groups (including supergroups) from the account dialogs."""
        result = (
            await self.get_all_dialogs_by_type()
            if limit is None
            else await self.get_dialogs_by_type(limit=limit)
        )
        return [chat for chat in result["groups"] if isinstance(chat, Chat)]

    async def get_channels(self, limit: int | None = None) -> list[Chat]:
        """Return channels from the account dialogs."""
        result = (
            await self.get_all_dialogs_by_type()
            if limit is None
            else await self.get_dialogs_by_type(limit=limit)
        )
        return [chat for chat in result["channels"] if isinstance(chat, Chat)]

    async def get_private_chats(self, limit: int | None = None) -> list[User]:
        """Return non-bot private users from the account dialogs."""
        result = (
            await self.get_all_dialogs_by_type()
            if limit is None
            else await self.get_dialogs_by_type(limit=limit)
        )
        return [user for user in result["private_chats"] if isinstance(user, User)]

    async def get_bots(self, limit: int | None = None) -> list[User]:
        """Return bot users from the account dialogs."""
        result = (
            await self.get_all_dialogs_by_type()
            if limit is None
            else await self.get_dialogs_by_type(limit=limit)
        )
        return [user for user in result["bots"] if isinstance(user, User)]

    async def get_file(
        self,
        file_id: int | str,
        access_hash: int | None = None,
        file_storage_version: int | None = None,
    ) -> dict[str, Any]:
        if access_hash is None:
            parts = str(file_id).split(":")
            if len(parts) != 3:
                raise ValueError(
                    "file_id must be '<access_hash>:<file_id>:<storage_version>'"
                )
            access_hash, file_id, file_storage_version = map(int, parts)
        if file_storage_version is not None and file_storage_version < 0:
            raise ValueError("file_storage_version cannot be negative")
        return await self.invoke(
            "ai.bale.server.Files",
            "GetNasimFileUrl",
            "request.GetNasimFileUrl",
            "response.GetNasimFileUrl",
            {
                "file": {
                    "file_id": _unsigned_int64(file_id, field_name="file_id"),
                    "access_hash": access_hash,
                    "file_storage_version": (
                        {"value": file_storage_version}
                        if file_storage_version is not None
                        else None
                    ),
                }
            },
        )

    get_file_url = get_file

    async def get_upload_limits(self) -> dict[str, int | bool]:
        """Return the upload capacity currently available to the account."""
        response = await self.invoke(
            "ai.bale.server.Files",
            "GetUploadLimits",
            "request.GetUploadLimits",
            "response.GetUploadLimits",
            {},
        )
        return {
            "upload_limit_bytes": int(response.get("upload_limit_bytes", 0)),
            "temporary_max_bytes": int(response.get("temporary_max_bytes", 0)),
            "permanent_max_bytes": int(response.get("permanent_max_bytes", 0)),
            "bought_capacity_remaining_bytes": int(
                response.get("bought_capacity_remaining_bytes", 0)
            ),
            "bought_capacity_unlimited": bool(
                response.get("bought_capacity_unlimited", False)
            ),
        }

    async def get_file_urls(
        self,
        peer: str,
        file_id: int | str,
        access_hash: int,
        file_storage_version: int,
        filename: str | None = None,
    ) -> dict[str, Any]:
        """Resolve a file URL with peer/filename context used by Bale Web."""
        return await self.invoke(
            "ai.bale.server.Files",
            "GetNasimFileUrls",
            "request.GetNasimFileUrls",
            "response.GetNasimFileUrls",
            {
                "peer": _out_peer(peer),
                "file": _file_location(file_id, access_hash, file_storage_version),
                "filename": {"value": filename} if filename else None,
            },
        )

    async def get_file_upload_resume(
        self, file_id: int | str, access_hash: int, file_storage_version: int
    ) -> dict[str, Any]:
        """Check whether Bale can resume an interrupted Nasim upload."""
        return await self.invoke(
            "ai.bale.server.Files",
            "GetNasimFileUploadResume",
            "request.GetNasimFileUploadResume",
            "response.GetNasimFileUploadResume",
            {"file": _file_location(file_id, access_hash, file_storage_version)},
        )

    async def cancel_file_upload(
        self, file_id: int | str, access_hash: int, file_storage_version: int
    ) -> bool:
        """Cancel an interrupted Nasim upload and return Bale's result."""
        response = await self.invoke(
            "ai.bale.server.Files",
            "FileUploadCancel",
            "request.FileUploadCancel",
            "response.FileUploadCancel",
            {"file": _file_location(file_id, access_hash, file_storage_version)},
        )
        return bool(response.get("canceled"))

    async def get_file_public_url(
        self,
        peer: str,
        file_id: int | str,
        access_hash: int,
        file_storage_version: int,
        filename: str | None = None,
    ) -> dict[str, Any]:
        """Resolve the public URL variant used for shareable media."""
        return await self.invoke(
            "ai.bale.server.Files",
            "GetNasimFilePublicUrl",
            "request.GetNasimFilePublicUrl",
            "response.GetNasimFilePublicUrl",
            {
                "peer": _out_peer(peer),
                "file": _file_location(file_id, access_hash, file_storage_version),
                "filename": {"value": filename} if filename else None,
            },
        )

    async def download_file(
        self,
        file_id: int | str,
        access_hash: int | None = None,
        file_storage_version: int | None = None,
    ) -> bytes:
        """Download a file identified by a Bale file reference."""
        description = await self.get_file(
            file_id, access_hash, file_storage_version=file_storage_version
        )
        file_url = description.get("file_url")
        if not isinstance(file_url, Mapping):
            raise ClientStateError("Bale did not return a file URL")
        url = file_url.get("url")
        if not isinstance(url, str) or not url:
            raise ClientStateError("Bale did not return a usable file URL")
        return await self._grpc.download(url, timeout=file_url.get("timeout"))

    download = download_file

    async def download_media(self, message: Message) -> bytes:
        """Download the media attached to a message."""
        content = message.raw.get("message") or {}
        if not isinstance(content, Mapping):
            raise ValueError("The message does not contain downloadable media")
        media = next(
            (
                value
                for key, value in content.items()
                if key
                in {
                    "audio_message",
                    "document_message",
                    "photo_message",
                    "video_message",
                    "voice_message",
                }
                and isinstance(value, Mapping)
            ),
            None,
        )
        if media is None or "file_id" not in media or "access_hash" not in media:
            raise ValueError("The message does not contain downloadable media")
        version = media.get("file_storage_version")
        if isinstance(version, Mapping):
            version = version.get("value")
        return await self.download_file(
            int(media["file_id"]),
            int(media["access_hash"]),
            int(version) if version is not None else None,
        )

    async def upload_file(
        self,
        chat_id: str,
        file: MediaInput,
        send_type: int = 6,
        *,
        expected_size: int | None = None,
        name: str | None = None,
        mime_type: str | None = None,
        crc: int = 0,
        chunk_size: int | None = None,
    ) -> dict[str, Any]:
        """Upload bytes or a local/remote file using Bale's Nasim protocol."""
        payload, inferred_name = await self._read_media(file)
        name = name or inferred_name
        expected_size = len(payload) if expected_size is None else expected_size
        if expected_size != len(payload):
            raise ValueError("expected_size does not match the file payload")
        mime_type = (
            mime_type or mimetypes.guess_type(name)[0] or "application/octet-stream"
        )
        result = await self.get_file_upload_url(
            expected_size,
            name,
            mime_type,
            crc=crc,
            chat_id=chat_id,
            send_type=send_type,
            chunk_size=chunk_size,
        )
        url = result.get("url")
        if isinstance(url, str) and url:
            await self._grpc.upload(
                url,
                payload,
                chunk_size=(
                    int(result["chunk_size"])
                    if result.get("chunk_size") is not None
                    else chunk_size
                ),
            )
        elif not result.get("duplicate"):
            raise ClientStateError("Bale did not return a file upload URL")
        return {
            **result,
            "file_size": int(result.get("file_size") or expected_size),
            "name": name,
            "mime_type": mime_type,
            "access_hash": _require_peer_tuple(chat_id)[0],
        }

    async def get_file_upload_url(
        self,
        expected_size: int,
        name: str,
        mime_type: str,
        *,
        crc: int = 0,
        uid: int | None = None,
        chat_id: str | None = None,
        send_type: int | None = None,
        chunk_size: int | None = None,
    ) -> dict[str, Any]:
        if expected_size < 0:
            raise ValueError("expected_size cannot be negative")
        owner_id = uid
        if owner_id is None:
            owner_id = self.user.id if self.user else None
        if owner_id is None and self._session is not None:
            owner_id = self._session.user_id
        if owner_id is None:
            raise AuthenticationError("Connect before requesting an upload URL")
        return await self.invoke(
            "ai.bale.server.Files",
            "GetNasimFileUploadUrl",
            "request.GetNasimFileUploadUrl",
            "response.GetNasimFileUploadUrl",
            {
                "expected_size": expected_size,
                "crc": crc,
                "uid": owner_id,
                "name": name,
                "mime_type": mime_type,
                "ex_peer": _out_peer(chat_id) if chat_id else None,
                "send_type": {"type": send_type} if send_type is not None else None,
                "chunk_size": chunk_size,
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

    send = send_message

    async def _send_media_message(
        self,
        chat_id: str,
        message_payload: Mapping[str, Any],
        reply_to: Message | None = None,
    ) -> Message:
        peer = _require_peer(chat_id)
        rid = WebSocketTransport.create_rid()
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "SendMessage",
            "request.SendMessage",
            "response.DefaultResponse",
            {
                "peer": peer,
                "rid": rid,
                "message": dict(message_payload),
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
                "message": dict(message_payload),
            }
        )

    async def send_photo(
        self,
        chat_id: str,
        photo: MediaInput,
        caption: str | None = None,
        *,
        width: int = 100,
        height: int = 100,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, photo, send_type=1)
        return await self._send_media_message(
            chat_id,
            {
                "document_message": _document_message(
                    uploaded, "photo", caption, width, height
                )
            },
            reply_to,
        )

    async def send_video(
        self,
        chat_id: str,
        video: MediaInput,
        caption: str | None = None,
        *,
        duration: int = 0,
        width: int = 100,
        height: int = 100,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, video, send_type=2)
        return await self._send_media_message(
            chat_id,
            {
                "document_message": _document_message(
                    uploaded, "video", caption, width, height, duration
                )
            },
            reply_to,
        )

    async def send_animation(
        self,
        chat_id: str,
        animation: MediaInput,
        caption: str | None = None,
        *,
        duration: int = 0,
        width: int = 100,
        height: int = 100,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, animation, send_type=4)
        return await self._send_media_message(
            chat_id,
            {
                "document_message": _document_message(
                    uploaded, "gif", caption, width, height, duration
                )
            },
            reply_to,
        )

    async def send_audio(
        self,
        chat_id: str,
        audio: MediaInput,
        caption: str | None = None,
        *,
        duration: int = 0,
        title: str | None = None,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, audio, send_type=5)
        return await self._send_media_message(
            chat_id,
            {
                "document_message": _document_message(
                    uploaded, "audio", caption, duration=duration, title=title
                )
            },
            reply_to,
        )

    async def send_voice(
        self,
        chat_id: str,
        voice: MediaInput,
        caption: str | None = None,
        *,
        duration: int = 0,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, voice, send_type=3)
        return await self._send_media_message(
            chat_id,
            {
                "document_message": _document_message(
                    uploaded, "voice", caption, duration=duration
                )
            },
            reply_to,
        )

    async def send_document(
        self,
        chat_id: str,
        document: MediaInput,
        caption: str | None = None,
        *,
        reply_to: Message | None = None,
    ) -> Message:
        uploaded = await self.upload_file(chat_id, document, send_type=6)
        return await self._send_media_message(
            chat_id,
            {"document_message": _document_message(uploaded, None, caption)},
            reply_to,
        )

    async def send_sticker(
        self,
        chat_id: str,
        sticker: str | Mapping[str, Any],
        *,
        reply_to: Message | None = None,
    ) -> Message:
        payload = _sticker_message(sticker)
        return await self._send_media_message(
            chat_id, {"sticker_message": payload}, reply_to
        )

    async def send_location(
        self,
        chat_id: str,
        latitude: float,
        longitude: float,
        *,
        reply_to: Message | None = None,
    ) -> Message:
        raw_json = json.dumps(
            {
                "dataType": "location",
                "data": {"location": {"latitude": latitude, "longitude": longitude}},
            },
            separators=(",", ":"),
        )
        return await self._send_media_message(
            chat_id, {"json_message": {"raw_json": raw_json}}, reply_to
        )

    async def send_contact(
        self,
        chat_id: str,
        phone_number: str,
        first_name: str,
        last_name: str | None = None,
        *,
        reply_to: Message | None = None,
    ) -> Message:
        # Bale's account RPC stores one contact display-name field; retain the
        # upstream behavior and use ``first_name`` as that field.
        del last_name
        name = first_name
        raw_json = json.dumps(
            {
                "dataType": "contact",
                "data": {
                    "contact": {"name": name, "emails": [""], "phones": [phone_number]}
                },
            },
            separators=(",", ":"),
        )
        return await self._send_media_message(
            chat_id, {"json_message": {"raw_json": raw_json}}, reply_to
        )

    async def send_media_group(
        self,
        chat_id: str,
        media: Iterable[MediaInput | Mapping[str, Any]],
    ) -> list[Message]:
        """Upload and send a 2-10 item media album."""
        normalized: list[dict[str, Any]] = []
        for item in media:
            if isinstance(item, Mapping) and isinstance(item.get("media"), Mapping):
                normalized.append(dict(item))
                continue
            source: MediaInput
            send_type = 6
            caption: str | None = None
            if isinstance(item, Mapping):
                source = item.get("media")  # type: ignore[assignment]
                send_type = int(item.get("send_type", send_type))
                caption = (
                    item.get("caption")
                    if isinstance(item.get("caption"), str)
                    else None
                )
            else:
                source = item
            uploaded = await self.upload_file(chat_id, source, send_type=send_type)
            ext_name = {1: "photo", 2: "video", 4: "gif"}.get(send_type)
            normalized.append(
                {
                    "random_id": WebSocketTransport.create_rid(),
                    "media": _document_message(uploaded, ext_name, caption),
                }
            )
        return await self.send_multi_media_message(chat_id, normalized)

    async def send_multi_media_message(
        self, chat_id: str, media: Iterable[Mapping[str, Any]]
    ) -> list[Message]:
        peer = _require_peer(chat_id)
        normalized: list[dict[str, Any]] = []
        for item in media:
            document = item.get("media")
            if not isinstance(document, Mapping):
                raise ValueError("Each media item must contain a 'media' mapping")
            normalized.append(
                {
                    "random_id": int(
                        item.get("random_id") or WebSocketTransport.create_rid()
                    ),
                    "media": dict(document),
                }
            )
        if not 2 <= len(normalized) <= 10:
            raise ValueError("A media album must contain between 2 and 10 items")
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "SendMultiMediaMessage",
            "request.SendMultiMediaMessage",
            "response.DefaultResponse",
            {
                "peer": _out_peer(chat_id),
                "multi_media": normalized,
                "grouped_id": WebSocketTransport.create_rid(),
            },
        )
        return [
            self._wrap_message(
                {
                    "peer": peer,
                    "sender_uid": self.user.id if self.user else 0,
                    "date": response.get("date", 0),
                    "rid": item["random_id"],
                    "message": {"document_message": item["media"]},
                }
            )
            for item in normalized
        ]

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
    send_chat_action = typing

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

    async def message_remove_reaction(
        self, chat_id: str, message_id: str, code: str
    ) -> dict[str, Any]:
        rid, date = _require_message_id(message_id)
        return await self.invoke(
            "bale.abacus.v1.Abacus",
            "MessageRemoveReaction",
            "request.MessageRemoveReaction",
            "response.MessageRemoveReaction",
            {
                "peer": _require_peer(chat_id),
                "rid": rid,
                "code": code,
                "date": date,
            },
        )

    async def get_messages_reactions(
        self, chat_id: str, message_ids: Iterable[str]
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.abacus.v1.Abacus",
            "GetMessagesReactions",
            "request.GetMessagesReactions",
            "response.GetMessagesReactions",
            {
                "peer": _require_peer(chat_id),
                "mids": [_message_identifier(value) for value in message_ids],
            },
        )

    async def get_messages_views(
        self,
        chat_id: str,
        message_ids: Iterable[str],
        *,
        increment: bool = False,
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.abacus.v1.Abacus",
            "GetMessagesViews",
            "request.GetMessagesViews",
            "response.GetMessagesViews",
            {
                "peer": _require_peer(chat_id),
                "mids": [_message_identifier(value) for value in message_ids],
                "increment": increment,
            },
        )

    async def click_inline_button(
        self, chat_id: str, message_id: str, data: str
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.ketf.v1.Ketf",
            "SendInlineCallback",
            "request.SendInlineCallback",
            "response.SendInlineCallback",
            {
                "peer": _require_peer(chat_id),
                "message_id": _message_identifier(message_id),
                "data": {"value": data},
            },
        )

    async def get_call_wss_url(self, call_id: int | str) -> str | None:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "GetWssURL",
            "request.GetWssUrl",
            "response.GetWssUrl",
            {"call_id": _require_call_id(call_id)},
        )
        url = response.get("url")
        return url if isinstance(url, str) else None

    async def start_call(
        self,
        chat_id: str,
        *,
        video: bool = False,
        invite_enable: bool | None = None,
    ) -> dict[str, Any]:
        """Start a private LiveKit call with one peer."""
        peer = _require_peer(chat_id)
        rid = WebSocketTransport.create_rid()
        return await self.invoke(
            "bale.meet.v1.Meet",
            "StartCall",
            "request.StartCall",
            "response.CallWithParticipants",
            {
                "peer": peer,
                "rid": rid,
                "video": video,
                "live_kit_call": {
                    "peer": peer,
                    "rid": rid,
                    "video": video,
                    "invite_enable": (
                        {"value": invite_enable}
                        if invite_enable is not None
                        else None
                    ),
                },
            },
        )

    async def accept_call(
        self, call_id: int | str, *, invite_enable: bool | None = None
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "AcceptCall",
            "request.AcceptCall",
            "response.CallWithParticipants",
            {
                "call_id": _require_call_id(call_id),
                "invite_enable": (
                    {"value": invite_enable} if invite_enable is not None else None
                ),
            },
        )

    async def receive_call(self, call_id: int | str) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "ReceiveCall",
            "request.ReceiveCall",
            "response.DefaultResponse",
            {"call_id": _require_call_id(call_id)},
        )
        return wrap_default(response)

    async def discard_call(
        self,
        call_id: int | str,
        *,
        duration: int = 0,
        reason: int = 0,
        type_: int = 0,
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "DiscardCall",
            "request.DiscardCall",
            "response.CallWithParticipants",
            {
                "call_id": _require_call_id(call_id),
                "duration": duration,
                "reason": reason,
                "type": type_,
            },
        )

    async def start_call_stream(
        self, stream_user: str, url: str, rtmp_server: str
    ) -> str | None:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "StartStream",
            "request.StartStream",
            "response.StartStream",
            {
                "stream_user": _out_peer(stream_user),
                "url": url,
                "rtmp_server": rtmp_server,
            },
        )
        key = response.get("stream_key")
        return key if isinstance(key, str) else None

    async def delete_call_stream(self, stream_user: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "DeleteStream",
            "request.DeleteStream",
            "response.DefaultResponse",
            {"stream_user": _out_peer(stream_user)},
        )
        return wrap_default(response)

    async def submit_call_feedback(
        self,
        call_id: int | str,
        rate: int,
        *,
        opinion: str | None = None,
        client: int = 0,
        client_version: str | None = None,
        extra_fields: Mapping[str, bytes] | None = None,
        is_stream: bool | None = None,
    ) -> DefaultResponse:
        if not 1 <= rate <= 5:
            raise ValueError("rate must be between 1 and 5")
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "SubmitCallFeedback",
            "request.SubmitCallFeedback",
            "response.DefaultResponse",
            {
                "call_id": _require_call_id(call_id),
                "rate": rate,
                "user_opinion": {"value": opinion} if opinion else None,
                "client": client,
                "client_version": (
                    {"value": client_version} if client_version else None
                ),
                "extra_fields": dict(extra_fields or {}),
                "is_stream": (
                    {"value": is_stream} if is_stream is not None else None
                ),
            },
        )
        return wrap_default(response)

    async def take_call_action(
        self,
        call_id: int | str,
        identity: str,
        *,
        raise_hand: bool,
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "TakeCallAction",
            "request.TakeCallAction",
            "response.EmptyResponse",
            {
                "call_id": _require_call_id(call_id),
                "raise_hand": {"user_identity": identity} if raise_hand else None,
                "lower_hand": {"user_identity": identity} if not raise_hand else None,
            },
        )

    async def raise_call_hand(
        self, call_id: int | str, identity: str
    ) -> dict[str, Any]:
        return await self.take_call_action(call_id, identity, raise_hand=True)

    async def lower_call_hand(
        self, call_id: int | str, identity: str
    ) -> dict[str, Any]:
        return await self.take_call_action(call_id, identity, raise_hand=False)

    async def start_group_call(
        self,
        chat_id: str,
        *,
        video: bool = False,
        mode: CallMode = CallMode.GROUP,
        invitees: Iterable[str] = (),
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "StartGroupCall",
            "request.StartGroupCall",
            "response.GroupCallWithSequence",
            {
                "peer": _require_peer(chat_id),
                "random_id": WebSocketTransport.create_rid(),
                "video": video,
                "mode": int(mode),
                "invitees": [_require_peer(value) for value in invitees],
            },
        )

    async def join_group_call(
        self, call_id: int | str, name: str | None = None
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "JoinGroupCall",
            "request.JoinGroupCall",
            "response.JoinGroupCall",
            {
                "call_id": _require_call_id(call_id),
                "name": {"value": name} if name else None,
            },
        )

    async def join_group_call_rtc(
        self, call_id: int | str, name: str | None = None
    ) -> CallRtcConnection:
        """Join a group call and return typed LiveKit credentials.

        Call ``await connection.connect()`` on the result to create and connect
        an official ``livekit.rtc.Room``. Leaving remains explicit through
        :meth:`leave_group_call`, so callers decide whether to end the call.
        """

        joined = await self.join_group_call(call_id, name)
        group_call = joined.get("group_call")
        if not isinstance(group_call, Mapping):
            raise ValueError("JoinGroupCall response does not contain GroupCall")
        raw_url = group_call.get("url")
        fallback_url = None
        if not isinstance(raw_url, Mapping) or not raw_url.get("text"):
            fallback_url = await self.get_call_wss_url(call_id)
        return call_rtc_connection_from_group_call(
            group_call, fallback_url=fallback_url
        )

    async def set_group_slow_mode(
        self, chat_id: str, seconds: int | None
    ) -> ProtobufMessage:
        """Set or disable a group's slow-mode interval."""

        peer_id, _peer_type = _require_peer_tuple(chat_id)
        return await self.recovered.call(
            "bale.groups.v1.Groups",
            "SetSlowMode",
            group={"groupId": peer_id, "accessHash": 1},
            seconds={"value": seconds} if seconds is not None else None,
        )

    async def set_group_sign_messages(
        self, chat_id: str, enabled: bool
    ) -> ProtobufMessage:
        """Enable or disable signed messages for a group."""

        peer_id, _peer_type = _require_peer_tuple(chat_id)
        return await self.recovered.call(
            "bale.groups.v1.Groups",
            "SetSignMessages",
            groupPeer={"groupId": peer_id, "accessHash": 1},
            signMessages=enabled,
        )

    async def get_bill_menu(self) -> ProtobufMessage:
        """Return the current bill-payment menu configuration."""

        return await self.recovered.call("bale.bill.v1.Bill", "GetBillMenu")

    async def get_all_stories(self) -> ProtobufMessage:
        """Return the current combined stories response."""

        return await self.recovered.call("bale.story.v1.Story", "GetAllStories")

    async def get_marketing_tools_config(self) -> ProtobufMessage:
        """Return Pishvaz marketing-tool configuration."""

        return await self.recovered.call(
            "bale.pishvaz.v1.Pishvaz", "GetMarketingToolsConfig"
        )

    async def search_bale_services(
        self, query: str, *, language: str = "fa", source: int = 0
    ) -> ProtobufMessage:
        """Search Bale service entries through the recovered Garson RPC."""

        return await self.recovered.call(
            "bale.garson.v1.Garson",
            "SearchServices",
            query={"value": query},
            language={"value": language},
            source=source,
        )

    async def leave_group_call(
        self, call_id: int | str, *, end: bool = False
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "LeaveGroupCall",
            "request.LeaveGroupCall",
            "response.GroupCallWithSequence",
            {"call_id": _require_call_id(call_id), "end": end},
        )

    async def invite_to_call(
        self, call_id: int | str, invitees: Iterable[str]
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "InviteToCall",
            "request.InviteToCall",
            "response.InviteToCall",
            {
                "call_id": _require_call_id(call_id),
                "invitees": [_require_peer(value) for value in invitees],
            },
        )

    async def get_group_call(self, chat_id: str) -> dict[str, Any] | None:
        try:
            response = await self.invoke(
                "bale.meet.v1.Meet",
                "GetGroupCall",
                "request.GetGroupCall",
                "response.GroupCall",
                {"peer": _require_peer(chat_id)},
            )
        except BaleRpcError as error:
            if error.code == 5 and error.message == "CallNotFound":
                return None
            raise
        value = response.get("group_call")
        return value if isinstance(value, dict) else None

    async def get_call_logs(
        self,
        page: int = 1,
        limit: int = 50,
        *,
        after_date: int | None = None,
        before_date: int | None = None,
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "GetCallLogs",
            "request.GetCallLogs",
            "response.GetCallLogs",
            {
                "page_number": {"value": page},
                "page_size": {"value": limit},
                "after_date": {"value": after_date} if after_date else None,
                "before_date": {"value": before_date} if before_date else None,
            },
        )

    async def get_ongoing_calls(
        self, page: int | None = None, limit: int | None = None
    ) -> list[dict[str, Any]]:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "GetOngoingCalls",
            "request.GetOngoingCalls",
            "response.GetOngoingCalls",
            {
                "page_number": {"value": page} if page is not None else None,
                "page_size": {"value": limit} if limit is not None else None,
            },
        )
        return list(response.get("call_logs", []))

    async def delete_call_logs(
        self,
        call_ids: Iterable[int | str] = (),
        *,
        all_: bool = False,
        invert: bool = False,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "DeleteCallLogs",
            "request.DeleteCallLogs",
            "response.DefaultResponse",
            {
                "call_ids": [{"value": _require_call_id(value)} for value in call_ids],
                "all": all_,
                "invert": invert,
            },
        )
        return wrap_default(response)

    async def generate_call_link(
        self,
        *,
        is_public: bool = True,
        call_id: int | str | None = None,
        title: str | None = None,
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.meet.v1.Meet",
            "GenerateCallLink",
            "request.GenerateCallLink",
            "response.GenerateCallLink",
            {
                "is_public": is_public,
                "call_id": (
                    {"value": _require_call_id(call_id)}
                    if call_id is not None
                    else None
                ),
                "title": {"value": title} if title else None,
            },
        )

    async def get_call_link_details(self, session: str) -> dict[str, Any] | None:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "GetCallLinkDetails",
            "request.GetCallLinkDetails",
            "response.GroupCall",
            {"session": session},
        )
        value = response.get("group_call")
        return value if isinstance(value, dict) else None

    async def set_call_link_title(
        self,
        title: str,
        *,
        call_id: int | str | None = None,
        link_url: str | None = None,
    ) -> DefaultResponse:
        if call_id is None and not link_url:
            raise ValueError("Either call_id or link_url is required")
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "SetLinkTitle",
            "request.SetCallLinkTitle",
            "response.DefaultResponse",
            {
                "title": title,
                "call_id": (
                    {"value": _require_call_id(call_id)}
                    if call_id is not None
                    else None
                ),
                "link_url": {"value": link_url} if link_url else None,
            },
        )
        return wrap_default(response)

    async def send_call_reaction(
        self, call_id: int | str, reaction: str
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "SendCallReaction",
            "request.SendCallReaction",
            "response.DefaultResponse",
            {"call_id": _require_call_id(call_id), "reaction": reaction},
        )
        return wrap_default(response)

    async def send_call_fanoos_event(
        self,
        event_name: str,
        items: Mapping[str, Any] | None = None,
        *,
        date: int | None = None,
    ) -> DefaultResponse:
        """Send a Meet analytics event using the current typed protobuf schema.

        ``items`` accepts strings, booleans, integers, floats, and nested arrays
        of those scalar values.  ``date`` defaults to Unix time in milliseconds,
        matching Bale Web.
        """
        if not event_name.strip():
            raise ValueError("event_name must not be empty")
        event_items = [
            {"key": str(key), "value": _fanoos_value(value)}
            for key, value in (items or {}).items()
        ]
        request = pb.WebSendFanoosEventRequest(
            eventName=event_name,
            items={"items": event_items},
            date=int(time.time() * 1000) if date is None else date,
        )
        await self.invoke_protobuf(
            "bale.meet.v1.Meet",
            "SendFanoosEvent",
            request,
            response_type=pb.WebT_Ou,
        )
        return wrap_default({})

    async def mute_call_participant(
        self,
        call_id: int | str,
        identity: str,
        *,
        track_id: str = "",
        revoke_publish_permission: bool = False,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "MuteParticipant",
            "request.MuteParticipant",
            "response.DefaultResponse",
            {
                "call_id": _require_call_id(call_id),
                "identity": identity,
                "track_id": track_id,
                "revoke_publish_permission": revoke_publish_permission,
            },
        )
        return wrap_default(response)

    async def remove_call_participant(
        self,
        call_id: int | str,
        identity: str,
        *,
        block: bool = False,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "RemoveParticipant",
            "request.RemoveParticipant",
            "response.DefaultResponse",
            {
                "call_id": _require_call_id(call_id),
                "identity": identity,
                "block_from_call": block,
            },
        )
        return wrap_default(response)

    async def start_call_recording(
        self,
        call_id: int | str,
        layout: str,
        quality: CallRecordQuality = CallRecordQuality.HIGH,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "StartRecording",
            "request.StartRecording",
            "response.DefaultResponse",
            {
                "call_id": _require_call_id(call_id),
                "layout": layout,
                "quality": int(quality),
            },
        )
        return wrap_default(response)

    async def stop_call_recording(self, call_id: int | str) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "StopRecording",
            "request.StopRecording",
            "response.DefaultResponse",
            {"call_id": _require_call_id(call_id)},
        )
        return wrap_default(response)

    async def update_call_layout(
        self, call_id: int | str, layout: str
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "UpdateLayout",
            "request.UpdateCallLayout",
            "response.DefaultResponse",
            {"call_id": _require_call_id(call_id), "requested_layout": layout},
        )
        return wrap_default(response)

    async def ask_to_join_call(self, call_id: int | str, name: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "AskToJoinCall",
            "request.AskToJoinCall",
            "response.DefaultResponse",
            {"call_id": _require_call_id(call_id), "name": name},
        )
        return wrap_default(response)

    async def answer_call_join_request(
        self,
        call_id: int | str,
        requester_identifier: str,
        *,
        allow: bool,
    ) -> DefaultResponse:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "AnswerCallJoinRequest",
            "request.AnswerCallJoinRequest",
            "response.DefaultResponse",
            {
                "call_id": _require_call_id(call_id),
                "requester_identifier": requester_identifier,
                "is_allowed": allow,
            },
        )
        return wrap_default(response)

    async def get_call_state(self, call_id: int | str) -> dict[str, Any] | None:
        response = await self.invoke(
            "bale.meet.v1.Meet",
            "GetCallState",
            "request.GetCallState",
            "response.GroupCall",
            {"call_id": _require_call_id(call_id)},
        )
        value = response.get("group_call")
        return value if isinstance(value, dict) else None

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

    async def pin_chat_message(
        self, chat_id: str, message_id: str, just_mine: bool = False
    ) -> DefaultResponse:
        """Pin a message in either a private peer or a group."""
        _peer_id, peer_type = _require_peer_tuple(chat_id)
        if peer_type in (1, 4):
            return await self.pin_message(chat_id, message_id, just_mine)
        return await self.pin_group_message(chat_id, message_id)

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
        _peer_id, peer_type = _require_peer_tuple(chat_id)
        if peer_type in (1, 4):
            return await self.unpin_messages(chat_id, [message_id])
        return await self.unpin_group_message(chat_id, message_id)

    async def unpin_all(self, chat_id: str) -> DefaultResponse:
        _peer_id, peer_type = _require_peer_tuple(chat_id)
        if peer_type in (1, 4):
            return await self.unpin_messages(chat_id, all_=True)
        return await self.remove_group_pins(chat_id)

    unpin_chat_message = unpin_message
    unpin_all_chat_messages = unpin_all

    async def pin_group_message(self, chat_id: str, message_id: str) -> DefaultResponse:
        rid, date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "PinMessage",
            "request.PinMessage",
            "response.DefaultResponse",
            {
                "group_peer": _group_peer(chat_id),
                "date": date,
                "msg_rid": rid,
            },
        )
        return wrap_default(response)

    async def unpin_group_message(
        self, chat_id: str, message_id: str
    ) -> DefaultResponse:
        rid, date = _require_message_id(message_id)
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RemoveSinglePin",
            "request.RemoveSinglePin",
            "response.DefaultResponse",
            {"group_peer": _group_peer(chat_id), "rid": rid, "date": date},
        )
        return wrap_default(response)

    remove_single_pin = unpin_group_message

    async def remove_group_pins(self, chat_id: str) -> DefaultResponse:
        response = await self.invoke(
            "bale.groups.v1.Groups",
            "RemovePin",
            "request.RemovePin",
            "response.DefaultResponse",
            {"group_peer": _group_peer(chat_id)},
        )
        return wrap_default(response)

    remove_all_pins = remove_group_pins

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

    async def edit_message_caption(
        self, chat_id: str, message_id: str, caption: str
    ) -> DefaultResponse:
        """Update the caption of a media message in an account session."""
        rid, date = _require_message_id(message_id)
        peer = _require_peer(chat_id)
        history = await self._load_history(peer, date, 20)
        source = next(
            (
                item
                for item in history.get("history", [])
                if int(item.get("rid", 0)) == rid
            ),
            None,
        )
        if not isinstance(source, Mapping) or not isinstance(
            source.get("message"), Mapping
        ):
            raise ClientStateError(f"Could not load source message {message_id}")
        updated_message = dict(source["message"])
        document = updated_message.get("document_message")
        if not isinstance(document, Mapping):
            raise ClientStateError(f"Message {message_id} does not contain media")
        updated_document = dict(document)
        updated_document["caption"] = {"text": caption}
        updated_message["document_message"] = updated_document
        response = await self.invoke(
            "bale.messaging.v2.Messaging",
            "UpdateMessage",
            "request.UpdateMessage",
            "response.DefaultResponse",
            {
                "peer": peer,
                "rid": rid,
                "updated_message": updated_message,
            },
        )
        return wrap_default(response)

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

    async def get_wallet(self) -> WalletResponse:
        cached = self._wallet_cache
        now = time.monotonic()
        if cached is not None and cached[0] > now:
            return cached[1]
        async with self._wallet_lock:
            cached = self._wallet_cache
            now = time.monotonic()
            if cached is not None and cached[0] > now:
                return cached[1]
            response = await self.invoke(
                "bale.kifpool.v1.Kifpool",
                "GetMyKifpools",
                "request.GetMyKifpools",
                "response.GetMyKifpools",
                {},
            )
            wallet = wrap_wallet_response(response)
            self._wallet_cache = (now + 60.0, wallet)
            return wallet

    get_my_kifpools = get_wallet

    async def prime_wallet_cache(self) -> WalletResponse | None:
        try:
            return await self.get_wallet()
        except Exception:
            return None

    async def send_gift(
        self,
        chat_id: str,
        amount: int,
        message: str,
        *,
        gift_count: int = 1,
        giving_type: GivingType = GivingType.SAME,
        show_amounts: bool = True,
        token: str | None = None,
    ) -> DefaultResponse:
        wallet_token = token
        if not wallet_token:
            wallet = await self.get_wallet()
            wallet_token = wallet.wallet.token if wallet.wallet else None
        if not wallet_token:
            raise ClientStateError("A wallet token is required to send a gift")
        response = await self.invoke(
            "bale.giftpacket.v1.GiftPacket",
            "SendGiftPacketWithWallet",
            "request.SendGiftPacketWithWallet",
            "response.DefaultResponse",
            {
                "peer": _require_peer(chat_id),
                "random_id": WebSocketTransport.create_rid(),
                "gift": {
                    "count": gift_count,
                    "total_amount": amount,
                    "giving_type": int(giving_type),
                    "message": {"value": message},
                    "owner_id": self.user.id if self.user else None,
                    "show_amounts": {"value": show_amounts},
                },
                "token": wallet_token,
            },
        )
        return wrap_default(response)

    send_gift_packet_with_wallet = send_gift
    send_giftpacket = send_gift

    async def open_gift(
        self, message: Message, receiver_token: str | None = None
    ) -> PacketResponse:
        wallet_token = receiver_token
        if not wallet_token:
            wallet = await self.get_wallet()
            wallet_token = wallet.wallet.token if wallet.wallet else None
        if not wallet_token:
            raise ClientStateError("A wallet token is required to open a gift")
        response = await self.invoke(
            "bale.giftpacket.v1.GiftPacket",
            "OpenGiftPacket",
            "request.OpenGiftPacket",
            "response.OpenGiftPacket",
            {"message": _info_message(message), "receiver_token": wallet_token},
        )
        return wrap_packet_response(response)

    open_gift_packet = open_gift
    open_packet = open_gift

    async def upvote_post(
        self, message: Message, album_id: int | None = None
    ) -> dict[str, Any]:
        return await self.invoke(
            "bale.magazine.v1.Magazine",
            "UpvotePost",
            "request.UpvotePost",
            "response.UpvoteResponse",
            {
                "message": _info_message(message),
                "album_id": {"value": album_id} if album_id is not None else None,
            },
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
        phone_number = self._phone_number
        while True:
            while not phone_number:
                phone_number = (
                    await _resolve_prompt(
                        self._phone_prompt,
                        "Bale phone number in international format (+989...): ",
                    )
                ).strip()
                if not re.sub(r"\D", "", phone_number):
                    _status("Please enter a valid phone number.", error=True)
                    phone_number = None
            try:
                sent = await self.start_phone_auth(phone_number)
                break
            except BaleRpcError as error:
                if error.message != "PHONE_NUMBER_INVALID":
                    raise
                _status(
                    "Bale rejected that phone number. Use international format, "
                    "for example +989121234567.",
                    error=True,
                )
                phone_number = None
                self._phone_number = None
        transaction_hash = str(sent.get("transaction_hash", ""))
        if not transaction_hash:
            raise AuthenticationError("Phone authentication response is incomplete")
        while True:
            code = (
                await _resolve_prompt(
                    self._code_prompt, "Enter the verification code sent by Bale: "
                )
            ).strip()
            try:
                return _parse_auth(await self.validate_code(transaction_hash, code))
            except BaleRpcError as error:
                if error.message == "PHONE_CODE_INVALID":
                    _status(
                        "The verification code is invalid; please try again.",
                        error=True,
                    )
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
                        self._password_prompt, "Two-step verification password: "
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
            try:
                await self.dispatcher.dispatch_raw_update(self, update)
                for event in build_updates(update, self._wrap_message):
                    if isinstance(event, NewMessage):
                        key = (event.message.chat.id, event.message.id)
                        content = json.dumps(
                            event.message.raw.get("message", {}),
                            ensure_ascii=False,
                            sort_keys=True,
                            default=str,
                        )
                        previous = self._seen_messages.get(key)
                        self._seen_messages[key] = content
                        if len(self._seen_messages) > 5000:
                            self._seen_messages.pop(next(iter(self._seen_messages)))
                        if previous is not None and previous != content:
                            event = MessageEdited(event.raw, event.message)
                    event.bind(self)
                    self._event_queue.put_nowait(event)
                    await self.dispatcher.dispatch_update(self, event)
                    message = getattr(event, "message", None)
                    if message is not None and int(message.rid) != 0:
                        await self.dispatcher.dispatch_message(self, message)
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

    async def _read_media(self, media: MediaInput) -> tuple[bytes, str]:
        if isinstance(media, bytes):
            return media, "upload"
        if isinstance(media, (bytearray, memoryview)):
            return bytes(media), "upload"
        if isinstance(media, Path):
            return await asyncio.to_thread(media.read_bytes), media.name
        if isinstance(media, str):
            parsed = urlsplit(media)
            if parsed.scheme in {"http", "https"}:
                data = await self._grpc.download(media)
                name = os.path.basename(parsed.path) or "download"
                return data, name
            path = Path(media)
            return await asyncio.to_thread(path.read_bytes), path.name
        if isinstance(media, BufferedIOBase) or hasattr(media, "read"):
            stream = media
            original_position = stream.tell() if hasattr(stream, "tell") else None
            if hasattr(stream, "seek"):
                stream.seek(0)
            value = stream.read()
            if original_position is not None and hasattr(stream, "seek"):
                stream.seek(original_position)
            if not isinstance(value, bytes):
                raise TypeError("file.read() must return bytes")
            raw_name = getattr(stream, "name", None)
            return value, os.path.basename(str(raw_name)) if raw_name else "upload"
        raise TypeError("media must be bytes, a path, URL, or binary file object")


def _is_session(value: str) -> bool:
    return re.fullmatch(r"\d+:.+", value, re.DOTALL) is not None


def _looks_like_phone(value: str) -> bool:
    return (
        re.fullmatch(r"[+()\-\d\s]+", value) is not None
        and len(re.sub(r"\D", "", value)) >= 7
    )


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


def _file_location(
    file_id: int | str, access_hash: int, file_storage_version: int
) -> dict[str, Any]:
    """Build the FileLocation shape shared by Bale's Nasim RPCs."""
    try:
        storage_version = int(file_storage_version)
    except (TypeError, ValueError) as error:
        raise ValueError("file_storage_version must be an integer") from error
    if not 0 <= storage_version <= (1 << 31) - 1:
        raise ValueError("file_storage_version must be a non-negative int32")
    return {
        "file_id": _unsigned_int64(file_id, field_name="file_id"),
        "access_hash": _signed_int64(access_hash, field_name="access_hash"),
        "file_storage_version": {"value": storage_version},
    }


def _out_peer(value: str) -> dict[str, int]:
    return {**_require_peer(value), "access_hash": 1}


def _user_peer(value: int | str, *, access_hash: int = 1) -> dict[str, int]:
    if isinstance(value, int):
        user_id = _user_id(value)
        return {
            "uid": user_id,
            "access_hash": _signed_int64(access_hash, field_name="access_hash"),
        }
    parsed = _parse_peer(value)
    user_id = _user_id(parsed[0] if parsed else value)
    return {
        "uid": user_id,
        "access_hash": _signed_int64(access_hash, field_name="access_hash"),
    }


def _user_id(value: int | str) -> int:
    try:
        user_id = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Expected a numeric Bale user id, got {value!r}") from error
    if not 0 < user_id <= (1 << 31) - 1:
        raise ValueError("Bale user id must be a positive int32")
    return user_id


def _require_message_id(value: str) -> tuple[int, int]:
    match = _MESSAGE_PATTERN.fullmatch(value.strip())
    if match is None:
        raise ValueError(
            "Expected a message id like '-123|1700000000', "
            f"got {value!r}"
        )
    rid = _signed_int64(match.group("rid"), field_name="message rid")
    date = _signed_int64(match.group("date"), field_name="message date")
    if date < 0:
        raise ValueError("message date cannot be negative")
    return rid, date


def _message_identifier(value: str) -> dict[str, int]:
    rid, date = _require_message_id(value)
    return {"rid": rid, "date": date}


def _require_call_id(value: int | str) -> int:
    try:
        call_id = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Expected a numeric Bale call id, got {value!r}") from error
    # Bale uses signed int64 call identifiers.  Real responses can therefore
    # contain negative ids; only zero represents a missing/invalid call id.
    if call_id == 0:
        raise ValueError("Bale call id must be non-zero")
    return call_id


def _unsigned_int64(value: int | str, *, field_name: str) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{field_name} must be an integer") from error
    if number < 0:
        number += 1 << 64
    if not 0 <= number < 1 << 64:
        raise ValueError(f"{field_name} is outside the uint64 range")
    return number


def _signed_int64(value: int | str, *, field_name: str) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{field_name} must be an integer") from error
    if not -(1 << 63) <= number < 1 << 63:
        raise ValueError(f"{field_name} is outside the int64 range")
    return number


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


def _group_token(value: str) -> str:
    token = value.strip()
    token = token.removeprefix("https://ble.ir/join/")
    token = token.removeprefix("ble.ir/join/")
    if not token:
        raise ValueError("A Bale group invite token cannot be empty")
    return token


def _member_is_admin(member: Mapping[str, Any]) -> bool:
    value = member.get("is_admin")
    if isinstance(value, Mapping):
        return bool(value.get("value"))
    return bool(value)


def _document_message(
    uploaded: Mapping[str, Any],
    ext_name: str | None,
    caption: str | None = None,
    width: int = 100,
    height: int = 100,
    duration: int = 0,
    title: str | None = None,
) -> dict[str, Any]:
    document: dict[str, Any] = {
        "file_id": int(uploaded["file_id"]),
        "access_hash": int(uploaded.get("access_hash", 0)),
        "file_size": int(uploaded.get("file_size", 0)),
        "name": str(uploaded.get("name", "upload")),
        "mime_type": str(uploaded.get("mime_type", "application/octet-stream")),
        "caption": {"text": caption} if caption is not None else None,
    }
    if ext_name in {"photo", "video", "gif"}:
        ext: dict[str, Any] = {"w": width, "h": height}
        if ext_name in {"video", "gif"}:
            ext["duration"] = duration
        document["ext"] = {f"document_ex_{ext_name}": ext}
    elif ext_name == "audio":
        document["ext"] = {
            "document_ex_audio": {
                "duration": duration,
                "track": title or document["name"],
            }
        }
    elif ext_name == "voice":
        document["ext"] = {"document_ex_voice": {"duration": duration}}
    return document


def _sticker_message(sticker: str | Mapping[str, Any]) -> dict[str, Any]:
    if isinstance(sticker, Mapping):
        return dict(sticker)
    parts = sticker.split(":")
    if len(parts) != 5:
        raise ValueError(
            "sticker must use '<file_id>:<access_hash>:<storage_version>:'"
            "<sticker_id>:<collection_id>'"
        )
    file_id, access_hash, storage_version, sticker_id, collection_id = map(int, parts)
    return {
        "sticker_id": {"value": sticker_id},
        "image512": {
            "file_location": {
                "file_id": _unsigned_int64(file_id, field_name="file_id"),
                "access_hash": access_hash,
                "file_storage_version": {"value": storage_version},
            }
        },
        "sticker_collection_id": {"value": collection_id},
    }


def _parse_auth(response: dict[str, Any]) -> Session:
    user = response.get("user") or {}
    jwt = response.get("jwt") or {}
    user_id, token = int(user.get("id", 0)), jwt.get("value")
    if not user_id or not isinstance(token, str) or not token:
        raise AuthenticationError("Bale authentication response is incomplete")
    return Session(user_id, token)


async def _terminal_prompt(text: str) -> str:
    return await asyncio.to_thread(input, _colorize(text, 33))


async def _terminal_password_prompt(text: str) -> str:
    return await asyncio.to_thread(getpass.getpass, _colorize(text, 33))


async def _resolve_prompt(prompt: Prompt, text: str) -> str:
    value = prompt(text)
    if inspect.isawaitable(value):
        value = await value
    return value


def _milliseconds() -> int:
    return int(time.time() * 1000)


def _is_authentication_failure(error: BaseException) -> bool:
    if isinstance(error, AuthenticationError):
        return True
    if isinstance(error, BaleRpcError):
        if error.code in {16, 401, 403}:
            return True
        message = f"{error.message} {error.reason or ''}".casefold()
        return any(
            marker in message
            for marker in ("unauthenticated", "unauthorized", "session", "jwt", "token")
        )
    status = getattr(error, "status_code", None)
    if status in {401, 403}:
        return True
    response = getattr(error, "response", None)
    if getattr(response, "status_code", None) in {401, 403}:
        return True
    message = str(error).casefold()
    return any(
        marker in message
        for marker in ("unauthenticated", "unauthorized", "invalid session", "jwt")
    )

from __future__ import annotations

from typing import Any

import pytest

from bale import Client, Message, filters
from bale.models import Chat, ChatType, User


class FakeGrpc:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []
        self.closed = False

    async def request(
        self,
        service: str,
        method: str,
        request_type: str,
        response_type: str,
        payload: dict[str, Any],
        *,
        access_token: str | None = None,
    ) -> dict[str, Any]:
        self.calls.append(
            {
                "service": service,
                "method": method,
                "request_type": request_type,
                "response_type": response_type,
                "payload": payload,
                "access_token": access_token,
            }
        )
        if method == "StartPhoneAuth":
            return {"transaction_hash": "transaction"}
        if method == "ValidateCode":
            return {"user": {"id": 55}, "jwt": {"value": "new-jwt"}}
        return {"seq": 1, "date": 1700000000000}

    async def close(self) -> None:
        self.closed = True


@pytest.mark.asyncio
async def test_phone_auth_supports_noninteractive_async_prompt(tmp_path) -> None:
    grpc = FakeGrpc()

    async def code_prompt(_text: str) -> str:
        return "12345"

    client = Client(
        "+989121234567",
        session_dir=tmp_path,
        code_prompt=code_prompt,
        grpc=grpc,  # type: ignore[arg-type]
    )

    session = await client._authenticate()

    assert str(session) == "55:new-jwt"
    assert [call["method"] for call in grpc.calls] == [
        "StartPhoneAuth",
        "ValidateCode",
    ]


@pytest.mark.asyncio
async def test_send_message_uses_user_session_rpc(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client(
        "42:jwt-token",
        session_dir=tmp_path,
        grpc=grpc,  # type: ignore[arg-type]
    )
    client.user = User(42).bind(client)

    message = await client.send_message("99|1", "hello")

    assert isinstance(message, Message)
    assert message.text == "hello"
    assert message.chat.id == "99|1"
    call = grpc.calls[-1]
    assert call["method"] == "SendMessage"
    assert call["access_token"] == "jwt-token"
    assert call["payload"]["message"] == {"text_message": {"text": "hello"}}


@pytest.mark.asyncio
async def test_composable_filters_and_error_handlers(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]
    handled: list[str] = []
    errors: list[str] = []

    @client.on_message(filters.private & filters.command("ping"))
    async def handler(message: Message, _client: Client) -> None:
        handled.append(message.content)
        raise RuntimeError("handler failed")

    @client.on_error
    async def error_handler(error: BaseException, _client: Client) -> None:
        errors.append(str(error))

    message = Message(
        rid=1,
        date=2,
        author=User(3),
        chat=Chat(4, 1, type=ChatType.PRIVATE),
        text="/ping now",
    ).bind(client)

    await client.dispatcher.dispatch_message(client, message)

    assert handled == ["/ping now"]
    assert errors == ["handler failed"]

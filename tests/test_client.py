from __future__ import annotations

from typing import Any

import pytest

from bale import BaleRpcError, Client, GivingType, Message, Session, filters
from bale.models import Chat, ChatType, User
from bale.proto import encode_message


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
        encode_message(request_type, payload)
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
        if method == "GetWssURL":
            return {"url": "wss://meet.example.test/ws"}
        if method == "GetMyKifpools":
            return {"wallet": [{"token": "wallet-token", "balance": 1000}]}
        if method == "OpenGiftPacket":
            return {
                "receivers": [{"id": 55, "amount": 10}],
                "status": "GIFT_OPENNING_SUCCESSFUL",
                "openned_count": 1,
                "win_amount": {"value": 10},
            }
        return {"seq": 1, "date": 1700000000000}

    async def request_raw(
        self,
        service: str,
        method: str,
        payload: bytes,
        *,
        access_token: str | None = None,
    ) -> bytes:
        self.calls.append(
            {
                "service": service,
                "method": method,
                "payload": payload,
                "access_token": access_token,
            }
        )
        return b"raw-response"

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
async def test_client_without_credential_prompts_when_session_is_missing(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    grpc = FakeGrpc()
    prompts: list[str] = []

    async def prompt(text: str) -> str:
        prompts.append(text)
        return "+989121234567" if "phone number" in text else "12345"

    connected: list[Session] = []

    async def connect_session(_client: Client, session: Session) -> None:
        connected.append(session)

    monkeypatch.setattr(Client, "_connect_session", connect_session)
    client = Client(
        session_dir=tmp_path,
        session_name="account",
        phone_prompt=prompt,
        code_prompt=prompt,
        grpc=grpc,  # type: ignore[arg-type]
    )

    await client.connect()

    assert connected == [Session(55, "new-jwt")]
    assert [call["method"] for call in grpc.calls] == [
        "StartPhoneAuth",
        "ValidateCode",
    ]
    assert any("phone number" in value for value in prompts)
    assert (tmp_path / "account.session").read_text() == "55:new-jwt"


@pytest.mark.asyncio
async def test_expired_session_is_deleted_and_terminal_login_is_retried(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    grpc = FakeGrpc()
    (tmp_path / "account.session").write_text("42:expired-jwt")

    async def prompt(text: str) -> str:
        return "+989121234567" if "phone number" in text else "12345"

    attempts: list[Session] = []

    async def connect_session(_client: Client, session: Session) -> None:
        attempts.append(session)
        if session.jwt == "expired-jwt":
            raise BaleRpcError(16, "UNAUTHENTICATED")

    monkeypatch.setattr(Client, "_connect_session", connect_session)
    client = Client(
        session_dir=tmp_path,
        session_name="account",
        phone_prompt=prompt,
        code_prompt=prompt,
        grpc=grpc,  # type: ignore[arg-type]
    )

    await client.connect()

    assert attempts == [Session(42, "expired-jwt"), Session(55, "new-jwt")]
    assert (tmp_path / "account.session").read_text() == "55:new-jwt"


@pytest.mark.asyncio
async def test_network_failure_does_not_delete_a_valid_session(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    session_file = tmp_path / "account.session"
    session_file.write_text("42:keep-this-jwt")

    async def unexpected_prompt(_text: str) -> str:
        raise AssertionError("network errors must not trigger terminal login")

    async def connect_session(_client: Client, _session: Session) -> None:
        raise OSError("network unavailable")

    monkeypatch.setattr(Client, "_connect_session", connect_session)
    client = Client(
        session_dir=tmp_path,
        session_name="account",
        phone_prompt=unexpected_prompt,
        grpc=FakeGrpc(),  # type: ignore[arg-type]
    )

    with pytest.raises(OSError, match="network unavailable"):
        await client.connect()

    assert session_file.read_text() == "42:keep-this-jwt"


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
async def test_inline_callback_and_call_methods_use_recorded_rpc_shapes(
    tmp_path,
) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    await client.click_inline_button("99|3", "123|456", "callback-data")
    await client.generate_call_link(is_public=True, title="Team call")
    await client.join_group_call(789, "Mahan")
    wss_url = await client.get_call_wss_url(789)

    callback, generate, join, wss = grpc.calls
    assert callback["method"] == "SendInlineCallback"
    assert callback["payload"] == {
        "peer": {"id": 99, "type": 3},
        "message_id": {"rid": 123, "date": 456},
        "data": {"value": "callback-data"},
    }
    assert generate["request_type"] == "request.GenerateCallLink"
    assert generate["payload"]["title"] == {"value": "Team call"}
    assert join["payload"] == {"call_id": 789, "name": {"value": "Mahan"}}
    assert wss["method"] == "GetWssURL"
    assert wss_url == "wss://meet.example.test/ws"


@pytest.mark.asyncio
async def test_call_methods_accept_signed_int64_call_ids(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    await client.get_call_state(-789)

    assert grpc.calls[-1]["payload"] == {"call_id": -789}


@pytest.mark.asyncio
async def test_call_methods_reject_zero_call_id(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="non-zero"):
        await client.get_call_state(0)


@pytest.mark.asyncio
async def test_invoke_raw_uses_session_without_a_schema(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    response = await client.invoke_raw("bale.new.v1.New", "NewMethod", b"\x08\x01")

    assert response == b"raw-response"
    assert grpc.calls[-1] == {
        "service": "bale.new.v1.New",
        "method": "NewMethod",
        "payload": b"\x08\x01",
        "access_token": "jwt-token",
    }


@pytest.mark.asyncio
async def test_balejs_file_group_pin_and_media_methods_use_expected_rpcs(
    tmp_path,
) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]
    client.user = User(42).bind(client)

    await client.remove_user_admin("99|2", 7)
    await client.edit_group_about("99|2", "description")
    await client.edit_group_avatar(
        "99|2",
        {"file_id": 11, "access_hash": 12, "file_storage_version": 2},
    )
    await client.pin_group_message("99|2", "13|14")
    await client.get_file(11, 12)
    await client.get_file_upload_url(
        2048,
        "photo.jpg",
        "image/jpeg",
        chat_id="99|2",
        send_type=1,
    )
    messages = await client.send_multi_media_message(
        "99|2",
        [
            {"random_id": 20, "media": {"caption": {"text": "one"}}},
            {"random_id": 21, "media": {"caption": {"text": "two"}}},
        ],
    )

    calls = {call["method"]: call for call in grpc.calls}
    assert calls["RemoveUserAdmin"]["payload"]["user_peer"]["uid"] == 7
    assert calls["EditGroupAbout"]["payload"]["about"] == {"value": "description"}
    assert calls["EditGroupAvatar"]["payload"]["file_location"] == {
        "file_id": 11,
        "access_hash": 12,
        "file_storage_version": {"value": 2},
    }
    assert calls["PinMessage"]["payload"]["msg_rid"] == 13
    assert calls["GetNasimFileUrl"]["payload"]["file"]["file_id"] == 11
    assert calls["GetNasimFileUploadUrl"]["payload"]["send_type"] == {"type": 1}
    assert calls["SendMultiMediaMessage"]["payload"]["multi_media"][0] == {
        "random_id": 20,
        "media": {"caption": {"text": "one"}},
    }
    assert messages[0].id == "20|1700000000000"


@pytest.mark.asyncio
async def test_file_location_converts_signed_ids_to_uint64(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    await client.get_file(-1, 12)
    await client.edit_group_avatar("99|2", {"file_id": -2, "access_hash": 13})

    assert grpc.calls[-2]["payload"]["file"]["file_id"] == (1 << 64) - 1
    assert grpc.calls[-1]["payload"]["file_location"]["file_id"] == (1 << 64) - 2


@pytest.mark.asyncio
async def test_multi_media_album_validates_server_item_limits(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="between 2 and 10"):
        await client.send_multi_media_message(
            "99|2", [{"media": {"caption": {"text": "one"}}}]
        )


@pytest.mark.asyncio
async def test_group_title_validates_live_server_limit(tmp_path) -> None:
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=FakeGrpc())  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="30"):
        await client.create_group("x" * 31)


@pytest.mark.asyncio
async def test_wallet_gift_and_message_object_helpers(tmp_path) -> None:
    grpc = FakeGrpc()
    client = Client("42:jwt-token", session_dir=tmp_path, grpc=grpc)  # type: ignore[arg-type]
    client.user = User(42).bind(client)
    message = Message(
        rid=10,
        date=20,
        author=User(42),
        chat=Chat(99, 1),
        gift=None,
    ).bind(client)

    wallet = await client.get_wallet()
    await client.send_gift(
        "99|1", 100, "gift", gift_count=2, giving_type=GivingType.RANDOM
    )
    opened = await message.open_gift()
    await message.pin_in_group()

    assert wallet.wallet is not None and wallet.wallet.token == "wallet-token"
    assert opened.win_amount == 10
    calls = {call["method"]: call for call in grpc.calls}
    assert calls["SendGiftPacketWithWallet"]["payload"]["gift"] == {
        "count": 2,
        "total_amount": 100,
        "giving_type": 1,
        "message": {"value": "gift"},
        "owner_id": 42,
        "show_amounts": {"value": True},
    }
    assert calls["OpenGiftPacket"]["payload"]["receiver_token"] == "wallet-token"
    assert calls["PinMessage"]["payload"]["group_peer"]["group_id"] == 99


def test_client_exposes_every_user_session_method_from_balejs() -> None:
    balejs_methods = {
        "check_nickname",
        "clear_chat",
        "connect",
        "copy_message",
        "create_channel",
        "create_group",
        "delete_chat",
        "delete_message",
        "disconnect",
        "edit_about",
        "edit_group_about",
        "edit_group_avatar",
        "edit_group_title",
        "edit_message",
        "edit_message_text",
        "edit_name",
        "edit_nickname",
        "edit_parameter",
        "forward_message",
        "get_chat",
        "get_file",
        "get_file_upload_url",
        "get_file_url",
        "get_full_group",
        "get_group_invite_url",
        "get_group_link",
        "get_group_members_count",
        "get_me",
        "get_messages_views",
        "get_my_kifpools",
        "get_parameters",
        "get_wallet",
        "invite_users",
        "join_chat",
        "join_group",
        "join_public_chat",
        "join_public_group",
        "kick_user",
        "leave_chat",
        "leave_group",
        "load_dialogs",
        "load_full_chat",
        "load_full_users",
        "load_group_avatars",
        "load_history",
        "load_members",
        "load_pinned_messages",
        "load_users",
        "message_read",
        "message_set_reaction",
        "open_gift",
        "open_gift_packet",
        "open_packet",
        "pin_group_message",
        "pin_message",
        "prime_wallet_cache",
        "remove_all_pins",
        "remove_group_avatar",
        "remove_group_pins",
        "remove_single_pin",
        "remove_user_admin",
        "report_chat",
        "report_message",
        "report_messages",
        "revoke_group_link",
        "revoke_invite_url",
        "search_contacts",
        "search_username",
        "seen_chat",
        "send_gift",
        "send_gift_packet_with_wallet",
        "send_giftpacket",
        "send_message",
        "send_multi_media_message",
        "set_member_permissions",
        "set_online",
        "sign_out",
        "sign_up",
        "start_phone_auth",
        "start_typing",
        "stop",
        "stop_typing",
        "typing",
        "unban_user",
        "unpin_all",
        "unpin_group_message",
        "unpin_message",
        "unpin_messages",
        "upvote_post",
        "validate_code",
        "validate_password",
    }

    assert len(balejs_methods) == 91
    assert not {name for name in balejs_methods if not hasattr(Client, name)}


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


@pytest.mark.asyncio
async def test_raw_update_handler_receives_every_decoded_update(tmp_path) -> None:
    client = Client("42:jwt", session_dir=tmp_path, grpc=FakeGrpc())  # type: ignore[arg-type]
    received: list[dict[str, Any]] = []

    @client.on_update
    async def handler(update: dict[str, Any], _client: Client) -> None:
        received.append(update)

    update = {"update": {"composed_update": {"message_sent": b"ack"}}}
    await client._process_update(update)

    assert received == [update]

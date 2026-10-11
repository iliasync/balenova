import json

from bale import Chat, ChatType, GiftPacket, Message, User, model_to_dict, model_to_json
from bale.proto import request_pb2


def test_models_are_easy_to_print_as_dict_and_json() -> None:
    user = User(42, username="alice", name="Alice")
    chat = Chat(99, 2, title="A group", type=ChatType.GROUP)
    message = Message(
        rid=2**63 - 1,
        date=1700000000,
        author=user,
        chat=chat,
        text="سلام",
        gift=GiftPacket(count=2, total_amount=100),
        raw={"private": "payload"},
    )

    value = message.to_dict()
    assert value["rid"] == 2**63 - 1
    assert value["author"]["id"] == 42
    assert value["chat"]["type"] == "group"
    assert value["gift"]["total_amount"] == 100
    assert "raw" not in value
    assert "_client" not in value

    decoded = json.loads(message.to_json(indent=None))
    assert decoded["text"] == "سلام"
    assert message.as_dict() == value
    assert json.loads(message.as_json(indent=None)) == decoded


def test_model_helpers_support_nested_values_and_explicit_raw() -> None:
    user = User(1, username="bob")
    value = model_to_dict({"user": user, "data": b"ok"})
    assert value == {
        "user": {"id": 1, "username": "bob", "name": None, "is_bot": False},
        "data": "b2s=",
    }
    assert "private" in model_to_json(
        Message(1, 1, user, Chat(2, 1), raw={"private": 1}), include_raw=True
    )


def test_proto_messages_can_be_printed_as_json() -> None:
    request = request_pb2.SetOnline()
    assert model_to_dict(request) == {}
    assert model_to_json(request, indent=None) == "{}"


def test_peer_and_chat_id_conversions() -> None:
    from bale import (
        Client,
        chat_id_to_peer_id,
        chat_type_to_peer_type,
        parse_chat_id,
        peer_id_to_chat_id,
    )

    # Function tests
    assert chat_id_to_peer_id("123456|1") == 123456
    assert chat_id_to_peer_id("987654|2") == 987654
    assert chat_id_to_peer_id(123456) == 123456
    assert chat_id_to_peer_id("123456") == 123456

    user = User(42, username="alice")
    chat = Chat(99, 2, title="A group")
    assert chat_id_to_peer_id(user) == 42
    assert chat_id_to_peer_id(chat) == 99

    assert peer_id_to_chat_id(123456, 1) == "123456|1"
    assert peer_id_to_chat_id(987654, 2) == "987654|2"
    assert peer_id_to_chat_id(987654, "group") == "987654|2"
    assert peer_id_to_chat_id(987654, ChatType.CHANNEL) == "987654|3"
    assert peer_id_to_chat_id(987654, "bot") == "987654|4"

    assert parse_chat_id("987654|2") == (987654, 2)
    assert parse_chat_id(chat) == (99, 2)

    assert chat_type_to_peer_type(ChatType.SUPERGROUP) == 5
    assert chat_type_to_peer_type("channel") == 3

    # Client class & instance method tests
    assert Client.chat_id_to_peer_id("123456|1") == 123456
    assert Client.peer_id_to_chat_id(123456, "private") == "123456|1"
    assert Client.parse_chat_id("123456|1") == (123456, 1)

    app = Client("dummy_session")
    assert app.chat_id_to_peer_id("555|3") == 555
    assert app.peer_id_to_chat_id(555, 3) == "555|3"
    assert app.parse_chat_id("555|3") == (555, 3)


from __future__ import annotations

import ast
import re
from pathlib import Path

from bale.proto import decode_message, encode_message


def test_codec_preserves_bytes_int64_and_nested_messages() -> None:
    payload = {
        "phone_number": 989121234567,
        "app_id": 4,
        "api_key": "secret",
        "device_hash": "device",
        "device_title": "Python",
        "send_code_type": 1,
        "options": b"\x00\x01",
    }

    encoded = encode_message("request.StartPhoneAuth", payload)
    decoded = decode_message("request.StartPhoneAuth", encoded)

    assert decoded["phone_number"] == 989121234567
    assert decoded["options"] == b"\x00\x01"


def test_codec_uses_enum_names_when_decoding() -> None:
    encoded = encode_message(
        "request.ReportInappropriateContent",
        {
            "report_body": {
                "kind": 5,
                "peer_report": {
                    "source": 1,
                    "peer": {"id": 10, "type": 1},
                },
            }
        },
    )

    decoded = decode_message("request.ReportInappropriateContent", encoded)

    assert decoded["report_body"]["kind"] == "REPORT_KIND_SPAM"
    assert decoded["report_body"]["peer_report"]["source"] == ("PEER_SOURCE_DIALOGS")


def test_unknown_proto_type_has_clear_error() -> None:
    try:
        encode_message("request.DoesNotExist", {})
    except LookupError as error:
        assert "request.DoesNotExist" in str(error)
    else:
        raise AssertionError("LookupError was not raised")


def test_recorded_call_and_inline_callback_protos_round_trip() -> None:
    callback = {
        "peer": {"id": 10, "type": 3},
        "message_id": {"date": 20, "rid": 30, "seq": 40},
        "data": {"value": "button-data"},
    }
    assert (
        decode_message(
            "request.SendInlineCallback",
            encode_message("request.SendInlineCallback", callback),
        )
        == callback
    )

    response = {
        "group_call": {
            "id": 99,
            "room": "room",
            "token": "token",
            "mode": "CALL_MODE_GROUP",
            "link": "https://example.test/call",
            "title": "Team call",
        },
        "link_expiration_period": 3600,
    }
    assert (
        decode_message(
            "response.GenerateCallLink",
            encode_message("response.GenerateCallLink", response),
        )
        == response
    )


def test_recorded_bulk_reaction_and_view_responses_round_trip() -> None:
    reactions = {
        "containers": [
            {
                "rid": 10,
                "date": 20,
                "reactions": [
                    {
                        "users": [1, 2],
                        "code": "👍",
                        "cardinality": {"value": 2},
                    }
                ],
            }
        ]
    }
    views = {
        "containers": [
            {
                "message_id": {"rid": 10, "date": 20},
                "views": {"value": 50},
            }
        ]
    }

    for type_name, payload in (
        ("response.GetMessagesReactions", reactions),
        ("response.GetMessagesViews", views),
    ):
        assert decode_message(type_name, encode_message(type_name, payload)) == payload


def test_current_web_file_and_config_response_shapes_round_trip() -> None:
    file_urls = {
        "file_urls": [
            {"file_id": 2**63 - 1, "url": "https://cdn.example/one"},
            {"file_id": 7, "unsigned_url": "https://cdn.example/two"},
        ]
    }
    parameters = {"parameters": [{"key": "upload.chunk", "value": "1048576"}]}

    assert (
        decode_message(
            "response.GetNasimFileUrls",
            encode_message("response.GetNasimFileUrls", file_urls),
        )
        == file_urls
    )
    assert (
        decode_message(
            "response.GetParameters",
            encode_message("response.GetParameters", parameters),
        )
        == parameters
    )


def test_current_web_user_profile_contact_and_privacy_shapes_round_trip() -> None:
    profile = {
        "full_user": {
            "id": 7,
            "access_hash": -(2**63),
            "name": "Seven",
            "local_name": {"value": "Local"},
            "contact_info": [
                {
                    "long_value": {"value": 989121234567},
                    "title": {"value": "mobile"},
                }
            ],
            "bot_commands": [{"slash_command": "start", "description": "Start"}],
            "preferred_languages": ["fa", "en"],
            "privacy_bar_mode": "PRIVACY_MODE_SPAM",
        }
    }
    contacts = {
        "users": [{"id": 7, "access_hash": 2**63 - 1, "name": "Seven"}],
        "user_peers": [{"uid": 7, "access_hash": -(2**63)}],
    }
    privacy = {
        "privacy": {
            "invite_privacy": 1,
            "presence_privacy": 2,
            "money_transfer_privacy": 3,
        }
    }

    for type_name, payload in (
        ("response.GetFullUser", profile),
        ("response.GetContacts", contacts),
        ("response.GetUserFullPrivacy", privacy),
    ):
        assert decode_message(type_name, encode_message(type_name, payload)) == payload

    preferred_languages = {"preferred_languages": ["fa", "en"]}
    assert (
        decode_message(
            "request.EditMyPreferredLanguages",
            encode_message("request.EditMyPreferredLanguages", preferred_languages),
        )
        == preferred_languages
    )


def test_every_protobuf_type_referenced_by_runtime_code_exists() -> None:
    source_root = Path(__file__).parents[1] / "src" / "bale"
    type_names: set[str] = set()
    for path in source_root.rglob("*.py"):
        if path.name.endswith("_pb2.py"):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
                continue
            if re.fullmatch(r"(?:request|response)\.[A-Za-z][A-Za-z0-9]*", node.value):
                type_names.add(node.value)

    assert type_names
    for type_name in sorted(type_names):
        encoded = encode_message(type_name, {})
        assert decode_message(type_name, encoded) == {}

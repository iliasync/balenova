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

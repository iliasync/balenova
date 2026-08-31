from __future__ import annotations

import json

import pytest

from bale.proto import encode_message
from bale.protocol import ProtocolRecorder
from bale.research import OfficialWebCapture


def events(recorder: ProtocolRecorder) -> list[dict]:
    return [
        json.loads(line)
        for line in (recorder.path / "events.jsonl").read_text().splitlines()
    ]


@pytest.mark.asyncio
async def test_official_capture_correlates_outbound_rpc_and_response(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    capture = OfficialWebCapture(recorder)
    nested_request = encode_message(
        "request.SendMessage",
        {
            "peer": {"id": 10, "type": 1},
            "rid": 11,
            "message": {"text_message": {"text": "hello"}},
        },
    )
    outbound = encode_message(
        "request.Request",
        {
            "ws_request": {
                "service_name": "bale.messaging.v2.Messaging",
                "method": "SendMessage",
                "payload": nested_request,
                "index": 7,
            }
        },
    )

    await capture.websocket_frame("outbound", outbound, url="wss://next-ws.bale.ai/ws/")

    nested_response = encode_message("response.DefaultResponse", {"seq": 2, "date": 3})
    inbound = encode_message(
        "response.Response",
        {"ws_response": {"index": 7, "response": nested_response}},
    )
    await capture.websocket_frame("inbound", inbound, url="wss://next-ws.bale.ai/ws/")

    captured = events(recorder)
    assert captured[0]["kind"] == "official_rpc_request"
    assert captured[0]["type"] == "request.SendMessage"
    assert captured[0]["service"] == "bale.messaging.v2.Messaging"
    assert captured[0]["payload"]["message"]["text_message"]["text"] == "hello"
    assert captured[1]["kind"] == "official_rpc_response"
    assert captured[1]["method"] == "SendMessage"
    assert captured[1]["details"]["index"] == 7


@pytest.mark.asyncio
async def test_official_capture_keeps_unknown_outbound_method_bytes(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    capture = OfficialWebCapture(recorder)
    unknown_payload = b"\x08\x96\x01"
    outbound = encode_message(
        "request.Request",
        {
            "ws_request": {
                "service_name": "bale.buttons.v1.Buttons",
                "method": "ClickButton",
                "payload": unknown_payload,
                "index": 99,
            }
        },
    )

    await capture.websocket_frame("outbound", outbound, url="wss://next-ws.bale.ai/ws/")

    event = events(recorder)[0]
    assert event["method"] == "ClickButton"
    assert "type" not in event
    assert (recorder.path / event["raw_file"]).read_bytes() == unknown_payload


@pytest.mark.asyncio
async def test_official_capture_rejects_non_rpc_envelope_metadata(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    capture = OfficialWebCapture(recorder)
    signaling_frame = encode_message(
        "request.Request",
        {
            "ws_request": {
                "service_name": "offer/v=0\r\na=ice-pwd:private-value",
                "method": "candidate:1 1 UDP",
                "payload": b"voice-signaling",
                "index": 5,
            }
        },
    )

    await capture.websocket_frame(
        "outbound", signaling_frame, url="wss://next-ws.bale.ai/ws/"
    )

    event = events(recorder)[0]
    assert event["kind"] == "official_unknown_frame"
    assert "service" not in event
    assert "method" not in event


@pytest.mark.asyncio
async def test_official_grpc_capture_unframes_body(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    capture = OfficialWebCapture(recorder)
    payload = b"\x08\x01"
    framed = b"\x00" + len(payload).to_bytes(4, "big") + payload

    await capture.grpc_frame(
        "outbound",
        framed,
        url="https://next-ws.bale.ai/bale.example.v1.Example/DoThing",
    )

    event = events(recorder)[0]
    assert event["service"] == "bale.example.v1.Example"
    assert event["method"] == "DoThing"
    assert (recorder.path / event["raw_file"]).read_bytes() == payload

from __future__ import annotations

import asyncio
import json
import os

import pytest

from bale.proto import encode_message
from bale.protocol import ProtocolRecorder
from bale.tools.proto import (
    build_inventory,
    build_trace_report,
    diff_inventories,
    replay_trace,
)


@pytest.mark.asyncio
async def test_recorder_redacts_auth_and_omits_raw_frame(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)

    await recorder.record(
        transport="grpc-web",
        direction="outbound",
        kind="rpc_request",
        type_name="request.ValidateCode",
        service="bale.auth.v1.Auth",
        method="ValidateCode",
        payload={
            "phone_number": 989121234567,
            "code": "12345",
            "nested": {"token": "secret"},
        },
        raw=b"sensitive-wire-data",
    )

    event = json.loads((recorder.path / "events.jsonl").read_text().strip())
    assert event["payload"]["phone_number"] == "<redacted>"
    assert event["payload"]["code"] == "<redacted>"
    assert event["payload"]["nested"]["token"] == "<redacted>"
    assert event["raw_omitted"] == "authentication event"
    assert "raw_file" not in event
    assert list((recorder.path / "frames").iterdir()) == []


@pytest.mark.asyncio
async def test_recorder_stores_non_auth_frames_privately_and_in_order(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)

    await asyncio.gather(
        *(
            recorder.record(
                transport="websocket",
                direction="inbound",
                kind="rpc_response",
                type_name="response.DefaultResponse",
                raw=encode_message("response.DefaultResponse", {"seq": index}),
            )
            for index in range(5)
        )
    )

    events = [
        json.loads(line)
        for line in (recorder.path / "events.jsonl").read_text().splitlines()
    ]
    assert [event["sequence"] for event in events] == [1, 2, 3, 4, 5]
    assert all(event.get("raw_file") for event in events)
    assert os.stat(recorder.path).st_mode & 0o777 == 0o700
    assert os.stat(recorder.path / "events.jsonl").st_mode & 0o777 == 0o600

    report = build_trace_report(recorder.path)
    assert report["events"] == 5
    assert report["by_kind"] == {"rpc_response": 5}

    replay = replay_trace(recorder.path)
    assert [item["payload"].get("seq", 0) for item in replay["decoded"]] == [
        0,
        1,
        2,
        3,
        4,
    ]


@pytest.mark.asyncio
async def test_recorder_strips_url_credentials_query_and_fragment(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)

    await recorder.record(
        transport="websocket",
        direction="outbound",
        kind="connection",
        details={"url": "wss://user:pass@example.test/ws?access_token=secret#fragment"},
    )

    event = json.loads((recorder.path / "events.jsonl").read_text().strip())
    assert event["details"]["url"] == "wss://example.test/ws"
    assert "secret" not in json.dumps(event)


@pytest.mark.asyncio
async def test_trace_report_rejects_non_rpc_metadata(tmp_path) -> None:
    recorder = ProtocolRecorder(tmp_path)
    await recorder.record(
        transport="official-websocket",
        direction="outbound",
        kind="official_rpc_request",
        service="offer/v=0\r\na=ice-pwd:private-value",
        method="candidate:1 1 UDP",
    )

    report = build_trace_report(recorder.path)

    assert report["rpc_methods"] == {}
    assert report["invalid_rpc_metadata"] == 1
    assert "private-value" not in json.dumps(report)


def test_inventory_contains_protocol_and_diff_detects_changes() -> None:
    before = build_inventory()
    assert "request.SendMessage" in before["messages"]
    assert "struct.ChatType" not in before["enums"]
    assert len(before["messages"]) > 50

    after = json.loads(json.dumps(before))
    after["messages"]["request.NewFeature"] = {"fields": []}
    difference = diff_inventories(before, after)

    assert difference["has_changes"] is True
    assert difference["messages"]["added"] == ["request.NewFeature"]

from __future__ import annotations

from typing import Any

import pytest
from google.protobuf.message import Message as ProtobufMessage

from bale import RECOVERED_METHODS, RECOVERED_RPCS, Client, RecoveredAPI


class FakeTypedClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, ProtobufMessage]] = []

    async def invoke_protobuf(
        self,
        service: str,
        method: str,
        request: ProtobufMessage,
        *,
        response_type: type[ProtobufMessage] | None = None,
    ) -> ProtobufMessage | bytes:
        self.calls.append((service, method, request))
        return response_type() if response_type else b""


def test_recovered_registry_contains_all_new_web_rpcs() -> None:
    assert len(RECOVERED_METHODS) == 80
    assert len(RECOVERED_RPCS) == 80
    assert len({service for service, _method in RECOVERED_RPCS}) == 12


@pytest.mark.asyncio
async def test_every_recovered_rpc_is_callable() -> None:
    client = FakeTypedClient()
    api = RecoveredAPI(client)

    for service, method in RECOVERED_RPCS:
        response = await api.call(service, method)
        assert isinstance(response, ProtobufMessage)

    assert [(service, method) for service, method, _ in client.calls] == list(
        RECOVERED_RPCS
    )


@pytest.mark.asyncio
async def test_recovered_service_supports_nested_keyword_fields() -> None:
    client = FakeTypedClient()
    api = RecoveredAPI(client)

    await api.groups.SetSlowMode(
        group={"groupId": 42, "accessHash": 1},
        seconds={"value": 30},
    )

    request = client.calls[-1][2]
    assert request.group.groupId == 42
    assert request.group.accessHash == 1
    assert request.seconds.value == 30


@pytest.mark.asyncio
async def test_high_level_recovered_convenience_methods(monkeypatch) -> None:
    client = Client("42:account-token")
    calls: list[tuple[str, dict[str, Any]]] = []

    async def capture(
        service: str, method: str, **fields: Any
    ) -> ProtobufMessage:
        calls.append((method, fields))
        return next(iter(RECOVERED_METHODS.values()))[1]()

    monkeypatch.setattr(client.recovered, "call", capture)

    await client.set_group_slow_mode("123|2", 45)
    await client.set_group_sign_messages("123|2", True)

    assert calls == [
        (
            "SetSlowMode",
            {
                "group": {"groupId": 123, "accessHash": 1},
                "seconds": {"value": 45},
            },
        ),
        (
            "SetSignMessages",
            {
                "groupPeer": {"groupId": 123, "accessHash": 1},
                "signMessages": True,
            },
        ),
    ]

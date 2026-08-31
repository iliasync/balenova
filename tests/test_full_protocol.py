from __future__ import annotations

import pytest
from google.protobuf.message import Message as ProtobufMessage

from bale import METHODS as PUBLIC_METHODS
from bale import BaleClient, Client, pb
from bale.full import ALL_RPCS, SERVICE_CLASSES, FullAPI, bale_pb2
from bale.full.bale_methods import METHODS


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
        return response_type() if response_type is not None else b""


class FakeRawGrpc:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, bytes, str | None]] = []

    async def request_raw(
        self,
        service: str,
        method: str,
        payload: bytes,
        *,
        access_token: str | None = None,
    ) -> bytes:
        self.calls.append((service, method, payload, access_token))
        return bale_pb2.GetMyGroupsResponse().SerializeToString()


def test_complete_protocol_registry_has_every_recovered_rpc() -> None:
    assert len(SERVICE_CLASSES) == 52
    assert len(ALL_RPCS) == 607
    assert len(METHODS) == 607
    assert len(bale_pb2.DESCRIPTOR.message_types_by_name) == 1715
    assert len(bale_pb2.DESCRIPTOR.services_by_name) == 44
    assert len(set(ALL_RPCS)) == len(ALL_RPCS)
    assert set(ALL_RPCS) == set(METHODS)


@pytest.mark.asyncio
async def test_every_complete_protocol_wrapper_builds_and_invokes() -> None:
    client = FakeTypedClient()
    api = FullAPI(client)
    services = {
        service_class.SERVICE: getattr(api, name)
        for name, service_class in SERVICE_CLASSES.items()
    }

    unary_rpcs = [
        pair
        for pair in ALL_RPCS
        if pair
        != ("bale.maviz.v1.MavizStream", "SubscribeToUpdates")
    ]
    for service, method in unary_rpcs:
        response = await getattr(services[service], method)()
        assert isinstance(response, ProtobufMessage)

    assert [(service, method) for service, method, _request in client.calls] == list(
        unary_rpcs
    )
    with pytest.raises(NotImplementedError, match="server-streaming"):
        await api.maviz_stream.SubscribeToUpdates()


@pytest.mark.asyncio
async def test_complete_api_accepts_keyword_fields_and_typed_requests() -> None:
    client = FakeTypedClient()
    api = FullAPI(client)

    await api.groups.GetMyGroups(mode=3, isOwner=True)
    request = bale_pb2.GetMyGroupsRequest(mode=4, isOwner=False)
    await api.groups.GetMyGroups(request)

    first = client.calls[0][2]
    second = client.calls[1][2]
    assert isinstance(first, bale_pb2.GetMyGroupsRequest)
    assert first.mode == 3
    assert first.isOwner is True
    assert second is request

    with pytest.raises(TypeError, match="either a request message or field kwargs"):
        await api.groups.GetMyGroups(request, mode=5)


def test_complete_api_introspection() -> None:
    api = FullAPI(FakeTypedClient())

    assert "groups" in api.services
    assert "meet" in api.services
    assert "search" in api.services
    assert api.has_rpc("bale.groups.v1.Groups", "GetMyGroups")
    assert not api.has_rpc("bale.groups.v1.Groups", "DoesNotExist")


def test_client_exposes_reference_compatible_service_namespaces() -> None:
    client = Client("42:jwt")

    assert client.groups is client.api.groups
    assert client.messaging is client.api.messaging
    assert client.meet is client.api.meet
    assert client.search is client.api.search
    assert client.story is client.api.story
    assert BaleClient is Client
    assert pb is bale_pb2
    assert PUBLIC_METHODS is METHODS


@pytest.mark.asyncio
async def test_client_complete_namespace_uses_existing_raw_transport(tmp_path) -> None:
    grpc = FakeRawGrpc()
    client = Client(
        "42:jwt-token",
        session_dir=tmp_path,
        grpc=grpc,  # type: ignore[arg-type]
    )

    response = await client.groups.GetMyGroups(mode=2, isOwner=True)

    assert isinstance(response, bale_pb2.GetMyGroupsResponse)
    service, method, payload, token = grpc.calls[0]
    request = bale_pb2.GetMyGroupsRequest.FromString(payload)
    assert (service, method, token) == (
        "bale.groups.v1.Groups",
        "GetMyGroups",
        "jwt-token",
    )
    assert request.mode == 2
    assert request.isOwner is True

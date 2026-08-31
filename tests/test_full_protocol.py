from __future__ import annotations

import pytest
from google.protobuf.message import Message as ProtobufMessage

from bale import METHODS as PUBLIC_METHODS
from bale import BaleClient, BaleRpcError, Client, RpcStatus, pb
from bale.api import ProtocolAPI
from bale.methods import METHODS
from bale.proto import request_pb2, response_pb2, struct_pb2
from bale.services import ALL_RPCS, SERVICE_CLASSES


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

    async def stream_protobuf(
        self,
        service: str,
        method: str,
        request: ProtobufMessage,
        *,
        response_type: type[ProtobufMessage],
        timeout: float | None = None,
    ):  # type: ignore[no-untyped-def]
        del timeout
        self.calls.append((service, method, request))
        yield response_type()


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
        return response_pb2.WebGetMyGroupsResponse().SerializeToString()


def test_complete_protocol_registry_has_every_recovered_rpc() -> None:
    assert len(SERVICE_CLASSES) == 52
    assert len(ALL_RPCS) == 610
    assert len(METHODS) == 610
    assert len(struct_pb2.DESCRIPTOR.message_types_by_name) == 830
    assert len(request_pb2.DESCRIPTOR.message_types_by_name) == 742
    assert len(response_pb2.DESCRIPTOR.message_types_by_name) == 507
    assert len(response_pb2.DESCRIPTOR.services_by_name) == 52
    assert sum(
        len(service.methods)
        for service in response_pb2.DESCRIPTOR.services_by_name.values()
    ) == 610
    assert len(set(ALL_RPCS)) == len(ALL_RPCS)
    assert set(ALL_RPCS) == set(METHODS)

    primary_modules = {
        request_type.__module__
        for request_type, response_type in METHODS.values()
        if request_type is not None
    } | {
        response_type.__module__
        for request_type, response_type in METHODS.values()
        if response_type is not None
    }
    assert primary_modules <= {
        "request_pb2",
        "response_pb2",
        "struct_pb2",
    }


@pytest.mark.asyncio
async def test_every_complete_protocol_wrapper_builds_and_invokes() -> None:
    client = FakeTypedClient()
    api = ProtocolAPI(client)
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
    streamed = [item async for item in api.maviz_stream.SubscribeToUpdates()]
    assert len(streamed) == 1
    assert isinstance(streamed[0], response_pb2.WebSubscribeToUpdatesResponse)
    assert client.calls[-1][:2] == (
        "bale.maviz.v1.MavizStream",
        "SubscribeToUpdates",
    )


@pytest.mark.asyncio
async def test_complete_api_accepts_keyword_fields_and_typed_requests() -> None:
    client = FakeTypedClient()
    api = ProtocolAPI(client)

    await api.groups.GetMyGroups(mode=3, isOwner=True)
    request = request_pb2.WebGetMyGroupsRequest(mode=4, isOwner=False)
    await api.groups.GetMyGroups(request)

    first = client.calls[0][2]
    second = client.calls[1][2]
    assert isinstance(first, request_pb2.WebGetMyGroupsRequest)
    assert first.mode == 3
    assert first.isOwner is True
    assert second is request

    with pytest.raises(TypeError, match="either a request message or field kwargs"):
        await api.groups.GetMyGroups(request, mode=5)


@pytest.mark.asyncio
async def test_newly_recovered_web_rpcs_build_typed_requests() -> None:
    client = FakeTypedClient()
    api = ProtocolAPI(client)

    upload_limits = await api.files.GetUploadLimits()
    await api.auth.ChangeLanguage(language=1)
    await api.fanoos.SendBatch(
        events=[
            {
                "eventName": "balenova_test",
                "items": {
                    "items": [
                        {
                            "key": "source",
                            "value": {"string_value": "tests"},
                        }
                    ]
                },
                "date": 1_788_000_000_000,
            }
        ]
    )

    assert isinstance(upload_limits, response_pb2.WebGetUploadLimitsResponse)
    assert isinstance(client.calls[0][2], request_pb2.WebGetUploadLimitsRequest)
    assert client.calls[1][2].language == 1
    event = client.calls[2][2].events[0]
    assert event.eventName == "balenova_test"
    assert event.items.items[0].key == "source"


def test_complete_api_introspection() -> None:
    api = ProtocolAPI(FakeTypedClient())

    assert "groups" in api.services
    assert "meet" in api.services
    assert "search" in api.services
    assert api.has_rpc("bale.groups.v1.Groups", "GetMyGroups")
    assert not api.has_rpc("bale.groups.v1.Groups", "DoesNotExist")


def test_complete_error_proto_builds_structured_rpc_exception() -> None:
    proto_error = pb.WebError(
        code=8,
        message="user_rate_limited retry_after 2",
    )

    error = BaleRpcError.from_proto(proto_error, reason="service/method")

    assert error.status is RpcStatus.RESOURCE_EXHAUSTED
    assert error.is_rate_limited
    assert error.retry_after == 2
    assert error.reason == "service/method"


def test_client_exposes_reference_compatible_service_namespaces() -> None:
    client = Client("42:jwt")

    assert client.groups is client.api.groups
    assert client.messaging is client.api.messaging
    assert client.meet is client.api.meet
    assert client.search is client.api.search
    assert client.story is client.api.story
    assert BaleClient is Client
    assert pb.WebGetMyGroupsRequest is request_pb2.WebGetMyGroupsRequest
    assert pb.WebGetMyGroupsResponse is response_pb2.WebGetMyGroupsResponse
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

    assert isinstance(response, response_pb2.WebGetMyGroupsResponse)
    service, method, payload, token = grpc.calls[0]
    request = request_pb2.WebGetMyGroupsRequest.FromString(payload)
    assert (service, method, token) == (
        "bale.groups.v1.Groups",
        "GetMyGroups",
        "jwt-token",
    )
    assert request.mode == 2
    assert request.isOwner is True

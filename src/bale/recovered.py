"""Callable namespace for RPCs recovered from the latest official web build."""

from __future__ import annotations

import asyncio
import re
from collections.abc import Mapping
from typing import Any

from google.protobuf.message import Message as ProtobufMessage

from bale.recovered_methods import RECOVERED_METHODS
from bale.rpc import build_request

RECOVERED_RPCS = tuple(RECOVERED_METHODS)


def _snake(value: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()


class RecoveredService:
    """One client-bound service containing newly recovered RPCs."""

    def __init__(
        self,
        client: Any,
        service: str,
        methods: Mapping[str, tuple[type[ProtobufMessage], type[ProtobufMessage]]],
    ) -> None:
        self._client = client
        self.service = service
        self._methods = dict(methods)

    @property
    def methods(self) -> tuple[str, ...]:
        return tuple(self._methods)

    async def call(
        self,
        method: str,
        request: ProtobufMessage | None = None,
        /,
        *,
        timeout: float = 10.0,
        **fields: Any,
    ) -> ProtobufMessage:
        try:
            request_type, response_type = self._methods[method]
        except KeyError as error:
            raise LookupError(
                f"unknown recovered RPC {self.service}.{method}"
            ) from error
        message = build_request(request_type, request, fields)
        result = await asyncio.wait_for(
            self._client.invoke_protobuf(
                self.service, method, message, response_type=response_type
            ),
            timeout=timeout,
        )
        if not isinstance(result, ProtobufMessage):
            raise TypeError("recovered RPC returned undecoded bytes")
        return result

    def __getattr__(self, method: str) -> Any:
        if method not in self._methods:
            raise AttributeError(method)

        async def invoke(
            request: ProtobufMessage | None = None,
            /,
            *,
            _timeout: float = 10.0,
            **fields: Any,
        ) -> ProtobufMessage:
            return await self.call(
                method, request, timeout=_timeout, **fields
            )

        invoke.__name__ = method
        invoke.__doc__ = f"Invoke recovered RPC {self.service}.{method}."
        return invoke


class RecoveredAPI:
    """Discoverable access to all RPCs added by the audited web build."""

    def __init__(self, client: Any) -> None:
        grouped: dict[
            str, dict[str, tuple[type[ProtobufMessage], type[ProtobufMessage]]]
        ] = {}
        for (service, method), types in RECOVERED_METHODS.items():
            grouped.setdefault(service, {})[method] = types
        self._services: dict[str, RecoveredService] = {}
        for service, methods in grouped.items():
            namespace = RecoveredService(client, service, methods)
            alias = _snake(service.rsplit(".", 1)[-1])
            self._services[service] = namespace
            setattr(self, alias, namespace)

    @property
    def services(self) -> tuple[str, ...]:
        return tuple(self._services)

    @property
    def rpcs(self) -> tuple[tuple[str, str], ...]:
        return RECOVERED_RPCS

    def has_rpc(self, service: str, method: str) -> bool:
        return (service, method) in RECOVERED_METHODS

    async def call(
        self,
        service: str,
        method: str,
        request: ProtobufMessage | None = None,
        /,
        *,
        timeout: float = 10.0,
        **fields: Any,
    ) -> ProtobufMessage:
        try:
            namespace = self._services[service]
        except KeyError as error:
            raise LookupError(f"unknown recovered Bale service {service}") from error
        return await namespace.call(
            method, request, timeout=timeout, **fields
        )


__all__ = [
    "RECOVERED_METHODS",
    "RECOVERED_RPCS",
    "RecoveredAPI",
    "RecoveredService",
]

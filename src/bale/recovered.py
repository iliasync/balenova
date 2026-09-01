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
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.lower()


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

    def _resolve_method(self, method: str) -> str:
        if method in self._methods:
            return method
        actual_method = next(
            (candidate for candidate in self._methods if _snake(candidate) == method),
            "",
        )
        if not actual_method:
            raise LookupError(f"unknown recovered RPC {self.service}.{method}")
        return actual_method

    async def call(
        self,
        method: str,
        request: ProtobufMessage | None = None,
        /,
        *,
        timeout: float = 10.0,
        **fields: Any,
    ) -> ProtobufMessage:
        actual_method = self._resolve_method(method)
        try:
            request_type, response_type = self._methods[actual_method]
        except KeyError as error:
            raise LookupError(
                f"unknown recovered RPC {self.service}.{method}"
            ) from error
        message = build_request(request_type, request, fields)
        result = await asyncio.wait_for(
            self._client.invoke_protobuf(
                self.service, actual_method, message, response_type=response_type
            ),
            timeout=timeout,
        )
        if not isinstance(result, ProtobufMessage):
            raise TypeError("recovered RPC returned undecoded bytes")
        return result

    def __getattr__(self, method: str) -> Any:
        try:
            actual_method = self._resolve_method(method)
        except LookupError:
            raise AttributeError(method) from None

        async def invoke(
            request: ProtobufMessage | None = None,
            /,
            *,
            _timeout: float = 10.0,
            **fields: Any,
        ) -> ProtobufMessage:
            return await self.call(
                actual_method, request, timeout=_timeout, **fields
            )

        invoke.__name__ = method
        invoke.__doc__ = f"Invoke recovered RPC {self.service}.{method}."
        return invoke

    def __dir__(self) -> list[str]:
        names = set(super().__dir__())
        names.update(_snake(method) for method in self._methods)
        return sorted(names)


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
        namespace = self._services.get(service)
        if namespace is None:
            short = service.rsplit(".", 1)[-1]
            namespace = next(
                (
                    candidate
                    for full_name, candidate in self._services.items()
                    if _snake(full_name.rsplit(".", 1)[-1]) == _snake(short)
                ),
                None,
            )
        if namespace is None:
            raise LookupError(f"unknown recovered Bale service {service}")
        return await namespace.call(
            method, request, timeout=timeout, **fields
        )


__all__ = [
    "RECOVERED_METHODS",
    "RECOVERED_RPCS",
    "RecoveredAPI",
    "RecoveredService",
]

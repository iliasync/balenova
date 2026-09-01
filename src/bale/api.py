"""Complete typed Bale Web RPC namespace backed by the main protobuf module."""

from __future__ import annotations

from typing import Any

from bale.recovered import RECOVERED_RPCS, RecoveredAPI
from bale.rpc import _snake_case
from bale.services import ALL_RPCS, SERVICE_CLASSES


class ProtocolAPI:
    """Expose every known Bale service and RPC on one client-bound namespace."""

    def __init__(self, client: Any) -> None:
        self._client = client
        for name, service_class in SERVICE_CLASSES.items():
            setattr(self, name, service_class(client))
        self.recovered = RecoveredAPI(client)

    @property
    def services(self) -> tuple[str, ...]:
        return tuple(SERVICE_CLASSES)

    @property
    def rpcs(self) -> tuple[tuple[str, str], ...]:
        return tuple(ALL_RPCS)

    @property
    def all_rpcs(self) -> tuple[tuple[str, str], ...]:
        """Return primary and recovered RPCs in one discoverable collection."""
        return tuple(dict.fromkeys((*ALL_RPCS, *RECOVERED_RPCS)))

    @property
    def all_services(self) -> tuple[str, ...]:
        """Return every fully-qualified primary and recovered service name."""
        return tuple(dict.fromkeys(service for service, _method in self.all_rpcs))

    def has_rpc(self, service: str, method: str) -> bool:
        for candidate_service, candidate_method in self.all_rpcs:
            short_service = _snake_case(candidate_service.rsplit(".", 1)[-1])
            if service not in {candidate_service, short_service}:
                continue
            if method in {candidate_method, _snake_case(candidate_method)}:
                return True
        return False

    async def call(
        self,
        service: str,
        method: str,
        request: Any | None = None,
        /,
        *,
        timeout: float = 10.0,
        **fields: Any,
    ) -> Any:
        """Call a primary or recovered RPC using a short, uniform API.

        ``service`` accepts either a namespace (``"groups"``) or a fully
        qualified service name.  Generated CamelCase method names and their
        snake_case aliases are both accepted.
        """
        namespace = None
        for key, service_class in SERVICE_CLASSES.items():
            if service == key or service == service_class.SERVICE:
                namespace = getattr(self, key)
                break
        if namespace is not None:
            try:
                operation = getattr(namespace, method)
            except AttributeError:
                operation = None
            if operation is not None:
                return await operation(request, _timeout=timeout, **fields)

        try:
            return await self.recovered.call(
                service, method, request, timeout=timeout, **fields
            )
        except LookupError as error:
            raise LookupError(f"unknown Bale RPC {service}.{method}") from error


__all__ = ["ALL_RPCS", "SERVICE_CLASSES", "ProtocolAPI"]

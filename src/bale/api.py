"""Complete typed Bale Web RPC namespace backed by the main protobuf module."""

from __future__ import annotations

from typing import Any

from bale.services import ALL_RPCS, SERVICE_CLASSES


class ProtocolAPI:
    """Expose every known Bale service and RPC on one client-bound namespace."""

    def __init__(self, client: Any) -> None:
        self._client = client
        for name, service_class in SERVICE_CLASSES.items():
            setattr(self, name, service_class(client))

    @property
    def services(self) -> tuple[str, ...]:
        return tuple(SERVICE_CLASSES)

    @property
    def rpcs(self) -> tuple[tuple[str, str], ...]:
        return tuple(ALL_RPCS)

    def has_rpc(self, service: str, method: str) -> bool:
        return (service, method) in ALL_RPCS


__all__ = ["ALL_RPCS", "SERVICE_CLASSES", "ProtocolAPI"]

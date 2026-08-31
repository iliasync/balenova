"""Complete typed Bale Web RPC surface.

The generated protocol and service wrappers are kept separate from BaleNova's
friendly high-level API. Access them through ``client.api``.
"""

from __future__ import annotations

from typing import Any

from bale.full import bale_ext_pb2, bale_pb2
from bale.full.services import ALL_RPCS, SERVICE_CLASSES


class FullAPI:
    """Namespace exposing every recovered Bale Web service and RPC."""

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


__all__ = [
    "ALL_RPCS",
    "FullAPI",
    "SERVICE_CLASSES",
    "bale_ext_pb2",
    "bale_pb2",
]

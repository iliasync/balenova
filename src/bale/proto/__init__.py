"""Generated Bale protocol definitions and encoding helpers."""

from __future__ import annotations

from types import ModuleType
from typing import Any

from bale.proto import request_pb2, response_pb2, struct_pb2
from bale.proto.codec import decode_message, encode_message


class ProtocolSchema:
    """Unified view over the request, response and shared protobuf modules."""

    _modules: tuple[ModuleType, ...] = (request_pb2, response_pb2, struct_pb2)

    def __getattr__(self, name: str) -> Any:
        for module in self._modules:
            value = getattr(module, name, None)
            if value is not None:
                return value
        raise AttributeError(f"Unknown Bale protobuf type: {name}")

    def __dir__(self) -> list[str]:
        return sorted(
            {
                name
                for module in self._modules
                for name in dir(module)
                if not name.startswith("_")
            }
        )


schema = ProtocolSchema()

__all__ = ["ProtocolSchema", "decode_message", "encode_message", "schema"]

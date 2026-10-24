"""Base serialization and formatting primitives for Bale models."""

from __future__ import annotations

import base64
import json
from dataclasses import fields
from enum import Enum
from typing import TYPE_CHECKING, Any, cast

from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message as ProtoMessage

if TYPE_CHECKING:
    pass


class Serializable:
    """Convenience conversion helpers shared by public response models."""

    def to_dict(self, *, include_raw: bool = False) -> dict[str, Any]:
        return cast(dict[str, Any], model_to_dict(self, include_raw=include_raw))

    def to_json(self, *, include_raw: bool = False, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(include_raw=include_raw),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )

    def as_dict(self, *, include_raw: bool = False) -> dict[str, Any]:
        """Alias for :meth:`to_dict` with a discoverable Pythonic name."""
        return self.to_dict(include_raw=include_raw)

    def as_json(self, *, include_raw: bool = False, indent: int | None = 2) -> str:
        """Alias for :meth:`to_json` suitable for generic serializers."""
        return self.to_json(include_raw=include_raw, indent=indent)


def model_to_dict(value: Any, *, include_raw: bool = False) -> Any:
    """Convert a Bale model (including nested models) to JSON-safe values."""
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, ProtoMessage):
        return MessageToDict(
            value,
            preserving_proto_field_name=True,
            use_integers_for_enums=True,
        )
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("ascii")
    if isinstance(value, Serializable):
        result = {}
        for item in fields(cast(Any, value)):
            if not item.name.startswith("_") and (include_raw or item.name != "raw"):
                attr_val = getattr(value, item.name)
                result[item.name] = model_to_dict(attr_val, include_raw=include_raw)
        return result
    if isinstance(value, dict):
        return {
            str(key): model_to_dict(item, include_raw=include_raw)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple, set)):
        return [model_to_dict(item, include_raw=include_raw) for item in value]
    return value


def model_to_json(
    value: Any, *, include_raw: bool = False, indent: int | None = 2
) -> str:
    """Serialize a model or response value as readable JSON."""
    return json.dumps(
        model_to_dict(value, include_raw=include_raw),
        ensure_ascii=False,
        indent=indent,
        sort_keys=True,
    )

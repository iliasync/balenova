"""Conversion between Python values and generated protobuf messages."""

from __future__ import annotations

import base64
from collections.abc import Iterable, Mapping
from typing import Any, cast

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.json_format import ParseDict
from google.protobuf.message import Message
from google.protobuf.unknown_fields import UnknownFieldSet

from bale.proto import request_pb2, response_pb2, struct_pb2

_MODULES = {
    "request": request_pb2,
    "response": response_pb2,
    "struct": struct_pb2,
}


def _message_class(type_name: str) -> type[Message]:
    try:
        namespace, class_name = type_name.split(".", 1)
        module = _MODULES[namespace]
        value = getattr(module, class_name)
    except (KeyError, AttributeError, ValueError) as error:
        raise LookupError(f"Unknown Bale protobuf type: {type_name}") from error
    return value  # type: ignore[no-any-return]


def _json_safe(value: Any) -> Any:
    if isinstance(value, bytes | bytearray | memoryview):
        return base64.b64encode(bytes(value)).decode("ascii")
    if isinstance(value, Mapping):
        return {
            str(key): _json_safe(item)
            for key, item in value.items()
            if item is not None
        }
    if isinstance(value, list | tuple):
        return [_json_safe(item) for item in value]
    return value


def encode_message(type_name: str, payload: Mapping[str, Any]) -> bytes:
    """Encode a mapping as a named Bale protobuf message."""
    message = _message_class(type_name)()
    ParseDict(_json_safe(payload), message, ignore_unknown_fields=False)
    return message.SerializeToString()


def _scalar_value(field: FieldDescriptor, value: Any) -> Any:
    if field.type == FieldDescriptor.TYPE_BYTES:
        return bytes(value)
    if field.type == FieldDescriptor.TYPE_ENUM:
        assert field.enum_type is not None
        enum_value = field.enum_type.values_by_number.get(int(value))
        return enum_value.name if enum_value is not None else int(value)
    return value


def _message_to_dict(message: Message) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for field, value in message.ListFields():
        if field.is_repeated:
            if (
                field.message_type is not None
                and field.message_type.GetOptions().map_entry
            ):
                result[field.name] = dict(value)
            elif field.type == FieldDescriptor.TYPE_MESSAGE:
                result[field.name] = [_message_to_dict(item) for item in value]
            else:
                result[field.name] = [_scalar_value(field, item) for item in value]
        elif field.type == FieldDescriptor.TYPE_MESSAGE:
            result[field.name] = _message_to_dict(value)
        else:
            result[field.name] = _scalar_value(field, value)
    unknown = [
        {
            "number": field.field_number,
            "wire_type": field.wire_type,
            "data": bytes(field.data)
            if isinstance(field.data, bytes | bytearray | memoryview)
            else field.data,
        }
        for field in cast(Iterable[Any], UnknownFieldSet(message))
    ]
    if unknown:
        # Protobuf normally discards unknown fields when converted to a dict.
        # Retaining them is essential for an unofficial client: newly-added
        # Bale update variants remain observable before a named schema lands.
        result["_unknown_fields"] = unknown
    return result


def decode_message(type_name: str, payload: bytes) -> dict[str, Any]:
    """Decode a named Bale protobuf message into Python-native values."""
    message = _message_class(type_name)()
    message.ParseFromString(payload)
    return _message_to_dict(message)

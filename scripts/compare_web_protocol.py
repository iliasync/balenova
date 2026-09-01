"""Compare an extracted official Bale Web protocol with this library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from google.protobuf.descriptor import FieldDescriptor

from bale.methods import METHODS
from bale.recovered_methods import RECOVERED_METHODS

BUNDLED_METHODS = {**METHODS, **RECOVERED_METHODS}

_FIELD_TYPES = {
    FieldDescriptor.TYPE_DOUBLE: "double",
    FieldDescriptor.TYPE_FLOAT: "float",
    FieldDescriptor.TYPE_INT64: "int64",
    FieldDescriptor.TYPE_UINT64: "uint64",
    FieldDescriptor.TYPE_INT32: "int32",
    FieldDescriptor.TYPE_FIXED64: "fixed64",
    FieldDescriptor.TYPE_FIXED32: "fixed32",
    FieldDescriptor.TYPE_BOOL: "bool",
    FieldDescriptor.TYPE_STRING: "string",
    FieldDescriptor.TYPE_MESSAGE: "message",
    FieldDescriptor.TYPE_BYTES: "bytes",
    FieldDescriptor.TYPE_UINT32: "uint32",
    # Generated Bale codecs serialize enums through protobuf int32 methods.
    FieldDescriptor.TYPE_ENUM: "int32",
    FieldDescriptor.TYPE_SFIXED32: "sfixed32",
    FieldDescriptor.TYPE_SFIXED64: "sfixed64",
    FieldDescriptor.TYPE_SINT32: "sint32",
    FieldDescriptor.TYPE_SINT64: "sint64",
}


def _library_fields(message_type: Any) -> list[dict[str, Any]]:
    if message_type is None:
        return []
    result = []
    for field in message_type.DESCRIPTOR.fields:
        message = field.message_type
        result.append(
            {
                "number": field.number,
                "name": field.name,
                "repeated": field.is_repeated,
                "map": bool(message and message.GetOptions().map_entry),
                "type": _FIELD_TYPES[field.type],
                "message_type": message.full_name if message else None,
            }
        )
    return result


def _shape(fields: list[dict[str, Any]]) -> list[tuple[Any, ...]]:
    return [
        (
            field["number"],
            field["name"],
            field["repeated"],
            field.get("map", False),
            field["type"],
        )
        for field in fields
    ]


def compare(audit: dict[str, Any]) -> dict[str, Any]:
    current = {(item["service"], item["method"]): item for item in audit["methods"]}
    bundled = set(BUNDLED_METHODS)
    live = set(current)
    added = []
    for key in sorted(live - bundled):
        item = current[key]
        added.append(
            {
                "service": key[0],
                "method": key[1],
                "request_fields": item["request_fields"],
                "response_fields": item["response_fields"],
            }
        )

    removed = [
        {
            "service": service,
            "method": method,
            "request_type": getattr(
                BUNDLED_METHODS[(service, method)][0], "__name__", None
            ),
            "response_type": getattr(
                BUNDLED_METHODS[(service, method)][1], "__name__", None
            ),
        }
        for service, method in sorted(bundled - live)
    ]
    changed = []
    exact = 0
    request_changes = 0
    response_changes = 0
    for key in sorted(live & bundled):
        request_type, response_type = BUNDLED_METHODS[key]
        old_request = _library_fields(request_type)
        old_response = _library_fields(response_type)
        new_request = current[key]["request_fields"]
        new_response = current[key]["response_fields"]
        request_changed = _shape(old_request) != _shape(new_request)
        response_changed = _shape(old_response) != _shape(new_response)
        request_changes += request_changed
        response_changes += response_changed
        if not request_changed and not response_changed:
            exact += 1
            continue
        changed.append(
            {
                "service": key[0],
                "method": key[1],
                "request_changed": request_changed,
                "response_changed": response_changed,
                "library": {
                    "request_type": getattr(request_type, "__name__", None),
                    "request_fields": old_request,
                    "response_type": getattr(response_type, "__name__", None),
                    "response_fields": old_response,
                },
                "official_web": {
                    "request_codec": current[key]["request_codec"],
                    "request_fields": new_request,
                    "response_codec": current[key]["response_codec"],
                    "response_fields": new_response,
                },
            }
        )

    return {
        "format": "balenova-official-web-diff",
        "format_version": 1,
        "official_releases": audit.get("releases", []),
        "counts": {
            "official_services": audit["counts"]["services"],
            "official_methods": len(live),
            "official_codecs": audit["counts"]["codecs"],
            "official_codec_fields": audit["counts"]["codec_fields"],
            "library_services": len({service for service, _method in bundled}),
            "library_methods": len(bundled),
            "common_methods": len(live & bundled),
            "exact_common_methods": exact,
            "schema_changed_common_methods": len(changed),
            "request_schema_changes": request_changes,
            "response_schema_changes": response_changes,
            "added_methods": len(added),
            "removed_methods": len(removed),
        },
        "added": added,
        "removed": removed,
        "schema_changed": changed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    result = compare(audit)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()

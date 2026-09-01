"""Generate the MkDocs RPC reference from bundled protobuf descriptors."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from google.protobuf.descriptor import FieldDescriptor

from bale.methods import METHODS
from bale.recovered_methods import RECOVERED_METHODS

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "rpc-reference.md"

_SCALARS = {
    FieldDescriptor.TYPE_DOUBLE: "double",
    FieldDescriptor.TYPE_FLOAT: "float",
    FieldDescriptor.TYPE_INT64: "int64",
    FieldDescriptor.TYPE_UINT64: "uint64",
    FieldDescriptor.TYPE_INT32: "int32",
    FieldDescriptor.TYPE_FIXED64: "fixed64",
    FieldDescriptor.TYPE_FIXED32: "fixed32",
    FieldDescriptor.TYPE_BOOL: "bool",
    FieldDescriptor.TYPE_STRING: "string",
    FieldDescriptor.TYPE_BYTES: "bytes",
    FieldDescriptor.TYPE_UINT32: "uint32",
    FieldDescriptor.TYPE_ENUM: "enum",
    FieldDescriptor.TYPE_SFIXED32: "sfixed32",
    FieldDescriptor.TYPE_SFIXED64: "sfixed64",
    FieldDescriptor.TYPE_SINT32: "sint32",
    FieldDescriptor.TYPE_SINT64: "sint64",
}


def _fields(message: Any) -> str:
    values = []
    for field in message.DESCRIPTOR.fields:
        suffix = "[]" if field.is_repeated else ""
        kind = field.message_type.name if field.message_type else _SCALARS[field.type]
        values.append(f"`{field.name}: {kind}{suffix}`")
    return "، ".join(values) if values else "—"


def main() -> None:
    grouped: dict[str, list[tuple[str, Any, Any, str]]] = defaultdict(list)
    for (service, method), (request, response) in METHODS.items():
        grouped[service].append((method, request, response, "bundled"))
    for (service, method), (request, response) in RECOVERED_METHODS.items():
        grouped[service].append((method, request, response, "web 5.5.1"))

    lines = [
        "# مرجع کامل RPCها",
        "",
        f"این مرجع شامل {sum(map(len, grouped.values()))} ورودی registry است: "
        f"{len(METHODS)} متد قبلی و {len(RECOVERED_METHODS)} متد تازه.",
        "",
        "هفت متد قدیمی برای سازگاری نگه داشته شده‌اند؛ بنابراین تعداد registry "
        "از ۶۸۳ descriptor فعال build رسمی بیشتر است.",
        "",
    ]
    for service in sorted(grouped):
        lines.extend(
            [
                f"## `{service}`",
                "",
                "| متد | ورودی | خروجی | منبع |",
                "|---|---|---|---|",
            ]
        )
        for method, request, response, source in sorted(grouped[service]):
            lines.append(
                f"| `{method}` | {_fields(request)} | {_fields(response)} | "
                f"{source} |"
            )
        lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

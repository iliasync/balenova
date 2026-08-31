"""Inventory, diff, and trace reporting for Bale protobuf development."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
from collections import Counter
from importlib.resources import files
from pathlib import Path
from typing import Any

from google.protobuf import descriptor_pb2
from google.protobuf.descriptor import Descriptor, EnumDescriptor, FileDescriptor
from google.protobuf.message import DecodeError

from bale.proto import request_pb2, response_pb2, struct_pb2
from bale.proto.codec import decode_message

_FIELD_TYPE_NAMES = {
    int(value): name for name, value in descriptor_pb2.FieldDescriptorProto.Type.items()
}
_SERVICE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_.]{2,199}$")
_METHOD_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]{1,99}$")


def build_inventory() -> dict[str, Any]:
    """Return a deterministic inventory of every bundled protobuf definition."""
    descriptors = (
        struct_pb2.DESCRIPTOR,
        request_pb2.DESCRIPTOR,
        response_pb2.DESCRIPTOR,
    )
    messages: dict[str, Any] = {}
    enums: dict[str, Any] = {}
    for descriptor in descriptors:
        for message in descriptor.message_types_by_name.values():
            _collect_message(message, messages, enums)
        for enum in descriptor.enum_types_by_name.values():
            enums[enum.full_name] = _enum_inventory(enum)
    return {
        "format": "bale-async-proto-inventory",
        "format_version": 1,
        "sources": {
            descriptor.name: _source_hash(descriptor) for descriptor in descriptors
        },
        "messages": dict(sorted(messages.items())),
        "enums": dict(sorted(enums.items())),
    }


def diff_inventories(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    """Compare two inventory snapshots at message and enum level."""
    result: dict[str, Any] = {}
    for section in ("messages", "enums"):
        old_items = old.get(section, {})
        new_items = new.get(section, {})
        old_names, new_names = set(old_items), set(new_items)
        changed = {
            name: {"old": old_items[name], "new": new_items[name]}
            for name in sorted(old_names & new_names)
            if old_items[name] != new_items[name]
        }
        result[section] = {
            "added": sorted(new_names - old_names),
            "removed": sorted(old_names - new_names),
            "changed": changed,
        }
    result["has_changes"] = any(
        value[change]
        for section, value in result.items()
        if section != "has_changes"
        for change in ("added", "removed", "changed")
    )
    return result


def build_trace_report(trace_directory: str | Path) -> dict[str, Any]:
    """Summarize event types and observed RPC methods in a protocol trace."""
    trace_path = Path(trace_directory)
    event_counts: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()
    rpc_counts: Counter[str] = Counter()
    directions: Counter[str] = Counter()
    raw_omitted = 0
    invalid_rpc_metadata = 0
    event_file = trace_path / "events.jsonl"
    with event_file.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid trace JSON at line {line_number}: {error}"
                ) from error
            event_counts[str(event.get("kind", "unknown"))] += 1
            directions[str(event.get("direction", "unknown"))] += 1
            if event.get("type"):
                type_counts[str(event["type"])] += 1
            service = event.get("service")
            method = event.get("method")
            if service or method:
                if _valid_rpc_name(service, method):
                    rpc_counts[f"{service}/{method}"] += 1
                else:
                    invalid_rpc_metadata += 1
            raw_omitted += int("raw_omitted" in event)
    return {
        "trace": str(trace_path),
        "events": sum(event_counts.values()),
        "by_kind": dict(sorted(event_counts.items())),
        "by_direction": dict(sorted(directions.items())),
        "protobuf_types": dict(sorted(type_counts.items())),
        "rpc_methods": dict(sorted(rpc_counts.items())),
        "invalid_rpc_metadata": invalid_rpc_metadata,
        "authentication_raw_frames_omitted": raw_omitted,
    }


def _valid_rpc_name(service: Any, method: Any) -> bool:
    return (
        isinstance(service, str)
        and isinstance(method, str)
        and _SERVICE_PATTERN.fullmatch(service) is not None
        and _METHOD_PATTERN.fullmatch(method) is not None
    )


def replay_trace(trace_directory: str | Path) -> dict[str, Any]:
    """Decode all stored frames again using the currently installed schema."""
    trace_path = Path(trace_directory)
    decoded_events = []
    skipped = 0
    with (trace_path / "events.jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            event = json.loads(line)
            raw_file, type_name = event.get("raw_file"), event.get("type")
            if not raw_file or not type_name:
                skipped += 1
                continue
            entry: dict[str, Any] = {
                "sequence": event.get("sequence"),
                "type": type_name,
                "raw_file": raw_file,
            }
            try:
                raw = (trace_path / raw_file).read_bytes()
                entry["payload"] = _json_safe(decode_message(type_name, raw))
            except (OSError, LookupError, DecodeError) as error:
                entry["error"] = str(error)
            decoded_events.append(entry)
    return {
        "trace": str(trace_path),
        "schema_sources": build_inventory()["sources"],
        "decoded": decoded_events,
        "skipped_without_raw_or_type": skipped,
    }


def _collect_message(
    descriptor: Descriptor,
    messages: dict[str, Any],
    enums: dict[str, Any],
) -> None:
    fields = []
    for field in sorted(descriptor.fields, key=lambda item: item.number):
        type_name = _FIELD_TYPE_NAMES[field.type]
        if field.message_type is not None:
            type_name = field.message_type.full_name
        elif field.enum_type is not None:
            type_name = field.enum_type.full_name
        fields.append(
            {
                "number": field.number,
                "name": field.name,
                "type": type_name,
                "repeated": field.is_repeated,
                "required": field.is_required,
                "oneof": field.containing_oneof.name
                if field.containing_oneof
                else None,
            }
        )
    messages[descriptor.full_name] = {"fields": fields}
    for nested in descriptor.nested_types:
        _collect_message(nested, messages, enums)
    for enum in descriptor.enum_types:
        enums[enum.full_name] = _enum_inventory(enum)


def _enum_inventory(descriptor: EnumDescriptor) -> dict[str, Any]:
    return {
        "values": [
            {"name": value.name, "number": value.number} for value in descriptor.values
        ]
    }


def _source_hash(descriptor: FileDescriptor) -> str:
    content = files("bale.proto").joinpath(descriptor.name).read_bytes()
    return hashlib.sha256(content).hexdigest()


def _load_json(path: str | Path) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def _json_safe(value: Any) -> Any:
    if isinstance(value, bytes):
        return {"$bytes_base64": base64.b64encode(value).decode("ascii")}
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def _write_or_print(value: dict[str, Any], output: str | None) -> None:
    rendered = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
        print(path)
    else:
        print(rendered, end="")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inventory = commands.add_parser("inventory", help="snapshot bundled protos")
    inventory.add_argument("--output", "-o")
    difference = commands.add_parser("diff", help="compare two snapshots")
    difference.add_argument("old")
    difference.add_argument("new")
    difference.add_argument("--output", "-o")
    report = commands.add_parser("report", help="summarize a trace directory")
    report.add_argument("trace_directory")
    report.add_argument("--output", "-o")
    replay = commands.add_parser(
        "replay", help="decode stored frames with the current schema"
    )
    replay.add_argument("trace_directory")
    replay.add_argument("--output", "-o")
    decode = commands.add_parser("decode", help="decode one protobuf frame")
    decode.add_argument("type_name")
    decode.add_argument("frame")
    decode.add_argument("--output", "-o")
    return parser


def main() -> None:
    args = _parser().parse_args()
    if args.command == "inventory":
        result = build_inventory()
    elif args.command == "diff":
        result = diff_inventories(_load_json(args.old), _load_json(args.new))
    elif args.command == "report":
        result = build_trace_report(args.trace_directory)
    elif args.command == "replay":
        result = replay_trace(args.trace_directory)
    else:
        raw = Path(args.frame).read_bytes()
        result = {
            "type": args.type_name,
            "frame": args.frame,
            "payload": _json_safe(decode_message(args.type_name, raw)),
        }
    _write_or_print(result, args.output)


if __name__ == "__main__":
    main()

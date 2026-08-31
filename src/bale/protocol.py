"""Optional diagnostic recording used by transports."""

from __future__ import annotations

import asyncio
import base64
import hashlib
import json
import os
import secrets
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

_SECRET_KEYS = {
    "access_token",
    "api_key",
    "authorization",
    "code",
    "cookie",
    "jwt",
    "password",
    "phone",
    "phone_number",
    "receiver_token",
    "token",
}
_AUTH_MARKERS = (
    "bale.auth",
    "request.StartPhoneAuth",
    "request.ValidateCode",
    "request.ValidatePassword",
    "request.SignUp",
    "response.Auth",
)


class ProtocolRecorder:
    """Write RPC and protobuf events to a self-contained trace directory.

    Tracing is disabled unless an instance is explicitly passed to ``Client``.
    Authentication frames and secret fields are excluded by default.
    """

    format_version = 1

    def __init__(
        self,
        directory: str | Path,
        *,
        capture_payloads: bool = True,
        capture_raw: bool = True,
        include_secrets: bool = False,
        strict: bool = False,
    ) -> None:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.path = Path(directory).expanduser() / (
            f"trace-{timestamp}-{secrets.token_hex(3)}"
        )
        self.capture_payloads = capture_payloads
        self.capture_raw = capture_raw
        self.include_secrets = include_secrets
        self.strict = strict
        self.last_error: OSError | None = None
        self._lock = asyncio.Lock()
        self._sequence = 0
        self._initialized = False

    async def start(self) -> None:
        """Create the trace directory even before the first captured event."""
        async with self._lock:
            await self._initialize()

    async def record(
        self,
        *,
        transport: str,
        direction: str,
        kind: str,
        type_name: str | None = None,
        service: str | None = None,
        method: str | None = None,
        payload: Mapping[str, Any] | None = None,
        details: Mapping[str, Any] | None = None,
        raw: bytes | None = None,
        error: str | None = None,
    ) -> None:
        """Record one event without allowing trace I/O to break networking."""
        try:
            await self._record(
                transport=transport,
                direction=direction,
                kind=kind,
                type_name=type_name,
                service=service,
                method=method,
                payload=payload,
                details=details,
                raw=raw,
                error=error,
            )
        except OSError as caught:
            self.last_error = caught
            if self.strict:
                raise

    async def _record(
        self,
        *,
        transport: str,
        direction: str,
        kind: str,
        type_name: str | None,
        service: str | None,
        method: str | None,
        payload: Mapping[str, Any] | None,
        details: Mapping[str, Any] | None,
        raw: bytes | None,
        error: str | None,
    ) -> None:
        async with self._lock:
            await self._initialize()
            self._sequence += 1
            sequence = self._sequence
            sensitive = _is_auth_event(type_name, service, method)
            raw_allowed = (
                self.capture_raw
                and raw is not None
                and (self.include_secrets or not sensitive)
            )
            raw_path = None
            if raw_allowed:
                assert raw is not None
                raw_path = f"frames/{sequence:06d}.bin"
                await asyncio.to_thread(_write_private_bytes, self.path / raw_path, raw)

            event: dict[str, Any] = {
                "sequence": sequence,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "transport": transport,
                "direction": direction,
                "kind": kind,
            }
            optional = {
                "type": type_name,
                "service": service,
                "method": method,
                "error": error,
                "raw_file": raw_path,
            }
            event.update({key: value for key, value in optional.items() if value})
            if raw is not None:
                event["raw_size"] = len(raw)
                event["raw_sha256"] = hashlib.sha256(raw).hexdigest()
                if sensitive and not raw_allowed:
                    event["raw_omitted"] = "authentication event"
            if self.capture_payloads and payload is not None:
                event["payload"] = _json_value(
                    payload, include_secrets=self.include_secrets
                )
            if details is not None:
                event["details"] = _json_value(
                    details, include_secrets=self.include_secrets
                )

            line = json.dumps(event, ensure_ascii=False, separators=(",", ":"))
            await asyncio.to_thread(
                _append_private_line, self.path / "events.jsonl", line
            )

    async def _initialize(self) -> None:
        if self._initialized:
            return
        manifest = {
            "format": "bale-async-protocol-trace",
            "format_version": self.format_version,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "capture_payloads": self.capture_payloads,
            "capture_raw": self.capture_raw,
            "include_secrets": self.include_secrets,
            "warning": "Trace payloads may contain private account data.",
        }
        await asyncio.to_thread(_create_trace, self.path, manifest)
        self._initialized = True


def _is_auth_event(
    type_name: str | None, service: str | None, method: str | None
) -> bool:
    identity = " ".join(filter(None, (type_name, service, method)))
    return any(marker.casefold() in identity.casefold() for marker in _AUTH_MARKERS)


def _json_value(value: Any, *, include_secrets: bool, key: str = "") -> Any:
    if not include_secrets and key.casefold() in _SECRET_KEYS:
        return "<redacted>"
    if (
        not include_secrets
        and key.casefold() in {"url", "uri"}
        and isinstance(value, str)
    ):
        try:
            parsed = urlsplit(value)
            host = parsed.hostname or ""
            if ":" in host and not host.startswith("["):
                host = f"[{host}]"
            if parsed.port:
                host = f"{host}:{parsed.port}"
            return urlunsplit((parsed.scheme, host, parsed.path, "", ""))
        except ValueError:
            return "<redacted-url>"
    if isinstance(value, bytes | bytearray | memoryview):
        return {"$bytes_base64": base64.b64encode(bytes(value)).decode("ascii")}
    if isinstance(value, Mapping):
        return {
            str(item_key): _json_value(
                item,
                include_secrets=include_secrets,
                key=str(item_key),
            )
            for item_key, item in value.items()
        }
    if isinstance(value, list | tuple):
        return [_json_value(item, include_secrets=include_secrets) for item in value]
    if value is None or isinstance(value, bool | int | float | str):
        return value
    return repr(value)


def _create_trace(path: Path, manifest: Mapping[str, Any]) -> None:
    path.mkdir(parents=True, exist_ok=False, mode=0o700)
    (path / "frames").mkdir(mode=0o700)
    manifest_path = path / "manifest.json"
    _write_private_bytes(
        manifest_path,
        (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode(),
    )


def _write_private_bytes(path: Path, content: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(content)


def _append_private_line(path: Path, line: str) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(descriptor, "a", encoding="utf-8") as stream:
        stream.write(line)
        stream.write("\n")

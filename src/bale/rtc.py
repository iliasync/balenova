"""Safe helpers for Bale's LiveKit RTC connection credentials.

Bale's Meet RPCs return a LiveKit server URL and a short-lived JWT. The browser
then opens ``/rtc/v1`` with ``access_token`` and protobuf ``join_request`` query
parameters. This module handles that credential/envelope layer; offers,
answers, ICE candidates, and media remain the official LiveKit SDK's job.
"""

from __future__ import annotations

import base64
import gzip
import importlib
import json
from collections.abc import Mapping
from dataclasses import dataclass, field
from io import BytesIO
from time import time
from typing import Any
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

_MAX_JOIN_REQUEST_BYTES = 1024 * 1024


@dataclass(frozen=True, slots=True)
class CallRtcPermissions:
    """Unverified LiveKit grants advertised by a call JWT."""

    can_publish: bool = False
    can_publish_data: bool = False
    can_subscribe: bool = False
    room_admin: bool = False
    room_join: bool = False


@dataclass(frozen=True, slots=True)
class LiveKitJoinRequest:
    """Decoded ``livekit.WrappedJoinRequest`` metadata.

    ``protobuf`` is the decompressed serialized ``livekit.JoinRequest``. It is
    hidden from representations because it can contain participant metadata.
    Use LiveKit's generated protocol types for the matching SDK version when
    individual fields are needed.
    """

    compression: str
    protobuf: bytes = field(repr=False)
    field_numbers: tuple[int, ...] = ()


@dataclass(frozen=True, slots=True)
class CallRtcConnection:
    """Credentials needed to connect the official LiveKit SDK to a Bale call.

    Secret and identifying values are excluded from ``repr`` so logging this
    object does not leak a usable call credential.
    """

    server_url: str
    access_token: str = field(repr=False)
    permissions: CallRtcPermissions = CallRtcPermissions()
    not_before: int | None = None
    expires_at: int | None = None
    issuer: str | None = field(default=None, repr=False)
    subject: str | None = field(default=None, repr=False)
    room: str | None = field(default=None, repr=False)
    join_request: LiveKitJoinRequest | None = field(default=None, repr=False)

    @property
    def expired(self) -> bool:
        """Whether the unverified JWT expiry timestamp is in the past."""

        return self.expires_at is not None and self.expires_at <= int(time())

    async def connect(self, options: Any | None = None) -> Any:
        """Connect and return an official ``livekit.rtc.Room`` instance."""

        try:
            rtc = importlib.import_module("livekit.rtc")
        except ImportError as error:
            raise RuntimeError(
                "Install BaleNova's voice extra: pip install 'balenova[voice]'"
            ) from error

        room = rtc.Room()
        if options is None:
            await room.connect(self.server_url, self.access_token)
        else:
            await room.connect(self.server_url, self.access_token, options)
        return room


def parse_call_wss_url(
    url: str, *, access_token: str | None = None
) -> CallRtcConnection:
    """Parse a Bale/LiveKit call URL without validating the JWT signature.

    The returned ``server_url`` has credential query parameters removed. A
    token may be supplied separately, as it is in Bale's ``GroupCall`` model,
    or embedded as ``access_token`` in a browser-captured WebSocket URL.
    """

    if not isinstance(url, str) or not url.strip():
        raise ValueError("call RTC URL must not be empty")
    parsed = urlsplit(url.strip())
    if parsed.scheme not in {"ws", "wss", "http", "https"} or not parsed.hostname:
        raise ValueError("call RTC URL must be an absolute WebSocket/HTTP URL")

    query = parse_qs(parsed.query, keep_blank_values=True)
    embedded_tokens = query.pop("access_token", [])
    if len(embedded_tokens) > 1:
        raise ValueError("call RTC URL contains multiple access tokens")
    embedded_token = embedded_tokens[0] if embedded_tokens else None
    if access_token and embedded_token and access_token != embedded_token:
        raise ValueError("embedded and supplied call access tokens differ")
    token = access_token or embedded_token
    if not token:
        raise ValueError("call RTC access token is missing")

    encoded_join_requests = query.pop("join_request", [])
    if len(encoded_join_requests) > 1:
        raise ValueError("call RTC URL contains multiple join requests")
    join_request = (
        decode_livekit_join_request(encoded_join_requests[0])
        if encoded_join_requests and encoded_join_requests[0]
        else None
    )

    server_url = urlunsplit(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            urlencode(query, doseq=True),
            "",
        )
    )
    claims = _decode_jwt_claims(token)
    grants = claims.get("video")
    if not isinstance(grants, Mapping):
        grants = {}
    permissions = CallRtcPermissions(
        can_publish=_bool_grant(grants, "canPublish"),
        can_publish_data=_bool_grant(grants, "canPublishData"),
        can_subscribe=_bool_grant(grants, "canSubscribe"),
        room_admin=_bool_grant(grants, "roomAdmin"),
        room_join=_bool_grant(grants, "roomJoin"),
    )
    return CallRtcConnection(
        server_url=server_url,
        access_token=token,
        permissions=permissions,
        not_before=_optional_int(claims.get("nbf")),
        expires_at=_optional_int(claims.get("exp")),
        issuer=_optional_str(claims.get("iss")),
        subject=_optional_str(claims.get("sub")),
        room=_optional_str(grants.get("room")),
        join_request=join_request,
    )


def call_rtc_connection_from_group_call(
    group_call: Mapping[str, Any], *, fallback_url: str | None = None
) -> CallRtcConnection:
    """Build typed RTC credentials from a Bale ``GroupCall`` response."""

    token = _unwrap(group_call.get("token"))
    url = _unwrap(group_call.get("url")) or fallback_url
    if not isinstance(token, str) or not token:
        raise ValueError("GroupCall does not contain an RTC access token")
    if not isinstance(url, str) or not url:
        raise ValueError("GroupCall does not contain an RTC server URL")
    return parse_call_wss_url(url, access_token=token)


def decode_livekit_join_request(encoded: str) -> LiveKitJoinRequest:
    """Decode a base64url ``livekit.WrappedJoinRequest`` value."""

    wrapped = _decode_base64url(encoded, "join_request")
    if len(wrapped) > _MAX_JOIN_REQUEST_BYTES:
        raise ValueError("wrapped join_request is too large")

    compression: int | None = None
    request: bytes | None = None
    position = 0
    while position < len(wrapped):
        tag, position = _read_varint(wrapped, position)
        number, wire_type = tag >> 3, tag & 7
        if number == 1 and wire_type == 0:
            compression, position = _read_varint(wrapped, position)
        elif number == 2 and wire_type == 2:
            request, position = _read_bytes(wrapped, position)
        else:
            position = _skip_field(wrapped, position, wire_type)

    if request is None:
        raise ValueError("wrapped join_request has no protobuf payload")
    if compression in (None, 0):
        protobuf = request
        compression_name = "none"
    elif compression == 1:
        protobuf = _decompress_gzip(request)
        compression_name = "gzip"
    else:
        raise ValueError(f"unsupported join_request compression: {compression}")
    if len(protobuf) > _MAX_JOIN_REQUEST_BYTES:
        raise ValueError("decompressed join_request is too large")
    return LiveKitJoinRequest(
        compression=compression_name,
        protobuf=protobuf,
        field_numbers=_protobuf_field_numbers(protobuf),
    )


def _decode_jwt_claims(token: str) -> Mapping[str, Any]:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("call RTC access token is not a three-part JWT")
    try:
        claims = json.loads(_decode_base64url(parts[1], "JWT payload"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("call RTC JWT payload is not valid JSON") from error
    if not isinstance(claims, Mapping):
        raise ValueError("call RTC JWT payload must be an object")
    return claims


def _decode_base64url(value: str, label: str) -> bytes:
    try:
        raw = value.encode("ascii")
        return base64.b64decode(
            raw + b"=" * (-len(raw) % 4), altchars=b"-_", validate=True
        )
    except (UnicodeEncodeError, ValueError) as error:
        raise ValueError(f"{label} is not valid base64url") from error


def _decompress_gzip(value: bytes) -> bytes:
    try:
        with gzip.GzipFile(fileobj=BytesIO(value)) as stream:
            result = stream.read(_MAX_JOIN_REQUEST_BYTES + 1)
    except (EOFError, OSError) as error:
        raise ValueError("join_request contains invalid gzip data") from error
    if len(result) > _MAX_JOIN_REQUEST_BYTES:
        raise ValueError("decompressed join_request is too large")
    return result


def _read_varint(data: bytes, position: int) -> tuple[int, int]:
    value = 0
    for shift in range(0, 70, 7):
        if position >= len(data):
            raise ValueError("truncated protobuf varint")
        byte = data[position]
        position += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, position
    raise ValueError("invalid protobuf varint")


def _read_bytes(data: bytes, position: int) -> tuple[bytes, int]:
    length, position = _read_varint(data, position)
    end = position + length
    if end > len(data):
        raise ValueError("truncated protobuf bytes field")
    return data[position:end], end


def _skip_field(data: bytes, position: int, wire_type: int) -> int:
    if wire_type == 0:
        _, position = _read_varint(data, position)
        return position
    if wire_type == 1:
        end = position + 8
    elif wire_type == 2:
        _, end = _read_bytes(data, position)
        return end
    elif wire_type == 5:
        end = position + 4
    else:
        raise ValueError(f"unsupported protobuf wire type: {wire_type}")
    if end > len(data):
        raise ValueError("truncated protobuf field")
    return end


def _protobuf_field_numbers(data: bytes) -> tuple[int, ...]:
    numbers: list[int] = []
    position = 0
    while position < len(data):
        tag, position = _read_varint(data, position)
        number, wire_type = tag >> 3, tag & 7
        if number == 0:
            raise ValueError("join_request contains protobuf field zero")
        numbers.append(number)
        position = _skip_field(data, position, wire_type)
    return tuple(numbers)


def _unwrap(value: Any) -> Any:
    if not isinstance(value, Mapping):
        return value
    if "value" in value:
        return value["value"]
    return value.get("text")


def _bool_grant(grants: Mapping[str, Any], key: str) -> bool:
    return grants.get(key) is True


def _optional_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _optional_str(value: Any) -> str | None:
    return value if isinstance(value, str) else None

"""Exceptions and status codes returned by Bale services."""

from __future__ import annotations

import re
from enum import IntEnum
from typing import Any

from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message as ProtobufMessage


class RpcStatus(IntEnum):
    """Standard gRPC status numbers also used by Bale's RPC envelope."""

    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    RESOURCE_EXHAUSTED = 8
    FAILED_PRECONDITION = 9
    ABORTED = 10
    OUT_OF_RANGE = 11
    UNIMPLEMENTED = 12
    INTERNAL = 13
    UNAVAILABLE = 14
    DATA_LOSS = 15
    UNAUTHENTICATED = 16


class BaleError(Exception):
    """Base class for all package-specific exceptions."""


class AuthenticationError(BaleError):
    """Raised when credentials are missing or invalid."""


class ClientStateError(BaleError):
    """Raised when an operation is invalid for the current client state."""


class BaleRpcError(BaleError):
    """An error returned by a Bale RPC service."""

    def __init__(
        self,
        code: int,
        message: str,
        *,
        reason: str | None = None,
        details: Any = None,
    ) -> None:
        super().__init__(message or f"Bale API error {code}")
        self.code = code
        self.message = message
        self.reason = reason
        self.details = details

    @classmethod
    def from_proto(
        cls,
        error: ProtobufMessage,
        *,
        reason: str | None = None,
    ) -> BaleRpcError:
        """Build an exception from the complete protobuf ``WebError`` type."""
        details = getattr(error, "details", None)
        decoded_details: Any = None
        if isinstance(details, ProtobufMessage):
            decoded_details = MessageToDict(
                details,
                preserving_proto_field_name=True,
                use_integers_for_enums=True,
            )
        return cls(
            int(getattr(error, "code", -1)),
            str(getattr(error, "message", "Unknown Bale RPC error")),
            reason=reason,
            details=decoded_details,
        )

    @property
    def status(self) -> RpcStatus | None:
        try:
            return RpcStatus(self.code)
        except ValueError:
            return None

    @property
    def is_rate_limited(self) -> bool:
        return self.code in {8, 429} or "rate_limit" in self.message.casefold()

    @property
    def retry_after(self) -> float | None:
        values = [self.message, str(self.details or "")]
        for value in values:
            match = re.search(
                r"retry[_ -]?after\s*[:=]?\s*(\d+(?:\.\d+)?)",
                value,
                re.IGNORECASE,
            )
            if match:
                return float(match.group(1))
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "status": self.status.name if self.status is not None else None,
            "message": self.message,
            "reason": self.reason,
            "details": self.details,
            "retry_after": self.retry_after,
        }

    def __str__(self) -> str:
        reason = f" ({self.reason})" if self.reason else ""
        return f"[{self.code}] {self.message}{reason}"

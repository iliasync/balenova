"""Exceptions raised by the Bale client."""


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
    ) -> None:
        super().__init__(message or f"Bale API error {code}")
        self.code = code
        self.message = message
        self.reason = reason

    def __str__(self) -> str:
        reason = f" ({self.reason})" if self.reason else ""
        return f"[{self.code}] {self.message}{reason}"

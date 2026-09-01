"""Runtime support for the generated per-service RPC wrappers (``bale.services``).

Each Bale web RPC becomes an ``async`` Python method that accepts either a
pre-built protobuf request message or keyword arguments naming request fields.
The keyword form is built by :func:`populate`, a generic recursive setter that
understands scalar, singular-message, repeated-scalar and repeated-message
fields (and accepts nested ``dict`` / ``Message`` values for sub-messages).
"""
from __future__ import annotations

import asyncio
import re
from collections.abc import AsyncIterator
from typing import Any, TypeVar, cast

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.message import Message as PbMessage

T = TypeVar("T", bound=PbMessage)


def _snake_case(value: str) -> str:
    """Convert generated RPC names (``GetJWTToken``) to Pythonic names."""
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.lower()


def populate(msg: PbMessage, fields: dict[str, Any]) -> PbMessage:
    """Recursively assign ``fields`` onto a protobuf ``msg`` in place.

    Values may be:
      * scalars for scalar fields,
      * a ``Message`` (merged) or a ``dict`` (recursed) for message fields,
      * a list of the above for repeated fields,
      * a ``dict`` for ``map<...>`` fields.
    ``None`` values are skipped so callers can pass optional kwargs uniformly.
    """
    desc = msg.DESCRIPTOR
    for key, value in fields.items():
        if value is None:
            continue
        field = desc.fields_by_name.get(key)
        actual_key = key
        if field is None:
            actual_key = next(
                (
                    candidate
                    for candidate in desc.fields_by_name
                    if _snake_case(candidate) == key
                ),
                "",
            )
            field = desc.fields_by_name.get(actual_key)
        if field is None:
            valid = sorted(
                {
                    name
                    for candidate in desc.fields_by_name
                    for name in (candidate, _snake_case(candidate))
                }
            )
            shown = ", ".join(valid[:20]) + (", …" if len(valid) > 20 else "")
            raise TypeError(f"{desc.name} has no field {key!r}; valid fields: {shown}")

        # map<,> fields present as repeated message in the descriptor but behave
        # like a dict on the Python message.
        if _is_map(field):
            getattr(msg, actual_key).update(value)
            continue

        if _is_repeated(field):
            if isinstance(value, (str, bytes)):
                # A bare str/bytes is iterable; without this guard it would be
                # silently expanded into one element per character/byte.
                raise TypeError(
                    f"field {key!r} is repeated; pass a list, not "
                    f"{type(value).__name__}"
                )
            container = getattr(msg, actual_key)
            for item in value:
                if field.type == FieldDescriptor.TYPE_MESSAGE:
                    sub = container.add()
                    if isinstance(item, PbMessage):
                        sub.MergeFrom(item)
                    else:
                        populate(sub, item)
                else:
                    container.append(item)
        elif field.type == FieldDescriptor.TYPE_MESSAGE:
            sub = getattr(msg, actual_key)
            if isinstance(value, PbMessage):
                sub.MergeFrom(value)
            else:
                populate(sub, value)
        else:
            setattr(msg, actual_key, value)
    return msg


def _is_repeated(field: Any) -> bool:
    # protobuf >= 5 exposes the non-deprecated ``is_repeated`` property; fall
    # back to the (deprecated) label comparison on older runtimes.
    is_rep = getattr(field, "is_repeated", None)
    if is_rep is not None:
        return bool(is_rep)
    return bool(field.label == FieldDescriptor.LABEL_REPEATED)


def _is_map(field: Any) -> bool:
    mt = getattr(field, "message_type", None)
    return bool(
        mt is not None
        and getattr(mt, "GetOptions", None)
        and mt.GetOptions().map_entry
    )


def build_request(
    req_type: type[T],
    request: PbMessage | None,
    fields: dict[str, Any],
) -> T:
    """Resolve a request message from either a pre-built ``request`` or kwargs."""
    if request is not None:
        if fields:
            raise TypeError(
                "pass either a request message or field kwargs, not both"
            )
        if not isinstance(request, req_type):
            raise TypeError(
                f"expected {req_type.__name__}, got {type(request).__name__}"
            )
        return request
    return cast(T, populate(req_type(), fields))


class ServiceBase:
    """Base for a generated service namespace bound to a :class:`BaleClient`."""

    #: Fully-qualified gRPC service name, e.g. ``"bale.messaging.v2.Messaging"``.
    SERVICE: str = ""

    def __init__(self, client: Any) -> None:
        self._client = client

    def __getattr__(self, name: str) -> Any:
        """Provide snake_case aliases for generated CamelCase RPC methods."""
        if name.startswith("_"):
            raise AttributeError(name)
        for candidate in type(self).__dict__:
            if not candidate.startswith("_") and _snake_case(candidate) == name:
                return getattr(self, candidate)
        raise AttributeError(name)

    def __dir__(self) -> list[str]:
        """Include generated snake-case aliases in interactive completion."""
        names = set(super().__dir__())
        names.update(
            _snake_case(candidate)
            for candidate in type(self).__dict__
            if not candidate.startswith("_")
        )
        return sorted(names)

    async def _invoke(
        self,
        method: str,
        req_type: type[PbMessage],
        resp_type: type[T] | None,
        request: PbMessage | None,
        fields: dict[str, Any],
        timeout: float,
    ) -> T | None:
        req = build_request(req_type, request, fields)
        return await asyncio.wait_for(
            self._client.invoke_protobuf(
                self.SERVICE,
                method,
                req,
                response_type=resp_type,
            ),
            timeout=timeout,
        )

    async def _invoke_raw(
        self,
        method: str,
        resp_type: type[T] | None,
        request_bytes: bytes,
        timeout: float,
    ) -> Any:
        """Invoke an RPC whose request protobuf schema we have not yet recovered.

        The caller supplies the already-serialized request bytes; the response is
        decoded with ``resp_type`` when known, else returned as raw bytes.
        """
        return await asyncio.wait_for(
            self._client.invoke_protobuf_bytes(
                self.SERVICE,
                method,
                request_bytes,
                response_type=resp_type,
            ),
            timeout=timeout,
        )

    def _stream(
        self,
        method: str,
        req_type: type[PbMessage],
        resp_type: type[T],
        request: PbMessage | None,
        fields: dict[str, Any],
        timeout: float | None,
    ) -> AsyncIterator[T]:
        """Build a request and return a decoded server-streaming iterator."""
        req = build_request(req_type, request, fields)
        return cast(
            AsyncIterator[T],
            self._client.stream_protobuf(
                self.SERVICE,
                method,
                req,
                response_type=resp_type,
                timeout=timeout,
            ),
        )

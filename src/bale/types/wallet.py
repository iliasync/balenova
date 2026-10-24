"""Wallet, gift packets, and default response models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from bale.enums import GiftOpening, GivingType
from bale.types.base import Serializable


@dataclass(slots=True)
class GiftPacket(Serializable):
    """Represents a gift packet sent in a chat."""

    count: int = 0
    total_amount: int = 0
    giving_type: GivingType = GivingType.SAME
    token: str | None = None
    message: str | None = None
    owner_id: int | None = None
    show_amounts: bool = False


@dataclass(frozen=True, slots=True)
class Winner(Serializable):
    """Winner entry in a gift packet claim list."""

    id: int
    amount: int = 0
    date: int | None = None


@dataclass(frozen=True, slots=True)
class PacketResponse(Serializable):
    """Status and winners of an opened gift packet."""

    receivers: tuple[Winner, ...] = ()
    status: GiftOpening = GiftOpening.ALREADY_RECEIVED
    opened_count: int = 0
    win_amount: int = 0
    rank: int = 0


@dataclass(frozen=True, slots=True)
class Wallet(Serializable):
    """User wallet details."""

    token: str
    is_merchant: bool = False
    app: str | None = None
    balance: int = 0
    level: int = 0
    pan: str | None = None
    account: str | None = None


@dataclass(frozen=True, slots=True)
class WalletResponse(Serializable):
    """Response containing wallet information."""

    wallet: Wallet | None = None
    first_name: str | None = None
    last_name: str | None = None


@dataclass(frozen=True, slots=True)
class DefaultResponse(Serializable):
    """Generic sequence/state response from Bale RPCs."""

    seq: int | None = None
    date: int | None = None
    state: bytes | None = None
    seq_big: int | None = None
    ext: dict[str, Any] = field(default_factory=dict)

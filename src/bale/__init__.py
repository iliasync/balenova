"""Typed asynchronous userbot library for Bale."""

from bale import filters
from bale.client import Client
from bale.errors import (
    AuthenticationError,
    BaleError,
    BaleRpcError,
    ClientStateError,
)
from bale.filters import Filter
from bale.models import (
    Chat,
    ChatType,
    DefaultResponse,
    GiftOpening,
    GiftPacket,
    GivingType,
    Message,
    OtherMessage,
    PacketResponse,
    PeerSource,
    ReportKind,
    User,
    Wallet,
    WalletResponse,
    Winner,
)
from bale.protocol import ProtocolRecorder
from bale.session import Session

__version__ = "0.1.0"

__all__ = [
    "AuthenticationError",
    "BaleError",
    "BaleRpcError",
    "Chat",
    "ChatType",
    "Client",
    "ClientStateError",
    "DefaultResponse",
    "Filter",
    "GiftOpening",
    "GiftPacket",
    "GivingType",
    "Message",
    "OtherMessage",
    "PacketResponse",
    "PeerSource",
    "ProtocolRecorder",
    "ReportKind",
    "Session",
    "User",
    "Wallet",
    "WalletResponse",
    "Winner",
    "filters",
]

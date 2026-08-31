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
    CallMode,
    CallRecordQuality,
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
    PrivacyStatus,
    PrivacyType,
    ReportKind,
    User,
    Wallet,
    WalletResponse,
    Winner,
    model_to_dict,
    model_to_json,
)
from bale.protocol import ProtocolRecorder
from bale.session import Session

__version__ = "0.2.0"

__all__ = [
    "AuthenticationError",
    "BaleError",
    "BaleRpcError",
    "CallMode",
    "CallRecordQuality",
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
    "PrivacyStatus",
    "PrivacyType",
    "ProtocolRecorder",
    "ReportKind",
    "Session",
    "User",
    "Wallet",
    "WalletResponse",
    "Winner",
    "filters",
    "model_to_dict",
    "model_to_json",
]

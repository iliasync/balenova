"""BaleNova: a friendly Python client for Bale accounts."""

from bale import events, filters
from bale.client import Client
from bale.errors import AuthenticationError, BaleError, BaleRpcError, ClientStateError
from bale.events import MessageSent, NewMessage, RawUpdate, Update
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
from bale.session import Session

__version__ = "0.3.0"

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
    "MessageSent",
    "NewMessage",
    "OtherMessage",
    "PacketResponse",
    "PeerSource",
    "PrivacyStatus",
    "PrivacyType",
    "RawUpdate",
    "ReportKind",
    "Session",
    "Update",
    "User",
    "Wallet",
    "WalletResponse",
    "Winner",
    "events",
    "filters",
    "model_to_dict",
    "model_to_json",
]

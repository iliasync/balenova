"""Compatibility package for the BaleNova client."""

from bale import events, filters
from bale.client import Client
from bale.errors import (
    AuthenticationError,
    BaleError,
    BaleRpcError,
    ClientStateError,
)
from bale.events import MessageEdited, MessageSent, NewMessage, RawUpdate, Update
from bale.filters import Filter
from bale.full import ALL_RPCS, SERVICE_CLASSES, FullAPI
from bale.full import bale_pb2 as pb
from bale.full.bale_methods import METHODS
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
BaleClient = Client

__all__ = [
    "ALL_RPCS",
    "METHODS",
    "SERVICE_CLASSES",
    "AuthenticationError",
    "BaleClient",
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
    "FullAPI",
    "GiftOpening",
    "GiftPacket",
    "GivingType",
    "Message",
    "MessageEdited",
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
    "pb",
]

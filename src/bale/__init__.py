"""Compatibility package for the BaleNova client."""

from bale import events, filters
from bale.api import ProtocolAPI
from bale.client import Client
from bale.errors import (
    AuthenticationError,
    BaleError,
    BaleRpcError,
    ClientStateError,
    RpcStatus,
)
from bale.events import MessageEdited, MessageSent, NewMessage, RawUpdate, Update
from bale.filters import Filter
from bale.methods import METHODS
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
from bale.proto import schema as pb
from bale.recovered import (
    RECOVERED_METHODS,
    RECOVERED_RPCS,
    RecoveredAPI,
    RecoveredService,
)
from bale.rtc import (
    CallRtcConnection,
    CallRtcPermissions,
    LiveKitJoinRequest,
    call_rtc_connection_from_group_call,
    decode_livekit_join_request,
    parse_call_wss_url,
)
from bale.services import ALL_RPCS, SERVICE_CLASSES
from bale.session import Session

__version__ = "0.3.1"
BaleClient = Client

__all__ = [
    "ALL_RPCS",
    "METHODS",
    "RECOVERED_METHODS",
    "RECOVERED_RPCS",
    "SERVICE_CLASSES",
    "AuthenticationError",
    "BaleClient",
    "BaleError",
    "BaleRpcError",
    "CallMode",
    "CallRecordQuality",
    "CallRtcConnection",
    "CallRtcPermissions",
    "Chat",
    "ChatType",
    "Client",
    "ClientStateError",
    "DefaultResponse",
    "Filter",
    "GiftOpening",
    "GiftPacket",
    "GivingType",
    "LiveKitJoinRequest",
    "Message",
    "MessageEdited",
    "MessageSent",
    "NewMessage",
    "OtherMessage",
    "PacketResponse",
    "PeerSource",
    "PrivacyStatus",
    "PrivacyType",
    "ProtocolAPI",
    "RawUpdate",
    "RecoveredAPI",
    "RecoveredService",
    "ReportKind",
    "RpcStatus",
    "Session",
    "Update",
    "User",
    "Wallet",
    "WalletResponse",
    "Winner",
    "call_rtc_connection_from_group_call",
    "decode_livekit_join_request",
    "events",
    "filters",
    "model_to_dict",
    "model_to_json",
    "parse_call_wss_url",
    "pb",
]

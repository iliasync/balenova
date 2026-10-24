"""Standard enumerations for Bale entities, chats, calls, and messages."""

from __future__ import annotations

from enum import Enum, IntEnum


class ChatType(str, Enum):
    """Types of chat in Bale."""

    PRIVATE = "private"
    GROUP = "group"
    CHANNEL = "channel"
    BOT = "bot"
    SUPERGROUP = "supergroup"
    THREAD = "thread"
    UNKNOWN = "unknown"

    @property
    def is_private(self) -> bool:
        return self in (ChatType.PRIVATE, ChatType.BOT)

    @property
    def is_group(self) -> bool:
        return self in (ChatType.GROUP, ChatType.SUPERGROUP)

    @property
    def is_channel(self) -> bool:
        return self == ChatType.CHANNEL


class GivingType(IntEnum):
    """Packet gift distribution strategy."""

    SAME = 0
    RANDOM = 1


class GiftOpening(IntEnum):
    """Result of attempting to open a gift packet."""

    ALREADY_RECEIVED = 0
    SOLD_OUT = 1
    GIFT_CREATOR = 2
    SUCCESSFUL = 3
    PENDING = 4


class ReportKind(IntEnum):
    """Reason for reporting a user, group, or message."""

    UNKNOWN = 0
    SCAM = 1
    INAPPROPRIATE_CONTENT = 2
    OTHER = 3
    VIOLENCE = 4
    SPAM = 5
    FALSE_INFORMATION = 6


class PeerSource(IntEnum):
    """Origin source of peer reference."""

    UNKNOWN = 0
    DIALOGS = 1
    VITRINE = 2
    MARKET = 3
    PRIVACY_BAR = 4


class PrivacyType(IntEnum):
    """Account privacy settings categories."""

    INVITE = 0
    PRESENCE = 1
    MONEY_TRANSFER = 2


class PrivacyStatus(IntEnum):
    """Visibility permission level for privacy settings."""

    EVERYONE = 0
    CONTACTS = 1
    NOBODY = 2


class CallMode(IntEnum):
    """WebRTC call operating mode."""

    UNKNOWN = 0
    PRIVATE = 1
    GROUP = 2
    MULTI_PEER = 3
    CHANNEL_LIVE = 4


class CallRecordQuality(IntEnum):
    """Audio/video call recording quality level."""

    NOT_SPECIFIED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    ULTRA = 4
    ULTRA_PLUS = 5


class MessageEntityType(str, Enum):
    """Formatting entity types in message text."""

    MENTION = "mention"
    BOT_COMMAND = "bot_command"
    HASHTAG = "hashtag"
    URL = "url"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"


class ChatAction(str, Enum):
    """Chat action status indicators."""

    TYPING = "typing"
    RECORD_VOICE = "record_voice"
    UPLOAD_VOICE = "upload_voice"
    RECORD_VIDEO = "record_video"
    UPLOAD_VIDEO = "upload_video"
    UPLOAD_PHOTO = "upload_photo"
    UPLOAD_DOCUMENT = "upload_document"
    FIND_LOCATION = "find_location"
    RECORD_VIDEO_NOTE = "record_video_note"
    UPLOAD_VIDEO_NOTE = "upload_video_note"
    CANCEL = "cancel"

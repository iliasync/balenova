"""Friendly class-based updates delivered by :class:`bale.Client`."""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, cast

from google.protobuf.message_factory import GetMessageClass

from bale.full import bale_pb2
from bale.models import Chat, ChatType, Message, Serializable, User, model_to_dict

if TYPE_CHECKING:
    from bale.client import Client


@dataclass(slots=True)
class Update(Serializable):
    """Base class for every update received by the client."""

    raw: dict[str, Any]
    _client: Client | None = field(default=None, init=False, repr=False, compare=False)

    @property
    def name(self) -> str:
        return type(self).__name__

    def bind(self, client: Client) -> Update:
        self._client = client
        return self

    def to_dict(self, *, include_raw: bool = True) -> dict[str, Any]:
        return super().to_dict(include_raw=include_raw)

    def to_json(self, *, include_raw: bool = True, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(include_raw=include_raw),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )


@dataclass(slots=True)
class NewMessage(Update):
    """A newly received or sent message."""

    message: Message

    def bind(self, client: Client) -> NewMessage:
        super().bind(client)
        self.message.bind(client)
        return self

    @property
    def text(self) -> str:
        return self.message.content

    @property
    def content(self) -> str:
        return self.message.content

    @property
    def chat(self) -> Chat:
        return self.message.chat

    @property
    def sender(self) -> User:
        return self.message.author

    @property
    def sender_id(self) -> int:
        return self.message.sender_id

    @property
    def is_private(self) -> bool:
        return self.chat.type is ChatType.PRIVATE

    @property
    def is_group(self) -> bool:
        return self.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP}

    @property
    def is_channel(self) -> bool:
        return self.chat.type is ChatType.CHANNEL

    async def answer(self, text: str) -> Message:
        return await self.message.answer(text)

    respond = answer

    async def reply(self, text: str) -> Message:
        return await self.message.reply(text)

    async def delete(self, just_me: bool = False) -> Any:
        return await self.message.delete(just_me)


@dataclass(slots=True)
class MessageEdited(NewMessage):
    """A message whose content changed while the client was running."""


@dataclass(slots=True)
class MessageSent(Update):
    """Confirmation data for a message sent by the current account."""

    data: Any


@dataclass(slots=True)
class RawUpdate(Update):
    """A decoded update that does not yet have a dedicated convenience class."""

    kind: str
    payload: Any


# Field numbers are part of Bale's wire contract. Keeping the complete known
# name table means an update added to our typed protobuf subset is still
# surfaced as e.g. ``RawUpdate(kind="typing")`` rather than disappearing.
_UPDATE_FIELD_NAMES = {
    1: "chatGroupsChanged", 4: "messageSent", 5: "contactRegistered",
    6: "typing", 7: "userOnline", 8: "userOffline", 9: "userLastSeen",
    16: "userAvatarChanged", 19: "messageRead",
    21: "groupUserInvitedObsolete", 23: "groupUserLeaveObsolete",
    24: "groupUserKickObsolete", 32: "userNameChanged", 33: "groupOnline",
    34: "userLastSeenUnknown", 36: "groupInviteObsolete",
    38: "groupTitleChangedObsolete", 39: "groupAvatarChangedObsolete",
    40: "contactsAdded", 41: "contactsRemoved",
    44: "groupMembersUpdateObsolete", 46: "messageDelete",
    47: "chatClear", 48: "chatDelete", 50: "messageReadByMe",
    51: "userLocalNameChanged", 54: "messageReceived", 55: "message",
    57: "groupNicknameChanged", 80: "rawUpdate", 81: "typingStop",
    85: "emptyUpdate", 86: "forceClearCache", 93: "chatShow",
    94: "chatArchive", 95: "chatFavourite", 131: "parameterChanged",
    134: "userContactsChanged", 161: "ownStickersChanged",
    162: "messageContentChanged", 163: "messageDateChanged",
    164: "stickerCollectionsChanged", 169: "messageQuotedChanged",
    209: "userNickChanged", 210: "userAboutChanged",
    212: "userPreferredLanguagesChanged", 213: "groupTopicChangedObsolete",
    214: "groupAboutChangedObsolete", 216: "userTimeZoneChanged",
    217: "userBotCommandsChanged", 218: "userExtChanged",
    219: "userFullExtChanged", 222: "reactionsUpdate",
    225: "userExInfoChanged", 226: "userDefaultBankAccountChanged",
    227: "userDefaultCardNumberChanged", 228: "userDefaultCardNumberRemoved",
    254: "cardinalityChanged", 721: "groupMessagePinned",
    722: "groupPinRemoved", 723: "groupRestrictionChanged",
    2609: "groupTitleChanged", 2610: "groupAvatarChanged",
    2612: "groupMemberChanged", 2613: "groupExtChanged",
    2614: "groupMembersUpdated", 2615: "groupMembersBecameAsync",
    2616: "groupTopicChanged", 2617: "groupAboutChanged",
    2618: "groupFullExtChanged", 2619: "groupOwnerChanged",
    2620: "groupHistoryShared", 2622: "groupMembersCountChanged",
    2623: "groupMemberDiff", 2624: "groupCanSendMessagesChanged",
    2625: "groupCanViewMembersChanged", 2626: "groupCanInviteMembersChanged",
    2627: "groupMemberAdminChanged", 2628: "groupBecameOrphaned",
    2629: "userBlocked", 2630: "userUnblocked",
    2865: "groupExInfoChanged", 2880: "channelNickChanged",
    3897: "requestLogin", 43607: "accountDeleted",
    52801: "channelAdvertisementTypeChanged", 52802: "channelAdTagIdChanged",
    52803: "phoneNumberChanged", 52804: "groupMemberPermissionsChanged",
    52805: "groupDefaultPermissionsChanged", 52806: "vitrineChanged",
    52807: "callStarted", 52808: "callAccepted", 52809: "callDiscarded",
    52810: "callReceived", 52811: "groupCallStarted",
    52812: "groupCallEnded", 52813: "callReactionSent",
    52814: "stickerPacksChanged", 52815: "messages", 52816: "callUpgraded",
    52817: "peersInvited", 52818: "multiPeerCallStarted",
    52819: "peersStateChanged", 52820: "savedGifsChanged",
    52824: "hidePrivacyBar", 52825: "messageReactions",
    52826: "callLinkGenerated", 52827: "callJoinRequestReceived",
    52828: "callJoinRequestAnswered", 52829: "mentionReadByMe",
    52830: "pinnedDialogsChanged", 52832: "messageReactionsReadByMe",
    54323: "messageNewReaction", 54324: "callEvent", 54328: "startLive",
    54329: "endLive", 54332: "folderCreated", 54333: "folderDeleted",
    54334: "foldersReordered", 54335: "dialogsMarkedAsRead",
    54336: "dialogsMarkedAsUnread", 54337: "folderEdited",
    54338: "callAction", 54339: "dialogsUnpinned", 54340: "messagePinned",
    54341: "messagesUnPinned", 54342: "transcriptReady",
    54343: "generalNotificationMessage", 54344: "askBotReview",
    54345: "dialogArchiveStatus", 54346: "premiumPurchaseStatus",
    54347: "endpointChanged", 54348: "topicCreated", 54349: "topicEdited",
    54350: "topicDeleted", 54351: "messageStreamChunks",
    54352: "peerHaveScheduleTask", 54353: "allContactsRemoved",
    62398: "requestBankiAccessFor", 62732: "walletUpdated",
    62753: "walletBalanceUpdated",
}


def _snake_case(value: str) -> str:
    return "".join(
        ("_" + char.lower()) if char.isupper() else char for char in value
    ).lstrip("_")


def _edited_message_payload(payload: dict[str, Any]) -> dict[str, Any]:
    date = payload.get("date", 0)
    if isinstance(date, dict):
        date = date.get("value", 0)
    updater = payload.get("updater_user_id", 0)
    if isinstance(updater, dict):
        updater = updater.get("value", 0)
    return {
        "peer": payload.get("peer", {}),
        "sender_uid": updater,
        "date": date,
        "rid": payload.get("rid", 0),
        "message": payload.get("message", {}),
        "quoted_message": payload.get("quoted_message", {}),
    }


def _decode_complete_update_field(field: dict[str, Any]) -> dict[str, Any]:
    """Decode a field omitted by the compact event schema with the full proto."""
    number = int(field.get("number", 0))
    data = field.get("data")
    update_type = cast(Any, bale_pb2).Update
    descriptor = update_type.DESCRIPTOR.fields_by_number.get(number)
    if descriptor is None or descriptor.message_type is None or not isinstance(
        data, bytes | bytearray | memoryview
    ):
        return field
    try:
        message_type = GetMessageClass(descriptor.message_type)
        message = message_type.FromString(bytes(data))
    except Exception:
        return field
    return {
        **field,
        "protobuf_type": descriptor.message_type.full_name,
        "decoded": model_to_dict(message, include_raw=True),
    }


def build_updates(
    raw: dict[str, Any],
    message_factory: Callable[[dict[str, Any]], Message],
) -> list[Update]:
    """Turn every decoded item in an update envelope into a public class."""
    update = raw.get("update")
    composed = update.get("composed_update") if isinstance(update, dict) else None
    if not isinstance(composed, dict) or not composed:
        return [RawUpdate(raw, "unknown", model_to_dict(raw, include_raw=True))]

    result: list[Update] = []
    for kind, payload in composed.items():
        if kind == "message" and isinstance(payload, dict):
            result.append(NewMessage(raw, message_factory(payload)))
        elif kind == "message_content_changed" and isinstance(payload, dict):
            result.append(
                MessageEdited(raw, message_factory(_edited_message_payload(payload)))
            )
        elif kind == "message_sent":
            result.append(MessageSent(raw, payload))
        elif kind == "_unknown_fields" and isinstance(payload, list):
            for field in payload:
                if not isinstance(field, dict):
                    continue
                number = int(field.get("number", 0))
                name = _UPDATE_FIELD_NAMES.get(number, f"field_{number}")
                result.append(
                    RawUpdate(
                        raw,
                        _snake_case(name),
                        _decode_complete_update_field(field),
                    )
                )
        else:
            result.append(RawUpdate(raw, kind, payload))
    return result


__all__ = ["MessageEdited", "MessageSent", "NewMessage", "RawUpdate", "Update"]

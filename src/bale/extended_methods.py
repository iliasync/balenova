"""Complete typed Pythonic methods for all 690 Bale RPC operations."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, cast
from google.protobuf.message import Message as ProtobufMessage


class ClientExtendedMethodsMixin:
    """Mixin providing complete, typed Pythonic methods for every Bale RPC."""

    async def register_google_push(
        self: Any,
        project_id: int | None = None,
        token: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.RegisterGooglePush` operation.

        Parameters:
        project_id: Wire field `projectId` (int | None).
        token: Wire field `token` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if project_id is not None:
            rpc_payload["projectId"] = project_id
        if token is not None:
            rpc_payload["token"] = token
        return cast(
            ProtobufMessage, await self.rpc("push", "RegisterGooglePush", **rpc_payload)
        )

    async def register_push(
        self: Any,
        register: Any | None = None,
        push_version: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.RegisterPush` operation.

        Parameters:
        register: Wire field `register` (Any | None).
        push_version: Wire field `pushVersion` (int | None).

        Returns fields: encryptionKey.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if register is not None:
            rpc_payload["register"] = register
        if push_version is not None:
            rpc_payload["pushVersion"] = push_version
        return cast(
            ProtobufMessage, await self.rpc("push", "RegisterPush", **rpc_payload)
        )

    async def set_config(
        self: Any, config: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.SetConfig` operation.

        Parameters:
        config: Wire field `config` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if config is not None:
            rpc_payload["config"] = config
        return cast(ProtobufMessage, await self.rpc("push", "SetConfig", **rpc_payload))

    async def unregister_all_push_credentials(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.UnregisterAllPushCredentials` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("push", "UnregisterAllPushCredentials", **rpc_payload),
        )

    async def unregister_google_push(
        self: Any, token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.UnregisterGooglePush` operation.

        Parameters:
        token: Wire field `token` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        return cast(
            ProtobufMessage,
            await self.rpc("push", "UnregisterGooglePush", **rpc_payload),
        )

    async def unregister_push(
        self: Any, unregister: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.pushak.Push.UnregisterPush` operation.

        Parameters:
        unregister: Wire field `unregister` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if unregister is not None:
            rpc_payload["unregister"] = unregister
        return cast(
            ProtobufMessage, await self.rpc("push", "UnregisterPush", **rpc_payload)
        )

    async def file_upload_cancel(
        self: Any, file: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.FileUploadCancel` operation.

        Parameters:
        file: Wire field `file` (Any | None).

        Returns fields: canceled.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if file is not None:
            rpc_payload["file"] = file
        return cast(
            ProtobufMessage, await self.rpc("files", "FileUploadCancel", **rpc_payload)
        )

    async def get_nasim_file_public_url(
        self: Any,
        peer: Any | None = None,
        file: Any | None = None,
        filename: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.GetNasimFilePublicUrl` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        file: Wire field `file` (Any | None).
        filename: Wire field `filename` (Any | None).

        Returns fields: fileUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if file is not None:
            rpc_payload["file"] = file
        if filename is not None:
            rpc_payload["filename"] = filename
        return cast(
            ProtobufMessage,
            await self.rpc("files", "GetNasimFilePublicUrl", **rpc_payload),
        )

    async def get_nasim_file_upload_resume(
        self: Any, file: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.GetNasimFileUploadResume` operation.

        Parameters:
        file: Wire field `file` (Any | None).

        Returns fields: fileUrl, canResume.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if file is not None:
            rpc_payload["file"] = file
        return cast(
            ProtobufMessage,
            await self.rpc("files", "GetNasimFileUploadResume", **rpc_payload),
        )

    async def get_nasim_file_upload_url(
        self: Any,
        expected_size: int | None = None,
        crc: int | None = None,
        uid: int | None = None,
        name: str | None = None,
        mime_type: str | None = None,
        ex_peer: Any | None = None,
        send_type: Any | None = None,
        chunk_size: int | None = None,
        compressed_size: int | None = None,
        file_kind: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.GetNasimFileUploadUrl` operation.

        Parameters:
        expected_size: Wire field `expectedSize` (int | None).
        crc: Wire field `crc` (int | None).
        uid: Wire field `uid` (int | None).
        name: Wire field `name` (str | None).
        mime_type: Wire field `mimeType` (str | None).
        ex_peer: Wire field `exPeer` (Any | None).
        send_type: Wire field `sendType` (Any | None).
        chunk_size: Wire field `chunkSize` (int | None).
        compressed_size: Wire field `compressedSize` (int | None).
        file_kind: Wire field `fileKind` (int | None).

        Returns fields: fileId, url, duplicate, chunkSize, blockSize.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if expected_size is not None:
            rpc_payload["expectedSize"] = expected_size
        if crc is not None:
            rpc_payload["crc"] = crc
        if uid is not None:
            rpc_payload["uid"] = uid
        if name is not None:
            rpc_payload["name"] = name
        if mime_type is not None:
            rpc_payload["mimeType"] = mime_type
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if send_type is not None:
            rpc_payload["sendType"] = send_type
        if chunk_size is not None:
            rpc_payload["chunkSize"] = chunk_size
        if compressed_size is not None:
            rpc_payload["compressedSize"] = compressed_size
        if file_kind is not None:
            rpc_payload["fileKind"] = file_kind
        return cast(
            ProtobufMessage,
            await self.rpc("files", "GetNasimFileUploadUrl", **rpc_payload),
        )

    async def get_nasim_file_url(
        self: Any,
        file: Any | None = None,
        ciphertext: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.GetNasimFileUrl` operation.

        Parameters:
        file: Wire field `file` (Any | None).
        ciphertext: Wire field `ciphertext` (bool | None).

        Returns fields: fileUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if file is not None:
            rpc_payload["file"] = file
        if ciphertext is not None:
            rpc_payload["ciphertext"] = ciphertext
        return cast(
            ProtobufMessage, await self.rpc("files", "GetNasimFileUrl", **rpc_payload)
        )

    async def get_nasim_file_urls(
        self: Any,
        files: Iterable[Any] | None = None,
        ciphertext: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `ai.bale.server.Files.GetNasimFileUrls` operation.

        Parameters:
        files: Wire field `files` (Iterable[Any] | None).
        ciphertext: Wire field `ciphertext` (bool | None).

        Returns fields: fileUrls.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if files is not None:
            rpc_payload["files"] = files
        if ciphertext is not None:
            rpc_payload["ciphertext"] = ciphertext
        return cast(
            ProtobufMessage, await self.rpc("files", "GetNasimFileUrls", **rpc_payload)
        )

    async def enable_show_reaction_flag(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.abacus.v1.Abacus.EnableShowReactionFlag` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("abacus", "EnableShowReactionFlag", **rpc_payload),
        )

    async def get_message_reactions_list(
        self: Any,
        peer: Any | None = None,
        rid: int | None = None,
        date: int | None = None,
        code: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.abacus.v1.Abacus.GetMessageReactionsList` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        rid: Wire field `rid` (int | None).
        date: Wire field `date` (int | None).
        code: Wire field `code` (str | None).
        page: Wire field `page` (int | None).
        limit: Wire field `limit` (int | None).

        Returns fields: userReactions.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if rid is not None:
            rpc_payload["rid"] = rid
        if date is not None:
            rpc_payload["date"] = date
        if code is not None:
            rpc_payload["code"] = code
        if page is not None:
            rpc_payload["page"] = page
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(
            ProtobufMessage,
            await self.rpc("abacus", "GetMessageReactionsList", **rpc_payload),
        )

    async def get_show_reaction_flag(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.abacus.v1.Abacus.GetShowReactionFlag` operation.

        Returns fields: userId, isEnable.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("abacus", "GetShowReactionFlag", **rpc_payload),
        )

    async def load_reactions(
        self: Any,
        peer: Any | None = None,
        mids: Iterable[Any] | None = None,
        ignore_count_views: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.abacus.v1.Abacus.LoadReactions` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        mids: Wire field `mids` (Iterable[Any] | None).
        ignore_count_views: Wire field `ignoreCountViews` (bool | None).

        Returns fields: containers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if mids is not None:
            rpc_payload["mids"] = mids
        if ignore_count_views is not None:
            rpc_payload["ignoreCountViews"] = ignore_count_views
        return cast(
            ProtobufMessage, await self.rpc("abacus", "LoadReactions", **rpc_payload)
        )

    async def message_reactions_read(
        self: Any, peer: Any | None = None, message_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.abacus.v1.Abacus.MessageReactionsRead` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage,
            await self.rpc("abacus", "MessageReactionsRead", **rpc_payload),
        )

    async def add_custom_income(
        self: Any,
        type_: int | None = None,
        amount: int | None = None,
        description: str | None = None,
        customer_user_id: int | None = None,
        customer_name: str | None = None,
        payment_method: int | None = None,
        payment_date: int | None = None,
        deposit_tracking_id: Any | None = None,
        ad_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.AddCustomIncome` operation.

        Parameters:
        type_: Wire field `type` (int | None).
        amount: Wire field `amount` (int | None).
        description: Wire field `description` (str | None).
        customer_user_id: Wire field `customerUserId` (int | None).
        customer_name: Wire field `customerName` (str | None).
        payment_method: Wire field `paymentMethod` (int | None).
        payment_date: Wire field `paymentDate` (int | None).
        deposit_tracking_id: Wire field `depositTrackingId` (Any | None).
        ad_id: Wire field `adId` (Any | None).

        Returns fields: id.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if type_ is not None:
            rpc_payload["type"] = type_
        if amount is not None:
            rpc_payload["amount"] = amount
        if description is not None:
            rpc_payload["description"] = description
        if customer_user_id is not None:
            rpc_payload["customerUserId"] = customer_user_id
        if customer_name is not None:
            rpc_payload["customerName"] = customer_name
        if payment_method is not None:
            rpc_payload["paymentMethod"] = payment_method
        if payment_date is not None:
            rpc_payload["paymentDate"] = payment_date
        if deposit_tracking_id is not None:
            rpc_payload["depositTrackingId"] = deposit_tracking_id
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "AddCustomIncome", **rpc_payload),
        )

    async def change_account_state(
        self: Any,
        state: int | None = None,
        owner_id: int | None = None,
        reason: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeAccountState` operation.

        Parameters:
        state: Wire field `state` (int | None).
        owner_id: Wire field `ownerId` (int | None).
        reason: Wire field `reason` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if state is not None:
            rpc_payload["state"] = state
        if owner_id is not None:
            rpc_payload["ownerId"] = owner_id
        if reason is not None:
            rpc_payload["reason"] = reason
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeAccountState", **rpc_payload),
        )

    async def change_ad_state(
        self: Any,
        ad_id: str | None = None,
        state: int | None = None,
        reason: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeAdState` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).
        state: Wire field `state` (int | None).
        reason: Wire field `reason` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        if state is not None:
            rpc_payload["state"] = state
        if reason is not None:
            rpc_payload["reason"] = reason
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeAdState", **rpc_payload),
        )

    async def change_bonus_code_state(
        self: Any, code: str | None = None, state: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeBonusCodeState` operation.

        Parameters:
        code: Wire field `code` (str | None).
        state: Wire field `state` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if code is not None:
            rpc_payload["code"] = code
        if state is not None:
            rpc_payload["state"] = state
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeBonusCodeState", **rpc_payload),
        )

    async def change_campaign_content_state(
        self: Any,
        campaign_id: str | None = None,
        state: int | None = None,
        reason: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeCampaignContentState` operation.

        Parameters:
        campaign_id: Wire field `campaignId` (str | None).
        state: Wire field `state` (int | None).
        reason: Wire field `reason` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if campaign_id is not None:
            rpc_payload["campaignId"] = campaign_id
        if state is not None:
            rpc_payload["state"] = state
        if reason is not None:
            rpc_payload["reason"] = reason
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "ChangeCampaignContentState", **rpc_payload
            ),
        )

    async def change_campaign_state(
        self: Any,
        campaign_id: str | None = None,
        state: int | None = None,
        rejection_reason: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeCampaignState` operation.

        Parameters:
        campaign_id: Wire field `campaignId` (str | None).
        state: Wire field `state` (int | None).
        rejection_reason: Wire field `rejectionReason` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if campaign_id is not None:
            rpc_payload["campaignId"] = campaign_id
        if state is not None:
            rpc_payload["state"] = state
        if rejection_reason is not None:
            rpc_payload["rejectionReason"] = rejection_reason
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeCampaignState", **rpc_payload),
        )

    async def change_channel_income_owner(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeChannelIncomeOwner` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeChannelIncomeOwner", **rpc_payload),
        )

    async def change_channel_show_ad_permissions(
        self: Any,
        peer_id: Any | None = None,
        show_ads: Any | None = None,
        time_restrict: Any | None = None,
        category_filter: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeChannelShowAdPermissions` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        show_ads: Wire field `showAds` (Any | None).
        time_restrict: Wire field `timeRestrict` (Any | None).
        category_filter: Wire field `categoryFilter` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if show_ads is not None:
            rpc_payload["showAds"] = show_ads
        if time_restrict is not None:
            rpc_payload["timeRestrict"] = time_restrict
        if category_filter is not None:
            rpc_payload["categoryFilter"] = category_filter
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "ChangeChannelShowAdPermissions", **rpc_payload
            ),
        )

    async def change_status_dialog_ad_order(
        self: Any,
        id_: str | None = None,
        target_status: int | None = None,
        date: int | None = None,
        rejection_reason: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeStatusDialogAdOrder` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        target_status: Wire field `targetStatus` (int | None).
        date: Wire field `date` (int | None).
        rejection_reason: Wire field `rejectionReason` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if target_status is not None:
            rpc_payload["targetStatus"] = target_status
        if date is not None:
            rpc_payload["date"] = date
        if rejection_reason is not None:
            rpc_payload["rejectionReason"] = rejection_reason
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeStatusDialogAdOrder", **rpc_payload),
        )

    async def change_user_data_state(
        self: Any,
        owner_id: int | None = None,
        state: int | None = None,
        reason: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChangeUserDataState` operation.

        Parameters:
        owner_id: Wire field `ownerId` (int | None).
        state: Wire field `state` (int | None).
        reason: Wire field `reason` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if owner_id is not None:
            rpc_payload["ownerId"] = owner_id
        if state is not None:
            rpc_payload["state"] = state
        if reason is not None:
            rpc_payload["reason"] = reason
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChangeUserDataState", **rpc_payload),
        )

    async def channel_income_get_credit(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChannelIncomeGetCredit` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChannelIncomeGetCredit", **rpc_payload),
        )

    async def channel_income_kif_transfer(
        self: Any,
        peer_id: Any | None = None,
        pay_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChannelIncomeKifTransfer` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        pay_type: Wire field `payType` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if pay_type is not None:
            rpc_payload["payType"] = pay_type
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChannelIncomeKifTransfer", **rpc_payload),
        )

    async def channel_income_payment(
        self: Any,
        peer_id: Any | None = None,
        pay_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ChannelIncomePayment` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        pay_type: Wire field `payType` (int | None).

        Returns fields: factorHtml.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if pay_type is not None:
            rpc_payload["payType"] = pay_type
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ChannelIncomePayment", **rpc_payload),
        )

    async def convert_income(
        self: Any,
        convert_to_points: Any | None = None,
        convert_to_gift_packet: Any | None = None,
        convert_to_gift_packet_for_channel_owner: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ConvertIncome` operation.

        Parameters:
        convert_to_points: Wire field `convertToPoints` (Any | None).
        convert_to_gift_packet: Wire field `convertToGiftPacket` (Any | None).
        convert_to_gift_packet_for_channel_owner: Wire field `convertToGiftPacketForChannelOwner` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if convert_to_points is not None:
            rpc_payload["convertToPoints"] = convert_to_points
        if convert_to_gift_packet is not None:
            rpc_payload["convertToGiftPacket"] = convert_to_gift_packet
        if convert_to_gift_packet_for_channel_owner is not None:
            rpc_payload["convertToGiftPacketForChannelOwner"] = (
                convert_to_gift_packet_for_channel_owner
            )
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ConvertIncome", **rpc_payload),
        )

    async def create_ad(
        self: Any,
        ad_data: Any | None = None,
        price: int | None = None,
        deposit_tracking_id: Any | None = None,
        payment_method: int | None = None,
        payment_date: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateAd` operation.

        Parameters:
        ad_data: Wire field `adData` (Any | None).
        price: Wire field `price` (int | None).
        deposit_tracking_id: Wire field `depositTrackingId` (Any | None).
        payment_method: Wire field `paymentMethod` (int | None).
        payment_date: Wire field `paymentDate` (Any | None).

        Returns fields: adId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_data is not None:
            rpc_payload["adData"] = ad_data
        if price is not None:
            rpc_payload["price"] = price
        if deposit_tracking_id is not None:
            rpc_payload["depositTrackingId"] = deposit_tracking_id
        if payment_method is not None:
            rpc_payload["paymentMethod"] = payment_method
        if payment_date is not None:
            rpc_payload["paymentDate"] = payment_date
        return cast(
            ProtobufMessage, await self.rpc("advertisement", "CreateAd", **rpc_payload)
        )

    async def create_and_start_channel_ad(
        self: Any,
        title: str | None = None,
        description: str | None = None,
        link: str | None = None,
        platform: int | None = None,
        view_count: int | None = None,
        click_count: int | None = None,
        start_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateAndStartChannelAd` operation.

        Parameters:
        title: Wire field `title` (str | None).
        description: Wire field `description` (str | None).
        link: Wire field `link` (str | None).
        platform: Wire field `platform` (int | None).
        view_count: Wire field `viewCount` (int | None).
        click_count: Wire field `clickCount` (int | None).
        start_time: Wire field `startTime` (int | None).

        Returns fields: id.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if title is not None:
            rpc_payload["title"] = title
        if description is not None:
            rpc_payload["description"] = description
        if link is not None:
            rpc_payload["link"] = link
        if platform is not None:
            rpc_payload["platform"] = platform
        if view_count is not None:
            rpc_payload["viewCount"] = view_count
        if click_count is not None:
            rpc_payload["clickCount"] = click_count
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CreateAndStartChannelAd", **rpc_payload),
        )

    async def create_bale_dialog_custom_ad(
        self: Any,
        pic: str | None = None,
        title: str | None = None,
        description: str | None = None,
        link: str | None = None,
        platform: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateBaleDialogCustomAd` operation.

        Parameters:
        pic: Wire field `pic` (str | None).
        title: Wire field `title` (str | None).
        description: Wire field `description` (str | None).
        link: Wire field `link` (str | None).
        platform: Wire field `platform` (int | None).

        Returns fields: id.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if pic is not None:
            rpc_payload["pic"] = pic
        if title is not None:
            rpc_payload["title"] = title
        if description is not None:
            rpc_payload["description"] = description
        if link is not None:
            rpc_payload["link"] = link
        if platform is not None:
            rpc_payload["platform"] = platform
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CreateBaleDialogCustomAd", **rpc_payload),
        )

    async def create_bonus_code(
        self: Any,
        data: Any | None = None,
        auto_generate: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateBonusCode` operation.

        Parameters:
        data: Wire field `data` (Any | None).
        auto_generate: Wire field `autoGenerate` (bool | None).

        Returns fields: code.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if data is not None:
            rpc_payload["data"] = data
        if auto_generate is not None:
            rpc_payload["autoGenerate"] = auto_generate
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CreateBonusCode", **rpc_payload),
        )

    async def create_channel_income_factor(
        self: Any,
        peer_id: Any | None = None,
        year: int | None = None,
        month: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateChannelIncomeFactor` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        year: Wire field `year` (int | None).
        month: Wire field `month` (int | None).

        Returns fields: factorHtml.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if year is not None:
            rpc_payload["year"] = year
        if month is not None:
            rpc_payload["month"] = month
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CreateChannelIncomeFactor", **rpc_payload),
        )

    async def create_custom_campaign_package(
        self: Any,
        user_id: int | None = None,
        base_credit: int | None = None,
        credit_expire_days: int | None = None,
        campaign_daily_capacity: int | None = None,
        allowed_concurrent_campaign: int | None = None,
        audience_id: int | None = None,
        campaign_view_coef: int | None = None,
        campaign_click_coef: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateCustomCampaignPackage` operation.

        Parameters:
        user_id: Wire field `userId` (int | None).
        base_credit: Wire field `baseCredit` (int | None).
        credit_expire_days: Wire field `creditExpireDays` (int | None).
        campaign_daily_capacity: Wire field `campaignDailyCapacity` (int | None).
        allowed_concurrent_campaign: Wire field `allowedConcurrentCampaign` (int | None).
        audience_id: Wire field `audienceId` (int | None).
        campaign_view_coef: Wire field `campaignViewCoef` (int | None).
        campaign_click_coef: Wire field `campaignClickCoef` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_id is not None:
            rpc_payload["userId"] = user_id
        if base_credit is not None:
            rpc_payload["baseCredit"] = base_credit
        if credit_expire_days is not None:
            rpc_payload["creditExpireDays"] = credit_expire_days
        if campaign_daily_capacity is not None:
            rpc_payload["campaignDailyCapacity"] = campaign_daily_capacity
        if allowed_concurrent_campaign is not None:
            rpc_payload["allowedConcurrentCampaign"] = allowed_concurrent_campaign
        if audience_id is not None:
            rpc_payload["audienceId"] = audience_id
        if campaign_view_coef is not None:
            rpc_payload["campaignViewCoef"] = campaign_view_coef
        if campaign_click_coef is not None:
            rpc_payload["campaignClickCoef"] = campaign_click_coef
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "CreateCustomCampaignPackage", **rpc_payload
            ),
        )

    async def delete_custom_income(
        self: Any, id_: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.DeleteCustomIncome` operation.

        Parameters:
        id_: Wire field `id` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "DeleteCustomIncome", **rpc_payload),
        )

    async def edit_account(
        self: Any,
        account: Any | None = None,
        is_restore_expired_credit: bool | None = None,
        deposit_tracking_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.EditAccount` operation.

        Parameters:
        account: Wire field `account` (Any | None).
        is_restore_expired_credit: Wire field `isRestoreExpiredCredit` (bool | None).
        deposit_tracking_id: Wire field `depositTrackingId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if account is not None:
            rpc_payload["account"] = account
        if is_restore_expired_credit is not None:
            rpc_payload["isRestoreExpiredCredit"] = is_restore_expired_credit
        if deposit_tracking_id is not None:
            rpc_payload["depositTrackingId"] = deposit_tracking_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "EditAccount", **rpc_payload),
        )

    async def edit_ad(
        self: Any, ad: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.EditAd` operation.

        Parameters:
        ad: Wire field `ad` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad is not None:
            rpc_payload["ad"] = ad
        return cast(
            ProtobufMessage, await self.rpc("advertisement", "EditAd", **rpc_payload)
        )

    async def edit_campaign_ad(
        self: Any, ad: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.EditCampaignAd` operation.

        Parameters:
        ad: Wire field `ad` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad is not None:
            rpc_payload["ad"] = ad
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "EditCampaignAd", **rpc_payload),
        )

    async def edit_campaign_content(
        self: Any, campaign: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.EditCampaignContent` operation.

        Parameters:
        campaign: Wire field `campaign` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if campaign is not None:
            rpc_payload["campaign"] = campaign
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "EditCampaignContent", **rpc_payload),
        )

    async def finish_ad(
        self: Any, id_: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.FinishAd` operation.

        Parameters:
        id_: Wire field `id` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage, await self.rpc("advertisement", "FinishAd", **rpc_payload)
        )

    async def finish_ad_v2(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.FinishAdV2` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "FinishAdV2", **rpc_payload),
        )

    async def finish_channel_ad(
        self: Any, id_: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.FinishChannelAd` operation.

        Parameters:
        id_: Wire field `id` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "FinishChannelAd", **rpc_payload),
        )

    async def get_account_data(
        self: Any, owner_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAccountData` operation.

        Parameters:
        owner_id: Wire field `ownerId` (int | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if owner_id is not None:
            rpc_payload["ownerId"] = owner_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAccountData", **rpc_payload),
        )

    async def get_accounts(
        self: Any, page_data: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAccounts` operation.

        Parameters:
        page_data: Wire field `pageData` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if page_data is not None:
            rpc_payload["pageData"] = page_data
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAccounts", **rpc_payload),
        )

    async def get_accounts_by_state(
        self: Any, state: int | None = None, page_data: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAccountsByState` operation.

        Parameters:
        state: Wire field `state` (int | None).
        page_data: Wire field `pageData` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if state is not None:
            rpc_payload["state"] = state
        if page_data is not None:
            rpc_payload["pageData"] = page_data
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAccountsByState", **rpc_payload),
        )

    async def get_active_ads(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetActiveAds` operation.

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetActiveAds", **rpc_payload),
        )

    async def get_active_channel_ads(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetActiveChannelAds` operation.

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetActiveChannelAds", **rpc_payload),
        )

    async def get_ad_data(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdData` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns fields: adData.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage, await self.rpc("advertisement", "GetAdData", **rpc_payload)
        )

    async def get_ad_detail(
        self: Any,
        title: str | None = None,
        from_: int | None = None,
        to: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdDetail` operation.

        Parameters:
        title: Wire field `title` (str | None).
        from_: Wire field `from` (int | None).
        to: Wire field `to` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if title is not None:
            rpc_payload["title"] = title
        if from_ is not None:
            rpc_payload["from"] = from_
        if to is not None:
            rpc_payload["to"] = to
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdDetail", **rpc_payload),
        )

    async def get_ad_provider(
        self: Any,
        peer_id: Any | None = None,
        ad_type: int | None = None,
        ad_spot: int | None = None,
        ad_count: int | None = None,
        include_non_zero_placements: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdProvider` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        ad_type: Wire field `adType` (int | None).
        ad_spot: Wire field `adSpot` (int | None).
        ad_count: Wire field `adCount` (int | None).
        include_non_zero_placements: Wire field `includeNonZeroPlacements` (Any | None).

        Returns fields: content.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if ad_type is not None:
            rpc_payload["adType"] = ad_type
        if ad_spot is not None:
            rpc_payload["adSpot"] = ad_spot
        if ad_count is not None:
            rpc_payload["adCount"] = ad_count
        if include_non_zero_placements is not None:
            rpc_payload["includeNonZeroPlacements"] = include_non_zero_placements
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdProvider", **rpc_payload),
        )

    async def get_ad_report(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdReport` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns fields: views, clicks, title, link.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdReport", **rpc_payload),
        )

    async def get_ad_report_v2(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdReportV2` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdReportV2", **rpc_payload),
        )

    async def get_ads_by_spot_and_platform(
        self: Any, spot: int | None = None, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdsBySpotAndPlatform` operation.

        Parameters:
        spot: Wire field `spot` (int | None).
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if spot is not None:
            rpc_payload["spot"] = spot
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdsBySpotAndPlatform", **rpc_payload),
        )

    async def get_ads_by_state_and_spot(
        self: Any,
        paging_data: Any | None = None,
        state: int | None = None,
        spot: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAdsByStateAndSpot` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        state: Wire field `state` (int | None).
        spot: Wire field `spot` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if state is not None:
            rpc_payload["state"] = state
        if spot is not None:
            rpc_payload["spot"] = spot
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAdsByStateAndSpot", **rpc_payload),
        )

    async def get_all_channel_incomes_factor(
        self: Any, year: int | None = None, month: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAllChannelIncomesFactor` operation.

        Parameters:
        year: Wire field `year` (int | None).
        month: Wire field `month` (int | None).

        Returns fields: factors.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if year is not None:
            rpc_payload["year"] = year
        if month is not None:
            rpc_payload["month"] = month
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetAllChannelIncomesFactor", **rpc_payload
            ),
        )

    async def get_available_campaign_start_date(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAvailableCampaignStartDate` operation.

        Returns fields: date.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetAvailableCampaignStartDate", **rpc_payload
            ),
        )

    async def get_awaiting_to_show_ads(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAwaitingToShowAds` operation.

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAwaitingToShowAds", **rpc_payload),
        )

    async def get_awaiting_to_show_channel_ads(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAwaitingToShowChannelAds` operation.

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetAwaitingToShowChannelAds", **rpc_payload
            ),
        )

    async def get_bale_custom_ad(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetBaleCustomAd` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns fields: ad.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetBaleCustomAd", **rpc_payload),
        )

    async def get_bonus_code_data(
        self: Any, code: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetBonusCodeData` operation.

        Parameters:
        code: Wire field `code` (str | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if code is not None:
            rpc_payload["code"] = code
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetBonusCodeData", **rpc_payload),
        )

    async def get_bonus_codes(
        self: Any, page_data: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetBonusCodes` operation.

        Parameters:
        page_data: Wire field `pageData` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if page_data is not None:
            rpc_payload["pageData"] = page_data
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetBonusCodes", **rpc_payload),
        )

    async def get_business_ads(
        self: Any,
        paging_data: Any | None = None,
        state: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetBusinessAds` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        state: Wire field `state` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if state is not None:
            rpc_payload["state"] = state
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetBusinessAds", **rpc_payload),
        )

    async def get_crm_issues(
        self: Any,
        user_issue: Any | None = None,
        all_issue: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCRMIssues` operation.

        Parameters:
        user_issue: Wire field `userIssue` (Any | None).
        all_issue: Wire field `allIssue` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_issue is not None:
            rpc_payload["userIssue"] = user_issue
        if all_issue is not None:
            rpc_payload["allIssue"] = all_issue
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCRMIssues", **rpc_payload),
        )

    async def get_campaign_ads(
        self: Any,
        paging_data: Any | None = None,
        state: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCampaignAds` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        state: Wire field `state` (int | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if state is not None:
            rpc_payload["state"] = state
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCampaignAds", **rpc_payload),
        )

    async def get_campaign_content_by_id(
        self: Any, campaign_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCampaignContentById` operation.

        Parameters:
        campaign_id: Wire field `campaignId` (str | None).

        Returns fields: campaign.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if campaign_id is not None:
            rpc_payload["campaignId"] = campaign_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCampaignContentById", **rpc_payload),
        )

    async def get_campaign_contents(
        self: Any,
        paging_data: Any | None = None,
        state: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCampaignContents` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        state: Wire field `state` (int | None).

        Returns fields: campaigns.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if state is not None:
            rpc_payload["state"] = state
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCampaignContents", **rpc_payload),
        )

    async def get_campaign_data(
        self: Any, campaign_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCampaignData` operation.

        Parameters:
        campaign_id: Wire field `campaignId` (str | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if campaign_id is not None:
            rpc_payload["campaignId"] = campaign_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCampaignData", **rpc_payload),
        )

    async def get_channel_ads(
        self: Any, group_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelAds` operation.

        Parameters:
        group_id: Wire field `groupId` (Any | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelAds", **rpc_payload),
        )

    async def get_channel_earn_money_info(
        self: Any, group_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelEarnMoneyInfo` operation.

        Parameters:
        group_id: Wire field `groupId` (Any | None).

        Returns fields: currentMonthIncome, notPaidIncome, adCount, adCountUpdateDate.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelEarnMoneyInfo", **rpc_payload),
        )

    async def get_channel_earn_money_status(
        self: Any, group_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelEarnMoneyStatus` operation.

        Parameters:
        group_id: Wire field `groupId` (Any | None).

        Returns fields: status.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelEarnMoneyStatus", **rpc_payload),
        )

    async def get_channel_graph_report(
        self: Any,
        peer_id: Any | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelGraphReport` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: viewGraph.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelGraphReport", **rpc_payload),
        )

    async def get_channel_income_report(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelIncomeReport` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: incomeReports.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelIncomeReport", **rpc_payload),
        )

    async def get_channel_owner_bank_information(
        self: Any, channel_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelOwnerBankInformation` operation.

        Parameters:
        channel_id: Wire field `channelId` (Any | None).

        Returns fields: userId, nationalCode, birthDate, address, postalCode, melliAccountNumber, firstName, lastName, phone, state, reason, channelNick.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelOwnerBankInformation", **rpc_payload
            ),
        )

    async def get_channel_show_ad_category_filter(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelShowAdCategoryFilter` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: categories.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelShowAdCategoryFilter", **rpc_payload
            ),
        )

    async def get_channel_show_ad_permissions(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelShowAdPermissions` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: showSponsoredAd, verifiedUserId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelShowAdPermissions", **rpc_payload
            ),
        )

    async def get_channel_show_ad_time_restrict(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelShowAdTimeRestrict` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelShowAdTimeRestrict", **rpc_payload
            ),
        )

    async def get_channels_view_report(
        self: Any,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelsViewReport` operation.

        Parameters:
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: channelsView.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetChannelsViewReport", **rpc_payload),
        )

    async def get_config(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetConfig` operation.

        Returns fields: config.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("advertisement", "GetConfig", **rpc_payload)
        )

    async def get_credit_history(
        self: Any,
        owner_id: int | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCreditHistory` operation.

        Parameters:
        owner_id: Wire field `ownerId` (int | None).
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: creditHistories.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if owner_id is not None:
            rpc_payload["ownerId"] = owner_id
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCreditHistory", **rpc_payload),
        )

    async def get_creditable_accounts(
        self: Any, page_data: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCreditableAccounts` operation.

        Parameters:
        page_data: Wire field `pageData` (Any | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if page_data is not None:
            rpc_payload["pageData"] = page_data
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCreditableAccounts", **rpc_payload),
        )

    async def get_custom_incomes(
        self: Any,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetCustomIncomes` operation.

        Parameters:
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: records.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetCustomIncomes", **rpc_payload),
        )

    async def get_dialog_ad_order_details(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetDialogAdOrderDetails` operation.

        Returns fields: dialogAdOrder.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetDialogAdOrderDetails", **rpc_payload),
        )

    async def get_dialog_ad_order_payment_token(
        self: Any,
        id_: str | None = None,
        rial_amount: int | None = None,
        coin_amount: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetDialogAdOrderPaymentToken` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        rial_amount: Wire field `rialAmount` (int | None).
        coin_amount: Wire field `coinAmount` (int | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if rial_amount is not None:
            rpc_payload["rialAmount"] = rial_amount
        if coin_amount is not None:
            rpc_payload["coinAmount"] = coin_amount
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetDialogAdOrderPaymentToken", **rpc_payload
            ),
        )

    async def get_factor_eligible_ads(
        self: Any, t_begin: int | None = None, t_end: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetFactorEligibleAds` operation.

        Parameters:
        t_begin: Wire field `tBegin` (int | None).
        t_end: Wire field `tEnd` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if t_begin is not None:
            rpc_payload["tBegin"] = t_begin
        if t_end is not None:
            rpc_payload["tEnd"] = t_end
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetFactorEligibleAds", **rpc_payload),
        )

    async def get_my_contact_popular_channels(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetMyContactPopularChannels` operation.

        Returns fields: channels.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetMyContactPopularChannels", **rpc_payload
            ),
        )

    async def get_on_boarding_channels(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetOnBoardingChannels` operation.

        Returns fields: channels, showOnBoarding.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetOnBoardingChannels", **rpc_payload),
        )

    async def get_onboarding_peers(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetOnboardingPeers` operation.

        Returns fields: peers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetOnboardingPeers", **rpc_payload),
        )

    async def get_onboarding_posts(
        self: Any, category_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetOnboardingPosts` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).

        Returns fields: posts.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetOnboardingPosts", **rpc_payload),
        )

    async def get_onboarding_spot_data(
        self: Any,
        onboarding_spot: int | None = None,
        suggested_peer_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetOnboardingSpotData` operation.

        Parameters:
        onboarding_spot: Wire field `onboardingSpot` (int | None).
        suggested_peer_type: Wire field `suggestedPeerType` (int | None).

        Returns fields: contactChannels, suggestedChannels.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if onboarding_spot is not None:
            rpc_payload["onboardingSpot"] = onboarding_spot
        if suggested_peer_type is not None:
            rpc_payload["suggestedPeerType"] = suggested_peer_type
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetOnboardingSpotData", **rpc_payload),
        )

    async def get_owner_id_by_phone(
        self: Any, phone_number: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetOwnerIdByPhone` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (str | None).

        Returns fields: userId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetOwnerIdByPhone", **rpc_payload),
        )

    async def get_paid_ads_by_time(
        self: Any,
        paging_data: Any | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetPaidAdsByTime` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetPaidAdsByTime", **rpc_payload),
        )

    async def get_payment_data(
        self: Any, ad_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetPaymentData` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetPaymentData", **rpc_payload),
        )

    async def get_period_capacity_data(
        self: Any,
        begin_date: int | None = None,
        end_date: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetPeriodCapacityData` operation.

        Parameters:
        begin_date: Wire field `beginDate` (int | None).
        end_date: Wire field `endDate` (int | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if begin_date is not None:
            rpc_payload["beginDate"] = begin_date
        if end_date is not None:
            rpc_payload["endDate"] = end_date
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetPeriodCapacityData", **rpc_payload),
        )

    async def get_user_ads(
        self: Any,
        paging_data: Any | None = None,
        user_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUserAds` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        user_id: Wire field `userId` (int | None).

        Returns fields: ads.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if user_id is not None:
            rpc_payload["userId"] = user_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUserAds", **rpc_payload),
        )

    async def get_user_auth_data(
        self: Any, channel_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUserAuthData` operation.

        Parameters:
        channel_id: Wire field `channelId` (Any | None).

        Returns fields: userId, nationalCode, birthDate, address, postalCode, melliAccountNumber, firstName, lastName, phone, state, reason, channelNick.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUserAuthData", **rpc_payload),
        )

    async def get_user_campaigns(
        self: Any,
        paging_data: Any | None = None,
        user_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUserCampaigns` operation.

        Parameters:
        paging_data: Wire field `pagingData` (Any | None).
        user_id: Wire field `userId` (int | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if paging_data is not None:
            rpc_payload["pagingData"] = paging_data
        if user_id is not None:
            rpc_payload["userId"] = user_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUserCampaigns", **rpc_payload),
        )

    async def get_user_onboarding_scenario(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUserOnboardingScenario` operation.

        Returns fields: scenario.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUserOnboardingScenario", **rpc_payload),
        )

    async def get_user_status(
        self: Any, user_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUserStatus` operation.

        Parameters:
        user_id: Wire field `userId` (int | None).

        Returns fields: status.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_id is not None:
            rpc_payload["userId"] = user_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUserStatus", **rpc_payload),
        )

    async def get_users_auth_data_by_state(
        self: Any, state: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetUsersAuthDataByState` operation.

        Parameters:
        state: Wire field `state` (int | None).

        Returns fields: usersData.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if state is not None:
            rpc_payload["state"] = state
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetUsersAuthDataByState", **rpc_payload),
        )

    async def get_vod_contents(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetVODContents` operation.

        Returns fields: contents.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetVODContents", **rpc_payload),
        )

    async def modify_capacity(
        self: Any, date: int | None = None, val: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.ModifyCapacity` operation.

        Parameters:
        date: Wire field `date` (int | None).
        val: Wire field `val` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if date is not None:
            rpc_payload["date"] = date
        if val is not None:
            rpc_payload["val"] = val
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "ModifyCapacity", **rpc_payload),
        )

    async def register_for_earn_money(
        self: Any, info: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.RegisterForEarnMoney` operation.

        Parameters:
        info: Wire field `info` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if info is not None:
            rpc_payload["info"] = info
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "RegisterForEarnMoney", **rpc_payload),
        )

    async def send_admin_message(
        self: Any,
        receiver: int | None = None,
        message_text: str | None = None,
        file_id: int | None = None,
        file_name: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SendAdminMessage` operation.

        Parameters:
        receiver: Wire field `receiver` (int | None).
        message_text: Wire field `messageText` (str | None).
        file_id: Wire field `fileId` (int | None).
        file_name: Wire field `fileName` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if receiver is not None:
            rpc_payload["receiver"] = receiver
        if message_text is not None:
            rpc_payload["messageText"] = message_text
        if file_id is not None:
            rpc_payload["fileId"] = file_id
        if file_name is not None:
            rpc_payload["fileName"] = file_name
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SendAdminMessage", **rpc_payload),
        )

    async def send_factor_message(
        self: Any,
        channel_id: int | None = None,
        message_text: str | None = None,
        file_id: int | None = None,
        file_name: str | None = None,
        year: int | None = None,
        month: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SendFactorMessage` operation.

        Parameters:
        channel_id: Wire field `channelId` (int | None).
        message_text: Wire field `messageText` (str | None).
        file_id: Wire field `fileId` (int | None).
        file_name: Wire field `fileName` (str | None).
        year: Wire field `year` (int | None).
        month: Wire field `month` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        if message_text is not None:
            rpc_payload["messageText"] = message_text
        if file_id is not None:
            rpc_payload["fileId"] = file_id
        if file_name is not None:
            rpc_payload["fileName"] = file_name
        if year is not None:
            rpc_payload["year"] = year
        if month is not None:
            rpc_payload["month"] = month
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SendFactorMessage", **rpc_payload),
        )

    async def set_ad_target(
        self: Any, ad_id: str | None = None, targeting: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetAdTarget` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).
        targeting: Wire field `targeting` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        if targeting is not None:
            rpc_payload["targeting"] = targeting
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SetAdTarget", **rpc_payload),
        )

    async def set_channel_invoice_info(
        self: Any,
        peer_id: Any | None = None,
        national_code: str | None = None,
        address: str | None = None,
        postal_code: str | None = None,
        name: str | None = None,
        tag1: int | None = None,
        tag2: int | None = None,
        birth_date: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetChannelInvoiceInfo` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        national_code: Wire field `nationalCode` (str | None).
        address: Wire field `address` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        name: Wire field `name` (str | None).
        tag1: Wire field `tag1` (int | None).
        tag2: Wire field `tag2` (int | None).
        birth_date: Wire field `birthDate` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if address is not None:
            rpc_payload["address"] = address
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if name is not None:
            rpc_payload["name"] = name
        if tag1 is not None:
            rpc_payload["tag1"] = tag1
        if tag2 is not None:
            rpc_payload["tag2"] = tag2
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SetChannelInvoiceInfo", **rpc_payload),
        )

    async def set_channel_owner_bank_information(
        self: Any,
        channel_id: Any | None = None,
        national_code: str | None = None,
        birth_date: str | None = None,
        address: str | None = None,
        postal_code: str | None = None,
        melli_account_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetChannelOwnerBankInformation` operation.

        Parameters:
        channel_id: Wire field `channelId` (Any | None).
        national_code: Wire field `nationalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).
        address: Wire field `address` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        melli_account_number: Wire field `melliAccountNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        if address is not None:
            rpc_payload["address"] = address
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if melli_account_number is not None:
            rpc_payload["melliAccountNumber"] = melli_account_number
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "SetChannelOwnerBankInformation", **rpc_payload
            ),
        )

    async def set_on_boarding_channels(
        self: Any, channels: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetOnBoardingChannels` operation.

        Parameters:
        channels: Wire field `channels` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channels is not None:
            rpc_payload["channels"] = channels
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SetOnBoardingChannels", **rpc_payload),
        )

    async def set_user_auth_data(
        self: Any,
        channel_id: Any | None = None,
        national_code: str | None = None,
        birth_date: str | None = None,
        address: str | None = None,
        postal_code: str | None = None,
        melli_account_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetUserAuthData` operation.

        Parameters:
        channel_id: Wire field `channelId` (Any | None).
        national_code: Wire field `nationalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).
        address: Wire field `address` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        melli_account_number: Wire field `melliAccountNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        if address is not None:
            rpc_payload["address"] = address
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if melli_account_number is not None:
            rpc_payload["melliAccountNumber"] = melli_account_number
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SetUserAuthData", **rpc_payload),
        )

    async def start_ad(
        self: Any,
        ad_id: str | None = None,
        start_time: int | None = None,
        platform: int | None = None,
        auto_finish: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.StartAd` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).
        start_time: Wire field `startTime` (int | None).
        platform: Wire field `platform` (int | None).
        auto_finish: Wire field `autoFinish` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if platform is not None:
            rpc_payload["platform"] = platform
        if auto_finish is not None:
            rpc_payload["autoFinish"] = auto_finish
        return cast(
            ProtobufMessage, await self.rpc("advertisement", "StartAd", **rpc_payload)
        )

    async def start_bale_custom_ad(
        self: Any,
        id_: str | None = None,
        platform: int | None = None,
        pic: str | None = None,
        title: str | None = None,
        description: str | None = None,
        link: str | None = None,
        start_time: int | None = None,
        view_count: int | None = None,
        click_count: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.StartBaleCustomAd` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        platform: Wire field `platform` (int | None).
        pic: Wire field `pic` (str | None).
        title: Wire field `title` (str | None).
        description: Wire field `description` (str | None).
        link: Wire field `link` (str | None).
        start_time: Wire field `startTime` (int | None).
        view_count: Wire field `viewCount` (int | None).
        click_count: Wire field `clickCount` (int | None).

        Returns fields: ad.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if platform is not None:
            rpc_payload["platform"] = platform
        if pic is not None:
            rpc_payload["pic"] = pic
        if title is not None:
            rpc_payload["title"] = title
        if description is not None:
            rpc_payload["description"] = description
        if link is not None:
            rpc_payload["link"] = link
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if view_count is not None:
            rpc_payload["viewCount"] = view_count
        if click_count is not None:
            rpc_payload["clickCount"] = click_count
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "StartBaleCustomAd", **rpc_payload),
        )

    async def start_channel_ad_from_order(
        self: Any,
        id_: str | None = None,
        title: str | None = None,
        description: str | None = None,
        link: str | None = None,
        start_time: int | None = None,
        view_count: int | None = None,
        click_count: int | None = None,
        platform: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.StartChannelAdFromOrder` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        title: Wire field `title` (str | None).
        description: Wire field `description` (str | None).
        link: Wire field `link` (str | None).
        start_time: Wire field `startTime` (int | None).
        view_count: Wire field `viewCount` (int | None).
        click_count: Wire field `clickCount` (int | None).
        platform: Wire field `platform` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if title is not None:
            rpc_payload["title"] = title
        if description is not None:
            rpc_payload["description"] = description
        if link is not None:
            rpc_payload["link"] = link
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if view_count is not None:
            rpc_payload["viewCount"] = view_count
        if click_count is not None:
            rpc_payload["clickCount"] = click_count
        if platform is not None:
            rpc_payload["platform"] = platform
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "StartChannelAdFromOrder", **rpc_payload),
        )

    async def start_from_order(
        self: Any,
        id_: str | None = None,
        platform: int | None = None,
        pic: str | None = None,
        title: str | None = None,
        description: str | None = None,
        link: str | None = None,
        start_time: int | None = None,
        view_count: int | None = None,
        click_count: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.StartFromOrder` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        platform: Wire field `platform` (int | None).
        pic: Wire field `pic` (str | None).
        title: Wire field `title` (str | None).
        description: Wire field `description` (str | None).
        link: Wire field `link` (str | None).
        start_time: Wire field `startTime` (int | None).
        view_count: Wire field `viewCount` (int | None).
        click_count: Wire field `clickCount` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if platform is not None:
            rpc_payload["platform"] = platform
        if pic is not None:
            rpc_payload["pic"] = pic
        if title is not None:
            rpc_payload["title"] = title
        if description is not None:
            rpc_payload["description"] = description
        if link is not None:
            rpc_payload["link"] = link
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if view_count is not None:
            rpc_payload["viewCount"] = view_count
        if click_count is not None:
            rpc_payload["clickCount"] = click_count
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "StartFromOrder", **rpc_payload),
        )

    async def stop_all_bale_custom_ads(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.StopAllBaleCustomAds` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "StopAllBaleCustomAds", **rpc_payload),
        )

    async def submit_channel_ad_order(
        self: Any, order: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SubmitChannelAdOrder` operation.

        Parameters:
        order: Wire field `order` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order is not None:
            rpc_payload["order"] = order
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SubmitChannelAdOrder", **rpc_payload),
        )

    async def submit_dialog_ad_order(
        self: Any, dialog_ad_order: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SubmitDialogAdOrder` operation.

        Parameters:
        dialog_ad_order: Wire field `dialogAdOrder` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if dialog_ad_order is not None:
            rpc_payload["dialogAdOrder"] = dialog_ad_order
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SubmitDialogAdOrder", **rpc_payload),
        )

    async def submit_photo_for_bale_custom_ad(
        self: Any, ad_id: str | None = None, pic: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SubmitPhotoForBaleCustomAd` operation.

        Parameters:
        ad_id: Wire field `adId` (str | None).
        pic: Wire field `pic` (str | None).

        Returns fields: ad.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ad_id is not None:
            rpc_payload["adId"] = ad_id
        if pic is not None:
            rpc_payload["pic"] = pic
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "SubmitPhotoForBaleCustomAd", **rpc_payload
            ),
        )

    async def update_business_ad(
        self: Any, updated_ad: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.UpdateBusinessAd` operation.

        Parameters:
        updated_ad: Wire field `updatedAd` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if updated_ad is not None:
            rpc_payload["updatedAd"] = updated_ad
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "UpdateBusinessAd", **rpc_payload),
        )

    async def update_crm_issue(
        self: Any,
        add_issue: Any | None = None,
        add_comment: Any | None = None,
        resolve_issue: Any | None = None,
        ignore_user: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.UpdateCRMIssue` operation.

        Parameters:
        add_issue: Wire field `addIssue` (Any | None).
        add_comment: Wire field `addComment` (Any | None).
        resolve_issue: Wire field `resolveIssue` (Any | None).
        ignore_user: Wire field `ignoreUser` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if add_issue is not None:
            rpc_payload["addIssue"] = add_issue
        if add_comment is not None:
            rpc_payload["addComment"] = add_comment
        if resolve_issue is not None:
            rpc_payload["resolveIssue"] = resolve_issue
        if ignore_user is not None:
            rpc_payload["ignoreUser"] = ignore_user
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "UpdateCRMIssue", **rpc_payload),
        )

    async def update_click(
        self: Any,
        id_: str | None = None,
        count: int | None = None,
        peer: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.UpdateClick` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        count: Wire field `count` (int | None).
        peer: Wire field `peer` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if count is not None:
            rpc_payload["count"] = count
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "UpdateClick", **rpc_payload),
        )

    async def update_group_status(
        self: Any, group_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.UpdateGroupStatus` operation.

        Parameters:
        group_id: Wire field `groupId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "UpdateGroupStatus", **rpc_payload),
        )

    async def update_view(
        self: Any,
        id_: str | None = None,
        count: int | None = None,
        peer_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.UpdateView` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        count: Wire field `count` (int | None).
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: isSuccessful.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if count is not None:
            rpc_payload["count"] = count
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "UpdateView", **rpc_payload),
        )

    async def get_user_anonymous_contact_page(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.anonymous_contact.v1.AnonymousContact.GetUserAnonymousContactPage` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc(
                "anonymouscontact", "GetUserAnonymousContactPage", **rpc_payload
            ),
        )

    async def get_menu_button(
        self: Any, bot_user_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.appzar.v1.Appzar.GetMenuButton` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).

        Returns fields: menuButton.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        return cast(
            ProtobufMessage, await self.rpc("appzar", "GetMenuButton", **rpc_payload)
        )

    async def get_mini_app_url(
        self: Any,
        bot_user_id: int | None = None,
        screen_mode: int | None = None,
        theme_params: Any | None = None,
        main: Any | None = None,
        menu_button: Any | None = None,
        keyboard_button: Any | None = None,
        direct_link: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.appzar.v1.Appzar.GetMiniAppUrl` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).
        screen_mode: Wire field `screenMode` (int | None).
        theme_params: Wire field `themeParams` (Any | None).
        main: Wire field `main` (Any | None).
        menu_button: Wire field `menuButton` (Any | None).
        keyboard_button: Wire field `keyboardButton` (Any | None).
        direct_link: Wire field `directLink` (Any | None).

        Returns fields: url, screenMode, queryId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if screen_mode is not None:
            rpc_payload["screenMode"] = screen_mode
        if theme_params is not None:
            rpc_payload["themeParams"] = theme_params
        if main is not None:
            rpc_payload["main"] = main
        if menu_button is not None:
            rpc_payload["menuButton"] = menu_button
        if keyboard_button is not None:
            rpc_payload["keyboardButton"] = keyboard_button
        if direct_link is not None:
            rpc_payload["directLink"] = direct_link
        return cast(
            ProtobufMessage, await self.rpc("appzar", "GetMiniAppUrl", **rpc_payload)
        )

    async def invoke_custom_method(
        self: Any,
        bot_user_id: int | None = None,
        method: str | None = None,
        params: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.appzar.v1.Appzar.InvokeCustomMethod` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).
        method: Wire field `method` (str | None).
        params: Wire field `params` (str | None).

        Returns fields: data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if method is not None:
            rpc_payload["method"] = method
        if params is not None:
            rpc_payload["params"] = params
        return cast(
            ProtobufMessage,
            await self.rpc("appzar", "InvokeCustomMethod", **rpc_payload),
        )

    async def change_language(
        self: Any, language: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.ChangeLanguage` operation.

        Parameters:
        language: Wire field `language` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if language is not None:
            rpc_payload["language"] = language
        return cast(
            ProtobufMessage, await self.rpc("auth", "ChangeLanguage", **rpc_payload)
        )

    async def change_phone(
        self: Any,
        phone_number: int | None = None,
        code: str | None = None,
        transaction_hash: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.ChangePhone` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (int | None).
        code: Wire field `code` (str | None).
        transaction_hash: Wire field `transactionHash` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if code is not None:
            rpc_payload["code"] = code
        if transaction_hash is not None:
            rpc_payload["transactionHash"] = transaction_hash
        return cast(
            ProtobufMessage, await self.rpc("auth", "ChangePhone", **rpc_payload)
        )

    async def delete_account(
        self: Any,
        code: str | None = None,
        transaction_hash: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.DeleteAccount` operation.

        Parameters:
        code: Wire field `code` (str | None).
        transaction_hash: Wire field `transactionHash` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if code is not None:
            rpc_payload["code"] = code
        if transaction_hash is not None:
            rpc_payload["transactionHash"] = transaction_hash
        return cast(
            ProtobufMessage, await self.rpc("auth", "DeleteAccount", **rpc_payload)
        )

    async def disable_two_factor_authentication(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.DisableTwoFactorAuthentication` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("auth", "DisableTwoFactorAuthentication", **rpc_payload),
        )

    async def enable_two_factor_authentication(
        self: Any, email: str | None = None, password: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.EnableTwoFactorAuthentication` operation.

        Parameters:
        email: Wire field `email` (str | None).
        password: Wire field `password` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if email is not None:
            rpc_payload["email"] = email
        if password is not None:
            rpc_payload["password"] = password
        return cast(
            ProtobufMessage,
            await self.rpc("auth", "EnableTwoFactorAuthentication", **rpc_payload),
        )

    async def get_baje_bam_ticket(
        self: Any,
        exp_date_time: int | None = None,
        mobile_no: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.GetBajeBamTicket` operation.

        Parameters:
        exp_date_time: Wire field `expDateTime` (int | None).
        mobile_no: Wire field `mobileNo` (str | None).

        Returns fields: ticket.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if exp_date_time is not None:
            rpc_payload["expDateTime"] = exp_date_time
        if mobile_no is not None:
            rpc_payload["mobileNo"] = mobile_no
        return cast(
            ProtobufMessage, await self.rpc("auth", "GetBajeBamTicket", **rpc_payload)
        )

    async def get_bale_ticket(
        self: Any,
        exp_date_time: int | None = None,
        mobile_no: str | None = None,
        client_id: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.GetBaleTicket` operation.

        Parameters:
        exp_date_time: Wire field `expDateTime` (int | None).
        mobile_no: Wire field `mobileNo` (str | None).
        client_id: Wire field `clientId` (str | None).

        Returns fields: redirectUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if exp_date_time is not None:
            rpc_payload["expDateTime"] = exp_date_time
        if mobile_no is not None:
            rpc_payload["mobileNo"] = mobile_no
        if client_id is not None:
            rpc_payload["clientId"] = client_id
        return cast(
            ProtobufMessage, await self.rpc("auth", "GetBaleTicket", **rpc_payload)
        )

    async def get_jwt_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.GetJWTToken` operation.

        Returns fields: jwt.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("auth", "GetJWTToken", **rpc_payload)
        )

    async def get_ticket(
        self: Any,
        json_request: str | None = None,
        json_sign: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.GetTicket` operation.

        Parameters:
        json_request: Wire field `jsonRequest` (str | None).
        json_sign: Wire field `jsonSign` (str | None).

        Returns fields: redirectUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if json_request is not None:
            rpc_payload["jsonRequest"] = json_request
        if json_sign is not None:
            rpc_payload["jsonSign"] = json_sign
        return cast(ProtobufMessage, await self.rpc("auth", "GetTicket", **rpc_payload))

    async def get_user_id_token(
        self: Any, ticket: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.GetUserIdToken` operation.

        Parameters:
        ticket: Wire field `ticket` (str | None).

        Returns fields: token, userId, source, service.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ticket is not None:
            rpc_payload["ticket"] = ticket
        return cast(
            ProtobufMessage, await self.rpc("auth", "GetUserIdToken", **rpc_payload)
        )

    async def is_two_factor_authentication_enabled(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.IsTwoFactorAuthenticationEnabled` operation.

        Returns fields: isEnabled.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("auth", "IsTwoFactorAuthenticationEnabled", **rpc_payload),
        )

    async def log_out(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.LogOut` operation.

        Returns fields: futureAuthToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(ProtobufMessage, await self.rpc("auth", "LogOut", **rpc_payload))

    async def recover_password(
        self: Any, transaction_hash: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.RecoverPassword` operation.

        Parameters:
        transaction_hash: Wire field `transactionHash` (str | None).

        Returns fields: emailPattern.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_hash is not None:
            rpc_payload["transactionHash"] = transaction_hash
        return cast(
            ProtobufMessage, await self.rpc("auth", "RecoverPassword", **rpc_payload)
        )

    async def send_change_phone_verification_code(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.SendChangePhoneVerificationCode` operation.

        Returns fields: transactionHash, activationType.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("auth", "SendChangePhoneVerificationCode", **rpc_payload),
        )

    async def send_delete_account_verification_code(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.SendDeleteAccountVerificationCode` operation.

        Returns fields: transactionHash, activationType.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("auth", "SendDeleteAccountVerificationCode", **rpc_payload),
        )

    async def set_new_password(
        self: Any,
        new_password: str | None = None,
        transaction_hash: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.SetNewPassword` operation.

        Parameters:
        new_password: Wire field `newPassword` (str | None).
        transaction_hash: Wire field `transactionHash` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if new_password is not None:
            rpc_payload["newPassword"] = new_password
        if transaction_hash is not None:
            rpc_payload["transactionHash"] = transaction_hash
        return cast(
            ProtobufMessage, await self.rpc("auth", "SetNewPassword", **rpc_payload)
        )

    async def verify_email(
        self: Any, email: str | None = None, code: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.VerifyEmail` operation.

        Parameters:
        email: Wire field `email` (str | None).
        code: Wire field `code` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if email is not None:
            rpc_payload["email"] = email
        if code is not None:
            rpc_payload["code"] = code
        return cast(
            ProtobufMessage, await self.rpc("auth", "VerifyEmail", **rpc_payload)
        )

    async def verify_password(
        self: Any, password: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.VerifyPassword` operation.

        Parameters:
        password: Wire field `password` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if password is not None:
            rpc_payload["password"] = password
        return cast(
            ProtobufMessage, await self.rpc("auth", "VerifyPassword", **rpc_payload)
        )

    async def verify_password_recovery(
        self: Any,
        code: str | None = None,
        transaction_hash: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.auth.v1.Auth.VerifyPasswordRecovery` operation.

        Parameters:
        code: Wire field `code` (str | None).
        transaction_hash: Wire field `transactionHash` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if code is not None:
            rpc_payload["code"] = code
        if transaction_hash is not None:
            rpc_payload["transactionHash"] = transaction_hash
        return cast(
            ProtobufMessage,
            await self.rpc("auth", "VerifyPasswordRecovery", **rpc_payload),
        )

    async def get_winner_i_ds(
        self: Any, gift_packet_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.balebank.v1.GoldGiftPacket.GetWinnerIDs` operation.

        Parameters:
        gift_packet_id: Wire field `giftPacketId` (int | None).

        Returns fields: winners.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if gift_packet_id is not None:
            rpc_payload["giftPacketId"] = gift_packet_id
        return cast(
            ProtobufMessage,
            await self.rpc("goldgiftpacket", "GetWinnerIDs", **rpc_payload),
        )

    async def open_gold_gift_packet(
        self: Any, gift_packet_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.balebank.v1.GoldGiftPacket.OpenGoldGiftPacket` operation.

        Parameters:
        gift_packet_id: Wire field `giftPacketId` (int | None).

        Returns fields: openedCount, selfWinAmount, rank, giftReceivers, status, verificationDeadline.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if gift_packet_id is not None:
            rpc_payload["giftPacketId"] = gift_packet_id
        return cast(
            ProtobufMessage,
            await self.rpc("goldgiftpacket", "OpenGoldGiftPacket", **rpc_payload),
        )

    async def send_gold_gift_packet(
        self: Any,
        amount: int | None = None,
        count: int | None = None,
        description: str | None = None,
        giving_type: int | None = None,
        random_id: int | None = None,
        peer: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.balebank.v1.GoldGiftPacket.SendGoldGiftPacket` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        count: Wire field `count` (int | None).
        description: Wire field `description` (str | None).
        giving_type: Wire field `givingType` (int | None).
        random_id: Wire field `randomId` (int | None).
        peer: Wire field `peer` (Any | None).

        Returns fields: giftPacketId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if count is not None:
            rpc_payload["count"] = count
        if description is not None:
            rpc_payload["description"] = description
        if giving_type is not None:
            rpc_payload["givingType"] = giving_type
        if random_id is not None:
            rpc_payload["randomId"] = random_id
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage,
            await self.rpc("goldgiftpacket", "SendGoldGiftPacket", **rpc_payload),
        )

    async def get_balance(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.balebank.v1.GoldWallet.GetBalance` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("goldwallet", "GetBalance", **rpc_payload)
        )

    async def buy_fast_charge(
        self: Any,
        amount: int | None = None,
        phone_number: Any | None = None,
        operator: int | None = None,
        charge_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.BuyFastCharge` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        phone_number: Wire field `phoneNumber` (Any | None).
        operator: Wire field `operator` (int | None).
        charge_type: Wire field `chargeType` (int | None).

        Returns fields: transactionDate, refrenceNumber, pin, serial.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if operator is not None:
            rpc_payload["operator"] = operator
        if charge_type is not None:
            rpc_payload["chargeType"] = charge_type
        return cast(
            ProtobufMessage, await self.rpc("bank", "BuyFastCharge", **rpc_payload)
        )

    async def get_card_remain(
        self: Any,
        card_number: str | None = None,
        cvv2: str | None = None,
        expire_date: str | None = None,
        pin2: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetCardRemain` operation.

        Parameters:
        card_number: Wire field `cardNumber` (str | None).
        cvv2: Wire field `cvv2` (str | None).
        expire_date: Wire field `expireDate` (str | None).
        pin2: Wire field `pin2` (str | None).

        Returns fields: currentBalanceAmount, availableBalanceAmount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_number is not None:
            rpc_payload["cardNumber"] = card_number
        if cvv2 is not None:
            rpc_payload["cvv2"] = cvv2
        if expire_date is not None:
            rpc_payload["expireDate"] = expire_date
        if pin2 is not None:
            rpc_payload["pin2"] = pin2
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetCardRemain", **rpc_payload)
        )

    async def get_otp_token(
        self: Any, card_number_starting_six: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetOTPToken` operation.

        Parameters:
        card_number_starting_six: Wire field `cardNumberStartingSix` (str | None).

        Returns fields: requestEndPoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_number_starting_six is not None:
            rpc_payload["cardNumberStartingSix"] = card_number_starting_six
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetOTPToken", **rpc_payload)
        )

    async def get_otp_token_v2(
        self: Any,
        message_peer: Any | None = None,
        msg_rid: int | None = None,
        msg_date: int | None = None,
        peer_user_id: Any | None = None,
        card_number_starting_six: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetOTPTokenV2` operation.

        Parameters:
        message_peer: Wire field `messagePeer` (Any | None).
        msg_rid: Wire field `msgRid` (int | None).
        msg_date: Wire field `msgDate` (int | None).
        peer_user_id: Wire field `peerUserId` (Any | None).
        card_number_starting_six: Wire field `cardNumberStartingSix` (str | None).

        Returns fields: requestEndPoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message_peer is not None:
            rpc_payload["messagePeer"] = message_peer
        if msg_rid is not None:
            rpc_payload["msgRid"] = msg_rid
        if msg_date is not None:
            rpc_payload["msgDate"] = msg_date
        if peer_user_id is not None:
            rpc_payload["peerUserId"] = peer_user_id
        if card_number_starting_six is not None:
            rpc_payload["cardNumberStartingSix"] = card_number_starting_six
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetOTPTokenV2", **rpc_payload)
        )

    async def get_organization_payment_token(
        self: Any,
        organization_id: str | None = None,
        invoice_id: str | None = None,
        amount: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetOrganizationPaymentToken` operation.

        Parameters:
        organization_id: Wire field `organizationId` (str | None).
        invoice_id: Wire field `invoiceId` (str | None).
        amount: Wire field `amount` (int | None).

        Returns fields: token, billHolderName, amount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if organization_id is not None:
            rpc_payload["organizationId"] = organization_id
        if invoice_id is not None:
            rpc_payload["invoiceId"] = invoice_id
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage,
            await self.rpc("bank", "GetOrganizationPaymentToken", **rpc_payload),
        )

    async def get_ps_proxy_payment_token(
        self: Any,
        payment_amount: int | None = None,
        msg: Any | None = None,
        description: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPSProxyPaymentToken` operation.

        Parameters:
        payment_amount: Wire field `paymentAmount` (int | None).
        msg: Wire field `msg` (Any | None).
        description: Wire field `description` (Any | None).

        Returns fields: endpoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if payment_amount is not None:
            rpc_payload["paymentAmount"] = payment_amount
        if msg is not None:
            rpc_payload["msg"] = msg
        if description is not None:
            rpc_payload["description"] = description
        return cast(
            ProtobufMessage,
            await self.rpc("bank", "GetPSProxyPaymentToken", **rpc_payload),
        )

    async def get_ps_proxy_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPSProxyToken` operation.

        Returns fields: endpoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPSProxyToken", **rpc_payload)
        )

    async def get_pay_money_request_token(
        self: Any,
        message_peer: Any | None = None,
        msg_rid: int | None = None,
        msg_date: int | None = None,
        recipient: int | None = None,
        description: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPayMoneyRequestToken` operation.

        Parameters:
        message_peer: Wire field `messagePeer` (Any | None).
        msg_rid: Wire field `msgRid` (int | None).
        msg_date: Wire field `msgDate` (int | None).
        recipient: Wire field `recipient` (int | None).
        description: Wire field `description` (Any | None).

        Returns fields: requestEndPoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message_peer is not None:
            rpc_payload["messagePeer"] = message_peer
        if msg_rid is not None:
            rpc_payload["msgRid"] = msg_rid
        if msg_date is not None:
            rpc_payload["msgDate"] = msg_date
        if recipient is not None:
            rpc_payload["recipient"] = recipient
        if description is not None:
            rpc_payload["description"] = description
        return cast(
            ProtobufMessage,
            await self.rpc("bank", "GetPayMoneyRequestToken", **rpc_payload),
        )

    async def get_payment_token(
        self: Any,
        msg: Any | None = None,
        description: Any | None = None,
        amount: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPaymentToken` operation.

        Parameters:
        msg: Wire field `msg` (Any | None).
        description: Wire field `description` (Any | None).
        amount: Wire field `amount` (Any | None).

        Returns fields: token, endpoint, terminalId, cardAcqId, orderId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if msg is not None:
            rpc_payload["msg"] = msg
        if description is not None:
            rpc_payload["description"] = description
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPaymentToken", **rpc_payload)
        )

    async def get_payvand_card(
        self: Any, index: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPayvandCard` operation.

        Parameters:
        index: Wire field `index` (str | None).

        Returns fields: card.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if index is not None:
            rpc_payload["index"] = index
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPayvandCard", **rpc_payload)
        )

    async def get_payvand_card_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetPayvandCardList` operation.

        Returns fields: payvandCards.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPayvandCardList", **rpc_payload)
        )

    async def get_recent_charges(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetRecentCharges` operation.

        Returns fields: recentCharges.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("bank", "GetRecentCharges", **rpc_payload)
        )

    async def get_remain_token(
        self: Any, card_number_starting_six: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetRemainToken` operation.

        Parameters:
        card_number_starting_six: Wire field `cardNumberStartingSix` (str | None).

        Returns fields: requestEndPoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_number_starting_six is not None:
            rpc_payload["cardNumberStartingSix"] = card_number_starting_six
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetRemainToken", **rpc_payload)
        )

    async def get_sadad_psp_payment_token(
        self: Any,
        msg: Any | None = None,
        payment_amount: int | None = None,
        description: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetSadadPSPPaymentToken` operation.

        Parameters:
        msg: Wire field `msg` (Any | None).
        payment_amount: Wire field `paymentAmount` (int | None).
        description: Wire field `description` (Any | None).

        Returns fields: endpoint, token, terminalId, merchantCode.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if msg is not None:
            rpc_payload["msg"] = msg
        if payment_amount is not None:
            rpc_payload["paymentAmount"] = payment_amount
        if description is not None:
            rpc_payload["description"] = description
        return cast(
            ProtobufMessage,
            await self.rpc("bank", "GetSadadPSPPaymentToken", **rpc_payload),
        )

    async def get_token_invoice(
        self: Any, service: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GetTokenInvoice` operation.

        Parameters:
        service: Wire field `service` (int | None).

        Returns fields: endpoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if service is not None:
            rpc_payload["service"] = service
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetTokenInvoice", **rpc_payload)
        )

    async def grant_banki_access(
        self: Any, bot: Any | None = None, service_key: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bank.v1.Bank.GrantBankiAccess` operation.

        Parameters:
        bot: Wire field `bot` (Any | None).
        service_key: Wire field `serviceKey` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot is not None:
            rpc_payload["bot"] = bot
        if service_key is not None:
            rpc_payload["serviceKey"] = service_key
        return cast(
            ProtobufMessage, await self.rpc("bank", "GrantBankiAccess", **rpc_payload)
        )

    async def buy_charge(
        self: Any,
        wallet_token: str | None = None,
        phone_number: str | None = None,
        amount: int | None = None,
        operator_type: int | None = None,
        remaining: Any | None = None,
        charge_type: int | None = None,
        target_user_id: Any | None = None,
        voucher_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.BuyCharge` operation.

        Parameters:
        wallet_token: Wire field `walletToken` (str | None).
        phone_number: Wire field `phoneNumber` (str | None).
        amount: Wire field `amount` (int | None).
        operator_type: Wire field `operatorType` (int | None).
        remaining: Wire field `remaining` (Any | None).
        charge_type: Wire field `chargeType` (int | None).
        target_user_id: Wire field `targetUserId` (Any | None).
        voucher_id: Wire field `voucherId` (Any | None).

        Returns fields: paymentToken, receipt.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_token is not None:
            rpc_payload["walletToken"] = wallet_token
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if amount is not None:
            rpc_payload["amount"] = amount
        if operator_type is not None:
            rpc_payload["operatorType"] = operator_type
        if remaining is not None:
            rpc_payload["remaining"] = remaining
        if charge_type is not None:
            rpc_payload["chargeType"] = charge_type
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        if voucher_id is not None:
            rpc_payload["voucherId"] = voucher_id
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "BuyCharge", **rpc_payload),
        )

    async def buy_internet_bundle(
        self: Any,
        wallet_token: str | None = None,
        phone_number: str | None = None,
        bundle_id: int | None = None,
        operator_type: int | None = None,
        remaining: Any | None = None,
        target_user_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.BuyInternetBundle` operation.

        Parameters:
        wallet_token: Wire field `walletToken` (str | None).
        phone_number: Wire field `phoneNumber` (str | None).
        bundle_id: Wire field `bundleId` (int | None).
        operator_type: Wire field `operatorType` (int | None).
        remaining: Wire field `remaining` (Any | None).
        target_user_id: Wire field `targetUserId` (Any | None).

        Returns fields: paymentToken, receipt.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_token is not None:
            rpc_payload["walletToken"] = wallet_token
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if bundle_id is not None:
            rpc_payload["bundleId"] = bundle_id
        if operator_type is not None:
            rpc_payload["operatorType"] = operator_type
        if remaining is not None:
            rpc_payload["remaining"] = remaining
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "BuyInternetBundle", **rpc_payload),
        )

    async def delete_recent_charge_order(
        self: Any, access_hash: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.DeleteRecentChargeOrder` operation.

        Parameters:
        access_hash: Wire field `accessHash` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if access_hash is not None:
            rpc_payload["accessHash"] = access_hash
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "DeleteRecentChargeOrder", **rpc_payload),
        )

    async def delete_recent_internet_bundle_order(
        self: Any, order_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.DeleteRecentInternetBundleOrder` operation.

        Parameters:
        order_id: Wire field `orderId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "charnetservice", "DeleteRecentInternetBundleOrder", **rpc_payload
            ),
        )

    async def get_available_charges(
        self: Any,
        operator: int | None = None,
        charge_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetAvailableCharges` operation.

        Parameters:
        operator: Wire field `operator` (int | None).
        charge_type: Wire field `chargeType` (int | None).

        Returns fields: amounts, canBeOptional.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if operator is not None:
            rpc_payload["operator"] = operator
        if charge_type is not None:
            rpc_payload["chargeType"] = charge_type
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "GetAvailableCharges", **rpc_payload),
        )

    async def get_internet_bundle_list(
        self: Any,
        operator_type: int | None = None,
        sim_card_type: int | None = None,
        phone_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetInternetBundleList` operation.

        Parameters:
        operator_type: Wire field `operatorType` (int | None).
        sim_card_type: Wire field `simCardType` (int | None).
        phone_number: Wire field `phoneNumber` (str | None).

        Returns fields: bundleLists.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if operator_type is not None:
            rpc_payload["operatorType"] = operator_type
        if sim_card_type is not None:
            rpc_payload["simCardType"] = sim_card_type
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "GetInternetBundleList", **rpc_payload),
        )

    async def get_internet_bundle_payment_token(
        self: Any,
        operator_type: int | None = None,
        bundle_id: int | None = None,
        phone_number: str | None = None,
        target_user_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetInternetBundlePaymentToken` operation.

        Parameters:
        operator_type: Wire field `operatorType` (int | None).
        bundle_id: Wire field `bundleId` (int | None).
        phone_number: Wire field `phoneNumber` (str | None).
        target_user_id: Wire field `targetUserId` (Any | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if operator_type is not None:
            rpc_payload["operatorType"] = operator_type
        if bundle_id is not None:
            rpc_payload["bundleId"] = bundle_id
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "charnetservice", "GetInternetBundlePaymentToken", **rpc_payload
            ),
        )

    async def get_recent_charge_orders(
        self: Any,
        count: int | None = None,
        types: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetRecentChargeOrders` operation.

        Parameters:
        count: Wire field `count` (int | None).
        types: Wire field `types` (Iterable[int] | None).

        Returns fields: orders.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if count is not None:
            rpc_payload["count"] = count
        if types is not None:
            rpc_payload["types"] = types
        return cast(
            ProtobufMessage,
            await self.rpc("charnetservice", "GetRecentChargeOrders", **rpc_payload),
        )

    async def get_recent_internet_bundle_orders(
        self: Any, count: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetRecentInternetBundleOrders` operation.

        Parameters:
        count: Wire field `count` (int | None).

        Returns fields: orders.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if count is not None:
            rpc_payload["count"] = count
        return cast(
            ProtobufMessage,
            await self.rpc(
                "charnetservice", "GetRecentInternetBundleOrders", **rpc_payload
            ),
        )

    async def get_top_up_charge_payment_token(
        self: Any,
        provider_code: str | None = None,
        topup_type: str | None = None,
        amount: int | None = None,
        target_phone_number: str | None = None,
        target_user_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetTopUpChargePaymentToken` operation.

        Parameters:
        provider_code: Wire field `providerCode` (str | None).
        topup_type: Wire field `topupType` (str | None).
        amount: Wire field `amount` (int | None).
        target_phone_number: Wire field `targetPhoneNumber` (str | None).
        target_user_id: Wire field `targetUserId` (Any | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if provider_code is not None:
            rpc_payload["providerCode"] = provider_code
        if topup_type is not None:
            rpc_payload["topupType"] = topup_type
        if amount is not None:
            rpc_payload["amount"] = amount
        if target_phone_number is not None:
            rpc_payload["targetPhoneNumber"] = target_phone_number
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "charnetservice", "GetTopUpChargePaymentToken", **rpc_payload
            ),
        )

    async def get_voucher_charge_payment_token(
        self: Any,
        provider_code: str | None = None,
        amount: int | None = None,
        target_user_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.charnet.v1.CharnetService.GetVoucherChargePaymentToken` operation.

        Parameters:
        provider_code: Wire field `providerCode` (str | None).
        amount: Wire field `amount` (int | None).
        target_user_id: Wire field `targetUserId` (Any | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if provider_code is not None:
            rpc_payload["providerCode"] = provider_code
        if amount is not None:
            rpc_payload["amount"] = amount
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "charnetservice", "GetVoucherChargePaymentToken", **rpc_payload
            ),
        )

    async def get_participants(
        self: Any,
        message_id: Any | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.crowdfunding.v1.CrowdFunding.GetParticipants` operation.

        Parameters:
        message_id: Wire field `messageId` (Any | None).
        limit: Wire field `limit` (int | None).
        offset: Wire field `offset` (int | None).

        Returns fields: userPayments.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        if limit is not None:
            rpc_payload["limit"] = limit
        if offset is not None:
            rpc_payload["offset"] = offset
        return cast(
            ProtobufMessage,
            await self.rpc("crowdfunding", "GetParticipants", **rpc_payload),
        )

    async def get_total_paid_amount(
        self: Any, message_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.crowdfunding.v1.CrowdFunding.GetTotalPaidAmount` operation.

        Parameters:
        message_id: Wire field `messageId` (Any | None).

        Returns fields: totalPaidAmount, creatorUserId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage,
            await self.rpc("crowdfunding", "GetTotalPaidAmount", **rpc_payload),
        )

    async def get_link_status(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.falake.v1.Falake.GetLinkStatus` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("falake", "GetLinkStatus", **rpc_payload)
        )

    async def send_batch(
        self: Any, events: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.fanoos.v1.fanoos.SendBatch` operation.

        Parameters:
        events: Wire field `events` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if events is not None:
            rpc_payload["events"] = events
        return cast(
            ProtobufMessage, await self.rpc("fanoos", "SendBatch", **rpc_payload)
        )

    async def send_feed_back(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.feedback.v1.FeedBack.SendFeedBack` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("feedback", "SendFeedBack", **rpc_payload)
        )

    async def edit_custom_services(
        self: Any, items: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.EditCustomServices` operation.

        Parameters:
        items: Wire field `items` (Iterable[int] | None).

        Returns fields: customItems.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if items is not None:
            rpc_payload["items"] = items
        return cast(
            ProtobufMessage,
            await self.rpc("garson", "EditCustomServices", **rpc_payload),
        )

    async def get_advertisement_bot(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetAdvertisementBot` operation.

        Returns fields: bots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetAdvertisementBot", **rpc_payload),
        )

    async def get_bot_banners(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetBotBanners` operation.

        Returns fields: banners.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("garson", "GetBotBanners", **rpc_payload)
        )

    async def get_bots_by_category(
        self: Any,
        category_id: int | None = None,
        pagination: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetBotsByCategory` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).
        pagination: Wire field `pagination` (Any | None).

        Returns fields: bots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetBotsByCategory", **rpc_payload),
        )

    async def get_categorized_bots(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetCategorizedBots` operation.

        Returns fields: categorizedBots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetCategorizedBots", **rpc_payload),
        )

    async def get_custom_services(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetCustomServices` operation.

        Returns fields: customItems.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetCustomServices", **rpc_payload),
        )

    async def get_recommended_bots(
        self: Any,
        bot_id: int | None = None,
        pagination: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetRecommendedBots` operation.

        Parameters:
        bot_id: Wire field `botId` (int | None).
        pagination: Wire field `pagination` (Any | None).

        Returns fields: bots, moreBotsUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_id is not None:
            rpc_payload["botId"] = bot_id
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetRecommendedBots", **rpc_payload),
        )

    async def get_services(
        self: Any, version: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetServices` operation.

        Parameters:
        version: Wire field `version` (int | None).

        Returns fields: version, isChanged, data, banners, services, sections.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage, await self.rpc("garson", "GetServices", **rpc_payload)
        )

    async def get_trend_bots(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetTrendBots` operation.

        Returns fields: bots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("garson", "GetTrendBots", **rpc_payload)
        )

    async def get_user_repeated_bots(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.GetUserRepeatedBots` operation.

        Returns fields: bots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("garson", "GetUserRepeatedBots", **rpc_payload),
        )

    async def get_diff(
        self: Any,
        states: Iterable[Any] | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ghasedak.v1.GhasedakService.GetDiff` operation.

        Parameters:
        states: Wire field `states` (Iterable[Any] | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: updates, usersRefs, groupsRefs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if states is not None:
            rpc_payload["states"] = states
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage, await self.rpc("ghasedakservice", "GetDiff", **rpc_payload)
        )

    async def get_routes_states(
        self: Any,
        group_peers: Iterable[Any] | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ghasedak.v1.GhasedakService.GetRoutesStates` operation.

        Parameters:
        group_peers: Wire field `groupPeers` (Iterable[Any] | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: seqs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peers is not None:
            rpc_payload["groupPeers"] = group_peers
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage,
            await self.rpc("ghasedakservice", "GetRoutesStates", **rpc_payload),
        )

    async def get_gift_packet_payment_token(
        self: Any,
        token: str | None = None,
        amount: int | None = None,
        peer: Any | None = None,
        message: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.giftpacket.v1.GiftPacket.GetGiftPacketPaymentToken` operation.

        Parameters:
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).
        peer: Wire field `peer` (Any | None).
        message: Wire field `message` (Any | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        if peer is not None:
            rpc_payload["peer"] = peer
        if message is not None:
            rpc_payload["message"] = message
        return cast(
            ProtobufMessage,
            await self.rpc("giftpacket", "GetGiftPacketPaymentToken", **rpc_payload),
        )

    async def add_discussion_group_admin(
        self: Any,
        channel: Any | None = None,
        discussion_group: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.AddDiscussionGroupAdmin` operation.

        Parameters:
        channel: Wire field `channel` (Any | None).
        discussion_group: Wire field `discussionGroup` (Any | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel is not None:
            rpc_payload["channel"] = channel
        if discussion_group is not None:
            rpc_payload["discussionGroup"] = discussion_group
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "AddDiscussionGroupAdmin", **rpc_payload),
        )

    async def edit_channel_nick(
        self: Any,
        group_peer: Any | None = None,
        nick: str | None = None,
        random_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.EditChannelNick` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        nick: Wire field `nick` (str | None).
        random_id: Wire field `randomId` (int | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if nick is not None:
            rpc_payload["nick"] = nick
        if random_id is not None:
            rpc_payload["randomId"] = random_id
        return cast(
            ProtobufMessage, await self.rpc("groups", "EditChannelNick", **rpc_payload)
        )

    async def edit_group_default_card_number(
        self: Any,
        group_peer: Any | None = None,
        card_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.EditGroupDefaultCardNumber` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        card_number: Wire field `cardNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if card_number is not None:
            rpc_payload["cardNumber"] = card_number
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "EditGroupDefaultCardNumber", **rpc_payload),
        )

    async def get_group_default_card_number(
        self: Any, group_peerr: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.GetGroupDefaultCardNumber` operation.

        Parameters:
        group_peerr: Wire field `groupPeerr` (Any | None).

        Returns fields: defaultCardNumber.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peerr is not None:
            rpc_payload["groupPeerr"] = group_peerr
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "GetGroupDefaultCardNumber", **rpc_payload),
        )

    async def get_group_recommendations(
        self: Any, source: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.GetGroupRecommendations` operation.

        Parameters:
        source: Wire field `source` (int | None).

        Returns fields: groups.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if source is not None:
            rpc_payload["source"] = source
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "GetGroupRecommendations", **rpc_payload),
        )

    async def get_pins(
        self: Any,
        group_peer: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.GetPins` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        page: Wire field `page` (int | None).
        limit: Wire field `limit` (int | None).

        Returns fields: pins, count.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if page is not None:
            rpc_payload["page"] = page
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(ProtobufMessage, await self.rpc("groups", "GetPins", **rpc_payload))

    async def load_full_groups(
        self: Any, groups: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.LoadFullGroups` operation.

        Parameters:
        groups: Wire field `groups` (Iterable[Any] | None).

        Returns fields: groups.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if groups is not None:
            rpc_payload["groups"] = groups
        return cast(
            ProtobufMessage, await self.rpc("groups", "LoadFullGroups", **rpc_payload)
        )

    async def make_user_admin(
        self: Any,
        group_peer: Any | None = None,
        user_peer: Any | None = None,
        admin_title: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.MakeUserAdmin` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        user_peer: Wire field `userPeer` (Any | None).
        admin_title: Wire field `adminTitle` (Any | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if user_peer is not None:
            rpc_payload["userPeer"] = user_peer
        if admin_title is not None:
            rpc_payload["adminTitle"] = admin_title
        return cast(
            ProtobufMessage, await self.rpc("groups", "MakeUserAdmin", **rpc_payload)
        )

    async def remove_discussion_group(
        self: Any, rid: int | None = None, channel: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.RemoveDiscussionGroup` operation.

        Parameters:
        rid: Wire field `rid` (int | None).
        channel: Wire field `channel` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if rid is not None:
            rpc_payload["rid"] = rid
        if channel is not None:
            rpc_payload["channel"] = channel
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "RemoveDiscussionGroup", **rpc_payload),
        )

    async def remove_pin(
        self: Any, group_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.RemovePin` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        return cast(
            ProtobufMessage, await self.rpc("groups", "RemovePin", **rpc_payload)
        )

    async def set_available_reactions(
        self: Any,
        group: Any | None = None,
        codes: Iterable[str] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetAvailableReactions` operation.

        Parameters:
        group: Wire field `group` (Any | None).
        codes: Wire field `codes` (Iterable[str] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group is not None:
            rpc_payload["group"] = group
        if codes is not None:
            rpc_payload["codes"] = codes
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetAvailableReactions", **rpc_payload),
        )

    async def set_can_see_history(
        self: Any,
        group_peer: Any | None = None,
        can_see_history: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetCanSeeHistory` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        can_see_history: Wire field `canSeeHistory` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if can_see_history is not None:
            rpc_payload["canSeeHistory"] = can_see_history
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetCanSeeHistory", **rpc_payload)
        )

    async def set_can_see_messages(
        self: Any,
        group_peer: Any | None = None,
        user_id: int | None = None,
        can_see_messages: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetCanSeeMessages` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        user_id: Wire field `userId` (int | None).
        can_see_messages: Wire field `canSeeMessages` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if user_id is not None:
            rpc_payload["userId"] = user_id
        if can_see_messages is not None:
            rpc_payload["canSeeMessages"] = can_see_messages
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetCanSeeMessages", **rpc_payload),
        )

    async def set_discussion_group(
        self: Any, rid: int | None = None, channel: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetDiscussionGroup` operation.

        Parameters:
        rid: Wire field `rid` (int | None).
        channel: Wire field `channel` (Any | None).

        Returns fields: discussionGroup, group.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if rid is not None:
            rpc_payload["rid"] = rid
        if channel is not None:
            rpc_payload["channel"] = channel
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetDiscussionGroup", **rpc_payload),
        )

    async def set_group_default_permissions(
        self: Any,
        group: Any | None = None,
        permissions: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetGroupDefaultPermissions` operation.

        Parameters:
        group: Wire field `group` (Any | None).
        permissions: Wire field `permissions` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group is not None:
            rpc_payload["group"] = group
        if permissions is not None:
            rpc_payload["permissions"] = permissions
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetGroupDefaultPermissions", **rpc_payload),
        )

    async def set_member_custom_title(
        self: Any,
        group_id: int | None = None,
        member_id: int | None = None,
        title: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetMemberCustomTitle` operation.

        Parameters:
        group_id: Wire field `groupId` (int | None).
        member_id: Wire field `memberId` (int | None).
        title: Wire field `title` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        if member_id is not None:
            rpc_payload["memberId"] = member_id
        if title is not None:
            rpc_payload["title"] = title
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetMemberCustomTitle", **rpc_payload),
        )

    async def set_restriction(
        self: Any,
        group_out_peer: Any | None = None,
        restriction: int | None = None,
        nick: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetRestriction` operation.

        Parameters:
        group_out_peer: Wire field `groupOutPeer` (Any | None).
        restriction: Wire field `restriction` (int | None).
        nick: Wire field `nick` (Any | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_out_peer is not None:
            rpc_payload["groupOutPeer"] = group_out_peer
        if restriction is not None:
            rpc_payload["restriction"] = restriction
        if nick is not None:
            rpc_payload["nick"] = nick
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetRestriction", **rpc_payload)
        )

    async def transfer_ownership(
        self: Any,
        group_peer: Any | None = None,
        new_owner: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.TransferOwnership` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        new_owner: Wire field `newOwner` (int | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if new_owner is not None:
            rpc_payload["newOwner"] = new_owner
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "TransferOwnership", **rpc_payload),
        )

    async def un_ban_user(
        self: Any,
        group_peer: Any | None = None,
        user: Any | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.UnBanUser` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        user: Wire field `user` (Any | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if user is not None:
            rpc_payload["user"] = user
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage, await self.rpc("groups", "UnBanUser", **rpc_payload)
        )

    async def get_bot_group_permissions(
        self: Any,
        bot_user_id: int | None = None,
        group_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetBotGroupPermissions` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).
        group_id: Wire field `groupId` (int | None).

        Returns fields: hasAccessToMessages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if group_id is not None:
            rpc_payload["groupId"] = group_id
        return cast(
            ProtobufMessage,
            await self.rpc("ketf", "GetBotGroupPermissions", **rpc_payload),
        )

    async def get_bot_white_list(
        self: Any, bot_user_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetBotWhiteList` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).

        Returns fields: list.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        return cast(
            ProtobufMessage, await self.rpc("ketf", "GetBotWhiteList", **rpc_payload)
        )

    async def get_inline_bot_results(
        self: Any,
        query: str | None = None,
        peer: Any | None = None,
        bot_user_id: int | None = None,
        offset: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetInlineBotResults` operation.

        Parameters:
        query: Wire field `query` (str | None).
        peer: Wire field `peer` (Any | None).
        bot_user_id: Wire field `botUserId` (int | None).
        offset: Wire field `offset` (str | None).

        Returns fields: results, nextOffset, queryId, isGallery.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if peer is not None:
            rpc_payload["peer"] = peer
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if offset is not None:
            rpc_payload["offset"] = offset
        return cast(
            ProtobufMessage,
            await self.rpc("ketf", "GetInlineBotResults", **rpc_payload),
        )

    async def get_payment_details(
        self: Any,
        purchase_message_id: Any | None = None,
        invoice_identifier: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetPaymentDetails` operation.

        Parameters:
        purchase_message_id: Wire field `purchaseMessageId` (Any | None).
        invoice_identifier: Wire field `invoiceIdentifier` (Any | None).

        Returns fields: title, totalAmount, paymentsHistory, session, disapproved, description, labeledPrices.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if purchase_message_id is not None:
            rpc_payload["purchaseMessageId"] = purchase_message_id
        if invoice_identifier is not None:
            rpc_payload["invoiceIdentifier"] = invoice_identifier
        return cast(
            ProtobufMessage, await self.rpc("ketf", "GetPaymentDetails", **rpc_payload)
        )

    async def get_user_context(
        self: Any, bot_user_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetUserContext` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).

        Returns fields: botUserId, userId, nonce, sign.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        return cast(
            ProtobufMessage, await self.rpc("ketf", "GetUserContext", **rpc_payload)
        )

    async def get_webapp_hash(
        self: Any,
        bot_user_id: int | None = None,
        data: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.GetWebappHash` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).
        data: Wire field `data` (str | None).

        Returns fields: hash, queryId, authDate.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if data is not None:
            rpc_payload["data"] = data
        return cast(
            ProtobufMessage, await self.rpc("ketf", "GetWebappHash", **rpc_payload)
        )

    async def invoke_custom_action(
        self: Any,
        id_: str | None = None,
        message_id: Any | None = None,
        peer: Any | None = None,
        open_dialog_action: Any | None = None,
        done: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.InvokeCustomAction` operation.

        Parameters:
        id_: Wire field `id` (str | None).
        message_id: Wire field `messageId` (Any | None).
        peer: Wire field `peer` (Any | None).
        open_dialog_action: Wire field `openDialogAction` (Any | None).
        done: Wire field `done` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        if peer is not None:
            rpc_payload["peer"] = peer
        if open_dialog_action is not None:
            rpc_payload["openDialogAction"] = open_dialog_action
        if done is not None:
            rpc_payload["done"] = done
        return cast(
            ProtobufMessage, await self.rpc("ketf", "InvokeCustomAction", **rpc_payload)
        )

    async def make_payment(
        self: Any,
        payment_session_id: str | None = None,
        payment_option_id: str | None = None,
        wallet: Any | None = None,
        gateway: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.MakePayment` operation.

        Parameters:
        payment_session_id: Wire field `paymentSessionId` (str | None).
        payment_option_id: Wire field `paymentOptionId` (str | None).
        wallet: Wire field `wallet` (Any | None).
        gateway: Wire field `gateway` (Any | None).

        Returns fields: gatewayRedirect, paymentReceipt.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if payment_session_id is not None:
            rpc_payload["paymentSessionId"] = payment_session_id
        if payment_option_id is not None:
            rpc_payload["paymentOptionId"] = payment_option_id
        if wallet is not None:
            rpc_payload["wallet"] = wallet
        if gateway is not None:
            rpc_payload["gateway"] = gateway
        return cast(
            ProtobufMessage, await self.rpc("ketf", "MakePayment", **rpc_payload)
        )

    async def send_authenticated_inline_call_back_data(
        self: Any,
        template_message_id: Any | None = None,
        data: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.SendAuthenticatedInlineCallBackData` operation.

        Parameters:
        template_message_id: Wire field `templateMessageId` (Any | None).
        data: Wire field `data` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if template_message_id is not None:
            rpc_payload["templateMessageId"] = template_message_id
        if data is not None:
            rpc_payload["data"] = data
        return cast(
            ProtobufMessage,
            await self.rpc(
                "ketf", "SendAuthenticatedInlineCallBackData", **rpc_payload
            ),
        )

    async def send_inline_call_back_data(
        self: Any,
        history_message_identifier: Any | None = None,
        data: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.SendInlineCallBackData` operation.

        Parameters:
        history_message_identifier: Wire field `historyMessageIdentifier` (Any | None).
        data: Wire field `data` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if history_message_identifier is not None:
            rpc_payload["historyMessageIdentifier"] = history_message_identifier
        if data is not None:
            rpc_payload["data"] = data
        return cast(
            ProtobufMessage,
            await self.rpc("ketf", "SendInlineCallBackData", **rpc_payload),
        )

    async def send_inline_callback(
        self: Any,
        peer: Any | None = None,
        message_id: Any | None = None,
        data: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.SendInlineCallback` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_id: Wire field `messageId` (Any | None).
        data: Wire field `data` (Any | None).

        Returns fields: answer.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        if data is not None:
            rpc_payload["data"] = data
        return cast(
            ProtobufMessage, await self.rpc("ketf", "SendInlineCallback", **rpc_payload)
        )

    async def send_mini_app_data(
        self: Any,
        bot_user_id: int | None = None,
        query_id: Any | None = None,
        data: Any | None = None,
        button_text: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ketf.v1.Ketf.SendMiniAppData` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).
        query_id: Wire field `queryId` (Any | None).
        data: Wire field `data` (Any | None).
        button_text: Wire field `buttonText` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        if query_id is not None:
            rpc_payload["queryId"] = query_id
        if data is not None:
            rpc_payload["data"] = data
        if button_text is not None:
            rpc_payload["buttonText"] = button_text
        return cast(
            ProtobufMessage, await self.rpc("ketf", "SendMiniAppData", **rpc_payload)
        )

    async def cash_out(
        self: Any,
        request_id: str | None = None,
        token: str | None = None,
        amount: int | None = None,
        account: Any | None = None,
        pan: Any | None = None,
        iban: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CashOut` operation.

        Parameters:
        request_id: Wire field `requestId` (str | None).
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).
        account: Wire field `account` (Any | None).
        pan: Wire field `pan` (Any | None).
        iban: Wire field `iban` (Any | None).

        Returns fields: referenceNo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if request_id is not None:
            rpc_payload["requestId"] = request_id
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        if account is not None:
            rpc_payload["account"] = account
        if pan is not None:
            rpc_payload["pan"] = pan
        if iban is not None:
            rpc_payload["iban"] = iban
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CashOut", **rpc_payload)
        )

    async def charge(
        self: Any,
        payment_token: str | None = None,
        reference_no: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.Charge` operation.

        Parameters:
        payment_token: Wire field `paymentToken` (str | None).
        reference_no: Wire field `referenceNo` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if payment_token is not None:
            rpc_payload["paymentToken"] = payment_token
        if reference_no is not None:
            rpc_payload["referenceNo"] = reference_no
        return cast(ProtobufMessage, await self.rpc("kifpool", "Charge", **rpc_payload))

    async def check_charge_permission(
        self: Any, payment_token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CheckChargePermission` operation.

        Parameters:
        payment_token: Wire field `paymentToken` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if payment_token is not None:
            rpc_payload["paymentToken"] = payment_token
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "CheckChargePermission", **rpc_payload),
        )

    async def create_kifpool(
        self: Any, national_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CreateKifpool` operation.

        Parameters:
        national_id: Wire field `nationalId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_id is not None:
            rpc_payload["nationalId"] = national_id
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CreateKifpool", **rpc_payload)
        )

    async def crypto_cash_out(
        self: Any,
        request_id: str | None = None,
        amount: int | None = None,
        account: Any | None = None,
        pan: Any | None = None,
        pocket_type: int | None = None,
        is_merchant: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CryptoCashOut` operation.

        Parameters:
        request_id: Wire field `requestId` (str | None).
        amount: Wire field `amount` (int | None).
        account: Wire field `account` (Any | None).
        pan: Wire field `pan` (Any | None).
        pocket_type: Wire field `pocketType` (int | None).
        is_merchant: Wire field `isMerchant` (Any | None).

        Returns fields: referenceNo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if request_id is not None:
            rpc_payload["requestId"] = request_id
        if amount is not None:
            rpc_payload["amount"] = amount
        if account is not None:
            rpc_payload["account"] = account
        if pan is not None:
            rpc_payload["pan"] = pan
        if pocket_type is not None:
            rpc_payload["pocketType"] = pocket_type
        if is_merchant is not None:
            rpc_payload["isMerchant"] = is_merchant
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoCashOut", **rpc_payload)
        )

    async def crypto_invoice(
        self: Any,
        token: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CryptoInvoice` operation.

        Parameters:
        token: Wire field `token` (str | None).
        page_size: Wire field `pageSize` (int | None).
        page_number: Wire field `pageNumber` (int | None).

        Returns fields: records.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if page_size is not None:
            rpc_payload["pageSize"] = page_size
        if page_number is not None:
            rpc_payload["pageNumber"] = page_number
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoInvoice", **rpc_payload)
        )

    async def crypto_purchase(
        self: Any,
        amount: int | None = None,
        src_token: str | None = None,
        dst_token: str | None = None,
        description: str | None = None,
        terminal_id: str | None = None,
        borna_trx_id: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CryptoPurchase` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        src_token: Wire field `srcToken` (str | None).
        dst_token: Wire field `dstToken` (str | None).
        description: Wire field `description` (str | None).
        terminal_id: Wire field `terminalId` (str | None).
        borna_trx_id: Wire field `bornaTrxId` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if src_token is not None:
            rpc_payload["srcToken"] = src_token
        if dst_token is not None:
            rpc_payload["dstToken"] = dst_token
        if description is not None:
            rpc_payload["description"] = description
        if terminal_id is not None:
            rpc_payload["terminalId"] = terminal_id
        if borna_trx_id is not None:
            rpc_payload["bornaTrxId"] = borna_trx_id
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoPurchase", **rpc_payload)
        )

    async def crypto_refund(
        self: Any,
        token: str | None = None,
        amount: int | None = None,
        approval_code: int | None = None,
        trx_ref_src: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CryptoRefund` operation.

        Parameters:
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).
        approval_code: Wire field `approvalCode` (int | None).
        trx_ref_src: Wire field `trxRefSrc` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        if approval_code is not None:
            rpc_payload["approvalCode"] = approval_code
        if trx_ref_src is not None:
            rpc_payload["trxRefSrc"] = trx_ref_src
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoRefund", **rpc_payload)
        )

    async def crypto_transfer(
        self: Any,
        amount: int | None = None,
        src_token: str | None = None,
        dst_token: str | None = None,
        description: Any | None = None,
        dst_phone_no: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.CryptoTransfer` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        src_token: Wire field `srcToken` (str | None).
        dst_token: Wire field `dstToken` (str | None).
        description: Wire field `description` (Any | None).
        dst_phone_no: Wire field `dstPhoneNo` (Any | None).

        Returns fields: amount, date, approvalCode, srcToken, dstToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if src_token is not None:
            rpc_payload["srcToken"] = src_token
        if dst_token is not None:
            rpc_payload["dstToken"] = dst_token
        if description is not None:
            rpc_payload["description"] = description
        if dst_phone_no is not None:
            rpc_payload["dstPhoneNo"] = dst_phone_no
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoTransfer", **rpc_payload)
        )

    async def get_charge_payment_token(
        self: Any,
        token: str | None = None,
        amount: int | None = None,
        callback_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetChargePaymentToken` operation.

        Parameters:
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).
        callback_type: Wire field `callbackType` (int | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        if callback_type is not None:
            rpc_payload["callbackType"] = callback_type
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetChargePaymentToken", **rpc_payload),
        )

    async def get_credit(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetCredit` operation.

        Returns fields: balance, hasCredit.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("kifpool", "GetCredit", **rpc_payload)
        )

    async def get_crypto_charge_payment_token(
        self: Any,
        token: str | None = None,
        amount: int | None = None,
        receiver_id: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetCryptoChargePaymentToken` operation.

        Parameters:
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).
        receiver_id: Wire field `receiverId` (str | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        if receiver_id is not None:
            rpc_payload["receiverId"] = receiver_id
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetCryptoChargePaymentToken", **rpc_payload),
        )

    async def get_crypto_wallets(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetCryptoWallets` operation.

        Returns fields: myCryptoWallets.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetCryptoWallets", **rpc_payload),
        )

    async def get_kifpool_owner(
        self: Any, wallet_token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetKifpoolOwner` operation.

        Parameters:
        wallet_token: Wire field `walletToken` (str | None).

        Returns fields: firstName, lastName, walletStatus, approvalCode.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_token is not None:
            rpc_payload["walletToken"] = wallet_token
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "GetKifpoolOwner", **rpc_payload)
        )

    async def get_kifpool_point_balance(
        self: Any, token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetKifpoolPointBalance` operation.

        Parameters:
        token: Wire field `token` (str | None).

        Returns fields: pointBalanceInfo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointBalance", **rpc_payload),
        )

    async def get_kifpool_point_details(
        self: Any,
        token: str | None = None,
        count: int | None = None,
        page: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetKifpoolPointDetails` operation.

        Parameters:
        token: Wire field `token` (str | None).
        count: Wire field `count` (int | None).
        page: Wire field `page` (int | None).

        Returns fields: pointDetailsInfo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if count is not None:
            rpc_payload["count"] = count
        if page is not None:
            rpc_payload["page"] = page
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointDetails", **rpc_payload),
        )

    async def get_kifpool_point_summery(
        self: Any, token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetKifpoolPointSummery` operation.

        Parameters:
        token: Wire field `token` (str | None).

        Returns fields: pointSummeryInfo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointSummery", **rpc_payload),
        )

    async def get_kifpool_transaction_point(
        self: Any,
        transaction_id: int | None = None,
        amount: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.GetKifpoolTransactionPoint` operation.

        Parameters:
        transaction_id: Wire field `transactionID` (int | None).
        amount: Wire field `amount` (int | None).

        Returns fields: calculatedPoint, point, unitAmount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_id is not None:
            rpc_payload["transactionID"] = transaction_id
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolTransactionPoint", **rpc_payload),
        )

    async def invoice(
        self: Any,
        token: str | None = None,
        page_size: int | None = None,
        page_number: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.Invoice` operation.

        Parameters:
        token: Wire field `token` (str | None).
        page_size: Wire field `pageSize` (int | None).
        page_number: Wire field `pageNumber` (int | None).

        Returns fields: records.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if page_size is not None:
            rpc_payload["pageSize"] = page_size
        if page_number is not None:
            rpc_payload["pageNumber"] = page_number
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "Invoice", **rpc_payload)
        )

    async def pay_for_message(
        self: Any,
        amount: int | None = None,
        charge_amount: int | None = None,
        message: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.PayForMessage` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        charge_amount: Wire field `chargeAmount` (int | None).
        message: Wire field `message` (Any | None).

        Returns fields: status, paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if charge_amount is not None:
            rpc_payload["chargeAmount"] = charge_amount
        if message is not None:
            rpc_payload["message"] = message
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "PayForMessage", **rpc_payload)
        )

    async def purchase(
        self: Any,
        amount: int | None = None,
        dst_token: str | None = None,
        src_token: str | None = None,
        description: str | None = None,
        use_credit: Any | None = None,
        coupon_id: Any | None = None,
        terminal_no: Any | None = None,
        stan: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.Purchase` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        dst_token: Wire field `dstToken` (str | None).
        src_token: Wire field `srcToken` (str | None).
        description: Wire field `description` (str | None).
        use_credit: Wire field `useCredit` (Any | None).
        coupon_id: Wire field `couponId` (Any | None).
        terminal_no: Wire field `terminalNo` (Any | None).
        stan: Wire field `stan` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if dst_token is not None:
            rpc_payload["dstToken"] = dst_token
        if src_token is not None:
            rpc_payload["srcToken"] = src_token
        if description is not None:
            rpc_payload["description"] = description
        if use_credit is not None:
            rpc_payload["useCredit"] = use_credit
        if coupon_id is not None:
            rpc_payload["couponId"] = coupon_id
        if terminal_no is not None:
            rpc_payload["terminalNo"] = terminal_no
        if stan is not None:
            rpc_payload["stan"] = stan
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "Purchase", **rpc_payload)
        )

    async def purchase_message(
        self: Any,
        history_id: Any | None = None,
        amount: Any | None = None,
        description: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.PurchaseMessage` operation.

        Parameters:
        history_id: Wire field `historyId` (Any | None).
        amount: Wire field `amount` (Any | None).
        description: Wire field `description` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if history_id is not None:
            rpc_payload["historyId"] = history_id
        if amount is not None:
            rpc_payload["amount"] = amount
        if description is not None:
            rpc_payload["description"] = description
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "PurchaseMessage", **rpc_payload)
        )

    async def purchase_message_with_charge(
        self: Any,
        history_id: Any | None = None,
        amount: Any | None = None,
        description: Any | None = None,
        charge_amount: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.PurchaseMessageWithCharge` operation.

        Parameters:
        history_id: Wire field `historyId` (Any | None).
        amount: Wire field `amount` (Any | None).
        description: Wire field `description` (Any | None).
        charge_amount: Wire field `chargeAmount` (int | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if history_id is not None:
            rpc_payload["historyId"] = history_id
        if amount is not None:
            rpc_payload["amount"] = amount
        if description is not None:
            rpc_payload["description"] = description
        if charge_amount is not None:
            rpc_payload["chargeAmount"] = charge_amount
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "PurchaseMessageWithCharge", **rpc_payload),
        )

    async def purchase_with_charge(
        self: Any,
        amount: int | None = None,
        dst_token: str | None = None,
        src_token: str | None = None,
        description: str | None = None,
        charge_amount: int | None = None,
        use_credit: Any | None = None,
        coupon_id: Any | None = None,
        terminal_no: Any | None = None,
        stan: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.PurchaseWithCharge` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        dst_token: Wire field `dstToken` (str | None).
        src_token: Wire field `srcToken` (str | None).
        description: Wire field `description` (str | None).
        charge_amount: Wire field `chargeAmount` (int | None).
        use_credit: Wire field `useCredit` (Any | None).
        coupon_id: Wire field `couponId` (Any | None).
        terminal_no: Wire field `terminalNo` (Any | None).
        stan: Wire field `stan` (Any | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if dst_token is not None:
            rpc_payload["dstToken"] = dst_token
        if src_token is not None:
            rpc_payload["srcToken"] = src_token
        if description is not None:
            rpc_payload["description"] = description
        if charge_amount is not None:
            rpc_payload["chargeAmount"] = charge_amount
        if use_credit is not None:
            rpc_payload["useCredit"] = use_credit
        if coupon_id is not None:
            rpc_payload["couponId"] = coupon_id
        if terminal_no is not None:
            rpc_payload["terminalNo"] = terminal_no
        if stan is not None:
            rpc_payload["stan"] = stan
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "PurchaseWithCharge", **rpc_payload),
        )

    async def transfer(
        self: Any,
        source_token: str | None = None,
        destination_token: Any | None = None,
        destination_phone: Any | None = None,
        destination_userid: Any | None = None,
        amount: int | None = None,
        description: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.Transfer` operation.

        Parameters:
        source_token: Wire field `sourceToken` (str | None).
        destination_token: Wire field `destinationToken` (Any | None).
        destination_phone: Wire field `destinationPhone` (Any | None).
        destination_userid: Wire field `destinationUserid` (Any | None).
        amount: Wire field `amount` (int | None).
        description: Wire field `description` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if source_token is not None:
            rpc_payload["sourceToken"] = source_token
        if destination_token is not None:
            rpc_payload["destinationToken"] = destination_token
        if destination_phone is not None:
            rpc_payload["destinationPhone"] = destination_phone
        if destination_userid is not None:
            rpc_payload["destinationUserid"] = destination_userid
        if amount is not None:
            rpc_payload["amount"] = amount
        if description is not None:
            rpc_payload["description"] = description
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "Transfer", **rpc_payload)
        )

    async def upgrade_kifpool(
        self: Any,
        token: str | None = None,
        national_id: Any | None = None,
        card_no: Any | None = None,
        account_no: Any | None = None,
        remain_reference_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.UpgradeKifpool` operation.

        Parameters:
        token: Wire field `token` (str | None).
        national_id: Wire field `nationalId` (Any | None).
        card_no: Wire field `cardNo` (Any | None).
        account_no: Wire field `accountNo` (Any | None).
        remain_reference_number: Wire field `remainReferenceNumber` (str | None).

        Returns fields: level.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if national_id is not None:
            rpc_payload["nationalId"] = national_id
        if card_no is not None:
            rpc_payload["cardNo"] = card_no
        if account_no is not None:
            rpc_payload["accountNo"] = account_no
        if remain_reference_number is not None:
            rpc_payload["remainReferenceNumber"] = remain_reference_number
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "UpgradeKifpool", **rpc_payload)
        )

    async def verify_cash_out_kifpool(
        self: Any, token: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.VerifyCashOutKifpool` operation.

        Parameters:
        token: Wire field `token` (str | None).

        Returns fields: accountNo, firstName, lastName.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "VerifyCashOutKifpool", **rpc_payload),
        )

    async def verify_purchase_message(
        self: Any, history_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.VerifyPurchaseMessage` operation.

        Parameters:
        history_id: Wire field `historyId` (Any | None).

        Returns fields: amount, paymentTypeTitle, paymentTitle.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if history_id is not None:
            rpc_payload["historyId"] = history_id
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "VerifyPurchaseMessage", **rpc_payload),
        )

    async def get_auth_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.llm_auth.v1.LLMAuthService.GetAuthToken` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("llmauthservice", "GetAuthToken", **rpc_payload),
        )

    async def get_message_upvoters(
        self: Any,
        load_more_state: Any | None = None,
        message: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.GetMessageUpvoters` operation.

        Parameters:
        load_more_state: Wire field `loadMoreState` (Any | None).
        message: Wire field `message` (Any | None).

        Returns fields: loadMoreState, users.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        if message is not None:
            rpc_payload["message"] = message
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "GetMessageUpvoters", **rpc_payload),
        )

    async def get_my_upvotes(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.GetMyUpvotes` operation.

        Returns fields: upvotes.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("magazine", "GetMyUpvotes", **rpc_payload)
        )

    async def get_similar_posts(
        self: Any,
        message: Any | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.GetSimilarPosts` operation.

        Parameters:
        message: Wire field `message` (Any | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: messages, loadMoreState, similarPosts.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message is not None:
            rpc_payload["message"] = message
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "GetSimilarPosts", **rpc_payload),
        )

    async def load_categories(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.LoadCategories` operation.

        Returns fields: categories.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("magazine", "LoadCategories", **rpc_payload)
        )

    async def load_category_feed_messages(
        self: Any,
        category_id: int | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.LoadCategoryFeedMessages` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: loadMoreState, messages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "LoadCategoryFeedMessages", **rpc_payload),
        )

    async def load_feed_messages(
        self: Any, load_more_state: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.LoadFeedMessages` operation.

        Parameters:
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: loadMoreState, messages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "LoadFeedMessages", **rpc_payload),
        )

    async def load_internal_feed_messages(
        self: Any, load_more_state: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.LoadInternalFeedMessages` operation.

        Parameters:
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: loadMoreState, messages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "LoadInternalFeedMessages", **rpc_payload),
        )

    async def revoke_upvoted_post(
        self: Any,
        message: Any | None = None,
        album_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.magazine.v1.Magazine.RevokeUpvotedPost` operation.

        Parameters:
        message: Wire field `message` (Any | None).
        album_id: Wire field `albumId` (Any | None).

        Returns fields: upvotes.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message is not None:
            rpc_payload["message"] = message
        if album_id is not None:
            rpc_payload["albumId"] = album_id
        return cast(
            ProtobufMessage,
            await self.rpc("magazine", "RevokeUpvotedPost", **rpc_payload),
        )

    async def accept_campaign_market(
        self: Any,
        market_id: int | None = None,
        is_permanent: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.AcceptCampaignMarket` operation.

        Parameters:
        market_id: Wire field `marketId` (int | None).
        is_permanent: Wire field `isPermanent` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if market_id is not None:
            rpc_payload["marketId"] = market_id
        if is_permanent is not None:
            rpc_payload["isPermanent"] = is_permanent
        return cast(
            ProtobufMessage,
            await self.rpc("market", "AcceptCampaignMarket", **rpc_payload),
        )

    async def accept_market_join_request(
        self: Any,
        market_peer_id: int | None = None,
        request_id: int | None = None,
        display_name: str | None = None,
        category_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.AcceptMarketJoinRequest` operation.

        Parameters:
        market_peer_id: Wire field `marketPeerId` (int | None).
        request_id: Wire field `requestId` (int | None).
        display_name: Wire field `displayName` (str | None).
        category_id: Wire field `categoryId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if market_peer_id is not None:
            rpc_payload["marketPeerId"] = market_peer_id
        if request_id is not None:
            rpc_payload["requestId"] = request_id
        if display_name is not None:
            rpc_payload["displayName"] = display_name
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        return cast(
            ProtobufMessage,
            await self.rpc("market", "AcceptMarketJoinRequest", **rpc_payload),
        )

    async def create_market_join_request(
        self: Any,
        market_peer_id: int | None = None,
        display_name: str | None = None,
        category_id: int | None = None,
        tag_ids: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.CreateMarketJoinRequest` operation.

        Parameters:
        market_peer_id: Wire field `marketPeerId` (int | None).
        display_name: Wire field `displayName` (str | None).
        category_id: Wire field `categoryId` (int | None).
        tag_ids: Wire field `tagIds` (Iterable[int] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if market_peer_id is not None:
            rpc_payload["marketPeerId"] = market_peer_id
        if display_name is not None:
            rpc_payload["displayName"] = display_name
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if tag_ids is not None:
            rpc_payload["tagIds"] = tag_ids
        return cast(
            ProtobufMessage,
            await self.rpc("market", "CreateMarketJoinRequest", **rpc_payload),
        )

    async def create_tag(
        self: Any,
        title: str | None = None,
        category_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.CreateTag` operation.

        Parameters:
        title: Wire field `title` (str | None).
        category_id: Wire field `categoryId` (int | None).

        Returns fields: tag.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if title is not None:
            rpc_payload["title"] = title
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        return cast(
            ProtobufMessage, await self.rpc("market", "CreateTag", **rpc_payload)
        )

    async def get_categories_list(
        self: Any,
        category_id: int | None = None,
        level: Any | None = None,
        include_sample_markets: Any | None = None,
        version: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetCategoriesList` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).
        level: Wire field `level` (Any | None).
        include_sample_markets: Wire field `includeSampleMarkets` (Any | None).
        version: Wire field `version` (Any | None).

        Returns fields: categories, version.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if level is not None:
            rpc_payload["level"] = level
        if include_sample_markets is not None:
            rpc_payload["includeSampleMarkets"] = include_sample_markets
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetCategoriesList", **rpc_payload),
        )

    async def get_category_markets(
        self: Any,
        category_id: int | None = None,
        pagination: Any | None = None,
        version: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetCategoryMarkets` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).
        pagination: Wire field `pagination` (Any | None).
        version: Wire field `version` (int | None).

        Returns fields: markets, version.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetCategoryMarkets", **rpc_payload),
        )

    async def get_category_products(
        self: Any,
        category_id: int | None = None,
        pagination: Any | None = None,
        version: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetCategoryProducts` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).
        pagination: Wire field `pagination` (Any | None).
        version: Wire field `version` (int | None).

        Returns fields: products, version.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetCategoryProducts", **rpc_payload),
        )

    async def get_indexed_products(
        self: Any,
        start_date: int | None = None,
        end_date: int | None = None,
        category_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetIndexedProducts` operation.

        Parameters:
        start_date: Wire field `startDate` (int | None).
        end_date: Wire field `endDate` (int | None).
        category_id: Wire field `categoryId` (int | None).

        Returns fields: products.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if start_date is not None:
            rpc_payload["startDate"] = start_date
        if end_date is not None:
            rpc_payload["endDate"] = end_date
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetIndexedProducts", **rpc_payload),
        )

    async def get_market(
        self: Any,
        peer_id: int | None = None,
        nick_name: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetMarket` operation.

        Parameters:
        peer_id: Wire field `peerId` (int | None).
        nick_name: Wire field `nickName` (str | None).

        Returns fields: market, lastRequest.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if nick_name is not None:
            rpc_payload["nickName"] = nick_name
        return cast(
            ProtobufMessage, await self.rpc("market", "GetMarket", **rpc_payload)
        )

    async def get_market_join_requests(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetMarketJoinRequests` operation.

        Returns fields: marketJoinRequests.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetMarketJoinRequests", **rpc_payload),
        )

    async def get_markets_pending_join_request(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetMarketsPendingJoinRequest` operation.

        Returns fields: requests.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetMarketsPendingJoinRequest", **rpc_payload),
        )

    async def get_number_of_sales(
        self: Any, peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetNumberOfSales` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).

        Returns fields: numberOfSales, isMarket.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage, await self.rpc("market", "GetNumberOfSales", **rpc_payload)
        )

    async def get_onboarding_status(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetOnboardingStatus` operation.

        Returns fields: status, categoryIds, gender.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetOnboardingStatus", **rpc_payload),
        )

    async def get_pending_campaign_markets(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetPendingCampaignMarkets` operation.

        Returns fields: markets.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("market", "GetPendingCampaignMarkets", **rpc_payload),
        )

    async def get_stores(
        self: Any, version: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetStores` operation.

        Parameters:
        version: Wire field `version` (int | None).

        Returns fields: stores, version.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage, await self.rpc("market", "GetStores", **rpc_payload)
        )

    async def get_tags(
        self: Any, category_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetTags` operation.

        Parameters:
        category_id: Wire field `categoryId` (int | None).

        Returns fields: tags.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_id is not None:
            rpc_payload["categoryId"] = category_id
        return cast(ProtobufMessage, await self.rpc("market", "GetTags", **rpc_payload))

    async def get_top_markets(
        self: Any,
        rating_type: int | None = None,
        pagination: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetTopMarkets` operation.

        Parameters:
        rating_type: Wire field `ratingType` (int | None).
        pagination: Wire field `pagination` (Any | None).

        Returns fields: markets.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if rating_type is not None:
            rpc_payload["ratingType"] = rating_type
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        return cast(
            ProtobufMessage, await self.rpc("market", "GetTopMarkets", **rpc_payload)
        )

    async def get_yalda_stores(
        self: Any, version: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.GetYaldaStores` operation.

        Parameters:
        version: Wire field `version` (int | None).

        Returns fields: stores, version.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if version is not None:
            rpc_payload["version"] = version
        return cast(
            ProtobufMessage, await self.rpc("market", "GetYaldaStores", **rpc_payload)
        )

    async def reject_campaign_market(
        self: Any,
        market_id: int | None = None,
        is_permanent: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.RejectCampaignMarket` operation.

        Parameters:
        market_id: Wire field `marketId` (int | None).
        is_permanent: Wire field `isPermanent` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if market_id is not None:
            rpc_payload["marketId"] = market_id
        if is_permanent is not None:
            rpc_payload["isPermanent"] = is_permanent
        return cast(
            ProtobufMessage,
            await self.rpc("market", "RejectCampaignMarket", **rpc_payload),
        )

    async def reject_market_join_request(
        self: Any,
        market_peer_id: int | None = None,
        reject_cause: int | None = None,
        request_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.RejectMarketJoinRequest` operation.

        Parameters:
        market_peer_id: Wire field `marketPeerId` (int | None).
        reject_cause: Wire field `rejectCause` (int | None).
        request_id: Wire field `requestId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if market_peer_id is not None:
            rpc_payload["marketPeerId"] = market_peer_id
        if reject_cause is not None:
            rpc_payload["rejectCause"] = reject_cause
        if request_id is not None:
            rpc_payload["requestId"] = request_id
        return cast(
            ProtobufMessage,
            await self.rpc("market", "RejectMarketJoinRequest", **rpc_payload),
        )

    async def set_generic_deep_links(
        self: Any, links: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.SetGenericDeepLinks` operation.

        Parameters:
        links: Wire field `links` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if links is not None:
            rpc_payload["links"] = links
        return cast(
            ProtobufMessage,
            await self.rpc("market", "SetGenericDeepLinks", **rpc_payload),
        )

    async def set_market_banners(
        self: Any, banners: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.SetMarketBanners` operation.

        Parameters:
        banners: Wire field `banners` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if banners is not None:
            rpc_payload["banners"] = banners
        return cast(
            ProtobufMessage, await self.rpc("market", "SetMarketBanners", **rpc_payload)
        )

    async def set_onboarding_data(
        self: Any,
        category_ids: Iterable[int] | None = None,
        gender: int | None = None,
        is_skipped: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.SetOnboardingData` operation.

        Parameters:
        category_ids: Wire field `categoryIds` (Iterable[int] | None).
        gender: Wire field `gender` (int | None).
        is_skipped: Wire field `isSkipped` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if category_ids is not None:
            rpc_payload["categoryIds"] = category_ids
        if gender is not None:
            rpc_payload["gender"] = gender
        if is_skipped is not None:
            rpc_payload["isSkipped"] = is_skipped
        return cast(
            ProtobufMessage,
            await self.rpc("market", "SetOnboardingData", **rpc_payload),
        )

    async def set_popular_searches(
        self: Any, items: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.SetPopularSearches` operation.

        Parameters:
        items: Wire field `items` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if items is not None:
            rpc_payload["items"] = items
        return cast(
            ProtobufMessage,
            await self.rpc("market", "SetPopularSearches", **rpc_payload),
        )

    async def submit_market_feedback(
        self: Any,
        rate: int | None = None,
        user_opinion: Any | None = None,
        client_version: Any | None = None,
        extra_fields: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.SubmitMarketFeedback` operation.

        Parameters:
        rate: Wire field `rate` (int | None).
        user_opinion: Wire field `userOpinion` (Any | None).
        client_version: Wire field `clientVersion` (Any | None).
        extra_fields: Wire field `extraFields` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if rate is not None:
            rpc_payload["rate"] = rate
        if user_opinion is not None:
            rpc_payload["userOpinion"] = user_opinion
        if client_version is not None:
            rpc_payload["clientVersion"] = client_version
        if extra_fields is not None:
            rpc_payload["extraFields"] = extra_fields
        return cast(
            ProtobufMessage,
            await self.rpc("market", "SubmitMarketFeedback", **rpc_payload),
        )

    async def update_market_info(
        self: Any,
        peer_id: int | None = None,
        display_name: Any | None = None,
        primary_category_id: Any | None = None,
        is_banned: Any | None = None,
        is_active: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.market.v1.Market.UpdateMarketInfo` operation.

        Parameters:
        peer_id: Wire field `peerId` (int | None).
        display_name: Wire field `displayName` (Any | None).
        primary_category_id: Wire field `primaryCategoryId` (Any | None).
        is_banned: Wire field `isBanned` (Any | None).
        is_active: Wire field `isActive` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if display_name is not None:
            rpc_payload["displayName"] = display_name
        if primary_category_id is not None:
            rpc_payload["primaryCategoryId"] = primary_category_id
        if is_banned is not None:
            rpc_payload["isBanned"] = is_banned
        if is_active is not None:
            rpc_payload["isActive"] = is_active
        return cast(
            ProtobufMessage, await self.rpc("market", "UpdateMarketInfo", **rpc_payload)
        )

    async def get_difference(
        self: Any,
        route_sequences: Iterable[Any] | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.maviz.v1.MavizStream.GetDifference` operation.

        Parameters:
        route_sequences: Wire field `routeSequences` (Iterable[Any] | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: groupEvents, usersRefs, groupsRefs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if route_sequences is not None:
            rpc_payload["routeSequences"] = route_sequences
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage,
            await self.rpc("mavizstream", "GetDifference", **rpc_payload),
        )

    async def subscribe_to_thread_updates(
        self: Any, peer: Any | None = None, thread_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.maviz.v1.MavizStream.SubscribeToThreadUpdates` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        thread_id: Wire field `threadId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if thread_id is not None:
            rpc_payload["threadId"] = thread_id
        return cast(
            ProtobufMessage,
            await self.rpc("mavizstream", "SubscribeToThreadUpdates", **rpc_payload),
        )

    async def subscribe_to_updates(
        self: Any, is_mt_proto: bool | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.maviz.v1.MavizStream.SubscribeToUpdates` operation.

        Parameters:
        is_mt_proto: Wire field `isMtProto` (bool | None).

        Returns fields: update, routeId, sequence, timestamp, weakEvent, mtupdate, updates.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if is_mt_proto is not None:
            rpc_payload["isMtProto"] = is_mt_proto
        return cast(
            ProtobufMessage,
            await self.rpc("mavizstream", "SubscribeToUpdates", **rpc_payload),
        )

    async def unsubscribe_from_thread_updates(
        self: Any, peer: Any | None = None, thread_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.maviz.v1.MavizStream.UnsubscribeFromThreadUpdates` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        thread_id: Wire field `threadId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if thread_id is not None:
            rpc_payload["threadId"] = thread_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "mavizstream", "UnsubscribeFromThreadUpdates", **rpc_payload
            ),
        )

    async def delete_stream(
        self: Any, stream_user: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.DeleteStream` operation.

        Parameters:
        stream_user: Wire field `streamUser` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if stream_user is not None:
            rpc_payload["streamUser"] = stream_user
        return cast(
            ProtobufMessage, await self.rpc("meet", "DeleteStream", **rpc_payload)
        )

    async def get_wss_url(
        self: Any, call_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.GetWssURL` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).

        Returns fields: url.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        return cast(ProtobufMessage, await self.rpc("meet", "GetWssURL", **rpc_payload))

    async def mute_participant(
        self: Any,
        call_id: int | None = None,
        identity: str | None = None,
        track_id: str | None = None,
        revoke_publish_permission: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.MuteParticipant` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).
        identity: Wire field `identity` (str | None).
        track_id: Wire field `trackId` (str | None).
        revoke_publish_permission: Wire field `revokePublishPermission` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        if identity is not None:
            rpc_payload["identity"] = identity
        if track_id is not None:
            rpc_payload["trackId"] = track_id
        if revoke_publish_permission is not None:
            rpc_payload["revokePublishPermission"] = revoke_publish_permission
        return cast(
            ProtobufMessage, await self.rpc("meet", "MuteParticipant", **rpc_payload)
        )

    async def remove_participant(
        self: Any,
        call_id: int | None = None,
        identity: str | None = None,
        block_from_call: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.RemoveParticipant` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).
        identity: Wire field `identity` (str | None).
        block_from_call: Wire field `blockFromCall` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        if identity is not None:
            rpc_payload["identity"] = identity
        if block_from_call is not None:
            rpc_payload["blockFromCall"] = block_from_call
        return cast(
            ProtobufMessage, await self.rpc("meet", "RemoveParticipant", **rpc_payload)
        )

    async def send_fanoos_event(
        self: Any,
        event_name: str | None = None,
        items: Any | None = None,
        date: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.SendFanoosEvent` operation.

        Parameters:
        event_name: Wire field `eventName` (str | None).
        items: Wire field `items` (Any | None).
        date: Wire field `date` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if event_name is not None:
            rpc_payload["eventName"] = event_name
        if items is not None:
            rpc_payload["items"] = items
        if date is not None:
            rpc_payload["date"] = date
        return cast(
            ProtobufMessage, await self.rpc("meet", "SendFanoosEvent", **rpc_payload)
        )

    async def set_link_title(
        self: Any,
        title: str | None = None,
        call_id: Any | None = None,
        link_url: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.SetLinkTitle` operation.

        Parameters:
        title: Wire field `title` (str | None).
        call_id: Wire field `callId` (Any | None).
        link_url: Wire field `linkUrl` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if title is not None:
            rpc_payload["title"] = title
        if call_id is not None:
            rpc_payload["callId"] = call_id
        if link_url is not None:
            rpc_payload["linkUrl"] = link_url
        return cast(
            ProtobufMessage, await self.rpc("meet", "SetLinkTitle", **rpc_payload)
        )

    async def start_recording(
        self: Any,
        call_id: int | None = None,
        layout: str | None = None,
        quality: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.StartRecording` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).
        layout: Wire field `layout` (str | None).
        quality: Wire field `quality` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        if layout is not None:
            rpc_payload["layout"] = layout
        if quality is not None:
            rpc_payload["quality"] = quality
        return cast(
            ProtobufMessage, await self.rpc("meet", "StartRecording", **rpc_payload)
        )

    async def start_stream(
        self: Any,
        stream_user: Any | None = None,
        url: str | None = None,
        rtmp_server: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.StartStream` operation.

        Parameters:
        stream_user: Wire field `streamUser` (Any | None).
        url: Wire field `url` (str | None).
        rtmp_server: Wire field `rtmpServer` (str | None).

        Returns fields: streamKey.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if stream_user is not None:
            rpc_payload["streamUser"] = stream_user
        if url is not None:
            rpc_payload["url"] = url
        if rtmp_server is not None:
            rpc_payload["rtmpServer"] = rtmp_server
        return cast(
            ProtobufMessage, await self.rpc("meet", "StartStream", **rpc_payload)
        )

    async def stop_recording(
        self: Any, call_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.StopRecording` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        return cast(
            ProtobufMessage, await self.rpc("meet", "StopRecording", **rpc_payload)
        )

    async def update_layout(
        self: Any,
        call_id: int | None = None,
        requested_layout: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.meet.v1.Meet.UpdateLayout` operation.

        Parameters:
        call_id: Wire field `callId` (int | None).
        requested_layout: Wire field `requestedLayout` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if call_id is not None:
            rpc_payload["callId"] = call_id
        if requested_layout is not None:
            rpc_payload["requestedLayout"] = requested_layout
        return cast(
            ProtobufMessage, await self.rpc("meet", "UpdateLayout", **rpc_payload)
        )

    async def cancel_message_stream(
        self: Any,
        ex_peer: Any | None = None,
        message_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.message_stream.v1.MessageStream.CancelMessageStream` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage,
            await self.rpc("messagestream", "CancelMessageStream", **rpc_payload),
        )

    async def receive_message_stream(
        self: Any,
        ex_peer: Any | None = None,
        message_id: Any | None = None,
        from_chunk_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.message_stream.v1.MessageStream.ReceiveMessageStream` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        message_id: Wire field `messageId` (Any | None).
        from_chunk_id: Wire field `fromChunkId` (Any | None).

        Returns fields: chunkTimeoutMillis.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        if from_chunk_id is not None:
            rpc_payload["fromChunkId"] = from_chunk_id
        return cast(
            ProtobufMessage,
            await self.rpc("messagestream", "ReceiveMessageStream", **rpc_payload),
        )

    async def create_reserved_folder(
        self: Any, folder_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.CreateReservedFolder` operation.

        Parameters:
        folder_id: Wire field `folderId` (int | None).

        Returns fields: index, unreadPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "CreateReservedFolder", **rpc_payload),
        )

    async def create_thread(
        self: Any,
        peer: Any | None = None,
        date: int | None = None,
        random_id: int | None = None,
        title: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.CreateThread` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        date: Wire field `date` (int | None).
        random_id: Wire field `randomId` (int | None).
        title: Wire field `title` (str | None).

        Returns fields: threadId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if date is not None:
            rpc_payload["date"] = date
        if random_id is not None:
            rpc_payload["randomId"] = random_id
        if title is not None:
            rpc_payload["title"] = title
        return cast(
            ProtobufMessage, await self.rpc("messaging", "CreateThread", **rpc_payload)
        )

    async def create_topic(
        self: Any, ex_peer: Any | None = None, title: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.CreateTopic` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        title: Wire field `title` (str | None).

        Returns fields: topicId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if title is not None:
            rpc_payload["title"] = title
        return cast(
            ProtobufMessage, await self.rpc("messaging", "CreateTopic", **rpc_payload)
        )

    async def delete_topic(
        self: Any,
        ex_peer: Any | None = None,
        topic_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.DeleteTopic` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        topic_id: Wire field `topicId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if topic_id is not None:
            rpc_payload["topicId"] = topic_id
        return cast(
            ProtobufMessage, await self.rpc("messaging", "DeleteTopic", **rpc_payload)
        )

    async def edit_folder(
        self: Any,
        folder_id: int | None = None,
        name: str | None = None,
        added_peers: Iterable[Any] | None = None,
        deleted_peers: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.EditFolder` operation.

        Parameters:
        folder_id: Wire field `folderId` (int | None).
        name: Wire field `name` (str | None).
        added_peers: Wire field `addedPeers` (Iterable[Any] | None).
        deleted_peers: Wire field `deletedPeers` (Iterable[Any] | None).

        Returns fields: unreadPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        if name is not None:
            rpc_payload["name"] = name
        if added_peers is not None:
            rpc_payload["addedPeers"] = added_peers
        if deleted_peers is not None:
            rpc_payload["deletedPeers"] = deleted_peers
        return cast(
            ProtobufMessage, await self.rpc("messaging", "EditFolder", **rpc_payload)
        )

    async def edit_topic(
        self: Any,
        ex_peer: Any | None = None,
        topic_id: Any | None = None,
        title: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.EditTopic` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        topic_id: Wire field `topicId` (Any | None).
        title: Wire field `title` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if topic_id is not None:
            rpc_payload["topicId"] = topic_id
        if title is not None:
            rpc_payload["title"] = title
        return cast(
            ProtobufMessage, await self.rpc("messaging", "EditTopic", **rpc_payload)
        )

    async def fetch_protected_message(
        self: Any, peer: Any | None = None, message_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.FetchProtectedMessage` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns fields: history.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "FetchProtectedMessage", **rpc_payload),
        )

    async def forward_messages(
        self: Any,
        peer: Any | None = None,
        rid: Iterable[int] | None = None,
        forwarded_messages: Iterable[Any] | None = None,
        grouped_id: Any | None = None,
        hide_sender: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.ForwardMessages` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        rid: Wire field `rid` (Iterable[int] | None).
        forwarded_messages: Wire field `forwardedMessages` (Iterable[Any] | None).
        grouped_id: Wire field `groupedId` (Any | None).
        hide_sender: Wire field `hideSender` (bool | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if rid is not None:
            rpc_payload["rid"] = rid
        if forwarded_messages is not None:
            rpc_payload["forwardedMessages"] = forwarded_messages
        if grouped_id is not None:
            rpc_payload["groupedId"] = grouped_id
        if hide_sender is not None:
            rpc_payload["hideSender"] = hide_sender
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "ForwardMessages", **rpc_payload),
        )

    async def get_discussion_message(
        self: Any, peer: Any | None = None, message_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.GetDiscussionMessage` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns fields: discussionMessage.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "GetDiscussionMessage", **rpc_payload),
        )

    async def get_messages_replies_info(
        self: Any,
        peer: Any | None = None,
        mids: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.GetMessagesRepliesInfo` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        mids: Wire field `mids` (Iterable[Any] | None).

        Returns fields: containers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if mids is not None:
            rpc_payload["mids"] = mids
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "GetMessagesRepliesInfo", **rpc_payload),
        )

    async def get_topic_by_id(
        self: Any,
        ex_peer: Any | None = None,
        topic_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.GetTopicByID` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        topic_id: Wire field `topicId` (Any | None).

        Returns fields: topic.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if topic_id is not None:
            rpc_payload["topicId"] = topic_id
        return cast(
            ProtobufMessage, await self.rpc("messaging", "GetTopicByID", **rpc_payload)
        )

    async def get_topics(
        self: Any,
        ex_peer: Any | None = None,
        min_date: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.GetTopics` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        min_date: Wire field `minDate` (int | None).
        limit: Wire field `limit` (int | None).

        Returns fields: topics.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if min_date is not None:
            rpc_payload["minDate"] = min_date
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(
            ProtobufMessage, await self.rpc("messaging", "GetTopics", **rpc_payload)
        )

    async def load_folder_dialogs(
        self: Any,
        min_date: int | None = None,
        limit: int | None = None,
        folder_id: int | None = None,
        archive_filter: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadFolderDialogs` operation.

        Parameters:
        min_date: Wire field `minDate` (int | None).
        limit: Wire field `limit` (int | None).
        folder_id: Wire field `folderId` (int | None).
        archive_filter: Wire field `archiveFilter` (int | None).

        Returns fields: dialogs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if min_date is not None:
            rpc_payload["minDate"] = min_date
        if limit is not None:
            rpc_payload["limit"] = limit
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        if archive_filter is not None:
            rpc_payload["archiveFilter"] = archive_filter
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "LoadFolderDialogs", **rpc_payload),
        )

    async def load_folders(
        self: Any,
        include_muted_unread_peers: bool | None = None,
        is_new_user: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadFolders` operation.

        Parameters:
        include_muted_unread_peers: Wire field `includeMutedUnreadPeers` (bool | None).
        is_new_user: Wire field `isNewUser` (bool | None).

        Returns fields: folders, unreadPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if include_muted_unread_peers is not None:
            rpc_payload["includeMutedUnreadPeers"] = include_muted_unread_peers
        if is_new_user is not None:
            rpc_payload["isNewUser"] = is_new_user
        return cast(
            ProtobufMessage, await self.rpc("messaging", "LoadFolders", **rpc_payload)
        )

    async def load_grouped_dialogs(
        self: Any,
        optimizations: Iterable[int] | None = None,
        archive_filter: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadGroupedDialogs` operation.

        Parameters:
        optimizations: Wire field `optimizations` (Iterable[int] | None).
        archive_filter: Wire field `archiveFilter` (int | None).

        Returns fields: dialogs, users, groups, showArchived, showInvite, userPeers, groupPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        if archive_filter is not None:
            rpc_payload["archiveFilter"] = archive_filter
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "LoadGroupedDialogs", **rpc_payload),
        )

    async def load_peer_dialogs(
        self: Any, peers: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadPeerDialogs` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).

        Returns fields: dialogs, groups, users, userPeers, groupPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "LoadPeerDialogs", **rpc_payload),
        )

    async def load_peers(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadPeers` operation.

        Returns fields: exPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("messaging", "LoadPeers", **rpc_payload)
        )

    async def load_pinned_dialogs(
        self: Any, folder_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadPinnedDialogs` operation.

        Parameters:
        folder_id: Wire field `folderId` (int | None).

        Returns fields: dialogs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "LoadPinnedDialogs", **rpc_payload),
        )

    async def load_replies(
        self: Any,
        peer: Any | None = None,
        thread_id: Any | None = None,
        date: int | None = None,
        load_mode: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.LoadReplies` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        thread_id: Wire field `threadId` (Any | None).
        date: Wire field `date` (int | None).
        load_mode: Wire field `loadMode` (int | None).
        limit: Wire field `limit` (int | None).

        Returns fields: history, users, userPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if thread_id is not None:
            rpc_payload["threadId"] = thread_id
        if date is not None:
            rpc_payload["date"] = date
        if load_mode is not None:
            rpc_payload["loadMode"] = load_mode
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(
            ProtobufMessage, await self.rpc("messaging", "LoadReplies", **rpc_payload)
        )

    async def mark_dialogs_as_read(
        self: Any, peers: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.MarkDialogsAsRead` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "MarkDialogsAsRead", **rpc_payload),
        )

    async def mark_dialogs_as_unread(
        self: Any, peers: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.MarkDialogsAsUnread` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "MarkDialogsAsUnread", **rpc_payload),
        )

    async def mention_read(
        self: Any, peer: Any | None = None, message_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.MentionRead` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage, await self.rpc("messaging", "MentionRead", **rpc_payload)
        )

    async def message_received(
        self: Any, peer: Any | None = None, date: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.MessageReceived` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        date: Wire field `date` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if date is not None:
            rpc_payload["date"] = date
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "MessageReceived", **rpc_payload),
        )

    async def pin_dialogs(
        self: Any,
        peers: Iterable[Any] | None = None,
        folder_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.PinDialogs` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).
        folder_id: Wire field `folderId` (int | None).

        Returns fields: dialogs, peers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        return cast(
            ProtobufMessage, await self.rpc("messaging", "PinDialogs", **rpc_payload)
        )

    async def reorder_folders(
        self: Any, folder_ids: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.ReorderFolders` operation.

        Parameters:
        folder_ids: Wire field `folderIds` (Iterable[int] | None).

        Returns fields: folderIds.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if folder_ids is not None:
            rpc_payload["folderIds"] = folder_ids
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "ReorderFolders", **rpc_payload),
        )

    async def reorder_pinned_dialogs(
        self: Any,
        peers: Iterable[Any] | None = None,
        folder_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.ReorderPinnedDialogs` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).
        folder_id: Wire field `folderId` (int | None).

        Returns fields: dialogs, peers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "ReorderPinnedDialogs", **rpc_payload),
        )

    async def un_archive_dialogs(
        self: Any, ex_peers: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.UnArchiveDialogs` operation.

        Parameters:
        ex_peers: Wire field `exPeers` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peers is not None:
            rpc_payload["exPeers"] = ex_peers
        return cast(
            ProtobufMessage,
            await self.rpc("messaging", "UnArchiveDialogs", **rpc_payload),
        )

    async def un_pin_messages(
        self: Any,
        peer: Any | None = None,
        message_ids: Iterable[Any] | None = None,
        all: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.UnPinMessages` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        message_ids: Wire field `messageIds` (Iterable[Any] | None).
        all: Wire field `all` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if message_ids is not None:
            rpc_payload["messageIds"] = message_ids
        if all is not None:
            rpc_payload["all"] = all
        return cast(
            ProtobufMessage, await self.rpc("messaging", "UnPinMessages", **rpc_payload)
        )

    async def unpin_dialogs(
        self: Any,
        peers: Iterable[Any] | None = None,
        folder_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.UnpinDialogs` operation.

        Parameters:
        peers: Wire field `peers` (Iterable[Any] | None).
        folder_id: Wire field `folderId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peers is not None:
            rpc_payload["peers"] = peers
        if folder_id is not None:
            rpc_payload["folderId"] = folder_id
        return cast(
            ProtobufMessage, await self.rpc("messaging", "UnpinDialogs", **rpc_payload)
        )

    async def update_message(
        self: Any,
        peer: Any | None = None,
        rid: int | None = None,
        updated_message: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.messaging.v2.Messaging.UpdateMessage` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).
        rid: Wire field `rid` (int | None).
        updated_message: Wire field `updatedMessage` (Any | None).

        Returns fields: seq, date, state, ext, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        if rid is not None:
            rpc_payload["rid"] = rid
        if updated_message is not None:
            rpc_payload["updatedMessage"] = updated_message
        return cast(
            ProtobufMessage, await self.rpc("messaging", "UpdateMessage", **rpc_payload)
        )

    async def get_bam_service_token(
        self: Any, service: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.microbanki.v1.MicroBanki.GetBamServiceToken` operation.

        Parameters:
        service: Wire field `service` (int | None).

        Returns fields: endpoint, token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if service is not None:
            rpc_payload["service"] = service
        return cast(
            ProtobufMessage,
            await self.rpc("microbanki", "GetBamServiceToken", **rpc_payload),
        )

    async def get_money_request_details(
        self: Any, message: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.microbanki.v1.MicroBanki.GetMoneyRequestDetails` operation.

        Parameters:
        message: Wire field `message` (Any | None).

        Returns fields: totalAmount, payCount, lastPayDate, responseType.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message is not None:
            rpc_payload["message"] = message
        return cast(
            ProtobufMessage,
            await self.rpc("microbanki", "GetMoneyRequestDetails", **rpc_payload),
        )

    async def get_money_request_payment_list(
        self: Any,
        message: Any | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.microbanki.v1.MicroBanki.GetMoneyRequestPaymentList` operation.

        Parameters:
        message: Wire field `message` (Any | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: payment, loadMoreState, responseType, userPeers, groupPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message is not None:
            rpc_payload["message"] = message
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage,
            await self.rpc("microbanki", "GetMoneyRequestPaymentList", **rpc_payload),
        )

    async def get_my_bank(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.my_bank.v1.MyBank.GetMyBank` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("mybank", "GetMyBank", **rpc_payload)
        )

    async def get_message_seen_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.negah.v1.Negah.GetMessageSeenList` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("negah", "GetMessageSeenList", **rpc_payload),
        )

    async def get_user_organization_info(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.organizations.v1.Organizations.GetUserOrganizationInfo` operation.

        Returns fields: userOrganization.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("organizations", "GetUserOrganizationInfo", **rpc_payload),
        )

    async def get_user_organizational_contacts(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.organizations.v1.Organizations.GetUserOrganizationalContacts` operation.

        Returns fields: userPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc(
                "organizations", "GetUserOrganizationalContacts", **rpc_payload
            ),
        )

    async def add_detail_to_transaction(
        self: Any, id_: Any | None = None, detail: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.AddDetailToTransaction` operation.

        Parameters:
        id_: Wire field `id` (Any | None).
        detail: Wire field `detail` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if detail is not None:
            rpc_payload["detail"] = detail
        return cast(
            ProtobufMessage,
            await self.rpc("pfm", "AddDetailToTransaction", **rpc_payload),
        )

    async def add_transaction_tags(
        self: Any,
        id_: Any | None = None,
        tags: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.AddTransactionTags` operation.

        Parameters:
        id_: Wire field `id` (Any | None).
        tags: Wire field `tags` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if tags is not None:
            rpc_payload["tags"] = tags
        return cast(
            ProtobufMessage, await self.rpc("pfm", "AddTransactionTags", **rpc_payload)
        )

    async def add_user_tags(
        self: Any, tags: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.AddUserTags` operation.

        Parameters:
        tags: Wire field `tags` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if tags is not None:
            rpc_payload["tags"] = tags
        return cast(
            ProtobufMessage, await self.rpc("pfm", "AddUserTags", **rpc_payload)
        )

    async def filter_tagged_transactions(
        self: Any, ids: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.FilterTaggedTransactions` operation.

        Parameters:
        ids: Wire field `ids` (Iterable[Any] | None).

        Returns fields: idsWithTag.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ids is not None:
            rpc_payload["ids"] = ids
        return cast(
            ProtobufMessage,
            await self.rpc("pfm", "FilterTaggedTransactions", **rpc_payload),
        )

    async def get_sub_transactions(
        self: Any, transaction_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.GetSubTransactions` operation.

        Parameters:
        transaction_id: Wire field `transactionId` (Any | None).

        Returns fields: transactionIds.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_id is not None:
            rpc_payload["transactionId"] = transaction_id
        return cast(
            ProtobufMessage, await self.rpc("pfm", "GetSubTransactions", **rpc_payload)
        )

    async def get_transaction_tags(
        self: Any, id_: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.GetTransactionTags` operation.

        Parameters:
        id_: Wire field `id` (Any | None).

        Returns fields: tags.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage, await self.rpc("pfm", "GetTransactionTags", **rpc_payload)
        )

    async def get_user_accounts(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.GetUserAccounts` operation.

        Returns fields: accounts, config.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("pfm", "GetUserAccounts", **rpc_payload)
        )

    async def get_user_tags(
        self: Any, get_user_tag_type: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.GetUserTags` operation.

        Parameters:
        get_user_tag_type: Wire field `getUserTagType` (int | None).

        Returns fields: tags.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if get_user_tag_type is not None:
            rpc_payload["getUserTagType"] = get_user_tag_type
        return cast(
            ProtobufMessage, await self.rpc("pfm", "GetUserTags", **rpc_payload)
        )

    async def load_transactions(
        self: Any,
        account_number: int | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        transaction_type: int | None = None,
        label: Iterable[Any] | None = None,
        limit: int | None = None,
        load_more_state: Any | None = None,
        load_mode: int | None = None,
        user_tag_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.LoadTransactions` operation.

        Parameters:
        account_number: Wire field `accountNumber` (int | None).
        start_date: Wire field `startDate` (Any | None).
        end_date: Wire field `endDate` (Any | None).
        transaction_type: Wire field `transactionType` (int | None).
        label: Wire field `label` (Iterable[Any] | None).
        limit: Wire field `limit` (int | None).
        load_more_state: Wire field `loadMoreState` (Any | None).
        load_mode: Wire field `loadMode` (int | None).
        user_tag_type: Wire field `userTagType` (int | None).

        Returns fields: transactions, totalAmounts, loadMoreState, totalAmountsPerDay.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if account_number is not None:
            rpc_payload["accountNumber"] = account_number
        if start_date is not None:
            rpc_payload["startDate"] = start_date
        if end_date is not None:
            rpc_payload["endDate"] = end_date
        if transaction_type is not None:
            rpc_payload["transactionType"] = transaction_type
        if label is not None:
            rpc_payload["label"] = label
        if limit is not None:
            rpc_payload["limit"] = limit
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        if load_mode is not None:
            rpc_payload["loadMode"] = load_mode
        if user_tag_type is not None:
            rpc_payload["userTagType"] = user_tag_type
        return cast(
            ProtobufMessage, await self.rpc("pfm", "LoadTransactions", **rpc_payload)
        )

    async def load_transactions_by_i_ds(
        self: Any, transaction_ids: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.LoadTransactionsByIDs` operation.

        Parameters:
        transaction_ids: Wire field `transactionIds` (Iterable[Any] | None).

        Returns fields: transactions.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_ids is not None:
            rpc_payload["transactionIds"] = transaction_ids
        return cast(
            ProtobufMessage,
            await self.rpc("pfm", "LoadTransactionsByIDs", **rpc_payload),
        )

    async def remove_transaction(
        self: Any, transaction_ids: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.RemoveTransaction` operation.

        Parameters:
        transaction_ids: Wire field `transactionIds` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_ids is not None:
            rpc_payload["transactionIds"] = transaction_ids
        return cast(
            ProtobufMessage, await self.rpc("pfm", "RemoveTransaction", **rpc_payload)
        )

    async def remove_transaction_tags(
        self: Any,
        id_: Any | None = None,
        tags: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.RemoveTransactionTags` operation.

        Parameters:
        id_: Wire field `id` (Any | None).
        tags: Wire field `tags` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if tags is not None:
            rpc_payload["tags"] = tags
        return cast(
            ProtobufMessage,
            await self.rpc("pfm", "RemoveTransactionTags", **rpc_payload),
        )

    async def remove_user_tags(
        self: Any, tags: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.RemoveUserTags` operation.

        Parameters:
        tags: Wire field `tags` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if tags is not None:
            rpc_payload["tags"] = tags
        return cast(
            ProtobufMessage, await self.rpc("pfm", "RemoveUserTags", **rpc_payload)
        )

    async def revive_transaction(
        self: Any, transaction_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.ReviveTransaction` operation.

        Parameters:
        transaction_id: Wire field `transactionId` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_id is not None:
            rpc_payload["transactionId"] = transaction_id
        return cast(
            ProtobufMessage, await self.rpc("pfm", "ReviveTransaction", **rpc_payload)
        )

    async def split_transaction(
        self: Any,
        transaction_id: Any | None = None,
        units: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.pfm.v1.Pfm.SplitTransaction` operation.

        Parameters:
        transaction_id: Wire field `transactionId` (Any | None).
        units: Wire field `units` (Iterable[Any] | None).

        Returns fields: splitTransactionIds.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_id is not None:
            rpc_payload["transactionId"] = transaction_id
        if units is not None:
            rpc_payload["units"] = units
        return cast(
            ProtobufMessage, await self.rpc("pfm", "SplitTransaction", **rpc_payload)
        )

    async def create_poll(
        self: Any,
        poll_message: Any | None = None,
        create_at: int | None = None,
        expeer: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.poll.v1.Poll.CreatePoll` operation.

        Parameters:
        poll_message: Wire field `pollMessage` (Any | None).
        create_at: Wire field `createAt` (int | None).
        expeer: Wire field `expeer` (Any | None).

        Returns fields: pollId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if poll_message is not None:
            rpc_payload["pollMessage"] = poll_message
        if create_at is not None:
            rpc_payload["createAt"] = create_at
        if expeer is not None:
            rpc_payload["expeer"] = expeer
        return cast(
            ProtobufMessage, await self.rpc("poll", "CreatePoll", **rpc_payload)
        )

    async def get_full_poll_result(
        self: Any, poll_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.poll.v1.Poll.GetFullPollResult` operation.

        Parameters:
        poll_id: Wire field `pollId` (int | None).

        Returns fields: fullPollResult.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if poll_id is not None:
            rpc_payload["pollId"] = poll_id
        return cast(
            ProtobufMessage, await self.rpc("poll", "GetFullPollResult", **rpc_payload)
        )

    async def vote(
        self: Any,
        poll_id: int | None = None,
        is_retract: bool | None = None,
        vote_at: int | None = None,
        option_ids: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.poll.v1.Poll.Vote` operation.

        Parameters:
        poll_id: Wire field `pollId` (int | None).
        is_retract: Wire field `isRetract` (bool | None).
        vote_at: Wire field `voteAt` (int | None).
        option_ids: Wire field `optionIds` (Iterable[int] | None).

        Returns fields: pollResult.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if poll_id is not None:
            rpc_payload["pollId"] = poll_id
        if is_retract is not None:
            rpc_payload["isRetract"] = is_retract
        if vote_at is not None:
            rpc_payload["voteAt"] = vote_at
        if option_ids is not None:
            rpc_payload["optionIds"] = option_ids
        return cast(ProtobufMessage, await self.rpc("poll", "Vote", **rpc_payload))

    async def calculate_discounted_price(
        self: Any,
        package_id: int | None = None,
        coupon_code: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.CalculateDiscountedPrice` operation.

        Parameters:
        package_id: Wire field `packageId` (int | None).
        coupon_code: Wire field `couponCode` (str | None).

        Returns fields: discountedPrice.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if package_id is not None:
            rpc_payload["packageId"] = package_id
        if coupon_code is not None:
            rpc_payload["couponCode"] = coupon_code
        return cast(
            ProtobufMessage,
            await self.rpc("premium", "CalculateDiscountedPrice", **rpc_payload),
        )

    async def get_badges(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.GetBadges` operation.

        Returns fields: categories.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("premium", "GetBadges", **rpc_payload)
        )

    async def get_packages(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.GetPackages` operation.

        Returns fields: packages, bundles.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("premium", "GetPackages", **rpc_payload)
        )

    async def is_premium(
        self: Any,
        user_id: int | None = None,
        with_detail_option: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.IsPremium` operation.

        Parameters:
        user_id: Wire field `userId` (int | None).
        with_detail_option: Wire field `withDetailOption` (Any | None).

        Returns fields: userStatus.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_id is not None:
            rpc_payload["userId"] = user_id
        if with_detail_option is not None:
            rpc_payload["withDetailOption"] = with_detail_option
        return cast(
            ProtobufMessage, await self.rpc("premium", "IsPremium", **rpc_payload)
        )

    async def is_premium_batch(
        self: Any,
        user_ids: Iterable[int] | None = None,
        with_detail_option: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.IsPremiumBatch` operation.

        Parameters:
        user_ids: Wire field `userIds` (Iterable[int] | None).
        with_detail_option: Wire field `withDetailOption` (Any | None).

        Returns fields: usersStatus.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_ids is not None:
            rpc_payload["userIds"] = user_ids
        if with_detail_option is not None:
            rpc_payload["withDetailOption"] = with_detail_option
        return cast(
            ProtobufMessage, await self.rpc("premium", "IsPremiumBatch", **rpc_payload)
        )

    async def purchase_package(
        self: Any,
        package_id: int | None = None,
        coupon_code: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.PurchasePackage` operation.

        Parameters:
        package_id: Wire field `packageId` (int | None).
        coupon_code: Wire field `couponCode` (Any | None).

        Returns fields: sadadPaymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if package_id is not None:
            rpc_payload["packageId"] = package_id
        if coupon_code is not None:
            rpc_payload["couponCode"] = coupon_code
        return cast(
            ProtobufMessage, await self.rpc("premium", "PurchasePackage", **rpc_payload)
        )

    async def set_user_badge(
        self: Any, badge_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.premium.v1.Premium.SetUserBadge` operation.

        Parameters:
        badge_id: Wire field `badgeId` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if badge_id is not None:
            rpc_payload["badgeId"] = badge_id
        return cast(
            ProtobufMessage, await self.rpc("premium", "SetUserBadge", **rpc_payload)
        )

    async def get_contacts_presences(
        self: Any, limit: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.GetContactsPresences` operation.

        Parameters:
        limit: Wire field `limit` (Any | None).

        Returns fields: presences.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "GetContactsPresences", **rpc_payload),
        )

    async def get_group_members_presences(
        self: Any, peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.GetGroupMembersPresences` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).

        Returns fields: presences.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "GetGroupMembersPresences", **rpc_payload),
        )

    async def get_group_online_count(
        self: Any, peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.GetGroupOnlineCount` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).

        Returns fields: count.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "GetGroupOnlineCount", **rpc_payload),
        )

    async def get_users_presence(
        self: Any, user_ids: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.GetUsersPresence` operation.

        Parameters:
        user_ids: Wire field `userIds` (Iterable[int] | None).

        Returns fields: presences.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_ids is not None:
            rpc_payload["userIds"] = user_ids
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "GetUsersPresence", **rpc_payload),
        )

    async def subscribe_from_group_online(
        self: Any, groups: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.SubscribeFromGroupOnline` operation.

        Parameters:
        groups: Wire field `groups` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if groups is not None:
            rpc_payload["groups"] = groups
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "SubscribeFromGroupOnline", **rpc_payload),
        )

    async def subscribe_from_online(
        self: Any, users: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.SubscribeFromOnline` operation.

        Parameters:
        users: Wire field `users` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if users is not None:
            rpc_payload["users"] = users
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "SubscribeFromOnline", **rpc_payload),
        )

    async def subscribe_to_group_online(
        self: Any, groups: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.SubscribeToGroupOnline` operation.

        Parameters:
        groups: Wire field `groups` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if groups is not None:
            rpc_payload["groups"] = groups
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "SubscribeToGroupOnline", **rpc_payload),
        )

    async def subscribe_to_online(
        self: Any, users: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.presence.v1.Presence.SubscribeToOnline` operation.

        Parameters:
        users: Wire field `users` (Iterable[Any] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if users is not None:
            rpc_payload["users"] = users
        return cast(
            ProtobufMessage,
            await self.rpc("presence", "SubscribeToOnline", **rpc_payload),
        )

    async def check_password(
        self: Any,
        password: str | None = None,
        services_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.CheckPassword` operation.

        Parameters:
        password: Wire field `password` (str | None).
        services_type: Wire field `servicesType` (int | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if password is not None:
            rpc_payload["password"] = password
        if services_type is not None:
            rpc_payload["servicesType"] = services_type
        return cast(
            ProtobufMessage, await self.rpc("ramz", "CheckPassword", **rpc_payload)
        )

    async def check_password_set(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.CheckPasswordSet` operation.

        Returns fields: hasSet, isSessionAuthorized.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("ramz", "CheckPasswordSet", **rpc_payload)
        )

    async def delete_password(
        self: Any, otp: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.DeletePassword` operation.

        Parameters:
        otp: Wire field `otp` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if otp is not None:
            rpc_payload["otp"] = otp
        return cast(
            ProtobufMessage, await self.rpc("ramz", "DeletePassword", **rpc_payload)
        )

    async def forget_password(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.ForgetPassword` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("ramz", "ForgetPassword", **rpc_payload)
        )

    async def send_otp(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.SendOTP` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(ProtobufMessage, await self.rpc("ramz", "SendOTP", **rpc_payload))

    async def set_password(
        self: Any, password: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.SetPassword` operation.

        Parameters:
        password: Wire field `password` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if password is not None:
            rpc_payload["password"] = password
        return cast(
            ProtobufMessage, await self.rpc("ramz", "SetPassword", **rpc_payload)
        )

    async def validate_otp(
        self: Any,
        otp: int | None = None,
        services_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.ramz.v1.Ramz.ValidateOTP` operation.

        Parameters:
        otp: Wire field `otp` (int | None).
        services_type: Wire field `servicesType` (int | None).

        Returns fields: otpValid.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if otp is not None:
            rpc_payload["otp"] = otp
        if services_type is not None:
            rpc_payload["servicesType"] = services_type
        return cast(
            ProtobufMessage, await self.rpc("ramz", "ValidateOTP", **rpc_payload)
        )

    async def get_channel_recommendations(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.recommender.v1.Recommender.GetChannelRecommendations` operation.

        Returns fields: channels.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("recommender", "GetChannelRecommendations", **rpc_payload),
        )

    async def get_groups_recommendation(
        self: Any, source: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.recommender.v1.Recommender.GetGroupsRecommendation` operation.

        Parameters:
        source: Wire field `source` (int | None).

        Returns fields: groups.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if source is not None:
            rpc_payload["source"] = source
        return cast(
            ProtobufMessage,
            await self.rpc("recommender", "GetGroupsRecommendation", **rpc_payload),
        )

    async def get_related_channels(
        self: Any, ex_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.recommender.v1.Recommender.GetRelatedChannels` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).

        Returns fields: relatedChannels.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage,
            await self.rpc("recommender", "GetRelatedChannels", **rpc_payload),
        )

    async def get_related_groups(
        self: Any, ex_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.recommender.v1.Recommender.GetRelatedGroups` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).

        Returns fields: relatedGroups.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage,
            await self.rpc("recommender", "GetRelatedGroups", **rpc_payload),
        )

    async def report_dismiss(
        self: Any, ex_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.report.v1.Report.ReportDismiss` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage, await self.rpc("report", "ReportDismiss", **rpc_payload)
        )

    async def report_inappropriate_content(
        self: Any, report: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.report.v1.Report.ReportInappropriateContent` operation.

        Parameters:
        report: Wire field `report` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if report is not None:
            rpc_payload["report"] = report
        return cast(
            ProtobufMessage,
            await self.rpc("report", "ReportInappropriateContent", **rpc_payload),
        )

    async def add_destination_cards(
        self: Any, cards: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.AddDestinationCards` operation.

        Parameters:
        cards: Wire field `cards` (Iterable[Any] | None).

        Returns fields: ids.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if cards is not None:
            rpc_payload["cards"] = cards
        return cast(
            ProtobufMessage, await self.rpc("sap", "AddDestinationCards", **rpc_payload)
        )

    async def add_new_cards(
        self: Any, card_info: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.AddNewCards` operation.

        Parameters:
        card_info: Wire field `cardInfo` (Iterable[Any] | None).

        Returns fields: cardId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_info is not None:
            rpc_payload["cardInfo"] = card_info
        return cast(
            ProtobufMessage, await self.rpc("sap", "AddNewCards", **rpc_payload)
        )

    async def deliver_otp(
        self: Any,
        card_id: str | None = None,
        destination_pan: str | None = None,
        amount: int | None = None,
        access_address: str | None = None,
        approval_code: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.DeliverOtp` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).
        destination_pan: Wire field `destinationPan` (str | None).
        amount: Wire field `amount` (int | None).
        access_address: Wire field `accessAddress` (str | None).
        approval_code: Wire field `approvalCode` (str | None).

        Returns fields: isDone.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        if destination_pan is not None:
            rpc_payload["destinationPan"] = destination_pan
        if amount is not None:
            rpc_payload["amount"] = amount
        if access_address is not None:
            rpc_payload["accessAddress"] = access_address
        if approval_code is not None:
            rpc_payload["approvalCode"] = approval_code
        return cast(ProtobufMessage, await self.rpc("sap", "DeliverOtp", **rpc_payload))

    async def edit_card_expiration_date(
        self: Any,
        card_id: str | None = None,
        card_exp_date: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.EditCardExpirationDate` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).
        card_exp_date: Wire field `cardExpDate` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        if card_exp_date is not None:
            rpc_payload["cardExpDate"] = card_exp_date
        return cast(
            ProtobufMessage,
            await self.rpc("sap", "EditCardExpirationDate", **rpc_payload),
        )

    async def enroll_new_card(
        self: Any, origin: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.EnrollNewCard` operation.

        Parameters:
        origin: Wire field `origin` (Any | None).

        Returns fields: transactionId, url.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if origin is not None:
            rpc_payload["origin"] = origin
        return cast(
            ProtobufMessage, await self.rpc("sap", "EnrollNewCard", **rpc_payload)
        )

    async def get_card_info(
        self: Any,
        transaction_id: str | None = None,
        card_info: Any | None = None,
        card_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.GetCardInfo` operation.

        Parameters:
        transaction_id: Wire field `transactionId` (str | None).
        card_info: Wire field `cardInfo` (Any | None).
        card_id: Wire field `cardId` (Any | None).

        Returns fields: cardId, maskedPan.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transaction_id is not None:
            rpc_payload["transactionId"] = transaction_id
        if card_info is not None:
            rpc_payload["cardInfo"] = card_info
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        return cast(
            ProtobufMessage, await self.rpc("sap", "GetCardInfo", **rpc_payload)
        )

    async def get_cards(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.GetCards` operation.

        Returns fields: userCards.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(ProtobufMessage, await self.rpc("sap", "GetCards", **rpc_payload))

    async def get_default_card(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.GetDefaultCard` operation.

        Returns fields: cardId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sap", "GetDefaultCard", **rpc_payload)
        )

    async def get_destination_card_info(
        self: Any,
        card_id: str | None = None,
        destination_pan: str | None = None,
        amount: int | None = None,
        source_address: str | None = None,
        localize: int | None = None,
        target_user_id: Any | None = None,
        message_data: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.GetDestinationCardInfo` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).
        destination_pan: Wire field `destinationPan` (str | None).
        amount: Wire field `amount` (int | None).
        source_address: Wire field `sourceAddress` (str | None).
        localize: Wire field `localize` (int | None).
        target_user_id: Wire field `targetUserId` (Any | None).
        message_data: Wire field `messageData` (Any | None).

        Returns fields: cardHolderName, approvalCode.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        if destination_pan is not None:
            rpc_payload["destinationPan"] = destination_pan
        if amount is not None:
            rpc_payload["amount"] = amount
        if source_address is not None:
            rpc_payload["sourceAddress"] = source_address
        if localize is not None:
            rpc_payload["localize"] = localize
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        if message_data is not None:
            rpc_payload["messageData"] = message_data
        return cast(
            ProtobufMessage,
            await self.rpc("sap", "GetDestinationCardInfo", **rpc_payload),
        )

    async def get_destination_cards(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.GetDestinationCards` operation.

        Returns fields: cards.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sap", "GetDestinationCards", **rpc_payload)
        )

    async def reactivate_app(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.ReactivateApp` operation.

        Returns fields: transactionId, reactivationAddress.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sap", "ReactivateApp", **rpc_payload)
        )

    async def remove_card(
        self: Any, card_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.RemoveCard` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        return cast(ProtobufMessage, await self.rpc("sap", "RemoveCard", **rpc_payload))

    async def remove_default_card(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.RemoveDefaultCard` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sap", "RemoveDefaultCard", **rpc_payload)
        )

    async def remove_destination_cards(
        self: Any, ids: Iterable[str] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.RemoveDestinationCards` operation.

        Parameters:
        ids: Wire field `ids` (Iterable[str] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ids is not None:
            rpc_payload["ids"] = ids
        return cast(
            ProtobufMessage,
            await self.rpc("sap", "RemoveDestinationCards", **rpc_payload),
        )

    async def set_default_card(
        self: Any, card_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.SetDefaultCard` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        return cast(
            ProtobufMessage, await self.rpc("sap", "SetDefaultCard", **rpc_payload)
        )

    async def transfer_money_by_card(
        self: Any,
        card_id: str | None = None,
        transfer_code: int | None = None,
        destination_pan: str | None = None,
        amount: int | None = None,
        pin: str | None = None,
        cvv2: str | None = None,
        expiry_date: str | None = None,
        source_address: str | None = None,
        localize: int | None = None,
        approval_code: str | None = None,
        encrypted_transfer_info: Any | None = None,
        message_data: Any | None = None,
        target_user_id: Any | None = None,
        description: Any | None = None,
        ramz_token: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sap.v1.Sap.TransferMoneyByCard` operation.

        Parameters:
        card_id: Wire field `cardId` (str | None).
        transfer_code: Wire field `transferCode` (int | None).
        destination_pan: Wire field `destinationPan` (str | None).
        amount: Wire field `amount` (int | None).
        pin: Wire field `pin` (str | None).
        cvv2: Wire field `cvv2` (str | None).
        expiry_date: Wire field `expiryDate` (str | None).
        source_address: Wire field `sourceAddress` (str | None).
        localize: Wire field `localize` (int | None).
        approval_code: Wire field `approvalCode` (str | None).
        encrypted_transfer_info: Wire field `encryptedTransferInfo` (Any | None).
        message_data: Wire field `messageData` (Any | None).
        target_user_id: Wire field `targetUserId` (Any | None).
        description: Wire field `description` (Any | None).
        ramz_token: Wire field `ramzToken` (Any | None).

        Returns fields: traceNumber, transactionTime.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if card_id is not None:
            rpc_payload["cardId"] = card_id
        if transfer_code is not None:
            rpc_payload["transferCode"] = transfer_code
        if destination_pan is not None:
            rpc_payload["destinationPan"] = destination_pan
        if amount is not None:
            rpc_payload["amount"] = amount
        if pin is not None:
            rpc_payload["pin"] = pin
        if cvv2 is not None:
            rpc_payload["cvv2"] = cvv2
        if expiry_date is not None:
            rpc_payload["expiryDate"] = expiry_date
        if source_address is not None:
            rpc_payload["sourceAddress"] = source_address
        if localize is not None:
            rpc_payload["localize"] = localize
        if approval_code is not None:
            rpc_payload["approvalCode"] = approval_code
        if encrypted_transfer_info is not None:
            rpc_payload["encryptedTransferInfo"] = encrypted_transfer_info
        if message_data is not None:
            rpc_payload["messageData"] = message_data
        if target_user_id is not None:
            rpc_payload["targetUserId"] = target_user_id
        if description is not None:
            rpc_payload["description"] = description
        if ramz_token is not None:
            rpc_payload["ramzToken"] = ramz_token
        return cast(
            ProtobufMessage, await self.rpc("sap", "TransferMoneyByCard", **rpc_payload)
        )

    async def execute_task_now(
        self: Any, task_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.schedule.v1.Scheduler.ExecuteTaskNow` operation.

        Parameters:
        task_id: Wire field `taskID` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if task_id is not None:
            rpc_payload["taskID"] = task_id
        return cast(
            ProtobufMessage,
            await self.rpc("scheduler", "ExecuteTaskNow", **rpc_payload),
        )

    async def list_tasks(
        self: Any,
        ex_peer: Any | None = None,
        type_: int | None = None,
        status: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.schedule.v1.Scheduler.ListTasks` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        type_: Wire field `type` (int | None).
        status: Wire field `status` (int | None).

        Returns fields: tasks.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if type_ is not None:
            rpc_payload["type"] = type_
        if status is not None:
            rpc_payload["status"] = status
        return cast(
            ProtobufMessage, await self.rpc("scheduler", "ListTasks", **rpc_payload)
        )

    async def peers_with_schedule_task(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.schedule.v1.Scheduler.PeersWithScheduleTask` operation.

        Returns fields: exPeer.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("scheduler", "PeersWithScheduleTask", **rpc_payload),
        )

    async def re_schedule_task(
        self: Any,
        task_id: int | None = None,
        scheduled_at: int | None = None,
        payload: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.schedule.v1.Scheduler.ReScheduleTask` operation.

        Parameters:
        task_id: Wire field `taskID` (int | None).
        scheduled_at: Wire field `scheduledAt` (int | None).
        payload: Wire field `payload` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if task_id is not None:
            rpc_payload["taskID"] = task_id
        if scheduled_at is not None:
            rpc_payload["scheduledAt"] = scheduled_at
        if payload is not None:
            rpc_payload["payload"] = payload
        return cast(
            ProtobufMessage,
            await self.rpc("scheduler", "ReScheduleTask", **rpc_payload),
        )

    async def un_schedule_task(
        self: Any, task_ids: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.schedule.v1.Scheduler.UnScheduleTask` operation.

        Parameters:
        task_ids: Wire field `taskIDs` (Iterable[int] | None).

        Returns fields: failedTaskIDs.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if task_ids is not None:
            rpc_payload["taskIDs"] = task_ids
        return cast(
            ProtobufMessage,
            await self.rpc("scheduler", "UnScheduleTask", **rpc_payload),
        )

    async def recommend_peer(
        self: Any, ex_peer_type: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.RecommendPeer` operation.

        Parameters:
        ex_peer_type: Wire field `exPeerType` (int | None).

        Returns fields: peer.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer_type is not None:
            rpc_payload["exPeerType"] = ex_peer_type
        return cast(
            ProtobufMessage, await self.rpc("search", "RecommendPeer", **rpc_payload)
        )

    async def search_content(
        self: Any,
        query: Any | None = None,
        content_type: int | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchContent` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        content_type: Wire field `contentType` (int | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: contentResults, loadMoreState, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if content_type is not None:
            rpc_payload["contentType"] = content_type
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchContent", **rpc_payload)
        )

    async def search_dialog(
        self: Any, query: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchDialog` operation.

        Parameters:
        query: Wire field `query` (Any | None).

        Returns fields: dialogResults.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchDialog", **rpc_payload)
        )

    async def search_market(
        self: Any,
        query: Any | None = None,
        with_category: Any | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMarket` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        with_category: Wire field `withCategory` (Any | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: marketResults, category, loadMoreState, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if with_category is not None:
            rpc_payload["withCategory"] = with_category
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchMarket", **rpc_payload)
        )

    async def search_market_popular(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMarketPopular` operation.

        Returns fields: popularResults.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("search", "SearchMarketPopular", **rpc_payload),
        )

    async def search_media(
        self: Any,
        query: Any | None = None,
        date: Any | None = None,
        optimizations: Iterable[int] | None = None,
        load_mode: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMedia` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        date: Wire field `date` (Any | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).
        load_mode: Wire field `loadMode` (int | None).

        Returns fields: searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if date is not None:
            rpc_payload["date"] = date
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        if load_mode is not None:
            rpc_payload["loadMode"] = load_mode
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchMedia", **rpc_payload)
        )

    async def search_members(
        self: Any,
        query: Any | None = None,
        ex_peer: Any | None = None,
        load_more_state: Any | None = None,
        users: Iterable[Any] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMembers` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        ex_peer: Wire field `exPeer` (Any | None).
        load_more_state: Wire field `loadMoreState` (Any | None).
        users: Wire field `users` (Iterable[Any] | None).

        Returns fields: users, loadMoreState.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        if users is not None:
            rpc_payload["users"] = users
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchMembers", **rpc_payload)
        )

    async def search_message_more(
        self: Any,
        load_more_state: Any | None = None,
        query: Any | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMessageMore` operation.

        Parameters:
        load_more_state: Wire field `loadMoreState` (Any | None).
        query: Wire field `query` (Any | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        if query is not None:
            rpc_payload["query"] = query
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage,
            await self.rpc("search", "SearchMessageMore", **rpc_payload),
        )

    async def search_messages(
        self: Any,
        query: Any | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchMessages` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: searchResults, users, groups, loadMoreState, userOutPeers, groupOutPeers, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchMessages", **rpc_payload)
        )

    async def search_peer(
        self: Any,
        query: Iterable[Any] | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchPeer` operation.

        Parameters:
        query: Wire field `query` (Iterable[Any] | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: searchResults, users, groups, userPeers, groupPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchPeer", **rpc_payload)
        )

    async def search_product(
        self: Any,
        query: Any | None = None,
        load_more_state: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.SearchProduct` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        load_more_state: Wire field `loadMoreState` (Any | None).

        Returns fields: productResults, loadMoreState, resultCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if load_more_state is not None:
            rpc_payload["loadMoreState"] = load_more_state
        return cast(
            ProtobufMessage, await self.rpc("search", "SearchProduct", **rpc_payload)
        )

    async def update_search_content_click(
        self: Any,
        message_id: Any | None = None,
        search_tab: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.search.v1.Search.UpdateSearchContentClick` operation.

        Parameters:
        message_id: Wire field `messageId` (Any | None).
        search_tab: Wire field `searchTab` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        if search_tab is not None:
            rpc_payload["searchTab"] = search_tab
        return cast(
            ProtobufMessage,
            await self.rpc("search", "UpdateSearchContentClick", **rpc_payload),
        )

    async def get_active_shared_media(
        self: Any, ex_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.shared_media.v1.SharedMediaService.GetActiveSharedMedia` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).

        Returns fields: activeTab.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage,
            await self.rpc("sharedmediaservice", "GetActiveSharedMedia", **rpc_payload),
        )

    async def load_media(
        self: Any,
        ex_peer: Any | None = None,
        date: Any | None = None,
        content_type: int | None = None,
        load_mode: int | None = None,
        minimum_results: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.shared_media.v1.SharedMediaService.LoadMedia` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        date: Wire field `date` (Any | None).
        content_type: Wire field `contentType` (int | None).
        load_mode: Wire field `loadMode` (int | None).
        minimum_results: Wire field `minimumResults` (int | None).

        Returns fields: mediaResults.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if date is not None:
            rpc_payload["date"] = date
        if content_type is not None:
            rpc_payload["contentType"] = content_type
        if load_mode is not None:
            rpc_payload["loadMode"] = load_mode
        if minimum_results is not None:
            rpc_payload["minimumResults"] = minimum_results
        return cast(
            ProtobufMessage,
            await self.rpc("sharedmediaservice", "LoadMedia", **rpc_payload),
        )

    async def add_bot_story(
        self: Any,
        ex_peer: Any | None = None,
        media_story: Any | None = None,
        text_story: Any | None = None,
        tag_ids: Iterable[int] | None = None,
        expiration_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.AddBotStory` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        media_story: Wire field `mediaStory` (Any | None).
        text_story: Wire field `textStory` (Any | None).
        tag_ids: Wire field `tagIds` (Iterable[int] | None).
        expiration_type: Wire field `expirationType` (int | None).

        Returns fields: storyId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if media_story is not None:
            rpc_payload["mediaStory"] = media_story
        if text_story is not None:
            rpc_payload["textStory"] = text_story
        if tag_ids is not None:
            rpc_payload["tagIds"] = tag_ids
        if expiration_type is not None:
            rpc_payload["expirationType"] = expiration_type
        return cast(
            ProtobufMessage, await self.rpc("story", "AddBotStory", **rpc_payload)
        )

    async def add_channel_story(
        self: Any,
        ex_peer: Any | None = None,
        media_story: Any | None = None,
        has_reply: bool | None = None,
        tag_ids: Iterable[int] | None = None,
        expiration_type: int | None = None,
        text_story: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.AddChannelStory` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        media_story: Wire field `mediaStory` (Any | None).
        has_reply: Wire field `hasReply` (bool | None).
        tag_ids: Wire field `tagIds` (Iterable[int] | None).
        expiration_type: Wire field `expirationType` (int | None).
        text_story: Wire field `textStory` (Any | None).

        Returns fields: storyId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if media_story is not None:
            rpc_payload["mediaStory"] = media_story
        if has_reply is not None:
            rpc_payload["hasReply"] = has_reply
        if tag_ids is not None:
            rpc_payload["tagIds"] = tag_ids
        if expiration_type is not None:
            rpc_payload["expirationType"] = expiration_type
        if text_story is not None:
            rpc_payload["textStory"] = text_story
        return cast(
            ProtobufMessage, await self.rpc("story", "AddChannelStory", **rpc_payload)
        )

    async def add_story(
        self: Any,
        media_story: Any | None = None,
        text_story: Any | None = None,
        tag_ids: Iterable[int] | None = None,
        expiration_type: int | None = None,
        exception_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.AddStory` operation.

        Parameters:
        media_story: Wire field `mediaStory` (Any | None).
        text_story: Wire field `textStory` (Any | None).
        tag_ids: Wire field `tagIds` (Iterable[int] | None).
        expiration_type: Wire field `expirationType` (int | None).
        exception_type: Wire field `exceptionType` (int | None).

        Returns fields: storyId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if media_story is not None:
            rpc_payload["mediaStory"] = media_story
        if text_story is not None:
            rpc_payload["textStory"] = text_story
        if tag_ids is not None:
            rpc_payload["tagIds"] = tag_ids
        if expiration_type is not None:
            rpc_payload["expirationType"] = expiration_type
        if exception_type is not None:
            rpc_payload["exceptionType"] = exception_type
        return cast(ProtobufMessage, await self.rpc("story", "AddStory", **rpc_payload))

    async def can_add_bot_story(
        self: Any, bot_user_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.CanAddBotStory` operation.

        Parameters:
        bot_user_id: Wire field `botUserId` (int | None).

        Returns fields: canAddBotStory.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_user_id is not None:
            rpc_payload["botUserId"] = bot_user_id
        return cast(
            ProtobufMessage, await self.rpc("story", "CanAddBotStory", **rpc_payload)
        )

    async def check_link_validity(
        self: Any, ex_peer: Any | None = None, link: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.CheckLinkValidity` operation.

        Parameters:
        ex_peer: Wire field `exPeer` (Any | None).
        link: Wire field `link` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        if link is not None:
            rpc_payload["link"] = link
        return cast(
            ProtobufMessage, await self.rpc("story", "CheckLinkValidity", **rpc_payload)
        )

    async def get_bot_stories(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetBotStories` operation.

        Returns fields: result, popularityList.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("story", "GetBotStories", **rpc_payload)
        )

    async def get_channel_stories(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetChannelStories` operation.

        Returns fields: result, popularityList.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("story", "GetChannelStories", **rpc_payload)
        )

    async def get_default_story_backgrounds(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetDefaultStoryBackgrounds` operation.

        Returns fields: defaultStoryBackgrounds.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("story", "GetDefaultStoryBackgrounds", **rpc_payload),
        )

    async def get_most_popular_stories(
        self: Any,
        get_special_stories: Any | None = None,
        optimization: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetMostPopularStories` operation.

        Parameters:
        get_special_stories: Wire field `getSpecialStories` (Any | None).
        optimization: Wire field `optimization` (int | None).

        Returns fields: result, popularityList.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if get_special_stories is not None:
            rpc_payload["getSpecialStories"] = get_special_stories
        if optimization is not None:
            rpc_payload["optimization"] = optimization
        return cast(
            ProtobufMessage,
            await self.rpc("story", "GetMostPopularStories", **rpc_payload),
        )

    async def get_stories(
        self: Any, get_unmutual: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetStories` operation.

        Parameters:
        get_unmutual: Wire field `getUnmutual` (Any | None).

        Returns fields: result, popularityList.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if get_unmutual is not None:
            rpc_payload["getUnmutual"] = get_unmutual
        return cast(
            ProtobufMessage, await self.rpc("story", "GetStories", **rpc_payload)
        )

    async def get_stories_by_list(
        self: Any, ex_peers: Iterable[Any] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetStoriesByList` operation.

        Parameters:
        ex_peers: Wire field `exPeers` (Iterable[Any] | None).

        Returns fields: userStories, channelStories, botStories.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ex_peers is not None:
            rpc_payload["exPeers"] = ex_peers
        return cast(
            ProtobufMessage, await self.rpc("story", "GetStoriesByList", **rpc_payload)
        )

    async def get_story_by_id(
        self: Any, story_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetStoryById` operation.

        Parameters:
        story_id: Wire field `storyId` (str | None).

        Returns fields: result, channelStoryResult, botStoryResult.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if story_id is not None:
            rpc_payload["storyId"] = story_id
        return cast(
            ProtobufMessage, await self.rpc("story", "GetStoryById", **rpc_payload)
        )

    async def get_story_tags(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetStoryTags` operation.

        Returns fields: tags.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("story", "GetStoryTags", **rpc_payload)
        )

    async def get_story_widgets(
        self: Any, story_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetStoryWidgets` operation.

        Parameters:
        story_id: Wire field `storyId` (str | None).

        Returns fields: widgets.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if story_id is not None:
            rpc_payload["storyId"] = story_id
        return cast(
            ProtobufMessage, await self.rpc("story", "GetStoryWidgets", **rpc_payload)
        )

    async def get_user_privacy_config(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetUserPrivacyConfig` operation.

        Returns fields: result.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("story", "GetUserPrivacyConfig", **rpc_payload),
        )

    async def get_user_story_config(
        self: Any,
        key: Iterable[int] | None = None,
        ex_peer: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetUserStoryConfig` operation.

        Parameters:
        key: Wire field `key` (Iterable[int] | None).
        ex_peer: Wire field `exPeer` (Any | None).

        Returns fields: config.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if key is not None:
            rpc_payload["key"] = key
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage,
            await self.rpc("story", "GetUserStoryConfig", **rpc_payload),
        )

    async def get_viewers(
        self: Any,
        story_id: str | None = None,
        pagination: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetViewers` operation.

        Parameters:
        story_id: Wire field `storyId` (str | None).
        pagination: Wire field `pagination` (Any | None).

        Returns fields: viewers, viewCount, likeCount, linkClickCount, emojiCount, restoryCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if story_id is not None:
            rpc_payload["storyId"] = story_id
        if pagination is not None:
            rpc_payload["pagination"] = pagination
        return cast(
            ProtobufMessage, await self.rpc("story", "GetViewers", **rpc_payload)
        )

    async def get_viewers_count(
        self: Any, story_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.GetViewersCount` operation.

        Parameters:
        story_id: Wire field `storyId` (str | None).

        Returns fields: viewCount, likeCount, linkClickCount, emojiCount, restoryCount.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if story_id is not None:
            rpc_payload["storyId"] = story_id
        return cast(
            ProtobufMessage, await self.rpc("story", "GetViewersCount", **rpc_payload)
        )

    async def set_user_privacy_config(
        self: Any, config: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.SetUserPrivacyConfig` operation.

        Parameters:
        config: Wire field `config` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if config is not None:
            rpc_payload["config"] = config
        return cast(
            ProtobufMessage,
            await self.rpc("story", "SetUserPrivacyConfig", **rpc_payload),
        )

    async def set_user_story_config(
        self: Any,
        set_type: int | None = None,
        config: Any | None = None,
        ex_peer: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.story.v1.Story.SetUserStoryConfig` operation.

        Parameters:
        set_type: Wire field `setType` (int | None).
        config: Wire field `config` (Any | None).
        ex_peer: Wire field `exPeer` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if set_type is not None:
            rpc_payload["setType"] = set_type
        if config is not None:
            rpc_payload["config"] = config
        if ex_peer is not None:
            rpc_payload["exPeer"] = ex_peer
        return cast(
            ProtobufMessage,
            await self.rpc("story", "SetUserStoryConfig", **rpc_payload),
        )

    async def ask_bot_review_callback(
        self: Any, bot_id: int | None = None, payload: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.timche.v1.Timche.AskBotReviewCallback` operation.

        Parameters:
        bot_id: Wire field `botId` (int | None).
        payload: Wire field `payload` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_id is not None:
            rpc_payload["botId"] = bot_id
        if payload is not None:
            rpc_payload["payload"] = payload
        return cast(
            ProtobufMessage,
            await self.rpc("timche", "AskBotReviewCallback", **rpc_payload),
        )

    async def get_bot_page(
        self: Any, bot_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.timche.v1.Timche.GetBotPage` operation.

        Parameters:
        bot_id: Wire field `botId` (int | None).

        Returns fields: name, nickname, activeUsers, averageRating, description, intro, avatar, imageLinks.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_id is not None:
            rpc_payload["botId"] = bot_id
        return cast(
            ProtobufMessage, await self.rpc("timche", "GetBotPage", **rpc_payload)
        )

    async def get_home_page(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.timche.v1.Timche.GetHomePage` operation.

        Returns fields: sections.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("timche", "GetHomePage", **rpc_payload)
        )

    async def get_section_page(
        self: Any, section_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.timche.v1.Timche.GetSectionPage` operation.

        Parameters:
        section_id: Wire field `sectionId` (int | None).

        Returns fields: sectionId, sectionName, bots.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if section_id is not None:
            rpc_payload["sectionId"] = section_id
        return cast(
            ProtobufMessage, await self.rpc("timche", "GetSectionPage", **rpc_payload)
        )

    async def submit_review(
        self: Any,
        bot_id: int | None = None,
        rating: Any | None = None,
        comment: Any | None = None,
        payload: Any | None = None,
        origin: int | None = None,
        language: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.timche.v1.Timche.SubmitReview` operation.

        Parameters:
        bot_id: Wire field `botId` (int | None).
        rating: Wire field `rating` (Any | None).
        comment: Wire field `comment` (Any | None).
        payload: Wire field `payload` (Any | None).
        origin: Wire field `origin` (int | None).
        language: Wire field `language` (Any | None).

        Returns fields: shouldAskBaleReview, baleReviewText.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bot_id is not None:
            rpc_payload["botId"] = bot_id
        if rating is not None:
            rpc_payload["rating"] = rating
        if comment is not None:
            rpc_payload["comment"] = comment
        if payload is not None:
            rpc_payload["payload"] = payload
        if origin is not None:
            rpc_payload["origin"] = origin
        if language is not None:
            rpc_payload["language"] = language
        return cast(
            ProtobufMessage, await self.rpc("timche", "SubmitReview", **rpc_payload)
        )

    async def get_top_peer(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.top_peer.v1.TopPeer.GetTopPeer` operation.

        Returns fields: topPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("toppeer", "GetTopPeer", **rpc_payload)
        )

    async def remove_peer(
        self: Any, peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.top_peer.v1.TopPeer.RemovePeer` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).

        Returns fields: isRemoved.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage, await self.rpc("toppeer", "RemovePeer", **rpc_payload)
        )

    async def get_transcript(
        self: Any,
        voice: Any | None = None,
        out_peer: Any | None = None,
        message_id: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.turing.v1.AI.GetTranscript` operation.

        Parameters:
        voice: Wire field `voice` (Any | None).
        out_peer: Wire field `outPeer` (Any | None).
        message_id: Wire field `messageId` (Any | None).

        Returns fields: mustWait, downloadSource.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if voice is not None:
            rpc_payload["voice"] = voice
        if out_peer is not None:
            rpc_payload["outPeer"] = out_peer
        if message_id is not None:
            rpc_payload["messageId"] = message_id
        return cast(
            ProtobufMessage, await self.rpc("ai", "GetTranscript", **rpc_payload)
        )

    async def send_event(
        self: Any, transcript_reaction_event: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.turing.v1.AI.SendEvent` operation.

        Parameters:
        transcript_reaction_event: Wire field `transcriptReactionEvent` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if transcript_reaction_event is not None:
            rpc_payload["transcriptReactionEvent"] = transcript_reaction_event
        return cast(ProtobufMessage, await self.rpc("ai", "SendEvent", **rpc_payload))

    async def add_card(
        self: Any, bank_code: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.AddCard` operation.

        Parameters:
        bank_code: Wire field `bankCode` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bank_code is not None:
            rpc_payload["bankCode"] = bank_code
        return cast(ProtobufMessage, await self.rpc("users", "AddCard", **rpc_payload))

    async def change_phone_number(
        self: Any, phone_number: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.ChangePhoneNumber` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        return cast(
            ProtobufMessage, await self.rpc("users", "ChangePhoneNumber", **rpc_payload)
        )

    async def check_nick_name(
        self: Any, nickname: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.CheckNickName` operation.

        Parameters:
        nickname: Wire field `nickname` (str | None).

        Returns fields: value.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if nickname is not None:
            rpc_payload["nickname"] = nickname
        return cast(
            ProtobufMessage, await self.rpc("users", "CheckNickName", **rpc_payload)
        )

    async def confirm_phone_number(
        self: Any, code: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.ConfirmPhoneNumber` operation.

        Parameters:
        code: Wire field `code` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if code is not None:
            rpc_payload["code"] = code
        return cast(
            ProtobufMessage,
            await self.rpc("users", "ConfirmPhoneNumber", **rpc_payload),
        )

    async def edit_my_preferred_languages(
        self: Any, preferred_languages: Iterable[str] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.EditMyPreferredLanguages` operation.

        Parameters:
        preferred_languages: Wire field `preferredLanguages` (Iterable[str] | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if preferred_languages is not None:
            rpc_payload["preferredLanguages"] = preferred_languages
        return cast(
            ProtobufMessage,
            await self.rpc("users", "EditMyPreferredLanguages", **rpc_payload),
        )

    async def edit_my_time_zone(
        self: Any, tz: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.EditMyTimeZone` operation.

        Parameters:
        tz: Wire field `tz` (str | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if tz is not None:
            rpc_payload["tz"] = tz
        return cast(
            ProtobufMessage, await self.rpc("users", "EditMyTimeZone", **rpc_payload)
        )

    async def edit_nick_name(
        self: Any, nickname: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.EditNickName` operation.

        Parameters:
        nickname: Wire field `nickname` (Any | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if nickname is not None:
            rpc_payload["nickname"] = nickname
        return cast(
            ProtobufMessage, await self.rpc("users", "EditNickName", **rpc_payload)
        )

    async def get_users_default_card_number(
        self: Any, user_id: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.GetUsersDefaultCardNumber` operation.

        Parameters:
        user_id: Wire field `userId` (Iterable[int] | None).

        Returns fields: defaultCardNo.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if user_id is not None:
            rpc_payload["userId"] = user_id
        return cast(
            ProtobufMessage,
            await self.rpc("users", "GetUsersDefaultCardNumber", **rpc_payload),
        )

    async def import_contacts(
        self: Any,
        phones: Iterable[Any] | None = None,
        optimizations: Iterable[int] | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.ImportContacts` operation.

        Parameters:
        phones: Wire field `phones` (Iterable[Any] | None).
        optimizations: Wire field `optimizations` (Iterable[int] | None).

        Returns fields: users, seq, state, userPeers.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phones is not None:
            rpc_payload["phones"] = phones
        if optimizations is not None:
            rpc_payload["optimizations"] = optimizations
        return cast(
            ProtobufMessage, await self.rpc("users", "ImportContacts", **rpc_payload)
        )

    async def is_name_allowed(
        self: Any, name: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.IsNameAllowed` operation.

        Parameters:
        name: Wire field `name` (str | None).

        Returns fields: value.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if name is not None:
            rpc_payload["name"] = name
        return cast(
            ProtobufMessage, await self.rpc("users", "IsNameAllowed", **rpc_payload)
        )

    async def notify_about_device_info(
        self: Any,
        preferred_languages: Iterable[str] | None = None,
        time_zone: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.NotifyAboutDeviceInfo` operation.

        Parameters:
        preferred_languages: Wire field `preferredLanguages` (Iterable[str] | None).
        time_zone: Wire field `timeZone` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if preferred_languages is not None:
            rpc_payload["preferredLanguages"] = preferred_languages
        if time_zone is not None:
            rpc_payload["timeZone"] = time_zone
        return cast(
            ProtobufMessage,
            await self.rpc("users", "NotifyAboutDeviceInfo", **rpc_payload),
        )

    async def reset_contacts(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.users.v1.Users.ResetContacts` operation.

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("users", "ResetContacts", **rpc_payload)
        )

    async def get_in_app_update(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.v1.Configs.GetInAppUpdate` operation.

        Returns fields: fileId, accessHash, fileSize.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("configs", "GetInAppUpdate", **rpc_payload)
        )

    async def add_gif(
        self: Any,
        gif: Any | None = None,
        thumb: bytes | None = None,
        mime_type: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.AddGif` operation.

        Parameters:
        gif: Wire field `gif` (Any | None).
        thumb: Wire field `thumb` (bytes | None).
        mime_type: Wire field `mimeType` (Any | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if gif is not None:
            rpc_payload["gif"] = gif
        if thumb is not None:
            rpc_payload["thumb"] = thumb
        if mime_type is not None:
            rpc_payload["mimeType"] = mime_type
        return cast(ProtobufMessage, await self.rpc("images", "AddGif", **rpc_payload))

    async def add_sticker_collection(
        self: Any, id_: int | None = None, access_hash: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.AddStickerCollection` operation.

        Parameters:
        id_: Wire field `id` (int | None).
        access_hash: Wire field `accessHash` (int | None).

        Returns fields: collections, seq, state.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if access_hash is not None:
            rpc_payload["accessHash"] = access_hash
        return cast(
            ProtobufMessage,
            await self.rpc("images", "AddStickerCollection", **rpc_payload),
        )

    async def add_sticker_pack(
        self: Any, id_: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.AddStickerPack` operation.

        Parameters:
        id_: Wire field `id` (int | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage, await self.rpc("images", "AddStickerPack", **rpc_payload)
        )

    async def get_saved_gifs(
        self: Any, offset: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.GetSavedGifs` operation.

        Parameters:
        offset: Wire field `offset` (Any | None).

        Returns fields: gifs, offset.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if offset is not None:
            rpc_payload["offset"] = offset
        return cast(
            ProtobufMessage, await self.rpc("images", "GetSavedGifs", **rpc_payload)
        )

    async def load_own_stickers(
        self: Any, offset: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.LoadOwnStickers` operation.

        Parameters:
        offset: Wire field `offset` (Any | None).

        Returns fields: ownStickers, offset.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if offset is not None:
            rpc_payload["offset"] = offset
        return cast(
            ProtobufMessage, await self.rpc("images", "LoadOwnStickers", **rpc_payload)
        )

    async def load_sticker_collection(
        self: Any, id_: int | None = None, access_hash: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.LoadStickerCollection` operation.

        Parameters:
        id_: Wire field `id` (int | None).
        access_hash: Wire field `accessHash` (int | None).

        Returns fields: collection.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if access_hash is not None:
            rpc_payload["accessHash"] = access_hash
        return cast(
            ProtobufMessage,
            await self.rpc("images", "LoadStickerCollection", **rpc_payload),
        )

    async def remove_gif(
        self: Any, gif: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.RemoveGif` operation.

        Parameters:
        gif: Wire field `gif` (Any | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if gif is not None:
            rpc_payload["gif"] = gif
        return cast(
            ProtobufMessage, await self.rpc("images", "RemoveGif", **rpc_payload)
        )

    async def remove_sticker_collection(
        self: Any, id_: int | None = None, access_hash: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.RemoveStickerCollection` operation.

        Parameters:
        id_: Wire field `id` (int | None).
        access_hash: Wire field `accessHash` (int | None).

        Returns fields: collections, seq, state.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if access_hash is not None:
            rpc_payload["accessHash"] = access_hash
        return cast(
            ProtobufMessage,
            await self.rpc("images", "RemoveStickerCollection", **rpc_payload),
        )

    async def remove_sticker_pack(
        self: Any, id_: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.RemoveStickerPack` operation.

        Parameters:
        id_: Wire field `id` (int | None).

        Returns fields: seq, state, seqBig.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        return cast(
            ProtobufMessage,
            await self.rpc("images", "RemoveStickerPack", **rpc_payload),
        )

    async def use_gif(
        self: Any, gif: Any | None = None, used_at: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.v1.Images.UseGif` operation.

        Parameters:
        gif: Wire field `gif` (Any | None).
        used_at: Wire field `usedAt` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if gif is not None:
            rpc_payload["gif"] = gif
        if used_at is not None:
            rpc_payload["usedAt"] = used_at
        return cast(ProtobufMessage, await self.rpc("images", "UseGif", **rpc_payload))

    async def activate_wallet(
        self: Any,
        national_id: str | None = None,
        is_auto_activated: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.ActivateWallet` operation.

        Parameters:
        national_id: Wire field `nationalId` (str | None).
        is_auto_activated: Wire field `isAutoActivated` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_id is not None:
            rpc_payload["nationalId"] = national_id
        if is_auto_activated is not None:
            rpc_payload["isAutoActivated"] = is_auto_activated
        return cast(
            ProtobufMessage, await self.rpc("wallet", "ActivateWallet", **rpc_payload)
        )

    async def cash_out_from_wallet(
        self: Any, token: str | None = None, amount: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.CashOutFromWallet` operation.

        Parameters:
        token: Wire field `token` (str | None).
        amount: Wire field `amount` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if token is not None:
            rpc_payload["token"] = token
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "CashOutFromWallet", **rpc_payload),
        )

    async def get_money_request_payment_token_by_card(
        self: Any,
        msg: Any | None = None,
        amount: Any | None = None,
        regarding: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetMoneyRequestPaymentTokenByCard` operation.

        Parameters:
        msg: Wire field `msg` (Any | None).
        amount: Wire field `amount` (Any | None).
        regarding: Wire field `regarding` (Any | None).

        Returns fields: token, endpoint, terminalId, merchantId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if msg is not None:
            rpc_payload["msg"] = msg
        if amount is not None:
            rpc_payload["amount"] = amount
        if regarding is not None:
            rpc_payload["regarding"] = regarding
        return cast(
            ProtobufMessage,
            await self.rpc(
                "wallet", "GetMoneyRequestPaymentTokenByCard", **rpc_payload
            ),
        )

    async def get_my_wallets(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetMyWallets` operation.

        Returns fields: wallets.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetMyWallets", **rpc_payload)
        )

    async def get_payment_token_by_card(
        self: Any,
        target_wallet: str | None = None,
        amount: int | None = None,
        regarding: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetPaymentTokenByCard` operation.

        Parameters:
        target_wallet: Wire field `targetWallet` (str | None).
        amount: Wire field `amount` (int | None).
        regarding: Wire field `regarding` (Any | None).

        Returns fields: token, endpoint, terminalId, merchantId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if target_wallet is not None:
            rpc_payload["targetWallet"] = target_wallet
        if amount is not None:
            rpc_payload["amount"] = amount
        if regarding is not None:
            rpc_payload["regarding"] = regarding
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "GetPaymentTokenByCard", **rpc_payload),
        )

    async def get_wallet_charge_token(
        self: Any,
        wallet_id: str | None = None,
        amount: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetWalletChargeToken` operation.

        Parameters:
        wallet_id: Wire field `walletId` (str | None).
        amount: Wire field `amount` (int | None).

        Returns fields: token, endpoint, terminalId, merchantId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_id is not None:
            rpc_payload["walletId"] = wallet_id
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "GetWalletChargeToken", **rpc_payload),
        )

    async def get_wallet_contracts(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetWalletContracts` operation.

        Returns fields: startDate, endDate, merchantCustomerUniqueValue, limitations, agreementId, status.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "GetWalletContracts", **rpc_payload),
        )

    async def get_wallet_invoice(
        self: Any,
        wallet_id: str | None = None,
        page_number: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.GetWalletInvoice` operation.

        Parameters:
        wallet_id: Wire field `walletId` (str | None).
        page_number: Wire field `pageNumber` (Any | None).

        Returns fields: invoices.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_id is not None:
            rpc_payload["walletId"] = wallet_id
        if page_number is not None:
            rpc_payload["pageNumber"] = page_number
        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetWalletInvoice", **rpc_payload)
        )

    async def pay_by_wallet(
        self: Any,
        source_wallet: str | None = None,
        target_wallet: str | None = None,
        amount: int | None = None,
        currency: int | None = None,
        regarding: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.PayByWallet` operation.

        Parameters:
        source_wallet: Wire field `sourceWallet` (str | None).
        target_wallet: Wire field `targetWallet` (str | None).
        amount: Wire field `amount` (int | None).
        currency: Wire field `currency` (int | None).
        regarding: Wire field `regarding` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if source_wallet is not None:
            rpc_payload["sourceWallet"] = source_wallet
        if target_wallet is not None:
            rpc_payload["targetWallet"] = target_wallet
        if amount is not None:
            rpc_payload["amount"] = amount
        if currency is not None:
            rpc_payload["currency"] = currency
        if regarding is not None:
            rpc_payload["regarding"] = regarding
        return cast(
            ProtobufMessage, await self.rpc("wallet", "PayByWallet", **rpc_payload)
        )

    async def pay_money_request_by_wallet(
        self: Any,
        source_wallet_id: str | None = None,
        msg: Any | None = None,
        amount: Any | None = None,
        regarding: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.PayMoneyRequestByWallet` operation.

        Parameters:
        source_wallet_id: Wire field `sourceWalletId` (str | None).
        msg: Wire field `msg` (Any | None).
        amount: Wire field `amount` (Any | None).
        regarding: Wire field `regarding` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if source_wallet_id is not None:
            rpc_payload["sourceWalletId"] = source_wallet_id
        if msg is not None:
            rpc_payload["msg"] = msg
        if amount is not None:
            rpc_payload["amount"] = amount
        if regarding is not None:
            rpc_payload["regarding"] = regarding
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "PayMoneyRequestByWallet", **rpc_payload),
        )

    async def verify_cash_out(
        self: Any,
        wallet_id: str | None = None,
        account_no: str | None = None,
        national_id: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.VerifyCashOut` operation.

        Parameters:
        wallet_id: Wire field `walletId` (str | None).
        account_no: Wire field `accountNo` (str | None).
        national_id: Wire field `nationalId` (str | None).

        Returns fields: token, name.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if wallet_id is not None:
            rpc_payload["walletId"] = wallet_id
        if account_no is not None:
            rpc_payload["accountNo"] = account_no
        if national_id is not None:
            rpc_payload["nationalId"] = national_id
        return cast(
            ProtobufMessage, await self.rpc("wallet", "VerifyCashOut", **rpc_payload)
        )

    async def verify_peer(
        self: Any, target_peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.VerifyPeer` operation.

        Parameters:
        target_peer: Wire field `targetPeer` (Any | None).

        Returns fields: targetWalletName, targetUserId, walletId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if target_peer is not None:
            rpc_payload["targetPeer"] = target_peer
        return cast(
            ProtobufMessage, await self.rpc("wallet", "VerifyPeer", **rpc_payload)
        )

    async def verify_qr_code(
        self: Any, target_wallet_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.wallet.v1.Wallet.VerifyQRCode` operation.

        Parameters:
        target_wallet_id: Wire field `targetWalletId` (str | None).

        Returns fields: targetWalletName, targetUserId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if target_wallet_id is not None:
            rpc_payload["targetWalletId"] = target_wallet_id
        return cast(
            ProtobufMessage, await self.rpc("wallet", "VerifyQRCode", **rpc_payload)
        )

    async def activate_yara_messaging(
        self: Any, account_number: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.BankAccountPreferences.v1.BankAccountPreferences.ActivateYaraMessaging` operation.

        Parameters:
        account_number: Wire field `accountNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if account_number is not None:
            rpc_payload["accountNumber"] = account_number
        return cast(
            ProtobufMessage,
            await self.rpc(
                "bankaccountpreferences", "ActivateYaraMessaging", **rpc_payload
            ),
        )

    async def edit_preference(
        self: Any, preference: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.BankAccountPreferences.v1.BankAccountPreferences.EditPreference` operation.

        Parameters:
        preference: Wire field `preference` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if preference is not None:
            rpc_payload["preference"] = preference
        return cast(
            ProtobufMessage,
            await self.rpc("bankaccountpreferences", "EditPreference", **rpc_payload),
        )

    async def get_preferences(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.BankAccountPreferences.v1.BankAccountPreferences.GetPreferences` operation.

        Returns fields: accounts.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("bankaccountpreferences", "GetPreferences", **rpc_payload),
        )

    async def build_audience_query(
        self: Any, definition: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.BuildAudienceQuery` operation.

        Parameters:
        definition: Wire field `definition` (Any | None).

        Returns fields: query, estimatedSize.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if definition is not None:
            rpc_payload["definition"] = definition
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "BuildAudienceQuery", **rpc_payload),
        )

    async def calculate_price(
        self: Any,
        spot: int | None = None,
        view_count: int | None = None,
        click_count: int | None = None,
        link: str | None = None,
        is_instant: bool | None = None,
        tag1: int | None = None,
        tag2: int | None = None,
        targeting: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CalculatePrice` operation.

        Parameters:
        spot: Wire field `spot` (int | None).
        view_count: Wire field `viewCount` (int | None).
        click_count: Wire field `clickCount` (int | None).
        link: Wire field `link` (str | None).
        is_instant: Wire field `isInstant` (bool | None).
        tag1: Wire field `tag1` (int | None).
        tag2: Wire field `tag2` (int | None).
        targeting: Wire field `targeting` (Any | None).

        Returns fields: finalPrice, clickUnitPrice.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if spot is not None:
            rpc_payload["spot"] = spot
        if view_count is not None:
            rpc_payload["viewCount"] = view_count
        if click_count is not None:
            rpc_payload["clickCount"] = click_count
        if link is not None:
            rpc_payload["link"] = link
        if is_instant is not None:
            rpc_payload["isInstant"] = is_instant
        if tag1 is not None:
            rpc_payload["tag1"] = tag1
        if tag2 is not None:
            rpc_payload["tag2"] = tag2
        if targeting is not None:
            rpc_payload["targeting"] = targeting
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CalculatePrice", **rpc_payload),
        )

    async def create_automated_audience(
        self: Any,
        definition: Any | None = None,
        single: Any | None = None,
        random_groups: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.CreateAutomatedAudience` operation.

        Parameters:
        definition: Wire field `definition` (Any | None).
        single: Wire field `single` (Any | None).
        random_groups: Wire field `randomGroups` (Any | None).

        Returns fields: result.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if definition is not None:
            rpc_payload["definition"] = definition
        if single is not None:
            rpc_payload["single"] = single
        if random_groups is not None:
            rpc_payload["randomGroups"] = random_groups
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "CreateAutomatedAudience", **rpc_payload),
        )

    async def estimate_channel_sponsored_income(
        self: Any, peer_id: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.EstimateChannelSponsoredIncome` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).

        Returns fields: estimatedViews, estimatedIncome.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "EstimateChannelSponsoredIncome", **rpc_payload
            ),
        )

    async def get_all_payment_history(
        self: Any,
        start_date: int | None = None,
        end_date: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetAllPaymentHistory` operation.

        Parameters:
        start_date: Wire field `startDate` (int | None).
        end_date: Wire field `endDate` (int | None).

        Returns fields: records.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if start_date is not None:
            rpc_payload["startDate"] = start_date
        if end_date is not None:
            rpc_payload["endDate"] = end_date
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetAllPaymentHistory", **rpc_payload),
        )

    async def get_channel_sponsored_income_report(
        self: Any,
        peer_id: Any | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelSponsoredIncomeReport` operation.

        Parameters:
        peer_id: Wire field `peerId` (Any | None).
        start_time: Wire field `startTime` (int | None).
        end_time: Wire field `endTime` (int | None).

        Returns fields: totalViews, totalIncome, totalAdCount, averageCtr, dailyReports, categoryReports.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer_id is not None:
            rpc_payload["peerId"] = peer_id
        if start_time is not None:
            rpc_payload["startTime"] = start_time
        if end_time is not None:
            rpc_payload["endTime"] = end_time
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelSponsoredIncomeReport", **rpc_payload
            ),
        )

    async def get_channel_undeposited_incomes(
        self: Any, year: int | None = None, month: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetChannelUndepositedIncomes` operation.

        Parameters:
        year: Wire field `year` (int | None).
        month: Wire field `month` (int | None).

        Returns fields: items.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if year is not None:
            rpc_payload["year"] = year
        if month is not None:
            rpc_payload["month"] = month
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "GetChannelUndepositedIncomes", **rpc_payload
            ),
        )

    async def get_invoice_content(
        self: Any, invoice_request_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetInvoiceContent` operation.

        Parameters:
        invoice_request_id: Wire field `invoiceRequestId` (str | None).

        Returns fields: id, description, responseCode, data.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if invoice_request_id is not None:
            rpc_payload["invoiceRequestId"] = invoice_request_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetInvoiceContent", **rpc_payload),
        )

    async def get_legal_org_channels(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.GetLegalOrgChannels` operation.

        Returns fields: channels.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "GetLegalOrgChannels", **rpc_payload),
        )

    async def merge_custom_income_records(
        self: Any, custom_income_ids: Iterable[str] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.MergeCustomIncomeRecords` operation.

        Parameters:
        custom_income_ids: Wire field `customIncomeIds` (Iterable[str] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if custom_income_ids is not None:
            rpc_payload["customIncomeIds"] = custom_income_ids
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "MergeCustomIncomeRecords", **rpc_payload),
        )

    async def merge_increase_credit_records(
        self: Any, increase_credit_ids: Iterable[str] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.MergeIncreaseCreditRecords` operation.

        Parameters:
        increase_credit_ids: Wire field `increaseCreditIds` (Iterable[str] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if increase_credit_ids is not None:
            rpc_payload["increaseCreditIds"] = increase_credit_ids
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "MergeIncreaseCreditRecords", **rpc_payload
            ),
        )

    async def retry_failed_auto_sent_invoice(
        self: Any, failed_invoice_request_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.RetryFailedAutoSentInvoice` operation.

        Parameters:
        failed_invoice_request_id: Wire field `failedInvoiceRequestId` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if failed_invoice_request_id is not None:
            rpc_payload["failedInvoiceRequestId"] = failed_invoice_request_id
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "RetryFailedAutoSentInvoice", **rpc_payload
            ),
        )

    async def send_invoice_for_payment_history_record(
        self: Any,
        record_id: str | None = None,
        deposit_tracking_id: Any | None = None,
        payment_history_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SendInvoiceForPaymentHistoryRecord` operation.

        Parameters:
        record_id: Wire field `recordId` (str | None).
        deposit_tracking_id: Wire field `depositTrackingId` (Any | None).
        payment_history_type: Wire field `paymentHistoryType` (int | None).

        Returns fields: invoiceRequestId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if record_id is not None:
            rpc_payload["recordId"] = record_id
        if deposit_tracking_id is not None:
            rpc_payload["depositTrackingId"] = deposit_tracking_id
        if payment_history_type is not None:
            rpc_payload["paymentHistoryType"] = payment_history_type
        return cast(
            ProtobufMessage,
            await self.rpc(
                "advertisement", "SendInvoiceForPaymentHistoryRecord", **rpc_payload
            ),
        )

    async def send_legal_org_channel_income(
        self: Any, channel_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SendLegalOrgChannelIncome` operation.

        Parameters:
        channel_id: Wire field `channelId` (int | None).

        Returns fields: results.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if channel_id is not None:
            rpc_payload["channelId"] = channel_id
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SendLegalOrgChannelIncome", **rpc_payload),
        )

    async def set_capacity_max_views(
        self: Any,
        data: Iterable[Any] | None = None,
        spot: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.advertisement.v1.Advertisement.SetCapacityMaxViews` operation.

        Parameters:
        data: Wire field `data` (Iterable[Any] | None).
        spot: Wire field `spot` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if data is not None:
            rpc_payload["data"] = data
        if spot is not None:
            rpc_payload["spot"] = spot
        return cast(
            ProtobufMessage,
            await self.rpc("advertisement", "SetCapacityMaxViews", **rpc_payload),
        )

    async def cash_payment_callback(
        self: Any,
        payment_code: str | None = None,
        national_code: str | None = None,
        user_id: int | None = None,
        order_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.CashPaymentCallback` operation.

        Parameters:
        payment_code: Wire field `paymentCode` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        user_id: Wire field `userId` (int | None).
        order_id: Wire field `orderId` (int | None).

        Returns fields: firstName, lastName.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if payment_code is not None:
            rpc_payload["paymentCode"] = payment_code
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if user_id is not None:
            rpc_payload["userId"] = user_id
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "CashPaymentCallback", **rpc_payload),
        )

    async def get_admin_station_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetAdminStationList` operation.

        Returns fields: stations.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetAdminStationList", **rpc_payload),
        )

    async def get_arbaeen_currencies_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetArbaeenCurrenciesList` operation.

        Returns fields: currencies, icmsWage.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetArbaeenCurrenciesList", **rpc_payload),
        )

    async def get_arbaeen_currency_price(
        self: Any,
        currency_type: int | None = None,
        currency_amount: int | None = None,
        reason: int | None = None,
        country_code: int | None = None,
        exit_date: str | None = None,
        national_code: str | None = None,
        delivery_station_type: int | None = None,
        station_id: str | None = None,
        bank_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetArbaeenCurrencyPrice` operation.

        Parameters:
        currency_type: Wire field `currencyType` (int | None).
        currency_amount: Wire field `currencyAmount` (int | None).
        reason: Wire field `reason` (int | None).
        country_code: Wire field `countryCode` (int | None).
        exit_date: Wire field `exitDate` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        station_id: Wire field `stationId` (str | None).
        bank_type: Wire field `bankType` (int | None).

        Returns fields: currencyRate, orderId, newCurrencyRate.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if currency_type is not None:
            rpc_payload["currencyType"] = currency_type
        if currency_amount is not None:
            rpc_payload["currencyAmount"] = currency_amount
        if reason is not None:
            rpc_payload["reason"] = reason
        if country_code is not None:
            rpc_payload["countryCode"] = country_code
        if exit_date is not None:
            rpc_payload["exitDate"] = exit_date
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if station_id is not None:
            rpc_payload["stationId"] = station_id
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetArbaeenCurrencyPrice", **rpc_payload),
        )

    async def get_arbaeen_payment_token(
        self: Any, order_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetArbaeenPaymentToken` operation.

        Parameters:
        order_id: Wire field `orderId` (int | None).

        Returns fields: token, paymentGatewayPrefix, terminalId, paymentUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetArbaeenPaymentToken", **rpc_payload),
        )

    async def get_list_of_arbaeen_delivery_stations(
        self: Any,
        delivery_station_type: int | None = None,
        reason: int | None = None,
        exit_date: str | None = None,
        bank_type: int | None = None,
        should_return_capacity: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetListOfArbaeenDeliveryStations` operation.

        Parameters:
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        reason: Wire field `reason` (int | None).
        exit_date: Wire field `ExitDate` (str | None).
        bank_type: Wire field `bankType` (int | None).
        should_return_capacity: Wire field `shouldReturnCapacity` (Any | None).

        Returns fields: stations.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if reason is not None:
            rpc_payload["reason"] = reason
        if exit_date is not None:
            rpc_payload["ExitDate"] = exit_date
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        if should_return_capacity is not None:
            rpc_payload["shouldReturnCapacity"] = should_return_capacity
        return cast(
            ProtobufMessage,
            await self.rpc(
                "arbaeen", "GetListOfArbaeenDeliveryStations", **rpc_payload
            ),
        )

    async def get_list_of_box_office(
        self: Any,
        station_id: str | None = None,
        exit_date: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetListOfBoxOffice` operation.

        Parameters:
        station_id: Wire field `stationId` (str | None).
        exit_date: Wire field `exitDate` (str | None).

        Returns fields: boxOffice.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if station_id is not None:
            rpc_payload["stationId"] = station_id
        if exit_date is not None:
            rpc_payload["exitDate"] = exit_date
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetListOfBoxOffice", **rpc_payload),
        )

    async def get_list_of_branches(
        self: Any,
        state_id: str | None = None,
        exit_date: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetListOfBranches` operation.

        Parameters:
        state_id: Wire field `stateId` (str | None).
        exit_date: Wire field `exitDate` (str | None).

        Returns fields: branches.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if state_id is not None:
            rpc_payload["stateId"] = state_id
        if exit_date is not None:
            rpc_payload["exitDate"] = exit_date
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetListOfBranches", **rpc_payload),
        )

    async def get_list_of_states(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetListOfStates` operation.

        Returns fields: states.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "GetListOfStates", **rpc_payload)
        )

    async def get_rate(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetRate` operation.

        Returns fields: rate.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "GetRate", **rpc_payload)
        )

    async def get_suggested_groups(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetSuggestedGroups` operation.

        Returns fields: suggestedGroups.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetSuggestedGroups", **rpc_payload),
        )

    async def get_valid_arbaeen_banks(
        self: Any,
        national_code: str | None = None,
        account_national_code: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.GetValidArbaeenBanks` operation.

        Parameters:
        national_code: Wire field `nationalCode` (str | None).
        account_national_code: Wire field `accountNationalCode` (Any | None).

        Returns fields: banks.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if account_national_code is not None:
            rpc_payload["accountNationalCode"] = account_national_code
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "GetValidArbaeenBanks", **rpc_payload),
        )

    async def load_arbaeen_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.LoadArbaeenHistory` operation.

        Returns fields: orders, approvalText.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "LoadArbaeenHistory", **rpc_payload),
        )

    async def send_otp_arbaeen(
        self: Any, phone_number: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.SendOTP` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "SendOTP", **rpc_payload)
        )

    async def start_bot(
        self: Any, peer: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.StartBot` operation.

        Parameters:
        peer: Wire field `peer` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if peer is not None:
            rpc_payload["peer"] = peer
        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "StartBot", **rpc_payload)
        )

    async def user_has_access(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.UserHasAccess` operation.

        Returns fields: access.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "UserHasAccess", **rpc_payload)
        )

    async def verify_otp(
        self: Any,
        phone_number: str | None = None,
        code: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.VerifyOTP` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (str | None).
        code: Wire field `code` (str | None).

        Returns fields: verified.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if code is not None:
            rpc_payload["code"] = code
        return cast(
            ProtobufMessage, await self.rpc("arbaeen", "VerifyOTP", **rpc_payload)
        )

    async def verify_user_arbaeen_authority(
        self: Any,
        first_name: str | None = None,
        last_name: str | None = None,
        national_code: str | None = None,
        passport_code: str | None = None,
        postal_code: str | None = None,
        birth_date: str | None = None,
        father_name: str | None = None,
        sh_id: str | None = None,
        bank_type: int | None = None,
        phone_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.VerifyUserArbaeenAuthority` operation.

        Parameters:
        first_name: Wire field `firstName` (str | None).
        last_name: Wire field `lastName` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        passport_code: Wire field `passportCode` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).
        father_name: Wire field `fatherName` (str | None).
        sh_id: Wire field `shId` (str | None).
        bank_type: Wire field `bankType` (int | None).
        phone_number: Wire field `phoneNumber` (str | None).

        Returns fields: approval.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if first_name is not None:
            rpc_payload["firstName"] = first_name
        if last_name is not None:
            rpc_payload["lastName"] = last_name
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if passport_code is not None:
            rpc_payload["passportCode"] = passport_code
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        if father_name is not None:
            rpc_payload["fatherName"] = father_name
        if sh_id is not None:
            rpc_payload["shId"] = sh_id
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "VerifyUserArbaeenAuthority", **rpc_payload),
        )

    async def verify_user_arbaeen_extra_info(
        self: Any, nakhoda_info: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.arbaeen.v1.Arbaeen.VerifyUserArbaeenExtraInfo` operation.

        Parameters:
        nakhoda_info: Wire field `nakhodaInfo` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if nakhoda_info is not None:
            rpc_payload["nakhodaInfo"] = nakhoda_info
        return cast(
            ProtobufMessage,
            await self.rpc("arbaeen", "VerifyUserArbaeenExtraInfo", **rpc_payload),
        )

    async def create_saved_bill(
        self: Any,
        name: str | None = None,
        bill_type: int | None = None,
        bill_parameter: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.CreateSavedBill` operation.

        Parameters:
        name: Wire field `name` (str | None).
        bill_type: Wire field `billType` (int | None).
        bill_parameter: Wire field `billParameter` (Any | None).

        Returns fields: id.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if name is not None:
            rpc_payload["name"] = name
        if bill_type is not None:
            rpc_payload["billType"] = bill_type
        if bill_parameter is not None:
            rpc_payload["billParameter"] = bill_parameter
        return cast(
            ProtobufMessage, await self.rpc("bill", "CreateSavedBill", **rpc_payload)
        )

    async def delete_saved_bills(
        self: Any, ids: Iterable[int] | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.DeleteSavedBills` operation.

        Parameters:
        ids: Wire field `ids` (Iterable[int] | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if ids is not None:
            rpc_payload["ids"] = ids
        return cast(
            ProtobufMessage, await self.rpc("bill", "DeleteSavedBills", **rpc_payload)
        )

    async def get_bill_history(
        self: Any, count: int | None = None, page: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.GetBillHistory` operation.

        Parameters:
        count: Wire field `count` (int | None).
        page: Wire field `page` (int | None).

        Returns fields: bills.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if count is not None:
            rpc_payload["count"] = count
        if page is not None:
            rpc_payload["page"] = page
        return cast(
            ProtobufMessage, await self.rpc("bill", "GetBillHistory", **rpc_payload)
        )

    async def get_saved_bills(
        self: Any, count: int | None = None, page: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.GetSavedBills` operation.

        Parameters:
        count: Wire field `count` (int | None).
        page: Wire field `page` (int | None).

        Returns fields: bills.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if count is not None:
            rpc_payload["count"] = count
        if page is not None:
            rpc_payload["page"] = page
        return cast(
            ProtobufMessage, await self.rpc("bill", "GetSavedBills", **rpc_payload)
        )

    async def inquiry_bill(
        self: Any,
        bill_type: int | None = None,
        bill_parameters: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.InquiryBill` operation.

        Parameters:
        bill_type: Wire field `billType` (int | None).
        bill_parameters: Wire field `billParameters` (Any | None).

        Returns fields: bills, customerName.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bill_type is not None:
            rpc_payload["billType"] = bill_type
        if bill_parameters is not None:
            rpc_payload["billParameters"] = bill_parameters
        return cast(
            ProtobufMessage, await self.rpc("bill", "InquiryBill", **rpc_payload)
        )

    async def pay_bill(
        self: Any, bill: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.PayBill` operation.

        Parameters:
        bill: Wire field `bill` (Any | None).

        Returns fields: paymentToken.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if bill is not None:
            rpc_payload["bill"] = bill
        return cast(ProtobufMessage, await self.rpc("bill", "PayBill", **rpc_payload))

    async def rename_saved_bill(
        self: Any, id_: int | None = None, name: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.bill.v1.Bill.RenameSavedBill` operation.

        Parameters:
        id_: Wire field `id` (int | None).
        name: Wire field `name` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if name is not None:
            rpc_payload["name"] = name
        return cast(
            ProtobufMessage, await self.rpc("bill", "RenameSavedBill", **rpc_payload)
        )

    async def get_evex_currencies_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.GetEvexCurrenciesList` operation.

        Returns fields: currencies, icmsWage.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("evex", "GetEvexCurrenciesList", **rpc_payload),
        )

    async def get_evex_currency_price(
        self: Any,
        currency_type: int | None = None,
        currency_amount: int | None = None,
        reason: int | None = None,
        country_code: int | None = None,
        exit_date: str | None = None,
        national_code: str | None = None,
        delivery_station_type: int | None = None,
        station_id: str | None = None,
        bank_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.GetEvexCurrencyPrice` operation.

        Parameters:
        currency_type: Wire field `currencyType` (int | None).
        currency_amount: Wire field `currencyAmount` (int | None).
        reason: Wire field `reason` (int | None).
        country_code: Wire field `countryCode` (int | None).
        exit_date: Wire field `exitDate` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        station_id: Wire field `stationId` (str | None).
        bank_type: Wire field `bankType` (int | None).

        Returns fields: currencyRate, orderId, amountToPay, rialAmount, melliWage, iceWage, otherWages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if currency_type is not None:
            rpc_payload["currencyType"] = currency_type
        if currency_amount is not None:
            rpc_payload["currencyAmount"] = currency_amount
        if reason is not None:
            rpc_payload["reason"] = reason
        if country_code is not None:
            rpc_payload["countryCode"] = country_code
        if exit_date is not None:
            rpc_payload["exitDate"] = exit_date
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if station_id is not None:
            rpc_payload["stationId"] = station_id
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        return cast(
            ProtobufMessage,
            await self.rpc("evex", "GetEvexCurrencyPrice", **rpc_payload),
        )

    async def get_evex_payment_token(
        self: Any, order_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.GetEvexPaymentToken` operation.

        Parameters:
        order_id: Wire field `orderId` (int | None).

        Returns fields: token, paymentGatewayPrefix, terminalId.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage,
            await self.rpc("evex", "GetEvexPaymentToken", **rpc_payload),
        )

    async def get_list_of_evex_delivery_stations(
        self: Any,
        delivery_station_type: int | None = None,
        reason: int | None = None,
        exit_date: str | None = None,
        bank_type: int | None = None,
        should_return_capacity: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.GetListOfEvexDeliveryStations` operation.

        Parameters:
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        reason: Wire field `reason` (int | None).
        exit_date: Wire field `ExitDate` (str | None).
        bank_type: Wire field `bankType` (int | None).
        should_return_capacity: Wire field `shouldReturnCapacity` (Any | None).

        Returns fields: stations.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if reason is not None:
            rpc_payload["reason"] = reason
        if exit_date is not None:
            rpc_payload["ExitDate"] = exit_date
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        if should_return_capacity is not None:
            rpc_payload["shouldReturnCapacity"] = should_return_capacity
        return cast(
            ProtobufMessage,
            await self.rpc("evex", "GetListOfEvexDeliveryStations", **rpc_payload),
        )

    async def get_valid_banks(
        self: Any,
        national_code: str | None = None,
        account_national_code: Any | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.GetValidBanks` operation.

        Parameters:
        national_code: Wire field `nationalCode` (str | None).
        account_national_code: Wire field `accountNationalCode` (Any | None).

        Returns fields: banks.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if account_national_code is not None:
            rpc_payload["accountNationalCode"] = account_national_code
        return cast(
            ProtobufMessage, await self.rpc("evex", "GetValidBanks", **rpc_payload)
        )

    async def load_evex_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.LoadEvexHistory` operation.

        Returns fields: orders, approvalText.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("evex", "LoadEvexHistory", **rpc_payload)
        )

    async def verify_user_evex_authority(
        self: Any,
        first_name: str | None = None,
        last_name: str | None = None,
        national_code: str | None = None,
        passport_code: str | None = None,
        postal_code: str | None = None,
        birth_date: str | None = None,
        father_name: str | None = None,
        sh_id: str | None = None,
        bank_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.VerifyUserEvexAuthority` operation.

        Parameters:
        first_name: Wire field `firstName` (str | None).
        last_name: Wire field `lastName` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        passport_code: Wire field `passportCode` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).
        father_name: Wire field `fatherName` (str | None).
        sh_id: Wire field `shId` (str | None).
        bank_type: Wire field `bankType` (int | None).

        Returns fields: approval.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if first_name is not None:
            rpc_payload["firstName"] = first_name
        if last_name is not None:
            rpc_payload["lastName"] = last_name
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if passport_code is not None:
            rpc_payload["passportCode"] = passport_code
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        if father_name is not None:
            rpc_payload["fatherName"] = father_name
        if sh_id is not None:
            rpc_payload["shId"] = sh_id
        if bank_type is not None:
            rpc_payload["bankType"] = bank_type
        return cast(
            ProtobufMessage,
            await self.rpc("evex", "VerifyUserEvexAuthority", **rpc_payload),
        )

    async def verify_user_evex_extra_info(
        self: Any, nakhoda_info: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.evex.v1.Evex.VerifyUserEvexExtraInfo` operation.

        Parameters:
        nakhoda_info: Wire field `nakhodaInfo` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if nakhoda_info is not None:
            rpc_payload["nakhodaInfo"] = nakhoda_info
        return cast(
            ProtobufMessage,
            await self.rpc("evex", "VerifyUserEvexExtraInfo", **rpc_payload),
        )

    async def get_currencies_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetCurrenciesList` operation.

        Returns fields: currencies, icmsWage.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetCurrenciesList", **rpc_payload),
        )

    async def get_currency_price(
        self: Any,
        currency_type: int | None = None,
        currency_amount: int | None = None,
        reason: int | None = None,
        country_code: int | None = None,
        exit_date: str | None = None,
        national_code: str | None = None,
        delivery_station_type: int | None = None,
        station_id: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetCurrencyPrice` operation.

        Parameters:
        currency_type: Wire field `currencyType` (int | None).
        currency_amount: Wire field `currencyAmount` (int | None).
        reason: Wire field `reason` (int | None).
        country_code: Wire field `countryCode` (int | None).
        exit_date: Wire field `exitDate` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        station_id: Wire field `stationId` (str | None).

        Returns fields: currencyRate, orderId, amountToPay, rialAmount, melliWage, iceWage, otherWages.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if currency_type is not None:
            rpc_payload["currencyType"] = currency_type
        if currency_amount is not None:
            rpc_payload["currencyAmount"] = currency_amount
        if reason is not None:
            rpc_payload["reason"] = reason
        if country_code is not None:
            rpc_payload["countryCode"] = country_code
        if exit_date is not None:
            rpc_payload["exitDate"] = exit_date
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if station_id is not None:
            rpc_payload["stationId"] = station_id
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetCurrencyPrice", **rpc_payload),
        )

    async def get_exchange_order_info(
        self: Any, order_id: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetExchangeOrderInfo` operation.

        Parameters:
        order_id: Wire field `orderId` (int | None).

        Returns fields: orderStatus.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetExchangeOrderInfo", **rpc_payload),
        )

    async def get_exchange_payment_token(
        self: Any,
        order_id: int | None = None,
        call_back: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetExchangePaymentToken` operation.

        Parameters:
        order_id: Wire field `orderId` (int | None).
        call_back: Wire field `callBack` (str | None).

        Returns fields: token.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        if call_back is not None:
            rpc_payload["callBack"] = call_back
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetExchangePaymentToken", **rpc_payload),
        )

    async def get_initial_config(
        self: Any, origin: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetInitialConfig` operation.

        Parameters:
        origin: Wire field `origin` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if origin is not None:
            rpc_payload["origin"] = origin
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetInitialConfig", **rpc_payload),
        )

    async def get_list_of_delivery_stations(
        self: Any,
        delivery_station_type: int | None = None,
        reason: int | None = None,
        exit_date: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetListOfDeliveryStations` operation.

        Parameters:
        delivery_station_type: Wire field `deliveryStationType` (int | None).
        reason: Wire field `reason` (int | None).
        exit_date: Wire field `ExitDate` (str | None).

        Returns fields: stations.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if delivery_station_type is not None:
            rpc_payload["deliveryStationType"] = delivery_station_type
        if reason is not None:
            rpc_payload["reason"] = reason
        if exit_date is not None:
            rpc_payload["ExitDate"] = exit_date
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetListOfDeliveryStations", **rpc_payload),
        )

    async def get_travel_currency_order_in_detail(
        self: Any,
        phone_number: str | None = None,
        national_code: str | None = None,
        user_id: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetTravelCurrencyOrderInDetail` operation.

        Parameters:
        phone_number: Wire field `phoneNumber` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        user_id: Wire field `userId` (int | None).

        Returns fields: orders.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if phone_number is not None:
            rpc_payload["phoneNumber"] = phone_number
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if user_id is not None:
            rpc_payload["userId"] = user_id
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetTravelCurrencyOrderInDetail", **rpc_payload),
        )

    async def get_user_icms_info(
        self: Any,
        national_code: str | None = None,
        birth_date: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.GetUserIcmsInfo` operation.

        Parameters:
        national_code: Wire field `nationalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).

        Returns fields: firstName, lastName, nationalCode, passportCode, postalCode, birthDate, fatherName, shId, IsValid.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetUserIcmsInfo", **rpc_payload),
        )

    async def load_exchange_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.LoadExchangeHistory` operation.

        Returns fields: orders, approvalText.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "LoadExchangeHistory", **rpc_payload),
        )

    async def verify_user_exchange_authority(
        self: Any,
        first_name: str | None = None,
        last_name: str | None = None,
        national_code: str | None = None,
        passport_code: str | None = None,
        postal_code: str | None = None,
        birth_date: str | None = None,
        father_name: str | None = None,
        sh_id: str | None = None,
        is_valid: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.exchange.v1.Exchange.VerifyUserExchangeAuthority` operation.

        Parameters:
        first_name: Wire field `firstName` (str | None).
        last_name: Wire field `lastName` (str | None).
        national_code: Wire field `nationalCode` (str | None).
        passport_code: Wire field `passportCode` (str | None).
        postal_code: Wire field `postalCode` (str | None).
        birth_date: Wire field `birthDate` (str | None).
        father_name: Wire field `fatherName` (str | None).
        sh_id: Wire field `shId` (str | None).
        is_valid: Wire field `isValid` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if first_name is not None:
            rpc_payload["firstName"] = first_name
        if last_name is not None:
            rpc_payload["lastName"] = last_name
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if passport_code is not None:
            rpc_payload["passportCode"] = passport_code
        if postal_code is not None:
            rpc_payload["postalCode"] = postal_code
        if birth_date is not None:
            rpc_payload["birthDate"] = birth_date
        if father_name is not None:
            rpc_payload["fatherName"] = father_name
        if sh_id is not None:
            rpc_payload["shId"] = sh_id
        if is_valid is not None:
            rpc_payload["isValid"] = is_valid
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "VerifyUserExchangeAuthority", **rpc_payload),
        )

    async def search_services(
        self: Any,
        query: Any | None = None,
        language: Any | None = None,
        source: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.garson.v1.Garson.SearchServices` operation.

        Parameters:
        query: Wire field `query` (Any | None).
        language: Wire field `language` (Any | None).
        source: Wire field `source` (int | None).

        Returns fields: sections.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if query is not None:
            rpc_payload["query"] = query
        if language is not None:
            rpc_payload["language"] = language
        if source is not None:
            rpc_payload["source"] = source
        return cast(
            ProtobufMessage, await self.rpc("garson", "SearchServices", **rpc_payload)
        )

    async def set_sign_messages(
        self: Any,
        group_peer: Any | None = None,
        sign_messages: bool | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetSignMessages` operation.

        Parameters:
        group_peer: Wire field `groupPeer` (Any | None).
        sign_messages: Wire field `signMessages` (bool | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group_peer is not None:
            rpc_payload["groupPeer"] = group_peer
        if sign_messages is not None:
            rpc_payload["signMessages"] = sign_messages
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetSignMessages", **rpc_payload)
        )

    async def set_slow_mode(
        self: Any, group: Any | None = None, seconds: Any | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.groups.v1.Groups.SetSlowMode` operation.

        Parameters:
        group: Wire field `group` (Any | None).
        seconds: Wire field `seconds` (Any | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if group is not None:
            rpc_payload["group"] = group
        if seconds is not None:
            rpc_payload["seconds"] = seconds
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetSlowMode", **rpc_payload)
        )

    async def fee_inquiry(
        self: Any,
        amount: int | None = None,
        transaction_type: Any | None = None,
        pocket_type: int | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.kifpool.v1.Kifpool.FeeInquiry` operation.

        Parameters:
        amount: Wire field `amount` (int | None).
        transaction_type: Wire field `transactionType` (Any | None).
        pocket_type: Wire field `pocketType` (int | None).

        Returns fields: amount, fee, responseData.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if amount is not None:
            rpc_payload["amount"] = amount
        if transaction_type is not None:
            rpc_payload["transactionType"] = transaction_type
        if pocket_type is not None:
            rpc_payload["pocketType"] = pocket_type
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "FeeInquiry", **rpc_payload)
        )

    async def get_onboarding_page_data(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.pishvaz.v1.Pishvaz.GetOnboardingPageData` operation.

        Returns fields: title, sections.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage,
            await self.rpc("pishvaz", "GetOnboardingPageData", **rpc_payload),
        )

    async def set_marketing_tool_action(
        self: Any, id_: int | None = None, action_type: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.pishvaz.v1.Pishvaz.SetMarketingToolAction` operation.

        Parameters:
        id_: Wire field `id` (int | None).
        action_type: Wire field `actionType` (int | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if id_ is not None:
            rpc_payload["id"] = id_
        if action_type is not None:
            rpc_payload["actionType"] = action_type
        return cast(
            ProtobufMessage,
            await self.rpc("pishvaz", "SetMarketingToolAction", **rpc_payload),
        )

    async def authenticate_user(
        self: Any,
        national_code: str | None = None,
        account_number: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.AuthenticateUser` operation.

        Parameters:
        national_code: Wire field `nationalCode` (str | None).
        account_number: Wire field `accountNumber` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if national_code is not None:
            rpc_payload["nationalCode"] = national_code
        if account_number is not None:
            rpc_payload["accountNumber"] = account_number
        return cast(
            ProtobufMessage,
            await self.rpc("sarrafi", "AuthenticateUser", **rpc_payload),
        )

    async def create_order(
        self: Any,
        symbol: int | None = None,
        side: int | None = None,
        price: str | None = None,
        quantity: str | None = None,
        **kwargs: Any,
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.CreateOrder` operation.

        Parameters:
        symbol: Wire field `symbol` (int | None).
        side: Wire field `side` (int | None).
        price: Wire field `price` (str | None).
        quantity: Wire field `quantity` (str | None).

        Returns: Default confirmation response.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if symbol is not None:
            rpc_payload["symbol"] = symbol
        if side is not None:
            rpc_payload["side"] = side
        if price is not None:
            rpc_payload["price"] = price
        if quantity is not None:
            rpc_payload["quantity"] = quantity
        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "CreateOrder", **rpc_payload)
        )

    async def get_charge_token(
        self: Any, currency: int | None = None, amount: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetChargeToken` operation.

        Parameters:
        currency: Wire field `currency` (int | None).
        amount: Wire field `amount` (str | None).

        Returns fields: tokenUrl.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if currency is not None:
            rpc_payload["currency"] = currency
        if amount is not None:
            rpc_payload["amount"] = amount
        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetChargeToken", **rpc_payload)
        )

    async def get_depth(
        self: Any, symbol: int | None = None, limit: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetDepth` operation.

        Parameters:
        symbol: Wire field `symbol` (int | None).
        limit: Wire field `limit` (int | None).

        Returns fields: marketDepth.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if symbol is not None:
            rpc_payload["symbol"] = symbol
        if limit is not None:
            rpc_payload["limit"] = limit
        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetDepth", **rpc_payload)
        )

    async def get_order(
        self: Any, order_id: str | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetOrder` operation.

        Parameters:
        order_id: Wire field `orderId` (str | None).

        Returns fields: order, trades.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if order_id is not None:
            rpc_payload["orderId"] = order_id
        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetOrder", **rpc_payload)
        )

    async def get_orders(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetOrders` operation.

        Returns fields: orders, limit, offset.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetOrders", **rpc_payload)
        )

    async def get_session(
        self: Any, symbol: int | None = None, **kwargs: Any
    ) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetSession` operation.

        Parameters:
        symbol: Wire field `symbol` (int | None).

        Returns fields: openAt, closeAt, openingPrice, brokerFeePercentage, marketFeePercentage, priceTolerancePercentage, quantityTickSize.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)
        if symbol is not None:
            rpc_payload["symbol"] = symbol
        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetSession", **rpc_payload)
        )

    async def get_tickers(self: Any, **kwargs: Any) -> ProtobufMessage:
        """Execute `bale.sarrafi.v1.Sarrafi.GetTickers` operation.

        Returns fields: usd, euro.
        """
        rpc_payload: dict[str, Any] = dict(kwargs)

        return cast(
            ProtobufMessage, await self.rpc("sarrafi", "GetTickers", **rpc_payload)
        )

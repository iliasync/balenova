"""
High-level extended Pythonic convenience methods for Client.
"""

from __future__ import annotations

from typing import Any, cast

from google.protobuf.message import Message as ProtobufMessage


class ClientExtendedMethodsMixin:
    """
    Mixin providing 110+ convenient high-level Pythonic methods for Bale client.
    """

    async def cash_out(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CashOut operation (requestId, token, amount, account, pan, iban).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "CashOut", **kwargs))

    async def charge(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool Charge operation (paymentToken, referenceNo).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "Charge", **kwargs))

    async def check_charge_permission(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CheckChargePermission operation (paymentToken).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "CheckChargePermission", **kwargs),
        )

    async def create_kifpool(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CreateKifpool operation (nationalId).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CreateKifpool", **kwargs)
        )

    async def crypto_cash_out(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CryptoCashOut operation (requestId, amount, account, pan,
        pocketType, isMerchant).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoCashOut", **kwargs)
        )

    async def crypto_invoice(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CryptoInvoice operation (token, pageSize, pageNumber).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoInvoice", **kwargs)
        )

    async def crypto_purchase(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CryptoPurchase operation (amount, srcToken, dstToken, description,
        terminalId, bornaTrxId).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoPurchase", **kwargs)
        )

    async def crypto_refund(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CryptoRefund operation (token, amount, approvalCode, trxRefSrc).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoRefund", **kwargs)
        )

    async def crypto_transfer(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool CryptoTransfer operation (amount, srcToken, dstToken, description,
        dstPhoneNo).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "CryptoTransfer", **kwargs)
        )

    async def fee_inquiry(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool FeeInquiry operation (amount, transactionType, pocketType).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "FeeInquiry", **kwargs))

    async def get_charge_payment_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetChargePaymentToken operation (token, amount, callbackType).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetChargePaymentToken", **kwargs),
        )

    async def get_credit(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetCredit operation (No parameters).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "GetCredit", **kwargs))

    async def get_crypto_charge_payment_token(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Kifpool GetCryptoChargePaymentToken operation (token, amount, receiverId).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetCryptoChargePaymentToken", **kwargs),
        )

    async def get_crypto_wallets(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetCryptoWallets operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "GetCryptoWallets", **kwargs)
        )

    async def get_kifpool_owner(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetKifpoolOwner operation (walletToken).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "GetKifpoolOwner", **kwargs)
        )

    async def get_kifpool_point_balance(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetKifpoolPointBalance operation (token).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointBalance", **kwargs),
        )

    async def get_kifpool_point_details(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetKifpoolPointDetails operation (token, count, page).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointDetails", **kwargs),
        )

    async def get_kifpool_point_summery(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool GetKifpoolPointSummery operation (token).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolPointSummery", **kwargs),
        )

    async def get_kifpool_transaction_point(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Kifpool GetKifpoolTransactionPoint operation (transactionID, amount).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "GetKifpoolTransactionPoint", **kwargs),
        )

    async def invoice(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool Invoice operation (token, pageSize, pageNumber).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "Invoice", **kwargs))

    async def pay_for_message(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool PayForMessage operation (amount, chargeAmount, message).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "PayForMessage", **kwargs)
        )

    async def purchase(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool Purchase operation (amount, dstToken, srcToken, description,
        useCredit, couponId, terminalNo, stan).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "Purchase", **kwargs))

    async def purchase_message(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool PurchaseMessage operation (historyId, amount, description).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "PurchaseMessage", **kwargs)
        )

    async def purchase_message_with_charge(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool PurchaseMessageWithCharge operation (historyId, amount,
        description, chargeAmount).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "PurchaseMessageWithCharge", **kwargs),
        )

    async def purchase_with_charge(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool PurchaseWithCharge operation (amount, dstToken, srcToken,
        description, chargeAmount, useCredit, couponId, terminalNo, stan).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "PurchaseWithCharge", **kwargs)
        )

    async def transfer(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool Transfer operation (sourceToken, destinationToken,
        destinationPhone, destinationUserid, amount, description).
        """
        return cast(ProtobufMessage, await self.rpc("kifpool", "Transfer", **kwargs))

    async def upgrade_kifpool(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool UpgradeKifpool operation (token, nationalId, cardNo, accountNo,
        remainReferenceNumber).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "UpgradeKifpool", **kwargs)
        )

    async def verify_cash_out_kifpool(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool VerifyCashOutKifpool operation (token).
        """
        return cast(
            ProtobufMessage, await self.rpc("kifpool", "VerifyCashOutKifpool", **kwargs)
        )

    async def verify_purchase_message(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Kifpool VerifyPurchaseMessage operation (historyId).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("kifpool", "VerifyPurchaseMessage", **kwargs),
        )

    async def activate_wallet(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet ActivateWallet operation (nationalId, isAutoActivated).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "ActivateWallet", **kwargs)
        )

    async def cash_out_from_wallet(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet CashOutFromWallet operation (token, amount).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "CashOutFromWallet", **kwargs)
        )

    async def get_money_request_payment_token_by_card(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Wallet GetMoneyRequestPaymentTokenByCard operation (msg, amount,
        regarding).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "GetMoneyRequestPaymentTokenByCard", **kwargs),
        )

    async def get_my_wallets(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet GetMyWallets operation (No parameters).
        """
        return cast(ProtobufMessage, await self.rpc("wallet", "GetMyWallets", **kwargs))

    async def get_payment_token_by_card(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet GetPaymentTokenByCard operation (targetWallet, amount, regarding).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetPaymentTokenByCard", **kwargs)
        )

    async def get_wallet_charge_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet GetWalletChargeToken operation (walletId, amount).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetWalletChargeToken", **kwargs)
        )

    async def get_wallet_contracts(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet GetWalletContracts operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetWalletContracts", **kwargs)
        )

    async def get_wallet_invoice(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet GetWalletInvoice operation (walletId, pageNumber).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "GetWalletInvoice", **kwargs)
        )

    async def pay_by_wallet(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet PayByWallet operation (sourceWallet, targetWallet, amount, currency,
        regarding).
        """
        return cast(ProtobufMessage, await self.rpc("wallet", "PayByWallet", **kwargs))

    async def pay_money_request_by_wallet(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet PayMoneyRequestByWallet operation (sourceWalletId, msg, amount,
        regarding).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("wallet", "PayMoneyRequestByWallet", **kwargs),
        )

    async def verify_cash_out(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet VerifyCashOut operation (walletId, accountNo, nationalId).
        """
        return cast(
            ProtobufMessage, await self.rpc("wallet", "VerifyCashOut", **kwargs)
        )

    async def verify_peer(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet VerifyPeer operation (targetPeer).
        """
        return cast(ProtobufMessage, await self.rpc("wallet", "VerifyPeer", **kwargs))

    async def verify_qr_code(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Wallet VerifyQRCode operation (targetWalletId).
        """
        return cast(ProtobufMessage, await self.rpc("wallet", "VerifyQRCode", **kwargs))

    async def buy_fast_charge(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank BuyFastCharge operation (amount, phoneNumber, operator, chargeType).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "BuyFastCharge", **kwargs))

    async def get_card_remain(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetCardRemain operation (cardNumber, cvv2, expireDate, pin2).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "GetCardRemain", **kwargs))

    async def get_organization_payment_token(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Bank GetOrganizationPaymentToken operation (organizationId, invoiceId,
        amount).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("bank", "GetOrganizationPaymentToken", **kwargs),
        )

    async def get_otp_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetOTPToken operation (cardNumberStartingSix).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "GetOTPToken", **kwargs))

    async def get_otp_token_v2(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetOTPTokenV2 operation (messagePeer, msgRid, msgDate, peerUserId,
        cardNumberStartingSix).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "GetOTPTokenV2", **kwargs))

    async def get_payment_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPaymentToken operation (msg, description, amount).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPaymentToken", **kwargs)
        )

    async def get_pay_money_request_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPayMoneyRequestToken operation (messagePeer, msgRid, msgDate,
        recipient, description).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPayMoneyRequestToken", **kwargs)
        )

    async def get_payvand_card(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPayvandCard operation (index).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "GetPayvandCard", **kwargs))

    async def get_payvand_card_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPayvandCardList operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPayvandCardList", **kwargs)
        )

    async def get_ps_proxy_payment_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPSProxyPaymentToken operation (paymentAmount, msg, description).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPSProxyPaymentToken", **kwargs)
        )

    async def get_ps_proxy_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetPSProxyToken operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetPSProxyToken", **kwargs)
        )

    async def get_recent_charges(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetRecentCharges operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetRecentCharges", **kwargs)
        )

    async def get_remain_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetRemainToken operation (cardNumberStartingSix).
        """
        return cast(ProtobufMessage, await self.rpc("bank", "GetRemainToken", **kwargs))

    async def get_sadad_psp_payment_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetSadadPSPPaymentToken operation (msg, paymentAmount, description).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetSadadPSPPaymentToken", **kwargs)
        )

    async def get_token_invoice(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GetTokenInvoice operation (service).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GetTokenInvoice", **kwargs)
        )

    async def grant_banki_access(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bank GrantBankiAccess operation (bot, serviceKey).
        """
        return cast(
            ProtobufMessage, await self.rpc("bank", "GrantBankiAccess", **kwargs)
        )

    async def create_saved_bill(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill CreateSavedBill operation (name, billType, billParameter).
        """
        return cast(
            ProtobufMessage, await self.rpc("bill", "CreateSavedBill", **kwargs)
        )

    async def delete_saved_bills(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill DeleteSavedBills operation (ids).
        """
        return cast(
            ProtobufMessage, await self.rpc("bill", "DeleteSavedBills", **kwargs)
        )

    async def get_bill_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill GetBillHistory operation (count, page).
        """
        return cast(ProtobufMessage, await self.rpc("bill", "GetBillHistory", **kwargs))

    async def get_saved_bills(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill GetSavedBills operation (count, page).
        """
        return cast(ProtobufMessage, await self.rpc("bill", "GetSavedBills", **kwargs))

    async def inquiry_bill(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill InquiryBill operation (billType, billParameters).
        """
        return cast(ProtobufMessage, await self.rpc("bill", "InquiryBill", **kwargs))

    async def pay_bill(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill PayBill operation (bill).
        """
        return cast(ProtobufMessage, await self.rpc("bill", "PayBill", **kwargs))

    async def rename_saved_bill(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Bill RenameSavedBill operation (id, name).
        """
        return cast(
            ProtobufMessage, await self.rpc("bill", "RenameSavedBill", **kwargs)
        )

    async def get_currencies_list(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetCurrenciesList operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("exchange", "GetCurrenciesList", **kwargs)
        )

    async def get_currency_price(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetCurrencyPrice operation (currencyType, currencyAmount, reason,
        countryCode, exitDate, nationalCode, deliveryStationType, stationId).
        """
        return cast(
            ProtobufMessage, await self.rpc("exchange", "GetCurrencyPrice", **kwargs)
        )

    async def get_exchange_order_info(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetExchangeOrderInfo operation (orderId).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetExchangeOrderInfo", **kwargs),
        )

    async def get_exchange_payment_token(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetExchangePaymentToken operation (orderId, callBack).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetExchangePaymentToken", **kwargs),
        )

    async def get_initial_config(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetInitialConfig operation (origin).
        """
        return cast(
            ProtobufMessage, await self.rpc("exchange", "GetInitialConfig", **kwargs)
        )

    async def get_list_of_delivery_stations(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Exchange GetListOfDeliveryStations operation (deliveryStationType, reason,
        ExitDate).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetListOfDeliveryStations", **kwargs),
        )

    async def get_travel_currency_order_in_detail(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Exchange GetTravelCurrencyOrderInDetail operation (phoneNumber,
        nationalCode, userId).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "GetTravelCurrencyOrderInDetail", **kwargs),
        )

    async def get_user_icms_info(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange GetUserIcmsInfo operation (nationalCode, birthDate).
        """
        return cast(
            ProtobufMessage, await self.rpc("exchange", "GetUserIcmsInfo", **kwargs)
        )

    async def load_exchange_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Exchange LoadExchangeHistory operation (No parameters).
        """
        return cast(
            ProtobufMessage, await self.rpc("exchange", "LoadExchangeHistory", **kwargs)
        )

    async def verify_user_exchange_authority(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Exchange VerifyUserExchangeAuthority operation (firstName, lastName,
        nationalCode, passportCode, postalCode, birthDate, fatherName, shId,
        isValid).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("exchange", "VerifyUserExchangeAuthority", **kwargs),
        )

    async def delete_stream(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet DeleteStream operation (streamUser).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "DeleteStream", **kwargs))

    async def get_wss_url(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet GetWssURL operation (callId).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "GetWssURL", **kwargs))

    async def mute_participant(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet MuteParticipant operation (callId, identity, trackId,
        revokePublishPermission).
        """
        return cast(
            ProtobufMessage, await self.rpc("meet", "MuteParticipant", **kwargs)
        )

    async def remove_participant(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet RemoveParticipant operation (callId, identity, blockFromCall).
        """
        return cast(
            ProtobufMessage, await self.rpc("meet", "RemoveParticipant", **kwargs)
        )

    async def send_fanoos_event(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet SendFanoosEvent operation (eventName, items, date).
        """
        return cast(
            ProtobufMessage, await self.rpc("meet", "SendFanoosEvent", **kwargs)
        )

    async def set_link_title(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet SetLinkTitle operation (title, callId, linkUrl).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "SetLinkTitle", **kwargs))

    async def start_recording(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet StartRecording operation (callId, layout, quality).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "StartRecording", **kwargs))

    async def start_stream(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet StartStream operation (streamUser, url, rtmpServer).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "StartStream", **kwargs))

    async def stop_recording(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet StopRecording operation (callId).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "StopRecording", **kwargs))

    async def update_layout(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Meet UpdateLayout operation (callId, requestedLayout).
        """
        return cast(ProtobufMessage, await self.rpc("meet", "UpdateLayout", **kwargs))

    async def add_discussion_group_admin(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups AddDiscussionGroupAdmin operation (channel, discussionGroup).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "AddDiscussionGroupAdmin", **kwargs),
        )

    async def edit_channel_nick(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups EditChannelNick operation (groupPeer, nick, randomId).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "EditChannelNick", **kwargs)
        )

    async def edit_group_default_card_number(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Groups EditGroupDefaultCardNumber operation (groupPeer, cardNumber).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "EditGroupDefaultCardNumber", **kwargs),
        )

    async def get_group_default_card_number(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Groups GetGroupDefaultCardNumber operation (groupPeerr).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "GetGroupDefaultCardNumber", **kwargs),
        )

    async def get_group_recommendations(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups GetGroupRecommendations operation (source).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "GetGroupRecommendations", **kwargs),
        )

    async def get_pins(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups GetPins operation (groupPeer, page, limit).
        """
        return cast(ProtobufMessage, await self.rpc("groups", "GetPins", **kwargs))

    async def load_full_groups(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups LoadFullGroups operation (groups).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "LoadFullGroups", **kwargs)
        )

    async def make_user_admin(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups MakeUserAdmin operation (groupPeer, userPeer, adminTitle).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "MakeUserAdmin", **kwargs)
        )

    async def remove_discussion_group(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups RemoveDiscussionGroup operation (rid, channel).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "RemoveDiscussionGroup", **kwargs)
        )

    async def remove_pin(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups RemovePin operation (groupPeer).
        """
        return cast(ProtobufMessage, await self.rpc("groups", "RemovePin", **kwargs))

    async def set_available_reactions(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetAvailableReactions operation (group, codes).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetAvailableReactions", **kwargs)
        )

    async def set_can_see_history(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetCanSeeHistory operation (groupPeer, canSeeHistory).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetCanSeeHistory", **kwargs)
        )

    async def set_can_see_messages(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetCanSeeMessages operation (groupPeer, userId, canSeeMessages).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetCanSeeMessages", **kwargs)
        )

    async def set_discussion_group(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetDiscussionGroup operation (rid, channel).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetDiscussionGroup", **kwargs)
        )

    async def set_group_default_permissions(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Groups SetGroupDefaultPermissions operation (group, permissions).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("groups", "SetGroupDefaultPermissions", **kwargs),
        )

    async def set_member_custom_title(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetMemberCustomTitle operation (groupId, memberId, title).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetMemberCustomTitle", **kwargs)
        )

    async def set_restriction(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetRestriction operation (groupOutPeer, restriction, nick).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetRestriction", **kwargs)
        )

    async def set_sign_messages(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetSignMessages operation (groupPeer, signMessages).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "SetSignMessages", **kwargs)
        )

    async def set_slow_mode(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups SetSlowMode operation (group, seconds).
        """
        return cast(ProtobufMessage, await self.rpc("groups", "SetSlowMode", **kwargs))

    async def transfer_ownership(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups TransferOwnership operation (groupPeer, newOwner).
        """
        return cast(
            ProtobufMessage, await self.rpc("groups", "TransferOwnership", **kwargs)
        )

    async def un_ban_user(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Groups UnBanUser operation (groupPeer, user, optimizations).
        """
        return cast(ProtobufMessage, await self.rpc("groups", "UnBanUser", **kwargs))

    async def add_card(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users AddCard operation (bankCode).
        """
        return cast(ProtobufMessage, await self.rpc("users", "AddCard", **kwargs))

    async def change_phone_number(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users ChangePhoneNumber operation (phoneNumber).
        """
        return cast(
            ProtobufMessage, await self.rpc("users", "ChangePhoneNumber", **kwargs)
        )

    async def check_nick_name(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users CheckNickName operation (nickname).
        """
        return cast(ProtobufMessage, await self.rpc("users", "CheckNickName", **kwargs))

    async def confirm_phone_number(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users ConfirmPhoneNumber operation (code).
        """
        return cast(
            ProtobufMessage, await self.rpc("users", "ConfirmPhoneNumber", **kwargs)
        )

    async def edit_my_preferred_languages(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users EditMyPreferredLanguages operation (preferredLanguages).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("users", "EditMyPreferredLanguages", **kwargs),
        )

    async def edit_my_time_zone(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users EditMyTimeZone operation (tz).
        """
        return cast(
            ProtobufMessage, await self.rpc("users", "EditMyTimeZone", **kwargs)
        )

    async def edit_nick_name(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users EditNickName operation (nickname).
        """
        return cast(ProtobufMessage, await self.rpc("users", "EditNickName", **kwargs))

    async def get_users_default_card_number(
        self: Any, **kwargs: Any
    ) -> ProtobufMessage:
        """
        Users GetUsersDefaultCardNumber operation (userId).
        """
        return cast(
            ProtobufMessage,
            await self.rpc("users", "GetUsersDefaultCardNumber", **kwargs),
        )

    async def import_contacts(self: Any, **kwargs: Any) -> ProtobufMessage:
        """
        Users ImportContacts operation (phones, optimizations).
        """
        return cast(
            ProtobufMessage, await self.rpc("users", "ImportContacts", **kwargs)
        )

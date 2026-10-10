# مرجع کاربردی متدهای پایتونیک BaleNova (بیش از ۸۳۰ متد مستقیم)

در کتابخانه **BaleNova** هر یک از ۶۹۰ متد پروتکل بله، علاوه بر متدهای سطح‌بالای اختصاصی، به عنوان یک متد مستقل پایتونیک روی شیء `app` (کلاس `Client`) تعریف شده است.

تمامی متدها دارای **آرگومان‌های صریح با Type Hint**، اعتبارسنجی خودکار و راهنمای داخلی Docstring هستند.

---

## 💳 بانک، کیف‌پول، پرداخت و ارز

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.activate_wallet` | `Wallet.ActivateWallet` | `nationalId، isAutoActivated` | `await app.activate_wallet(national_id=...)` |
| `app.activate_yara_messaging` | `BankAccountPreferences.ActivateYaraMessaging` | `accountNumber` | `await app.activate_yara_messaging(account_number=...)` |
| `app.add_destination_cards` | `Sap.AddDestinationCards` | `cards` | `await app.add_destination_cards(cards=...)` |
| `app.add_detail_to_transaction` | `Pfm.AddDetailToTransaction` | `id، detail` | `await app.add_detail_to_transaction(id=...)` |
| `app.add_new_cards` | `Sap.AddNewCards` | `cardInfo` | `await app.add_new_cards(card_info=...)` |
| `app.add_transaction_tags` | `Pfm.AddTransactionTags` | `id، tags` | `await app.add_transaction_tags(id=...)` |
| `app.add_user_tags` | `Pfm.AddUserTags` | `tags` | `await app.add_user_tags(tags=...)` |
| `app.authenticate_user` | `Sarrafi.AuthenticateUser` | `nationalCode، accountNumber` | `await app.authenticate_user(national_code=...)` |
| `app.buy_charge` | `CharnetService.BuyCharge` | `walletToken، phoneNumber، amount (+5)` | `await app.buy_charge(wallet_token=...)` |
| `app.buy_fast_charge` | `Bank.BuyFastCharge` | `amount، phoneNumber، operator (+1)` | `await app.buy_fast_charge(amount=...)` |
| `app.buy_internet_bundle` | `CharnetService.BuyInternetBundle` | `walletToken، phoneNumber، bundleId (+3)` | `await app.buy_internet_bundle(wallet_token=...)` |
| `app.cash_out` | `Kifpool.CashOut` | `requestId، token، amount (+3)` | `await app.cash_out(request_id=...)` |
| `app.cash_out_from_wallet` | `Wallet.CashOutFromWallet` | `token، amount` | `await app.cash_out_from_wallet(token=...)` |
| `app.charge` | `Kifpool.Charge` | `paymentToken، referenceNo` | `await app.charge(payment_token=...)` |
| `app.check_charge_permission` | `Kifpool.CheckChargePermission` | `paymentToken` | `await app.check_charge_permission(payment_token=...)` |
| `app.create_kifpool` | `Kifpool.CreateKifpool` | `nationalId` | `await app.create_kifpool(national_id=...)` |
| `app.create_order` | `Sarrafi.CreateOrder` | `symbol، side، price (+1)` | `await app.create_order(symbol=...)` |
| `app.create_saved_bill` | `Bill.CreateSavedBill` | `name، billType، billParameter` | `await app.create_saved_bill(name=...)` |
| `app.crypto_cash_out` | `Kifpool.CryptoCashOut` | `requestId، amount، account (+3)` | `await app.crypto_cash_out(request_id=...)` |
| `app.crypto_invoice` | `Kifpool.CryptoInvoice` | `token، pageSize، pageNumber` | `await app.crypto_invoice(token=...)` |
| `app.crypto_purchase` | `Kifpool.CryptoPurchase` | `amount، srcToken، dstToken (+3)` | `await app.crypto_purchase(amount=...)` |
| `app.crypto_refund` | `Kifpool.CryptoRefund` | `token، amount، approvalCode (+1)` | `await app.crypto_refund(token=...)` |
| `app.crypto_transfer` | `Kifpool.CryptoTransfer` | `amount، srcToken، dstToken (+2)` | `await app.crypto_transfer(amount=...)` |
| `app.delete_recent_charge_order` | `CharnetService.DeleteRecentChargeOrder` | `accessHash` | `await app.delete_recent_charge_order(access_hash=...)` |
| `app.delete_recent_internet_bundle_order` | `CharnetService.DeleteRecentInternetBundleOrder` | `orderId` | `await app.delete_recent_internet_bundle_order(order_id=...)` |
| `app.delete_saved_bills` | `Bill.DeleteSavedBills` | `ids` | `await app.delete_saved_bills(ids=...)` |
| `app.deliver_otp` | `Sap.DeliverOtp` | `cardId، destinationPan، amount (+2)` | `await app.deliver_otp(card_id=...)` |
| `app.edit_card_expiration_date` | `Sap.EditCardExpirationDate` | `cardId، cardExpDate` | `await app.edit_card_expiration_date(card_id=...)` |
| `app.edit_preference` | `BankAccountPreferences.EditPreference` | `preference` | `await app.edit_preference(preference=...)` |
| `app.enroll_new_card` | `Sap.EnrollNewCard` | `origin` | `await app.enroll_new_card(origin=...)` |
| `app.fee_inquiry` | `Kifpool.FeeInquiry` | `amount، transactionType، pocketType` | `await app.fee_inquiry(amount=...)` |
| `app.filter_tagged_transactions` | `Pfm.FilterTaggedTransactions` | `ids` | `await app.filter_tagged_transactions(ids=...)` |
| `app.get_available_charges` | `CharnetService.GetAvailableCharges` | `operator، chargeType` | `await app.get_available_charges(operator=...)` |
| `app.get_balance` | `GoldWallet.GetBalance` | `بدون پارامتر` | `await app.get_balance()` |
| `app.get_bam_service_token` | `MicroBanki.GetBamServiceToken` | `service` | `await app.get_bam_service_token(service=...)` |
| `app.get_bill_history` | `Bill.GetBillHistory` | `count، page` | `await app.get_bill_history(count=...)` |
| `app.get_bill_menu` | `Bill.GetBillMenu` | `بدون پارامتر` | `await app.get_bill_menu()` |
| `app.get_card_info` | `Sap.GetCardInfo` | `transactionId، cardInfo، cardId` | `await app.get_card_info(transaction_id=...)` |
| `app.get_card_remain` | `Bank.GetCardRemain` | `cardNumber، cvv2، expireDate (+1)` | `await app.get_card_remain(card_number=...)` |
| `app.get_card_transfer_token` | `Bank.GetCardTransferToken` | `peerUserId، msgRid، description` | `await app.get_card_transfer_token(peer_user_id=...)` |
| `app.get_cards` | `Sap.GetCards` | `بدون پارامتر` | `await app.get_cards()` |
| `app.get_charge_payment_token` | `Kifpool.GetChargePaymentToken` | `token، amount، callbackType` | `await app.get_charge_payment_token(token=...)` |
| `app.get_charge_token` | `Sarrafi.GetChargeToken` | `currency، amount` | `await app.get_charge_token(currency=...)` |
| `app.get_credit` | `Kifpool.GetCredit` | `بدون پارامتر` | `await app.get_credit()` |
| `app.get_crypto_charge_payment_token` | `Kifpool.GetCryptoChargePaymentToken` | `token، amount، receiverId` | `await app.get_crypto_charge_payment_token(token=...)` |
| `app.get_crypto_wallets` | `Kifpool.GetCryptoWallets` | `بدون پارامتر` | `await app.get_crypto_wallets()` |
| `app.get_currencies_list` | `Exchange.GetCurrenciesList` | `بدون پارامتر` | `await app.get_currencies_list()` |
| `app.get_currency_price` | `Exchange.GetCurrencyPrice` | `currencyType، currencyAmount، reason (+5)` | `await app.get_currency_price(currency_type=...)` |
| `app.get_default_card` | `Sap.GetDefaultCard` | `بدون پارامتر` | `await app.get_default_card()` |
| `app.get_depth` | `Sarrafi.GetDepth` | `symbol، limit` | `await app.get_depth(symbol=...)` |
| `app.get_destination_card_info` | `Sap.GetDestinationCardInfo` | `cardId، destinationPan، amount (+4)` | `await app.get_destination_card_info(card_id=...)` |
| `app.get_destination_cards` | `Sap.GetDestinationCards` | `بدون پارامتر` | `await app.get_destination_cards()` |
| `app.get_exchange_order_info` | `Exchange.GetExchangeOrderInfo` | `orderId` | `await app.get_exchange_order_info(order_id=...)` |
| `app.get_exchange_payment_token` | `Exchange.GetExchangePaymentToken` | `orderId، callBack` | `await app.get_exchange_payment_token(order_id=...)` |
| `app.get_initial_config` | `Exchange.GetInitialConfig` | `origin` | `await app.get_initial_config(origin=...)` |
| `app.get_internet_bundle_list` | `CharnetService.GetInternetBundleList` | `operatorType، simCardType، phoneNumber` | `await app.get_internet_bundle_list(operator_type=...)` |
| `app.get_internet_bundle_payment_token` | `CharnetService.GetInternetBundlePaymentToken` | `operatorType، bundleId، phoneNumber (+1)` | `await app.get_internet_bundle_payment_token(operator_type=...)` |
| `app.get_kifpool_owner` | `Kifpool.GetKifpoolOwner` | `walletToken` | `await app.get_kifpool_owner(wallet_token=...)` |
| `app.get_kifpool_point_balance` | `Kifpool.GetKifpoolPointBalance` | `token` | `await app.get_kifpool_point_balance(token=...)` |
| `app.get_kifpool_point_details` | `Kifpool.GetKifpoolPointDetails` | `token، count، page` | `await app.get_kifpool_point_details(token=...)` |
| `app.get_kifpool_point_summery` | `Kifpool.GetKifpoolPointSummery` | `token` | `await app.get_kifpool_point_summery(token=...)` |
| `app.get_kifpool_transaction_point` | `Kifpool.GetKifpoolTransactionPoint` | `transactionID، amount` | `await app.get_kifpool_transaction_point(transaction_id=...)` |
| `app.get_list_of_delivery_stations` | `Exchange.GetListOfDeliveryStations` | `deliveryStationType، reason، ExitDate` | `await app.get_list_of_delivery_stations(delivery_station_type=...)` |
| `app.get_money_request_details` | `MicroBanki.GetMoneyRequestDetails` | `message` | `await app.get_money_request_details(message=...)` |
| `app.get_money_request_payment_list` | `MicroBanki.GetMoneyRequestPaymentList` | `message، loadMoreState` | `await app.get_money_request_payment_list(message=...)` |
| `app.get_money_request_payment_token_by_card` | `Wallet.GetMoneyRequestPaymentTokenByCard` | `msg، amount، regarding` | `await app.get_money_request_payment_token_by_card(msg=...)` |
| `app.get_my_bank` | `MyBank.GetMyBank` | `بدون پارامتر` | `await app.get_my_bank()` |
| `app.get_my_kifpools` | `Kifpool.GetMyKifpools` | `invocationSpot، pocketType` | `await app.get_my_kifpools(invocation_spot=...)` |
| `app.get_my_wallets` | `Wallet.GetMyWallets` | `بدون پارامتر` | `await app.get_my_wallets()` |
| `app.get_otp_token` | `Bank.GetOTPToken` | `cardNumberStartingSix` | `await app.get_otp_token(card_number_starting_six=...)` |
| `app.get_otp_token_v2` | `Bank.GetOTPTokenV2` | `messagePeer، msgRid، msgDate (+2)` | `await app.get_otp_token_v2(message_peer=...)` |
| `app.get_order` | `Sarrafi.GetOrder` | `orderId` | `await app.get_order(order_id=...)` |
| `app.get_orders` | `Sarrafi.GetOrders` | `بدون پارامتر` | `await app.get_orders()` |
| `app.get_organization_payment_token` | `Bank.GetOrganizationPaymentToken` | `organizationId، invoiceId، amount` | `await app.get_organization_payment_token(organization_id=...)` |
| `app.get_ps_proxy_payment_token` | `Bank.GetPSProxyPaymentToken` | `paymentAmount، msg، description` | `await app.get_ps_proxy_payment_token(payment_amount=...)` |
| `app.get_ps_proxy_token` | `Bank.GetPSProxyToken` | `بدون پارامتر` | `await app.get_ps_proxy_token()` |
| `app.get_pay_money_request_token` | `Bank.GetPayMoneyRequestToken` | `messagePeer، msgRid، msgDate (+2)` | `await app.get_pay_money_request_token(message_peer=...)` |
| `app.get_payment_token` | `Bank.GetPaymentToken` | `msg، description، amount` | `await app.get_payment_token(msg=...)` |
| `app.get_payment_token_by_card` | `Wallet.GetPaymentTokenByCard` | `targetWallet، amount، regarding` | `await app.get_payment_token_by_card(target_wallet=...)` |
| `app.get_payvand_card` | `Bank.GetPayvandCard` | `index` | `await app.get_payvand_card(index=...)` |
| `app.get_payvand_card_list` | `Bank.GetPayvandCardList` | `بدون پارامتر` | `await app.get_payvand_card_list()` |
| `app.get_preferences` | `BankAccountPreferences.GetPreferences` | `بدون پارامتر` | `await app.get_preferences()` |
| `app.get_recent_charge_orders` | `CharnetService.GetRecentChargeOrders` | `count، types` | `await app.get_recent_charge_orders(count=...)` |
| `app.get_recent_charges` | `Bank.GetRecentCharges` | `بدون پارامتر` | `await app.get_recent_charges()` |
| `app.get_recent_internet_bundle_orders` | `CharnetService.GetRecentInternetBundleOrders` | `count` | `await app.get_recent_internet_bundle_orders(count=...)` |
| `app.get_remain_token` | `Bank.GetRemainToken` | `cardNumberStartingSix` | `await app.get_remain_token(card_number_starting_six=...)` |
| `app.get_sadad_psp_payment_token` | `Bank.GetSadadPSPPaymentToken` | `msg، paymentAmount، description` | `await app.get_sadad_psp_payment_token(msg=...)` |
| `app.get_saved_bills` | `Bill.GetSavedBills` | `count، page` | `await app.get_saved_bills(count=...)` |
| `app.get_session` | `Sarrafi.GetSession` | `symbol` | `await app.get_session(symbol=...)` |
| `app.get_sub_transactions` | `Pfm.GetSubTransactions` | `transactionId` | `await app.get_sub_transactions(transaction_id=...)` |
| `app.get_tickers` | `Sarrafi.GetTickers` | `بدون پارامتر` | `await app.get_tickers()` |
| `app.get_token_invoice` | `Bank.GetTokenInvoice` | `service` | `await app.get_token_invoice(service=...)` |
| `app.get_top_up_charge_payment_token` | `CharnetService.GetTopUpChargePaymentToken` | `providerCode، topupType، amount (+2)` | `await app.get_top_up_charge_payment_token(provider_code=...)` |
| `app.get_transaction_tags` | `Pfm.GetTransactionTags` | `id` | `await app.get_transaction_tags(id=...)` |
| `app.get_travel_currency_order_in_detail` | `Exchange.GetTravelCurrencyOrderInDetail` | `phoneNumber، nationalCode، userId` | `await app.get_travel_currency_order_in_detail(phone_number=...)` |
| `app.get_user_accounts` | `Pfm.GetUserAccounts` | `بدون پارامتر` | `await app.get_user_accounts()` |
| `app.get_user_icms_info` | `Exchange.GetUserIcmsInfo` | `nationalCode، birthDate` | `await app.get_user_icms_info(national_code=...)` |
| `app.get_user_tags` | `Pfm.GetUserTags` | `getUserTagType` | `await app.get_user_tags(get_user_tag_type=...)` |
| `app.get_voucher_charge_payment_token` | `CharnetService.GetVoucherChargePaymentToken` | `providerCode، amount، targetUserId` | `await app.get_voucher_charge_payment_token(provider_code=...)` |
| `app.get_wallet` | `Sarrafi.GetWallet` | `بدون پارامتر` | `await app.get_wallet()` |
| `app.get_wallet_charge_token` | `Wallet.GetWalletChargeToken` | `walletId، amount` | `await app.get_wallet_charge_token(wallet_id=...)` |
| `app.get_wallet_contracts` | `Wallet.GetWalletContracts` | `بدون پارامتر` | `await app.get_wallet_contracts()` |
| `app.get_wallet_invoice` | `Wallet.GetWalletInvoice` | `walletId، pageNumber` | `await app.get_wallet_invoice(wallet_id=...)` |
| `app.get_winner_i_ds` | `GoldGiftPacket.GetWinnerIDs` | `giftPacketId` | `await app.get_winner_i_ds(gift_packet_id=...)` |
| `app.grant_banki_access` | `Bank.GrantBankiAccess` | `bot، serviceKey` | `await app.grant_banki_access(bot=...)` |
| `app.inquiry_bill` | `Bill.InquiryBill` | `billType، billParameters` | `await app.inquiry_bill(bill_type=...)` |
| `app.invoice` | `Kifpool.Invoice` | `token، pageSize، pageNumber` | `await app.invoice(token=...)` |
| `app.load_exchange_history` | `Exchange.LoadExchangeHistory` | `بدون پارامتر` | `await app.load_exchange_history()` |
| `app.load_transactions` | `Pfm.LoadTransactions` | `accountNumber، startDate، endDate (+6)` | `await app.load_transactions(account_number=...)` |
| `app.load_transactions_by_i_ds` | `Pfm.LoadTransactionsByIDs` | `transactionIds` | `await app.load_transactions_by_i_ds(transaction_ids=...)` |
| `app.open_gold_gift_packet` | `GoldGiftPacket.OpenGoldGiftPacket` | `giftPacketId` | `await app.open_gold_gift_packet(gift_packet_id=...)` |
| `app.pay_bill` | `Bill.PayBill` | `bill` | `await app.pay_bill(bill=...)` |
| `app.pay_by_wallet` | `Wallet.PayByWallet` | `sourceWallet، targetWallet، amount (+2)` | `await app.pay_by_wallet(source_wallet=...)` |
| `app.pay_for_message` | `Kifpool.PayForMessage` | `amount، chargeAmount، message` | `await app.pay_for_message(amount=...)` |
| `app.pay_money_request_by_wallet` | `Wallet.PayMoneyRequestByWallet` | `sourceWalletId، msg، amount (+1)` | `await app.pay_money_request_by_wallet(source_wallet_id=...)` |
| `app.purchase` | `Kifpool.Purchase` | `amount، dstToken، srcToken (+5)` | `await app.purchase(amount=...)` |
| `app.purchase_message` | `Kifpool.PurchaseMessage` | `historyId، amount، description` | `await app.purchase_message(history_id=...)` |
| `app.purchase_message_with_charge` | `Kifpool.PurchaseMessageWithCharge` | `historyId، amount، description (+1)` | `await app.purchase_message_with_charge(history_id=...)` |
| `app.purchase_with_charge` | `Kifpool.PurchaseWithCharge` | `amount، dstToken، srcToken (+6)` | `await app.purchase_with_charge(amount=...)` |
| `app.reactivate_app` | `Sap.ReactivateApp` | `بدون پارامتر` | `await app.reactivate_app()` |
| `app.remove_card` | `Sap.RemoveCard` | `cardId` | `await app.remove_card(card_id=...)` |
| `app.remove_default_card` | `Sap.RemoveDefaultCard` | `بدون پارامتر` | `await app.remove_default_card()` |
| `app.remove_destination_cards` | `Sap.RemoveDestinationCards` | `ids` | `await app.remove_destination_cards(ids=...)` |
| `app.remove_transaction` | `Pfm.RemoveTransaction` | `transactionIds` | `await app.remove_transaction(transaction_ids=...)` |
| `app.remove_transaction_tags` | `Pfm.RemoveTransactionTags` | `id، tags` | `await app.remove_transaction_tags(id=...)` |
| `app.remove_user_tags` | `Pfm.RemoveUserTags` | `tags` | `await app.remove_user_tags(tags=...)` |
| `app.rename_saved_bill` | `Bill.RenameSavedBill` | `id، name` | `await app.rename_saved_bill(id=...)` |
| `app.revive_transaction` | `Pfm.ReviveTransaction` | `transactionId` | `await app.revive_transaction(transaction_id=...)` |
| `app.send_gold_gift_packet` | `GoldGiftPacket.SendGoldGiftPacket` | `amount، count، description (+3)` | `await app.send_gold_gift_packet(amount=...)` |
| `app.set_default_card` | `Sap.SetDefaultCard` | `cardId` | `await app.set_default_card(card_id=...)` |
| `app.split_transaction` | `Pfm.SplitTransaction` | `transactionId، units` | `await app.split_transaction(transaction_id=...)` |
| `app.transfer` | `Kifpool.Transfer` | `sourceToken، destinationToken، destinationPhone (+3)` | `await app.transfer(source_token=...)` |
| `app.transfer_money_by_card` | `Sap.TransferMoneyByCard` | `cardId، transferCode، destinationPan (+12)` | `await app.transfer_money_by_card(card_id=...)` |
| `app.upgrade_kifpool` | `Kifpool.UpgradeKifpool` | `token، nationalId، cardNo (+2)` | `await app.upgrade_kifpool(token=...)` |
| `app.verify_cash_out` | `Wallet.VerifyCashOut` | `walletId، accountNo، nationalId` | `await app.verify_cash_out(wallet_id=...)` |
| `app.verify_cash_out_kifpool` | `Kifpool.VerifyCashOutKifpool` | `token` | `await app.verify_cash_out_kifpool(token=...)` |
| `app.verify_peer` | `Wallet.VerifyPeer` | `targetPeer` | `await app.verify_peer(target_peer=...)` |
| `app.verify_purchase_message` | `Kifpool.VerifyPurchaseMessage` | `historyId` | `await app.verify_purchase_message(history_id=...)` |
| `app.verify_qr_code` | `Wallet.VerifyQRCode` | `targetWalletId` | `await app.verify_qr_code(target_wallet_id=...)` |
| `app.verify_user_exchange_authority` | `Exchange.VerifyUserExchangeAuthority` | `firstName، lastName، nationalCode (+6)` | `await app.verify_user_exchange_authority(first_name=...)` |

## 💬 پیام‌رسانی، فایل‌ها، رسانه‌ها و استیکر

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.add_gif` | `Images.AddGif` | `gif، thumb، mimeType` | `await app.add_gif(gif=...)` |
| `app.add_sticker_collection` | `Images.AddStickerCollection` | `id، accessHash` | `await app.add_sticker_collection(id=...)` |
| `app.add_sticker_pack` | `Images.AddStickerPack` | `id` | `await app.add_sticker_pack(id=...)` |
| `app.archive_dialogs` | `Messaging.ArchiveDialogs` | `exPeers` | `await app.archive_dialogs(ex_peers=...)` |
| `app.cancel_message_stream` | `MessageStream.CancelMessageStream` | `exPeer، messageId` | `await app.cancel_message_stream(ex_peer=...)` |
| `app.clear_chat` | `Messaging.ClearChat` | `peer` | `await app.clear_chat(peer=...)` |
| `app.create_folder` | `Messaging.CreateFolder` | `name، peers` | `await app.create_folder(name=...)` |
| `app.create_reserved_folder` | `Messaging.CreateReservedFolder` | `folderId` | `await app.create_reserved_folder(folder_id=...)` |
| `app.create_thread` | `Messaging.CreateThread` | `peer، date، randomId (+1)` | `await app.create_thread(peer=...)` |
| `app.create_topic` | `Messaging.CreateTopic` | `exPeer، title` | `await app.create_topic(ex_peer=...)` |
| `app.delete_chat` | `Messaging.DeleteChat` | `peer` | `await app.delete_chat(peer=...)` |
| `app.delete_folder` | `Messaging.DeleteFolder` | `folderId` | `await app.delete_folder(folder_id=...)` |
| `app.delete_message` | `Messaging.DeleteMessage` | `peer، rids، dates (+1)` | `await app.delete_message(peer=...)` |
| `app.delete_topic` | `Messaging.DeleteTopic` | `exPeer، topicId` | `await app.delete_topic(ex_peer=...)` |
| `app.edit_folder` | `Messaging.EditFolder` | `folderId، name، addedPeers (+1)` | `await app.edit_folder(folder_id=...)` |
| `app.edit_topic` | `Messaging.EditTopic` | `exPeer، topicId، title` | `await app.edit_topic(ex_peer=...)` |
| `app.enable_show_reaction_flag` | `Abacus.EnableShowReactionFlag` | `بدون پارامتر` | `await app.enable_show_reaction_flag()` |
| `app.fetch_protected_message` | `Messaging.FetchProtectedMessage` | `peer، messageId` | `await app.fetch_protected_message(peer=...)` |
| `app.file_upload_cancel` | `Files.FileUploadCancel` | `file` | `await app.file_upload_cancel(file=...)` |
| `app.forward_messages` | `Messaging.ForwardMessages` | `peer، rid، forwardedMessages (+2)` | `await app.forward_messages(peer=...)` |
| `app.get_active_shared_media` | `SharedMediaService.GetActiveSharedMedia` | `exPeer` | `await app.get_active_shared_media(ex_peer=...)` |
| `app.get_discussion_message` | `Messaging.GetDiscussionMessage` | `peer، messageId` | `await app.get_discussion_message(peer=...)` |
| `app.get_message_reactions_list` | `Abacus.GetMessageReactionsList` | `peer، rid، date (+3)` | `await app.get_message_reactions_list(peer=...)` |
| `app.get_messages_reactions` | `Abacus.GetMessagesReactions` | `peer، mids، originPeer (+1)` | `await app.get_messages_reactions(peer=...)` |
| `app.get_messages_replies_info` | `Messaging.GetMessagesRepliesInfo` | `peer، mids` | `await app.get_messages_replies_info(peer=...)` |
| `app.get_messages_views` | `Abacus.GetMessagesViews` | `peer، mids، increment (+1)` | `await app.get_messages_views(peer=...)` |
| `app.get_nasim_file_public_url` | `Files.GetNasimFilePublicUrl` | `peer، file، filename` | `await app.get_nasim_file_public_url(peer=...)` |
| `app.get_nasim_file_upload_resume` | `Files.GetNasimFileUploadResume` | `file` | `await app.get_nasim_file_upload_resume(file=...)` |
| `app.get_nasim_file_upload_url` | `Files.GetNasimFileUploadUrl` | `expectedSize، crc، uid (+7)` | `await app.get_nasim_file_upload_url(expected_size=...)` |
| `app.get_nasim_file_url` | `Files.GetNasimFileUrl` | `file، ciphertext` | `await app.get_nasim_file_url(file=...)` |
| `app.get_nasim_file_urls` | `Files.GetNasimFileUrls` | `files، ciphertext` | `await app.get_nasim_file_urls(files=...)` |
| `app.get_saved_gifs` | `Images.GetSavedGifs` | `offset` | `await app.get_saved_gifs(offset=...)` |
| `app.get_show_reaction_flag` | `Abacus.GetShowReactionFlag` | `بدون پارامتر` | `await app.get_show_reaction_flag()` |
| `app.get_topic_by_id` | `Messaging.GetTopicByID` | `exPeer، topicId` | `await app.get_topic_by_id(ex_peer=...)` |
| `app.get_topics` | `Messaging.GetTopics` | `exPeer، minDate، limit` | `await app.get_topics(ex_peer=...)` |
| `app.get_upload_limits` | `Files.GetUploadLimits` | `بدون پارامتر` | `await app.get_upload_limits()` |
| `app.load_dialogs` | `Messaging.LoadDialogs` | `minDate، limit، optimizations (+3)` | `await app.load_dialogs(min_date=...)` |
| `app.load_folder_dialogs` | `Messaging.LoadFolderDialogs` | `minDate، limit، folderId (+1)` | `await app.load_folder_dialogs(min_date=...)` |
| `app.load_folders` | `Messaging.LoadFolders` | `includeMutedUnreadPeers، isNewUser` | `await app.load_folders(include_muted_unread_peers=...)` |
| `app.load_grouped_dialogs` | `Messaging.LoadGroupedDialogs` | `optimizations، archiveFilter` | `await app.load_grouped_dialogs(optimizations=...)` |
| `app.load_history` | `Messaging.LoadHistory` | `peer، date، loadMode (+2)` | `await app.load_history(peer=...)` |
| `app.load_media` | `SharedMediaService.LoadMedia` | `exPeer، date، contentType (+2)` | `await app.load_media(ex_peer=...)` |
| `app.load_own_stickers` | `Images.LoadOwnStickers` | `offset` | `await app.load_own_stickers(offset=...)` |
| `app.load_peer_dialogs` | `Messaging.LoadPeerDialogs` | `peers` | `await app.load_peer_dialogs(peers=...)` |
| `app.load_peers` | `Messaging.LoadPeers` | `بدون پارامتر` | `await app.load_peers()` |
| `app.load_pinned_dialogs` | `Messaging.LoadPinnedDialogs` | `folderId` | `await app.load_pinned_dialogs(folder_id=...)` |
| `app.load_pinned_messages` | `Messaging.LoadPinnedMessages` | `peer` | `await app.load_pinned_messages(peer=...)` |
| `app.load_reactions` | `Abacus.LoadReactions` | `peer، mids، ignoreCountViews` | `await app.load_reactions(peer=...)` |
| `app.load_replies` | `Messaging.LoadReplies` | `peer، threadId، date (+2)` | `await app.load_replies(peer=...)` |
| `app.load_sticker_collection` | `Images.LoadStickerCollection` | `id، accessHash` | `await app.load_sticker_collection(id=...)` |
| `app.mark_dialogs_as_read` | `Messaging.MarkDialogsAsRead` | `peers` | `await app.mark_dialogs_as_read(peers=...)` |
| `app.mark_dialogs_as_unread` | `Messaging.MarkDialogsAsUnread` | `peers` | `await app.mark_dialogs_as_unread(peers=...)` |
| `app.mention_read` | `Messaging.MentionRead` | `peer، messageId` | `await app.mention_read(peer=...)` |
| `app.message_reactions_read` | `Abacus.MessageReactionsRead` | `peer، messageId` | `await app.message_reactions_read(peer=...)` |
| `app.message_read` | `Messaging.MessageRead` | `peer، date، exPeer` | `await app.message_read(peer=...)` |
| `app.message_received` | `Messaging.MessageReceived` | `peer، date` | `await app.message_received(peer=...)` |
| `app.message_remove_reaction` | `Abacus.MessageRemoveReaction` | `peer، rid، code (+1)` | `await app.message_remove_reaction(peer=...)` |
| `app.message_set_reaction` | `Abacus.MessageSetReaction` | `peer، rid، code (+1)` | `await app.message_set_reaction(peer=...)` |
| `app.pin_dialogs` | `Messaging.PinDialogs` | `peers، folderId` | `await app.pin_dialogs(peers=...)` |
| `app.pin_message` | `Messaging.PinMessage` | `peer، messageId، justMine` | `await app.pin_message(peer=...)` |
| `app.receive_message_stream` | `MessageStream.ReceiveMessageStream` | `exPeer، messageId، fromChunkId` | `await app.receive_message_stream(ex_peer=...)` |
| `app.register_google_push` | `Push.RegisterGooglePush` | `projectId، token` | `await app.register_google_push(project_id=...)` |
| `app.register_push` | `Push.RegisterPush` | `register، pushVersion` | `await app.register_push(register=...)` |
| `app.remove_gif` | `Images.RemoveGif` | `gif` | `await app.remove_gif(gif=...)` |
| `app.remove_sticker_collection` | `Images.RemoveStickerCollection` | `id، accessHash` | `await app.remove_sticker_collection(id=...)` |
| `app.remove_sticker_pack` | `Images.RemoveStickerPack` | `id` | `await app.remove_sticker_pack(id=...)` |
| `app.reorder_folders` | `Messaging.ReorderFolders` | `folderIds` | `await app.reorder_folders(folder_ids=...)` |
| `app.reorder_pinned_dialogs` | `Messaging.ReorderPinnedDialogs` | `peers، folderId` | `await app.reorder_pinned_dialogs(peers=...)` |
| `app.send_message` | `Messaging.SendMessage` | `peer، rid، message (+5)` | `await app.send_message(peer=...)` |
| `app.send_multi_media_message` | `Messaging.SendMultiMediaMessage` | `peer، multiMedia، repliedMessage (+1)` | `await app.send_multi_media_message(peer=...)` |
| `app.set_config` | `Push.SetConfig` | `config` | `await app.set_config(config=...)` |
| `app.un_archive_dialogs` | `Messaging.UnArchiveDialogs` | `exPeers` | `await app.un_archive_dialogs(ex_peers=...)` |
| `app.un_pin_messages` | `Messaging.UnPinMessages` | `peer، messageIds، all` | `await app.un_pin_messages(peer=...)` |
| `app.unpin_dialogs` | `Messaging.UnpinDialogs` | `peers، folderId` | `await app.unpin_dialogs(peers=...)` |
| `app.unregister_all_push_credentials` | `Push.UnregisterAllPushCredentials` | `بدون پارامتر` | `await app.unregister_all_push_credentials()` |
| `app.unregister_google_push` | `Push.UnregisterGooglePush` | `token` | `await app.unregister_google_push(token=...)` |
| `app.unregister_push` | `Push.UnregisterPush` | `unregister` | `await app.unregister_push(unregister=...)` |
| `app.update_message` | `Messaging.UpdateMessage` | `peer، rid، updatedMessage` | `await app.update_message(peer=...)` |
| `app.use_gif` | `Images.UseGif` | `gif، usedAt` | `await app.use_gif(gif=...)` |

## 👥 گروه‌ها، کانال‌ها، کاربران و حضور

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.add_card` | `Users.AddCard` | `bankCode` | `await app.add_card(bank_code=...)` |
| `app.add_contact` | `Users.AddContact` | `uid، accessHash` | `await app.add_contact(uid=...)` |
| `app.add_discussion_group_admin` | `Groups.AddDiscussionGroupAdmin` | `channel، discussionGroup` | `await app.add_discussion_group_admin(channel=...)` |
| `app.block_user` | `Users.BlockUser` | `peer` | `await app.block_user(peer=...)` |
| `app.change_default_card_number` | `Users.ChangeDefaultCardNumber` | `defaultCardNumber` | `await app.change_default_card_number(default_card_number=...)` |
| `app.change_phone_number` | `Users.ChangePhoneNumber` | `phoneNumber` | `await app.change_phone_number(phone_number=...)` |
| `app.check_nick_name` | `Users.CheckNickName` | `nickname` | `await app.check_nick_name(nickname=...)` |
| `app.confirm_phone_number` | `Users.ConfirmPhoneNumber` | `code` | `await app.confirm_phone_number(code=...)` |
| `app.create_group` | `Groups.CreateGroup` | `rid، title، users (+4)` | `await app.create_group(rid=...)` |
| `app.edit_about` | `Users.EditAbout` | `about` | `await app.edit_about(about=...)` |
| `app.edit_avatar` | `Users.EditAvatar` | `fileLocation` | `await app.edit_avatar(file_location=...)` |
| `app.edit_birth_date` | `Users.EditBirthDate` | `date` | `await app.edit_birth_date(date=...)` |
| `app.edit_channel_nick` | `Groups.EditChannelNick` | `groupPeer، nick، randomId` | `await app.edit_channel_nick(group_peer=...)` |
| `app.edit_group_about` | `Groups.EditGroupAbout` | `groupPeer، rid، about (+1)` | `await app.edit_group_about(group_peer=...)` |
| `app.edit_group_avatar` | `Groups.EditGroupAvatar` | `groupPeer، fileLocation، rid (+1)` | `await app.edit_group_avatar(group_peer=...)` |
| `app.edit_group_default_card_number` | `Groups.EditGroupDefaultCardNumber` | `groupPeer، cardNumber` | `await app.edit_group_default_card_number(group_peer=...)` |
| `app.edit_group_title` | `Groups.EditGroupTitle` | `groupPeer، title، rid (+1)` | `await app.edit_group_title(group_peer=...)` |
| `app.edit_my_preferred_languages` | `Users.EditMyPreferredLanguages` | `preferredLanguages` | `await app.edit_my_preferred_languages(preferred_languages=...)` |
| `app.edit_my_time_zone` | `Users.EditMyTimeZone` | `tz` | `await app.edit_my_time_zone(tz=...)` |
| `app.edit_name` | `Users.EditName` | `name` | `await app.edit_name(name=...)` |
| `app.edit_nick_name` | `Users.EditNickName` | `nickname` | `await app.edit_nick_name(nickname=...)` |
| `app.edit_sex` | `Users.EditSex` | `sex` | `await app.edit_sex(sex=...)` |
| `app.edit_user_local_name` | `Users.EditUserLocalName` | `uid، accessHash، name` | `await app.edit_user_local_name(uid=...)` |
| `app.fetch_group_admins` | `Groups.FetchGroupAdmins` | `groupOutPeer` | `await app.fetch_group_admins(group_out_peer=...)` |
| `app.get_banned_users` | `Groups.GetBannedUsers` | `group` | `await app.get_banned_users(group=...)` |
| `app.get_can_see_messages` | `Groups.GetCanSeeMessages` | `groupPeer، userId` | `await app.get_can_see_messages(group_peer=...)` |
| `app.get_contacts` | `Users.GetContacts` | `contactsHash، optimizations` | `await app.get_contacts(contacts_hash=...)` |
| `app.get_contacts_presences` | `Presence.GetContactsPresences` | `limit` | `await app.get_contacts_presences(limit=...)` |
| `app.get_full_group` | `Groups.GetFullGroup` | `peer` | `await app.get_full_group(peer=...)` |
| `app.get_full_user` | `Users.GetFullUser` | `peer` | `await app.get_full_user(peer=...)` |
| `app.get_group_default_card_number` | `Groups.GetGroupDefaultCardNumber` | `groupPeerr` | `await app.get_group_default_card_number(group_peerr=...)` |
| `app.get_group_invite_url` | `Groups.GetGroupInviteURL` | `groupPeer` | `await app.get_group_invite_url(group_peer=...)` |
| `app.get_group_members_count` | `Groups.GetGroupMembersCount` | `group` | `await app.get_group_members_count(group=...)` |
| `app.get_group_members_presences` | `Presence.GetGroupMembersPresences` | `peer` | `await app.get_group_members_presences(peer=...)` |
| `app.get_group_online_count` | `Presence.GetGroupOnlineCount` | `peer` | `await app.get_group_online_count(peer=...)` |
| `app.get_group_preview` | `Groups.GetGroupPreview` | `token، isOpenedOutsideBale` | `await app.get_group_preview(token=...)` |
| `app.get_group_recommendations` | `Groups.GetGroupRecommendations` | `source` | `await app.get_group_recommendations(source=...)` |
| `app.get_member_permissions` | `Groups.GetMemberPermissions` | `group، user` | `await app.get_member_permissions(group=...)` |
| `app.get_mutual_groups` | `Groups.GetMutualGroups` | `peer` | `await app.get_mutual_groups(peer=...)` |
| `app.get_my_groups` | `Groups.GetMyGroups` | `mode، isOwner، filters` | `await app.get_my_groups(mode=...)` |
| `app.get_pins` | `Groups.GetPins` | `groupPeer، page، limit` | `await app.get_pins(group_peer=...)` |
| `app.get_user_full_privacy` | `Users.GetUserFullPrivacy` | `userId` | `await app.get_user_full_privacy(user_id=...)` |
| `app.get_user_organization_info` | `Organizations.GetUserOrganizationInfo` | `بدون پارامتر` | `await app.get_user_organization_info()` |
| `app.get_user_organizational_contacts` | `Organizations.GetUserOrganizationalContacts` | `بدون پارامتر` | `await app.get_user_organizational_contacts()` |
| `app.get_user_privacy_status` | `Users.GetUserPrivacyStatus` | `userId، type` | `await app.get_user_privacy_status(user_id=...)` |
| `app.get_users_default_card_number` | `Users.GetUsersDefaultCardNumber` | `userId` | `await app.get_users_default_card_number(user_id=...)` |
| `app.get_users_presence` | `Presence.GetUsersPresence` | `userIds` | `await app.get_users_presence(user_ids=...)` |
| `app.import_contacts` | `Users.ImportContacts` | `phones، optimizations` | `await app.import_contacts(phones=...)` |
| `app.invite_user` | `Groups.InviteUser` | `groupPeer، user، rid (+2)` | `await app.invite_user(group_peer=...)` |
| `app.invite_users` | `Groups.InviteUsers` | `groupPeer، rid، users` | `await app.invite_users(group_peer=...)` |
| `app.is_name_allowed` | `Users.IsNameAllowed` | `name` | `await app.is_name_allowed(name=...)` |
| `app.join_group` | `Groups.JoinGroup` | `token، optimizations` | `await app.join_group(token=...)` |
| `app.join_public_group` | `Groups.JoinPublicGroup` | `peer، optimizations` | `await app.join_public_group(peer=...)` |
| `app.kick_user` | `Groups.KickUser` | `groupPeer، user، rid (+1)` | `await app.kick_user(group_peer=...)` |
| `app.leave_group` | `Groups.LeaveGroup` | `groupPeer، rid، optimizations (+1)` | `await app.leave_group(group_peer=...)` |
| `app.load_avatars` | `Users.LoadAvatars` | `peer` | `await app.load_avatars(peer=...)` |
| `app.load_blocked_users` | `Users.LoadBlockedUsers` | `بدون پارامتر` | `await app.load_blocked_users()` |
| `app.load_full_groups` | `Groups.LoadFullGroups` | `groups` | `await app.load_full_groups(groups=...)` |
| `app.load_full_users` | `Users.LoadFullUsers` | `userPeers` | `await app.load_full_users(user_peers=...)` |
| `app.load_full_users_sequentially` | `Users.LoadFullUsersSequentially` | `userPeers` | `await app.load_full_users_sequentially(user_peers=...)` |
| `app.load_group_avatars` | `Groups.LoadGroupAvatars` | `peer` | `await app.load_group_avatars(peer=...)` |
| `app.load_groups` | `Groups.LoadGroups` | `peers` | `await app.load_groups(peers=...)` |
| `app.load_members` | `Groups.LoadMembers` | `group، limit، next (+1)` | `await app.load_members(group=...)` |
| `app.load_users` | `Users.LoadUsers` | `peers` | `await app.load_users(peers=...)` |
| `app.make_user_admin` | `Groups.MakeUserAdmin` | `groupPeer، userPeer، adminTitle` | `await app.make_user_admin(group_peer=...)` |
| `app.notify_about_device_info` | `Users.NotifyAboutDeviceInfo` | `preferredLanguages، timeZone` | `await app.notify_about_device_info(preferred_languages=...)` |
| `app.pin_message` | `Groups.PinMessage` | `senderUserId، groupPeer، date (+1)` | `await app.pin_message(sender_user_id=...)` |
| `app.remove_avatar` | `Users.RemoveAvatar` | `avaterId` | `await app.remove_avatar(avater_id=...)` |
| `app.remove_contact` | `Users.RemoveContact` | `uid، accessHash` | `await app.remove_contact(uid=...)` |
| `app.remove_default_card_number` | `Users.RemoveDefaultCardNumber` | `بدون پارامتر` | `await app.remove_default_card_number()` |
| `app.remove_discussion_group` | `Groups.RemoveDiscussionGroup` | `rid، channel` | `await app.remove_discussion_group(rid=...)` |
| `app.remove_group_avatar` | `Groups.RemoveGroupAvatar` | `groupPeer، rid، optimizations (+1)` | `await app.remove_group_avatar(group_peer=...)` |
| `app.remove_pin` | `Groups.RemovePin` | `groupPeer` | `await app.remove_pin(group_peer=...)` |
| `app.remove_single_pin` | `Groups.RemoveSinglePin` | `groupPeer، msgRid، msgDate` | `await app.remove_single_pin(group_peer=...)` |
| `app.remove_user_admin` | `Groups.RemoveUserAdmin` | `groupPeer، userPeer` | `await app.remove_user_admin(group_peer=...)` |
| `app.reset_contacts` | `Users.ResetContacts` | `بدون پارامتر` | `await app.reset_contacts()` |
| `app.revoke_invite_url` | `Groups.RevokeInviteURL` | `groupPeer` | `await app.revoke_invite_url(group_peer=...)` |
| `app.search_contacts` | `Users.SearchContacts` | `request، optimizations` | `await app.search_contacts(request=...)` |
| `app.set_available_reactions` | `Groups.SetAvailableReactions` | `group، codes` | `await app.set_available_reactions(group=...)` |
| `app.set_can_see_history` | `Groups.SetCanSeeHistory` | `groupPeer، canSeeHistory` | `await app.set_can_see_history(group_peer=...)` |
| `app.set_can_see_messages` | `Groups.SetCanSeeMessages` | `groupPeer، userId، canSeeMessages` | `await app.set_can_see_messages(group_peer=...)` |
| `app.set_discussion_group` | `Groups.SetDiscussionGroup` | `rid، channel` | `await app.set_discussion_group(rid=...)` |
| `app.set_group_default_permissions` | `Groups.SetGroupDefaultPermissions` | `group، permissions` | `await app.set_group_default_permissions(group=...)` |
| `app.set_member_custom_title` | `Groups.SetMemberCustomTitle` | `groupId، memberId، title` | `await app.set_member_custom_title(group_id=...)` |
| `app.set_member_permissions` | `Groups.SetMemberPermissions` | `group، user، permissions` | `await app.set_member_permissions(group=...)` |
| `app.set_online` | `Presence.SetOnline` | `isOnline، timeout، deviceType (+1)` | `await app.set_online(is_online=...)` |
| `app.set_restriction` | `Groups.SetRestriction` | `groupOutPeer، restriction، nick` | `await app.set_restriction(group_out_peer=...)` |
| `app.set_sign_messages` | `Groups.SetSignMessages` | `groupPeer، signMessages` | `await app.set_sign_messages(group_peer=...)` |
| `app.set_slow_mode` | `Groups.SetSlowMode` | `group، seconds` | `await app.set_slow_mode(group=...)` |
| `app.set_user_privacy_status` | `Users.SetUserPrivacyStatus` | `userId، type، status` | `await app.set_user_privacy_status(user_id=...)` |
| `app.stop_typing` | `Presence.StopTyping` | `peer، typingType` | `await app.stop_typing(peer=...)` |
| `app.subscribe_from_group_online` | `Presence.SubscribeFromGroupOnline` | `groups` | `await app.subscribe_from_group_online(groups=...)` |
| `app.subscribe_from_online` | `Presence.SubscribeFromOnline` | `users` | `await app.subscribe_from_online(users=...)` |
| `app.subscribe_to_group_online` | `Presence.SubscribeToGroupOnline` | `groups` | `await app.subscribe_to_group_online(groups=...)` |
| `app.subscribe_to_online` | `Presence.SubscribeToOnline` | `users` | `await app.subscribe_to_online(users=...)` |
| `app.transfer_ownership` | `Groups.TransferOwnership` | `groupPeer، newOwner` | `await app.transfer_ownership(group_peer=...)` |
| `app.typing` | `Presence.Typing` | `peer، typingType` | `await app.typing(peer=...)` |
| `app.un_ban_user` | `Groups.UnBanUser` | `groupPeer، user، optimizations` | `await app.un_ban_user(group_peer=...)` |
| `app.unblock_user` | `Users.UnblockUser` | `peer` | `await app.unblock_user(peer=...)` |

## 📞 تماس‌های صوتی و تصویری Realtime

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.accept_call` | `Meet.AcceptCall` | `callId، inviteEnable` | `await app.accept_call(call_id=...)` |
| `app.answer_call_join_request` | `Meet.AnswerCallJoinRequest` | `callId، requesterIdentifier، isAllowed` | `await app.answer_call_join_request(call_id=...)` |
| `app.ask_to_join_call` | `Meet.AskToJoinCall` | `callId، name` | `await app.ask_to_join_call(call_id=...)` |
| `app.delete_call_logs` | `Meet.DeleteCallLogs` | `callIds، all، invert` | `await app.delete_call_logs(call_ids=...)` |
| `app.delete_stream` | `Meet.DeleteStream` | `streamUser` | `await app.delete_stream(stream_user=...)` |
| `app.discard_call` | `Meet.DiscardCall` | `callId، duration، reason (+1)` | `await app.discard_call(call_id=...)` |
| `app.generate_call_link` | `Meet.GenerateCallLink` | `isPublic، callId، title` | `await app.generate_call_link(is_public=...)` |
| `app.get_call_link_details` | `Meet.GetCallLinkDetails` | `session` | `await app.get_call_link_details(session=...)` |
| `app.get_call_logs` | `Meet.GetCallLogs` | `pageNumber، pageSize، afterDate (+1)` | `await app.get_call_logs(page_number=...)` |
| `app.get_call_state` | `Meet.GetCallState` | `callId` | `await app.get_call_state(call_id=...)` |
| `app.get_group_call` | `Meet.GetGroupCall` | `peer` | `await app.get_group_call(peer=...)` |
| `app.get_ongoing_calls` | `Meet.GetOngoingCalls` | `pageNumber، pageSize` | `await app.get_ongoing_calls(page_number=...)` |
| `app.get_wss_url` | `Meet.GetWssURL` | `callId` | `await app.get_wss_url(call_id=...)` |
| `app.invite_to_call` | `Meet.InviteToCall` | `callId، invitees` | `await app.invite_to_call(call_id=...)` |
| `app.join_group_call` | `Meet.JoinGroupCall` | `callId، name` | `await app.join_group_call(call_id=...)` |
| `app.leave_group_call` | `Meet.LeaveGroupCall` | `callId، end` | `await app.leave_group_call(call_id=...)` |
| `app.mute_participant` | `Meet.MuteParticipant` | `callId، identity، trackId (+1)` | `await app.mute_participant(call_id=...)` |
| `app.receive_call` | `Meet.ReceiveCall` | `callId` | `await app.receive_call(call_id=...)` |
| `app.remove_participant` | `Meet.RemoveParticipant` | `callId، identity، blockFromCall` | `await app.remove_participant(call_id=...)` |
| `app.send_call_reaction` | `Meet.SendCallReaction` | `callId، reaction` | `await app.send_call_reaction(call_id=...)` |
| `app.send_fanoos_event` | `Meet.SendFanoosEvent` | `eventName، items، date` | `await app.send_fanoos_event(event_name=...)` |
| `app.set_link_title` | `Meet.SetLinkTitle` | `title، callId، linkUrl` | `await app.set_link_title(title=...)` |
| `app.start_call` | `Meet.StartCall` | `peer، rid، video (+3)` | `await app.start_call(peer=...)` |
| `app.start_group_call` | `Meet.StartGroupCall` | `peer، randomId، video (+2)` | `await app.start_group_call(peer=...)` |
| `app.start_recording` | `Meet.StartRecording` | `callId، layout، quality` | `await app.start_recording(call_id=...)` |
| `app.start_stream` | `Meet.StartStream` | `streamUser، url، rtmpServer` | `await app.start_stream(stream_user=...)` |
| `app.stop_recording` | `Meet.StopRecording` | `callId` | `await app.stop_recording(call_id=...)` |
| `app.submit_call_feedback` | `Meet.SubmitCallFeedback` | `callId، rate، userOpinion (+4)` | `await app.submit_call_feedback(call_id=...)` |
| `app.take_call_action` | `Meet.TakeCallAction` | `callId، lowerHand، raiseHand` | `await app.take_call_action(call_id=...)` |
| `app.update_layout` | `Meet.UpdateLayout` | `callId، requestedLayout` | `await app.update_layout(call_id=...)` |

## 🤖 ربات‌ها، مینی‌اپ‌ها و هوش مصنوعی

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.edit_custom_services` | `Garson.EditCustomServices` | `items` | `await app.edit_custom_services(items=...)` |
| `app.file_upload_cancel` | `Files.FileUploadCancel` | `file` | `await app.file_upload_cancel(file=...)` |
| `app.get_advertisement_bot` | `Garson.GetAdvertisementBot` | `بدون پارامتر` | `await app.get_advertisement_bot()` |
| `app.get_bot_banners` | `Garson.GetBotBanners` | `بدون پارامتر` | `await app.get_bot_banners()` |
| `app.get_bot_group_permissions` | `Ketf.GetBotGroupPermissions` | `botUserId، groupId` | `await app.get_bot_group_permissions(bot_user_id=...)` |
| `app.get_bot_info` | `Ketf.GetBotInfo` | `botUserId` | `await app.get_bot_info(bot_user_id=...)` |
| `app.get_bot_white_list` | `Ketf.GetBotWhiteList` | `botUserId` | `await app.get_bot_white_list(bot_user_id=...)` |
| `app.get_bots` | `Ketf.GetBots` | `pagination` | `await app.get_bots(pagination=...)` |
| `app.get_bots_by_category` | `Garson.GetBotsByCategory` | `categoryId، pagination` | `await app.get_bots_by_category(category_id=...)` |
| `app.get_categorized_bots` | `Garson.GetCategorizedBots` | `بدون پارامتر` | `await app.get_categorized_bots()` |
| `app.get_custom_services` | `Garson.GetCustomServices` | `بدون پارامتر` | `await app.get_custom_services()` |
| `app.get_inline_bot_results` | `Ketf.GetInlineBotResults` | `query، peer، botUserId (+1)` | `await app.get_inline_bot_results(query=...)` |
| `app.get_link_preview` | `TLDR.GetLinkPreview` | `url` | `await app.get_link_preview(url=...)` |
| `app.get_link_summary` | `TLDR.GetLinkSummary` | `url` | `await app.get_link_summary(url=...)` |
| `app.get_menu_button` | `Appzar.GetMenuButton` | `botUserId` | `await app.get_menu_button(bot_user_id=...)` |
| `app.get_mini_app_url` | `Appzar.GetMiniAppUrl` | `botUserId، screenMode، themeParams (+4)` | `await app.get_mini_app_url(bot_user_id=...)` |
| `app.get_nasim_file_public_url` | `Files.GetNasimFilePublicUrl` | `peer، file، filename` | `await app.get_nasim_file_public_url(peer=...)` |
| `app.get_nasim_file_upload_resume` | `Files.GetNasimFileUploadResume` | `file` | `await app.get_nasim_file_upload_resume(file=...)` |
| `app.get_nasim_file_upload_url` | `Files.GetNasimFileUploadUrl` | `expectedSize، crc، uid (+7)` | `await app.get_nasim_file_upload_url(expected_size=...)` |
| `app.get_nasim_file_url` | `Files.GetNasimFileUrl` | `file، ciphertext` | `await app.get_nasim_file_url(file=...)` |
| `app.get_nasim_file_urls` | `Files.GetNasimFileUrls` | `files، ciphertext` | `await app.get_nasim_file_urls(files=...)` |
| `app.get_payment_details` | `Ketf.GetPaymentDetails` | `purchaseMessageId، invoiceIdentifier` | `await app.get_payment_details(purchase_message_id=...)` |
| `app.get_recommended_bots` | `Garson.GetRecommendedBots` | `botId، pagination` | `await app.get_recommended_bots(bot_id=...)` |
| `app.get_services` | `Garson.GetServices` | `version` | `await app.get_services(version=...)` |
| `app.get_transcript` | `AI.GetTranscript` | `voice، outPeer، messageId` | `await app.get_transcript(voice=...)` |
| `app.get_trend_bots` | `Garson.GetTrendBots` | `بدون پارامتر` | `await app.get_trend_bots()` |
| `app.get_upload_limits` | `Files.GetUploadLimits` | `بدون پارامتر` | `await app.get_upload_limits()` |
| `app.get_user_context` | `Ketf.GetUserContext` | `botUserId` | `await app.get_user_context(bot_user_id=...)` |
| `app.get_user_repeated_bots` | `Garson.GetUserRepeatedBots` | `بدون پارامتر` | `await app.get_user_repeated_bots()` |
| `app.get_webapp_hash` | `Ketf.GetWebappHash` | `botUserId، data` | `await app.get_webapp_hash(bot_user_id=...)` |
| `app.invoke_custom_action` | `Ketf.InvokeCustomAction` | `id، messageId، peer (+2)` | `await app.invoke_custom_action(id=...)` |
| `app.invoke_custom_method` | `Appzar.InvokeCustomMethod` | `botUserId، method، params` | `await app.invoke_custom_method(bot_user_id=...)` |
| `app.make_payment` | `Ketf.MakePayment` | `paymentSessionId، paymentOptionId، wallet (+1)` | `await app.make_payment(payment_session_id=...)` |
| `app.register_google_push` | `Push.RegisterGooglePush` | `projectId، token` | `await app.register_google_push(project_id=...)` |
| `app.register_push` | `Push.RegisterPush` | `register، pushVersion` | `await app.register_push(register=...)` |
| `app.search_services` | `Garson.SearchServices` | `query، language، source` | `await app.search_services(query=...)` |
| `app.send_authenticated_inline_call_back_data` | `Ketf.SendAuthenticatedInlineCallBackData` | `templateMessageId، data` | `await app.send_authenticated_inline_call_back_data(template_message_id=...)` |
| `app.send_event` | `AI.SendEvent` | `transcriptReactionEvent` | `await app.send_event(transcript_reaction_event=...)` |
| `app.send_inline_call_back_data` | `Ketf.SendInlineCallBackData` | `historyMessageIdentifier، data` | `await app.send_inline_call_back_data(history_message_identifier=...)` |
| `app.send_inline_callback` | `Ketf.SendInlineCallback` | `peer، messageId، data` | `await app.send_inline_callback(peer=...)` |
| `app.send_mini_app_data` | `Ketf.SendMiniAppData` | `botUserId، queryId، data (+1)` | `await app.send_mini_app_data(bot_user_id=...)` |
| `app.set_config` | `Push.SetConfig` | `config` | `await app.set_config(config=...)` |
| `app.unregister_all_push_credentials` | `Push.UnregisterAllPushCredentials` | `بدون پارامتر` | `await app.unregister_all_push_credentials()` |
| `app.unregister_google_push` | `Push.UnregisterGooglePush` | `token` | `await app.unregister_google_push(token=...)` |
| `app.unregister_push` | `Push.UnregisterPush` | `unregister` | `await app.unregister_push(unregister=...)` |

## 📸 استوری‌ها، نظرسنجی و مارکت

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.accept_campaign_market` | `Market.AcceptCampaignMarket` | `marketId، isPermanent` | `await app.accept_campaign_market(market_id=...)` |
| `app.accept_market_join_request` | `Market.AcceptMarketJoinRequest` | `marketPeerId، requestId، displayName (+1)` | `await app.accept_market_join_request(market_peer_id=...)` |
| `app.add_bot_story` | `Story.AddBotStory` | `exPeer، mediaStory، textStory (+2)` | `await app.add_bot_story(ex_peer=...)` |
| `app.add_channel_story` | `Story.AddChannelStory` | `exPeer، mediaStory، hasReply (+3)` | `await app.add_channel_story(ex_peer=...)` |
| `app.add_story` | `Story.AddStory` | `mediaStory، textStory، tagIds (+2)` | `await app.add_story(media_story=...)` |
| `app.ask_bot_review_callback` | `Timche.AskBotReviewCallback` | `botId، payload` | `await app.ask_bot_review_callback(bot_id=...)` |
| `app.can_add_bot_story` | `Story.CanAddBotStory` | `botUserId` | `await app.can_add_bot_story(bot_user_id=...)` |
| `app.check_link_validity` | `Story.CheckLinkValidity` | `exPeer، link` | `await app.check_link_validity(ex_peer=...)` |
| `app.close_poll` | `Poll.ClosePoll` | `pollId` | `await app.close_poll(poll_id=...)` |
| `app.create_market_join_request` | `Market.CreateMarketJoinRequest` | `marketPeerId، displayName، categoryId (+1)` | `await app.create_market_join_request(market_peer_id=...)` |
| `app.create_poll` | `Poll.CreatePoll` | `pollMessage، createAt، expeer` | `await app.create_poll(poll_message=...)` |
| `app.create_tag` | `Market.CreateTag` | `title، categoryId` | `await app.create_tag(title=...)` |
| `app.get_all_stories` | `Story.GetAllStories` | `بدون پارامتر` | `await app.get_all_stories()` |
| `app.get_bot_page` | `Timche.GetBotPage` | `botId` | `await app.get_bot_page(bot_id=...)` |
| `app.get_bot_stories` | `Story.GetBotStories` | `بدون پارامتر` | `await app.get_bot_stories()` |
| `app.get_categories_list` | `Market.GetCategoriesList` | `categoryId، level، includeSampleMarkets (+1)` | `await app.get_categories_list(category_id=...)` |
| `app.get_category_markets` | `Market.GetCategoryMarkets` | `categoryId، pagination، version` | `await app.get_category_markets(category_id=...)` |
| `app.get_category_products` | `Market.GetCategoryProducts` | `categoryId، pagination، version` | `await app.get_category_products(category_id=...)` |
| `app.get_channel_recommendations` | `Recommender.GetChannelRecommendations` | `بدون پارامتر` | `await app.get_channel_recommendations()` |
| `app.get_channel_stories` | `Story.GetChannelStories` | `بدون پارامتر` | `await app.get_channel_stories()` |
| `app.get_default_story_backgrounds` | `Story.GetDefaultStoryBackgrounds` | `بدون پارامتر` | `await app.get_default_story_backgrounds()` |
| `app.get_full_poll_result` | `Poll.GetFullPollResult` | `pollId` | `await app.get_full_poll_result(poll_id=...)` |
| `app.get_groups_recommendation` | `Recommender.GetGroupsRecommendation` | `source` | `await app.get_groups_recommendation(source=...)` |
| `app.get_home_page` | `Timche.GetHomePage` | `بدون پارامتر` | `await app.get_home_page()` |
| `app.get_indexed_products` | `Market.GetIndexedProducts` | `startDate، endDate، categoryId` | `await app.get_indexed_products(start_date=...)` |
| `app.get_market` | `Market.GetMarket` | `peerId، nickName` | `await app.get_market(peer_id=...)` |
| `app.get_market_join_requests` | `Market.GetMarketJoinRequests` | `بدون پارامتر` | `await app.get_market_join_requests()` |
| `app.get_markets_pending_join_request` | `Market.GetMarketsPendingJoinRequest` | `بدون پارامتر` | `await app.get_markets_pending_join_request()` |
| `app.get_message_upvoters` | `Magazine.GetMessageUpvoters` | `loadMoreState، message` | `await app.get_message_upvoters(load_more_state=...)` |
| `app.get_most_popular_stories` | `Story.GetMostPopularStories` | `getSpecialStories، optimization` | `await app.get_most_popular_stories(get_special_stories=...)` |
| `app.get_my_upvotes` | `Magazine.GetMyUpvotes` | `بدون پارامتر` | `await app.get_my_upvotes()` |
| `app.get_number_of_sales` | `Market.GetNumberOfSales` | `peer` | `await app.get_number_of_sales(peer=...)` |
| `app.get_onboarding_status` | `Market.GetOnboardingStatus` | `بدون پارامتر` | `await app.get_onboarding_status()` |
| `app.get_pending_campaign_markets` | `Market.GetPendingCampaignMarkets` | `بدون پارامتر` | `await app.get_pending_campaign_markets()` |
| `app.get_poll_results` | `Poll.GetPollResults` | `pollIds` | `await app.get_poll_results(poll_ids=...)` |
| `app.get_related_channels` | `Recommender.GetRelatedChannels` | `exPeer` | `await app.get_related_channels(ex_peer=...)` |
| `app.get_related_groups` | `Recommender.GetRelatedGroups` | `exPeer` | `await app.get_related_groups(ex_peer=...)` |
| `app.get_section_page` | `Timche.GetSectionPage` | `sectionId` | `await app.get_section_page(section_id=...)` |
| `app.get_similar_posts` | `Magazine.GetSimilarPosts` | `message، loadMoreState` | `await app.get_similar_posts(message=...)` |
| `app.get_stores` | `Market.GetStores` | `version` | `await app.get_stores(version=...)` |
| `app.get_stories` | `Story.GetStories` | `getUnmutual` | `await app.get_stories(get_unmutual=...)` |
| `app.get_stories_by_list` | `Story.GetStoriesByList` | `exPeers` | `await app.get_stories_by_list(ex_peers=...)` |
| `app.get_story_by_id` | `Story.GetStoryById` | `storyId` | `await app.get_story_by_id(story_id=...)` |
| `app.get_story_reaction_emojis` | `Story.GetStoryReactionEmojis` | `بدون پارامتر` | `await app.get_story_reaction_emojis()` |
| `app.get_story_tags` | `Story.GetStoryTags` | `بدون پارامتر` | `await app.get_story_tags()` |
| `app.get_story_widgets` | `Story.GetStoryWidgets` | `storyId` | `await app.get_story_widgets(story_id=...)` |
| `app.get_tags` | `Market.GetTags` | `categoryId` | `await app.get_tags(category_id=...)` |
| `app.get_top_markets` | `Market.GetTopMarkets` | `ratingType، pagination` | `await app.get_top_markets(rating_type=...)` |
| `app.get_user_privacy_config` | `Story.GetUserPrivacyConfig` | `بدون پارامتر` | `await app.get_user_privacy_config()` |
| `app.get_user_story_config` | `Story.GetUserStoryConfig` | `key، exPeer` | `await app.get_user_story_config(key=...)` |
| `app.get_viewers` | `Story.GetViewers` | `storyId، pagination` | `await app.get_viewers(story_id=...)` |
| `app.get_viewers_count` | `Story.GetViewersCount` | `storyId` | `await app.get_viewers_count(story_id=...)` |
| `app.get_yalda_stores` | `Market.GetYaldaStores` | `version` | `await app.get_yalda_stores(version=...)` |
| `app.load_categories` | `Magazine.LoadCategories` | `بدون پارامتر` | `await app.load_categories()` |
| `app.load_category_feed_messages` | `Magazine.LoadCategoryFeedMessages` | `categoryId، loadMoreState` | `await app.load_category_feed_messages(category_id=...)` |
| `app.load_feed_messages` | `Magazine.LoadFeedMessages` | `loadMoreState` | `await app.load_feed_messages(load_more_state=...)` |
| `app.load_internal_feed_messages` | `Magazine.LoadInternalFeedMessages` | `loadMoreState` | `await app.load_internal_feed_messages(load_more_state=...)` |
| `app.react_to_story` | `Story.ReactToStory` | `storyId، reaction، type (+2)` | `await app.react_to_story(story_id=...)` |
| `app.reject_campaign_market` | `Market.RejectCampaignMarket` | `marketId، isPermanent` | `await app.reject_campaign_market(market_id=...)` |
| `app.reject_market_join_request` | `Market.RejectMarketJoinRequest` | `marketPeerId، rejectCause، requestId` | `await app.reject_market_join_request(market_peer_id=...)` |
| `app.remove_story` | `Story.RemoveStory` | `storyId` | `await app.remove_story(story_id=...)` |
| `app.revoke_upvoted_post` | `Magazine.RevokeUpvotedPost` | `message، albumId` | `await app.revoke_upvoted_post(message=...)` |
| `app.set_generic_deep_links` | `Market.SetGenericDeepLinks` | `links` | `await app.set_generic_deep_links(links=...)` |
| `app.set_market_banners` | `Market.SetMarketBanners` | `banners` | `await app.set_market_banners(banners=...)` |
| `app.set_onboarding_data` | `Market.SetOnboardingData` | `categoryIds، gender، isSkipped` | `await app.set_onboarding_data(category_ids=...)` |
| `app.set_popular_searches` | `Market.SetPopularSearches` | `items` | `await app.set_popular_searches(items=...)` |
| `app.set_user_privacy_config` | `Story.SetUserPrivacyConfig` | `config` | `await app.set_user_privacy_config(config=...)` |
| `app.set_user_story_config` | `Story.SetUserStoryConfig` | `setType، config، exPeer` | `await app.set_user_story_config(set_type=...)` |
| `app.submit_market_feedback` | `Market.SubmitMarketFeedback` | `rate، userOpinion، clientVersion (+1)` | `await app.submit_market_feedback(rate=...)` |
| `app.submit_review` | `Timche.SubmitReview` | `botId، rating، comment (+3)` | `await app.submit_review(bot_id=...)` |
| `app.update_market_info` | `Market.UpdateMarketInfo` | `peerId، displayName، primaryCategoryId (+2)` | `await app.update_market_info(peer_id=...)` |
| `app.upvote_post` | `Magazine.UpvotePost` | `message، albumId` | `await app.upvote_post(message=...)` |
| `app.vote` | `Poll.Vote` | `pollId، isRetract، voteAt (+1)` | `await app.vote(poll_id=...)` |

## ⚙️ احراز هویت، امنیت، سشن و تنظیمات

| نام متد روی `app` | سرویس رسمی بله | پارامترهای ورودی | نمونه کد فراخوانی پایتونیک |
| :--- | :--- | :--- | :--- |
| `app.calculate_discounted_price` | `Premium.CalculateDiscountedPrice` | `packageId، couponCode` | `await app.calculate_discounted_price(package_id=...)` |
| `app.change_language` | `Auth.ChangeLanguage` | `language` | `await app.change_language(language=...)` |
| `app.change_phone` | `Auth.ChangePhone` | `phoneNumber، code، transactionHash` | `await app.change_phone(phone_number=...)` |
| `app.check_password` | `Ramz.CheckPassword` | `password، servicesType` | `await app.check_password(password=...)` |
| `app.check_password_set` | `Ramz.CheckPasswordSet` | `بدون پارامتر` | `await app.check_password_set()` |
| `app.delete_account` | `Auth.DeleteAccount` | `code، transactionHash` | `await app.delete_account(code=...)` |
| `app.delete_password` | `Ramz.DeletePassword` | `otp` | `await app.delete_password(otp=...)` |
| `app.disable_two_factor_authentication` | `Auth.DisableTwoFactorAuthentication` | `بدون پارامتر` | `await app.disable_two_factor_authentication()` |
| `app.edit_parameter` | `Configs.EditParameter` | `key، value` | `await app.edit_parameter(key=...)` |
| `app.enable_two_factor_authentication` | `Auth.EnableTwoFactorAuthentication` | `email، password` | `await app.enable_two_factor_authentication(email=...)` |
| `app.forget_password` | `Ramz.ForgetPassword` | `بدون پارامتر` | `await app.forget_password()` |
| `app.get_auth_sessions` | `Auth.GetAuthSessions` | `بدون پارامتر` | `await app.get_auth_sessions()` |
| `app.get_auth_token` | `LLMAuthService.GetAuthToken` | `بدون پارامتر` | `await app.get_auth_token()` |
| `app.get_badges` | `Premium.GetBadges` | `بدون پارامتر` | `await app.get_badges()` |
| `app.get_baje_bam_ticket` | `Auth.GetBajeBamTicket` | `expDateTime، mobileNo` | `await app.get_baje_bam_ticket(exp_date_time=...)` |
| `app.get_bale_ticket` | `Auth.GetBaleTicket` | `expDateTime، mobileNo، clientId` | `await app.get_bale_ticket(exp_date_time=...)` |
| `app.get_in_app_update` | `Configs.GetInAppUpdate` | `بدون پارامتر` | `await app.get_in_app_update()` |
| `app.get_jwt_token` | `Auth.GetJWTToken` | `بدون پارامتر` | `await app.get_jwt_token()` |
| `app.get_marketing_tools_config` | `Pishvaz.GetMarketingToolsConfig` | `بدون پارامتر` | `await app.get_marketing_tools_config()` |
| `app.get_onboarding_page_data` | `Pishvaz.GetOnboardingPageData` | `بدون پارامتر` | `await app.get_onboarding_page_data()` |
| `app.get_packages` | `Premium.GetPackages` | `بدون پارامتر` | `await app.get_packages()` |
| `app.get_parameters` | `Configs.GetParameters` | `بدون پارامتر` | `await app.get_parameters()` |
| `app.get_ticket` | `Auth.GetTicket` | `jsonRequest، jsonSign` | `await app.get_ticket(json_request=...)` |
| `app.get_top_peer` | `TopPeer.GetTopPeer` | `بدون پارامتر` | `await app.get_top_peer()` |
| `app.get_user_id_token` | `Auth.GetUserIdToken` | `ticket` | `await app.get_user_id_token(ticket=...)` |
| `app.is_premium` | `Premium.IsPremium` | `userId، withDetailOption` | `await app.is_premium(user_id=...)` |
| `app.is_premium_batch` | `Premium.IsPremiumBatch` | `userIds، withDetailOption` | `await app.is_premium_batch(user_ids=...)` |
| `app.is_two_factor_authentication_enabled` | `Auth.IsTwoFactorAuthenticationEnabled` | `بدون پارامتر` | `await app.is_two_factor_authentication_enabled()` |
| `app.log_out` | `Auth.LogOut` | `بدون پارامتر` | `await app.log_out()` |
| `app.purchase_package` | `Premium.PurchasePackage` | `packageId، couponCode` | `await app.purchase_package(package_id=...)` |
| `app.recover_password` | `Auth.RecoverPassword` | `transactionHash` | `await app.recover_password(transaction_hash=...)` |
| `app.remove_peer` | `TopPeer.RemovePeer` | `peer` | `await app.remove_peer(peer=...)` |
| `app.report_dismiss` | `Report.ReportDismiss` | `exPeer` | `await app.report_dismiss(ex_peer=...)` |
| `app.report_inappropriate_content` | `Report.ReportInappropriateContent` | `report` | `await app.report_inappropriate_content(report=...)` |
| `app.send_change_phone_verification_code` | `Auth.SendChangePhoneVerificationCode` | `بدون پارامتر` | `await app.send_change_phone_verification_code()` |
| `app.send_delete_account_verification_code` | `Auth.SendDeleteAccountVerificationCode` | `بدون پارامتر` | `await app.send_delete_account_verification_code()` |
| `app.send_otp` | `Ramz.SendOTP` | `بدون پارامتر` | `await app.send_otp()` |
| `app.set_marketing_tool_action` | `Pishvaz.SetMarketingToolAction` | `id، actionType` | `await app.set_marketing_tool_action(id=...)` |
| `app.set_new_password` | `Auth.SetNewPassword` | `newPassword، transactionHash` | `await app.set_new_password(new_password=...)` |
| `app.set_password` | `Ramz.SetPassword` | `password` | `await app.set_password(password=...)` |
| `app.set_user_badge` | `Premium.SetUserBadge` | `badgeId` | `await app.set_user_badge(badge_id=...)` |
| `app.sign_out` | `Auth.SignOut` | `بدون پارامتر` | `await app.sign_out()` |
| `app.sign_up` | `Auth.SignUp` | `transactionHash، name، sex (+2)` | `await app.sign_up(transaction_hash=...)` |
| `app.start_phone_auth` | `Auth.StartPhoneAuth` | `phoneNumber، appId، apiKey (+7)` | `await app.start_phone_auth(phone_number=...)` |
| `app.terminate_all_sessions` | `Auth.TerminateAllSessions` | `بدون پارامتر` | `await app.terminate_all_sessions()` |
| `app.terminate_session` | `Auth.TerminateSession` | `id` | `await app.terminate_session(id=...)` |
| `app.validate_code` | `Auth.ValidateCode` | `transactionHash، code، isJwt (+2)` | `await app.validate_code(transaction_hash=...)` |
| `app.validate_otp` | `Ramz.ValidateOTP` | `otp، servicesType` | `await app.validate_otp(otp=...)` |
| `app.validate_password` | `Auth.ValidatePassword` | `transactionHash، password، isJwt (+1)` | `await app.validate_password(transaction_hash=...)` |
| `app.verify_email` | `Auth.VerifyEmail` | `email، code` | `await app.verify_email(email=...)` |
| `app.verify_password` | `Auth.VerifyPassword` | `password` | `await app.verify_password(password=...)` |
| `app.verify_password_recovery` | `Auth.VerifyPasswordRecovery` | `code، transactionHash` | `await app.verify_password_recovery(code=...)` |


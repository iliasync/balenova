# راهنمای جامع ۶۹۰ متد پروتکل بله با پارامترها و نمونه کد

در **BaleNova** تمامی ۶۹۰ متد رسمی وب بله به شکل کامل پیاده‌سازی و پشتیبانی می‌شوند.

### نحوه فراخوانی استاندارد در کد پایتون
برای هر متد، سه روش فراخوانی وجود دارد:
```python
# روش ۱: متد پایتونیک سطح‌بالا
await app.send_message("123|1", "سلام")

# روش ۲: با ساختار app.rpc (نام سرویس و متد)
res = await app.rpc("bank", "GetCardRemain", pan="6037...", cvv2="123", expireDate="28/05", pin2="...")

# روش ۳: از طریق namespace تایپ‌شده api
res = await app.api.bank.GetCardRemain(pan="6037...", cvv2="123", expireDate="28/05", pin2="...")
```

---

## سرویس `ai.bale.pushak.Push` (6 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `RegisterGooglePush` | `projectId، token` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("push", "RegisterGooglePush")` |
| `RegisterPush` | `register، pushVersion` | `encryptionKey` | `await app.rpc("push", "RegisterPush")` |
| `SetConfig` | `config` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("push", "SetConfig")` |
| `UnregisterAllPushCredentials` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("push", "UnregisterAllPushCredentials")` |
| `UnregisterGooglePush` | `token` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("push", "UnregisterGooglePush")` |
| `UnregisterPush` | `unregister` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("push", "UnregisterPush")` |

## سرویس `ai.bale.server.Files` (7 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `FileUploadCancel` | `file` | `canceled` | `await app.rpc("files", "FileUploadCancel")` |
| `GetNasimFilePublicUrl` | `peer، file، filename` | `fileUrl` | `await app.rpc("files", "GetNasimFilePublicUrl")` |
| `GetNasimFileUploadResume` | `file` | `fileUrl، canResume` | `await app.rpc("files", "GetNasimFileUploadResume")` |
| `GetNasimFileUploadUrl` | `expectedSize، crc، uid، name (+6)` | `fileId، url، duplicate (+2)` | `await app.rpc("files", "GetNasimFileUploadUrl")` |
| `GetNasimFileUrl` | `file، ciphertext` | `fileUrl` | `await app.rpc("files", "GetNasimFileUrl")` |
| `GetNasimFileUrls` | `files، ciphertext` | `fileUrls` | `await app.rpc("files", "GetNasimFileUrls")` |
| `GetUploadLimits` | `بدون پارامتر` | `uploadLimitBytes، temporaryMaxBytes، permanentMaxBytes (+2)` | `await app.rpc("files", "GetUploadLimits")` |

## سرویس `bale.BankAccountPreferences.v1.BankAccountPreferences` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ActivateYaraMessaging` | `accountNumber` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("bankaccountpreferences", "ActivateYaraMessaging")` |
| `EditPreference` | `preference` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("bankaccountpreferences", "EditPreference")` |
| `GetPreferences` | `بدون پارامتر` | `accounts` | `await app.rpc("bankaccountpreferences", "GetPreferences")` |

## سرویس `bale.abacus.v1.Abacus` (9 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `EnableShowReactionFlag` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("abacus", "EnableShowReactionFlag")` |
| `GetMessageReactionsList` | `peer، rid، date، code (+2)` | `userReactions` | `await app.rpc("abacus", "GetMessageReactionsList")` |
| `GetMessagesReactions` | `peer، mids، originPeer، originMids` | `containers` | `await app.rpc("abacus", "GetMessagesReactions")` |
| `GetMessagesViews` | `peer، mids، increment، correctMids` | `containers` | `await app.rpc("abacus", "GetMessagesViews")` |
| `GetShowReactionFlag` | `بدون پارامتر` | `userId، isEnable` | `await app.rpc("abacus", "GetShowReactionFlag")` |
| `LoadReactions` | `peer، mids، ignoreCountViews` | `containers` | `await app.rpc("abacus", "LoadReactions")` |
| `MessageReactionsRead` | `peer، messageId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("abacus", "MessageReactionsRead")` |
| `MessageRemoveReaction` | `peer، rid، code، date` | `seq، reactions، state` | `await app.rpc("abacus", "MessageRemoveReaction")` |
| `MessageSetReaction` | `peer، rid، code، date` | `seq، reactions، state` | `await app.rpc("abacus", "MessageSetReaction")` |

## سرویس `bale.advertisement.v1.Advertisement` (123 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddCustomIncome` | `type، amount، description، customerUserId (+5)` | `id` | `await app.rpc("advertisement", "AddCustomIncome")` |
| `BuildAudienceQuery` | `definition` | `query، estimatedSize` | `await app.rpc("advertisement", "BuildAudienceQuery")` |
| `CalculatePrice` | `spot، viewCount، clickCount، link (+4)` | `finalPrice، clickUnitPrice` | `await app.rpc("advertisement", "CalculatePrice")` |
| `ChangeAccountState` | `state، ownerId، reason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeAccountState")` |
| `ChangeAdState` | `adId، state، reason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeAdState")` |
| `ChangeBonusCodeState` | `code، state` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeBonusCodeState")` |
| `ChangeCampaignContentState` | `campaignId، state، reason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeCampaignContentState")` |
| `ChangeCampaignState` | `campaignId، state، rejectionReason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeCampaignState")` |
| `ChangeChannelIncomeOwner` | `peerId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeChannelIncomeOwner")` |
| `ChangeChannelShowAdPermissions` | `peerId، showAds، timeRestrict، categoryFilter` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeChannelShowAdPermissions")` |
| `ChangeStatusDialogAdOrder` | `id، targetStatus، date، rejectionReason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeStatusDialogAdOrder")` |
| `ChangeUserDataState` | `ownerId، state، reason` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChangeUserDataState")` |
| `ChannelIncomeGetCredit` | `peerId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChannelIncomeGetCredit")` |
| `ChannelIncomeKifTransfer` | `peerId، payType` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ChannelIncomeKifTransfer")` |
| `ChannelIncomePayment` | `peerId، payType` | `factorHtml` | `await app.rpc("advertisement", "ChannelIncomePayment")` |
| `ConvertIncome` | `convertToPoints، convertToGiftPacket، convertToGiftPacketForChannelOwner` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ConvertIncome")` |
| `CreateAd` | `adData، price، depositTrackingId، paymentMethod (+1)` | `adId` | `await app.rpc("advertisement", "CreateAd")` |
| `CreateAndStartChannelAd` | `title، description، link، platform (+3)` | `id` | `await app.rpc("advertisement", "CreateAndStartChannelAd")` |
| `CreateAutomatedAudience` | `definition، single، randomGroups` | `result` | `await app.rpc("advertisement", "CreateAutomatedAudience")` |
| `CreateBaleDialogCustomAd` | `pic، title، description، link (+1)` | `id` | `await app.rpc("advertisement", "CreateBaleDialogCustomAd")` |
| `CreateBonusCode` | `data، autoGenerate` | `code` | `await app.rpc("advertisement", "CreateBonusCode")` |
| `CreateChannelIncomeFactor` | `peerId، year، month` | `factorHtml` | `await app.rpc("advertisement", "CreateChannelIncomeFactor")` |
| `CreateCustomCampaignPackage` | `userId، baseCredit، creditExpireDays، campaignDailyCapacity (+4)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "CreateCustomCampaignPackage")` |
| `DeleteCustomIncome` | `id` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "DeleteCustomIncome")` |
| `EditAccount` | `account، isRestoreExpiredCredit، depositTrackingId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "EditAccount")` |
| `EditAd` | `ad` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "EditAd")` |
| `EditCampaignAd` | `ad` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "EditCampaignAd")` |
| `EditCampaignContent` | `campaign` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "EditCampaignContent")` |
| `EstimateChannelSponsoredIncome` | `peerId` | `estimatedViews، estimatedIncome` | `await app.rpc("advertisement", "EstimateChannelSponsoredIncome")` |
| `FinishAd` | `id` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "FinishAd")` |
| `FinishAdV2` | `adId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "FinishAdV2")` |
| `FinishChannelAd` | `id` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "FinishChannelAd")` |
| `GetAccountData` | `ownerId` | `data` | `await app.rpc("advertisement", "GetAccountData")` |
| `GetAccounts` | `pageData` | `data` | `await app.rpc("advertisement", "GetAccounts")` |
| `GetAccountsByState` | `state، pageData` | `data` | `await app.rpc("advertisement", "GetAccountsByState")` |
| `GetActiveAds` | `بدون پارامتر` | `ads` | `await app.rpc("advertisement", "GetActiveAds")` |
| `GetActiveChannelAds` | `بدون پارامتر` | `ads` | `await app.rpc("advertisement", "GetActiveChannelAds")` |
| `GetAdData` | `adId` | `adData` | `await app.rpc("advertisement", "GetAdData")` |
| `GetAdDetail` | `title، from، to` | `ads` | `await app.rpc("advertisement", "GetAdDetail")` |
| `GetAdProvider` | `peerId، adType، adSpot، adCount (+1)` | `content` | `await app.rpc("advertisement", "GetAdProvider")` |
| `GetAdReport` | `adId` | `views، clicks، title (+1)` | `await app.rpc("advertisement", "GetAdReport")` |
| `GetAdReportV2` | `adId` | `data` | `await app.rpc("advertisement", "GetAdReportV2")` |
| `GetAdsBySpotAndPlatform` | `spot، peerId` | `data` | `await app.rpc("advertisement", "GetAdsBySpotAndPlatform")` |
| `GetAdsByStateAndSpot` | `pagingData، state، spot` | `ads` | `await app.rpc("advertisement", "GetAdsByStateAndSpot")` |
| `GetAllChannelIncomesFactor` | `year، month` | `factors` | `await app.rpc("advertisement", "GetAllChannelIncomesFactor")` |
| `GetAllPaymentHistory` | `startDate، endDate` | `records` | `await app.rpc("advertisement", "GetAllPaymentHistory")` |
| `GetAvailableCampaignStartDate` | `بدون پارامتر` | `date` | `await app.rpc("advertisement", "GetAvailableCampaignStartDate")` |
| `GetAwaitingToShowAds` | `بدون پارامتر` | `ads` | `await app.rpc("advertisement", "GetAwaitingToShowAds")` |
| `GetAwaitingToShowChannelAds` | `بدون پارامتر` | `ads` | `await app.rpc("advertisement", "GetAwaitingToShowChannelAds")` |
| `GetBaleCustomAd` | `adId` | `ad` | `await app.rpc("advertisement", "GetBaleCustomAd")` |
| `GetBonusCodeData` | `code` | `data` | `await app.rpc("advertisement", "GetBonusCodeData")` |
| `GetBonusCodes` | `pageData` | `data` | `await app.rpc("advertisement", "GetBonusCodes")` |
| `GetBusinessAds` | `pagingData، state` | `ads` | `await app.rpc("advertisement", "GetBusinessAds")` |
| `GetCRMIssues` | `userIssue، allIssue` | `data` | `await app.rpc("advertisement", "GetCRMIssues")` |
| `GetCampaignAds` | `pagingData، state` | `data` | `await app.rpc("advertisement", "GetCampaignAds")` |
| `GetCampaignContentById` | `campaignId` | `campaign` | `await app.rpc("advertisement", "GetCampaignContentById")` |
| `GetCampaignContents` | `pagingData، state` | `campaigns` | `await app.rpc("advertisement", "GetCampaignContents")` |
| `GetCampaignData` | `campaignId` | `data` | `await app.rpc("advertisement", "GetCampaignData")` |
| `GetChannelAds` | `groupId` | `ads` | `await app.rpc("advertisement", "GetChannelAds")` |
| `GetChannelEarnMoneyInfo` | `groupId` | `currentMonthIncome، notPaidIncome، adCount (+1)` | `await app.rpc("advertisement", "GetChannelEarnMoneyInfo")` |
| `GetChannelEarnMoneyStatus` | `groupId` | `status` | `await app.rpc("advertisement", "GetChannelEarnMoneyStatus")` |
| `GetChannelGraphReport` | `peerId، startTime، endTime` | `viewGraph` | `await app.rpc("advertisement", "GetChannelGraphReport")` |
| `GetChannelIncomeReport` | `peerId` | `incomeReports` | `await app.rpc("advertisement", "GetChannelIncomeReport")` |
| `GetChannelOwnerBankInformation` | `channelId` | `userId، nationalCode، birthDate (+9)` | `await app.rpc("advertisement", "GetChannelOwnerBankInformation")` |
| `GetChannelShowAdCategoryFilter` | `peerId` | `categories` | `await app.rpc("advertisement", "GetChannelShowAdCategoryFilter")` |
| `GetChannelShowAdPermissions` | `peerId` | `showSponsoredAd، verifiedUserId` | `await app.rpc("advertisement", "GetChannelShowAdPermissions")` |
| `GetChannelShowAdTimeRestrict` | `peerId` | `data` | `await app.rpc("advertisement", "GetChannelShowAdTimeRestrict")` |
| `GetChannelSponsoredIncomeReport` | `peerId، startTime، endTime` | `totalViews، totalIncome، totalAdCount (+3)` | `await app.rpc("advertisement", "GetChannelSponsoredIncomeReport")` |
| `GetChannelUndepositedIncomes` | `year، month` | `items` | `await app.rpc("advertisement", "GetChannelUndepositedIncomes")` |
| `GetChannelsViewReport` | `startTime، endTime` | `channelsView` | `await app.rpc("advertisement", "GetChannelsViewReport")` |
| `GetConfig` | `بدون پارامتر` | `config` | `await app.rpc("advertisement", "GetConfig")` |
| `GetCreditHistory` | `ownerId، startTime، endTime` | `creditHistories` | `await app.rpc("advertisement", "GetCreditHistory")` |
| `GetCreditableAccounts` | `pageData` | `data` | `await app.rpc("advertisement", "GetCreditableAccounts")` |
| `GetCustomIncomes` | `startTime، endTime` | `records` | `await app.rpc("advertisement", "GetCustomIncomes")` |
| `GetDialogAdOrderDetails` | `بدون پارامتر` | `dialogAdOrder` | `await app.rpc("advertisement", "GetDialogAdOrderDetails")` |
| `GetDialogAdOrderPaymentToken` | `id، rialAmount، coinAmount` | `token` | `await app.rpc("advertisement", "GetDialogAdOrderPaymentToken")` |
| `GetFactorEligibleAds` | `tBegin، tEnd` | `ads` | `await app.rpc("advertisement", "GetFactorEligibleAds")` |
| `GetInvoiceContent` | `invoiceRequestId` | `id، description، responseCode (+1)` | `await app.rpc("advertisement", "GetInvoiceContent")` |
| `GetLegalOrgChannels` | `بدون پارامتر` | `channels` | `await app.rpc("advertisement", "GetLegalOrgChannels")` |
| `GetMyContactPopularChannels` | `بدون پارامتر` | `channels` | `await app.rpc("advertisement", "GetMyContactPopularChannels")` |
| `GetOnBoardingChannels` | `بدون پارامتر` | `channels، showOnBoarding` | `await app.rpc("advertisement", "GetOnBoardingChannels")` |
| `GetOnboardingPeers` | `بدون پارامتر` | `peers` | `await app.rpc("advertisement", "GetOnboardingPeers")` |
| `GetOnboardingPosts` | `categoryId` | `posts` | `await app.rpc("advertisement", "GetOnboardingPosts")` |
| `GetOnboardingSpotData` | `onboardingSpot، suggestedPeerType` | `contactChannels، suggestedChannels` | `await app.rpc("advertisement", "GetOnboardingSpotData")` |
| `GetOwnerIdByPhone` | `phoneNumber` | `userId` | `await app.rpc("advertisement", "GetOwnerIdByPhone")` |
| `GetPaidAdsByTime` | `pagingData، startTime، endTime` | `ads` | `await app.rpc("advertisement", "GetPaidAdsByTime")` |
| `GetPaymentData` | `adId` | `data` | `await app.rpc("advertisement", "GetPaymentData")` |
| `GetPeriodCapacityData` | `beginDate، endDate` | `data` | `await app.rpc("advertisement", "GetPeriodCapacityData")` |
| `GetUserAds` | `pagingData، userId` | `ads` | `await app.rpc("advertisement", "GetUserAds")` |
| `GetUserAuthData` | `channelId` | `userId، nationalCode، birthDate (+9)` | `await app.rpc("advertisement", "GetUserAuthData")` |
| `GetUserCampaigns` | `pagingData، userId` | `data` | `await app.rpc("advertisement", "GetUserCampaigns")` |
| `GetUserOnboardingScenario` | `بدون پارامتر` | `scenario` | `await app.rpc("advertisement", "GetUserOnboardingScenario")` |
| `GetUserStatus` | `userId` | `status` | `await app.rpc("advertisement", "GetUserStatus")` |
| `GetUsersAuthDataByState` | `state` | `usersData` | `await app.rpc("advertisement", "GetUsersAuthDataByState")` |
| `GetVODContents` | `بدون پارامتر` | `contents` | `await app.rpc("advertisement", "GetVODContents")` |
| `MergeCustomIncomeRecords` | `customIncomeIds` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "MergeCustomIncomeRecords")` |
| `MergeIncreaseCreditRecords` | `increaseCreditIds` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "MergeIncreaseCreditRecords")` |
| `ModifyCapacity` | `date، val` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "ModifyCapacity")` |
| `RegisterForEarnMoney` | `info` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "RegisterForEarnMoney")` |
| `RetryFailedAutoSentInvoice` | `failedInvoiceRequestId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "RetryFailedAutoSentInvoice")` |
| `SendAdminMessage` | `receiver، messageText، fileId، fileName` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SendAdminMessage")` |
| `SendFactorMessage` | `channelId، messageText، fileId، fileName (+2)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SendFactorMessage")` |
| `SendInvoiceForPaymentHistoryRecord` | `recordId، depositTrackingId، paymentHistoryType` | `invoiceRequestId` | `await app.rpc("advertisement", "SendInvoiceForPaymentHistoryRecord")` |
| `SendLegalOrgChannelIncome` | `channelId` | `results` | `await app.rpc("advertisement", "SendLegalOrgChannelIncome")` |
| `SetAdTarget` | `adId، targeting` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetAdTarget")` |
| `SetCapacityMaxViews` | `data، spot` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetCapacityMaxViews")` |
| `SetChannelInvoiceInfo` | `peerId، nationalCode، address، postalCode (+4)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetChannelInvoiceInfo")` |
| `SetChannelOwnerBankInformation` | `channelId، nationalCode، birthDate، address (+2)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetChannelOwnerBankInformation")` |
| `SetOnBoardingChannels` | `channels` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetOnBoardingChannels")` |
| `SetUserAuthData` | `channelId، nationalCode، birthDate، address (+2)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SetUserAuthData")` |
| `StartAd` | `adId، startTime، platform، autoFinish` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "StartAd")` |
| `StartBaleCustomAd` | `id، platform، pic، title (+5)` | `ad` | `await app.rpc("advertisement", "StartBaleCustomAd")` |
| `StartChannelAdFromOrder` | `id، title، description، link (+4)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "StartChannelAdFromOrder")` |
| `StartFromOrder` | `id، platform، pic، title (+5)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "StartFromOrder")` |
| `StopAllBaleCustomAds` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "StopAllBaleCustomAds")` |
| `SubmitChannelAdOrder` | `order` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SubmitChannelAdOrder")` |
| `SubmitDialogAdOrder` | `dialogAdOrder` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "SubmitDialogAdOrder")` |
| `SubmitPhotoForBaleCustomAd` | `adId، pic` | `ad` | `await app.rpc("advertisement", "SubmitPhotoForBaleCustomAd")` |
| `UpdateBusinessAd` | `updatedAd` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "UpdateBusinessAd")` |
| `UpdateCRMIssue` | `addIssue، addComment، resolveIssue، ignoreUser` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "UpdateCRMIssue")` |
| `UpdateClick` | `id، count، peer` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "UpdateClick")` |
| `UpdateGroupStatus` | `groupId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("advertisement", "UpdateGroupStatus")` |
| `UpdateView` | `id، count، peerId` | `isSuccessful` | `await app.rpc("advertisement", "UpdateView")` |

## سرویس `bale.anonymous_contact.v1.AnonymousContact` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetUserAnonymousContactPage` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("anonymouscontact", "GetUserAnonymousContactPage")` |

## سرویس `bale.appzar.v1.Appzar` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetMenuButton` | `botUserId` | `menuButton` | `await app.rpc("appzar", "GetMenuButton")` |
| `GetMiniAppUrl` | `botUserId، screenMode، themeParams، main (+3)` | `url، screenMode، queryId` | `await app.rpc("appzar", "GetMiniAppUrl")` |
| `InvokeCustomMethod` | `botUserId، method، params` | `data` | `await app.rpc("appzar", "InvokeCustomMethod")` |

## سرویس `bale.arbaeen.v1.Arbaeen` (19 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CashPaymentCallback` | `paymentCode، nationalCode، userId، orderId` | `firstName، lastName` | `await app.rpc("arbaeen", "CashPaymentCallback")` |
| `GetAdminStationList` | `بدون پارامتر` | `stations` | `await app.rpc("arbaeen", "GetAdminStationList")` |
| `GetArbaeenCurrenciesList` | `بدون پارامتر` | `currencies، icmsWage` | `await app.rpc("arbaeen", "GetArbaeenCurrenciesList")` |
| `GetArbaeenCurrencyPrice` | `currencyType، currencyAmount، reason، countryCode (+5)` | `currencyRate، orderId، newCurrencyRate` | `await app.rpc("arbaeen", "GetArbaeenCurrencyPrice")` |
| `GetArbaeenPaymentToken` | `orderId` | `token، paymentGatewayPrefix، terminalId (+1)` | `await app.rpc("arbaeen", "GetArbaeenPaymentToken")` |
| `GetListOfArbaeenDeliveryStations` | `deliveryStationType، reason، ExitDate، bankType (+1)` | `stations` | `await app.rpc("arbaeen", "GetListOfArbaeenDeliveryStations")` |
| `GetListOfBoxOffice` | `stationId، exitDate` | `boxOffice` | `await app.rpc("arbaeen", "GetListOfBoxOffice")` |
| `GetListOfBranches` | `stateId، exitDate` | `branches` | `await app.rpc("arbaeen", "GetListOfBranches")` |
| `GetListOfStates` | `بدون پارامتر` | `states` | `await app.rpc("arbaeen", "GetListOfStates")` |
| `GetRate` | `بدون پارامتر` | `rate` | `await app.rpc("arbaeen", "GetRate")` |
| `GetSuggestedGroups` | `بدون پارامتر` | `suggestedGroups` | `await app.rpc("arbaeen", "GetSuggestedGroups")` |
| `GetValidArbaeenBanks` | `nationalCode، accountNationalCode` | `banks` | `await app.rpc("arbaeen", "GetValidArbaeenBanks")` |
| `LoadArbaeenHistory` | `بدون پارامتر` | `orders، approvalText` | `await app.rpc("arbaeen", "LoadArbaeenHistory")` |
| `SendOTP` | `phoneNumber` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("arbaeen", "SendOTP")` |
| `StartBot` | `peer` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("arbaeen", "StartBot")` |
| `UserHasAccess` | `بدون پارامتر` | `access` | `await app.rpc("arbaeen", "UserHasAccess")` |
| `VerifyOTP` | `phoneNumber، code` | `verified` | `await app.rpc("arbaeen", "VerifyOTP")` |
| `VerifyUserArbaeenAuthority` | `firstName، lastName، nationalCode، passportCode (+6)` | `approval` | `await app.rpc("arbaeen", "VerifyUserArbaeenAuthority")` |
| `VerifyUserArbaeenExtraInfo` | `nakhodaInfo` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("arbaeen", "VerifyUserArbaeenExtraInfo")` |

## سرویس `bale.auth.v1.Auth` (27 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ChangeLanguage` | `language` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "ChangeLanguage")` |
| `ChangePhone` | `phoneNumber، code، transactionHash` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "ChangePhone")` |
| `DeleteAccount` | `code، transactionHash` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "DeleteAccount")` |
| `DisableTwoFactorAuthentication` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "DisableTwoFactorAuthentication")` |
| `EnableTwoFactorAuthentication` | `email، password` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "EnableTwoFactorAuthentication")` |
| `GetAuthSessions` | `بدون پارامتر` | `userAuths` | `await app.rpc("auth", "GetAuthSessions")` |
| `GetBajeBamTicket` | `expDateTime، mobileNo` | `ticket` | `await app.rpc("auth", "GetBajeBamTicket")` |
| `GetBaleTicket` | `expDateTime، mobileNo، clientId` | `redirectUrl` | `await app.rpc("auth", "GetBaleTicket")` |
| `GetJWTToken` | `بدون پارامتر` | `jwt` | `await app.rpc("auth", "GetJWTToken")` |
| `GetTicket` | `jsonRequest، jsonSign` | `redirectUrl` | `await app.rpc("auth", "GetTicket")` |
| `GetUserIdToken` | `ticket` | `token، userId، source (+1)` | `await app.rpc("auth", "GetUserIdToken")` |
| `IsTwoFactorAuthenticationEnabled` | `بدون پارامتر` | `isEnabled` | `await app.rpc("auth", "IsTwoFactorAuthenticationEnabled")` |
| `LogOut` | `بدون پارامتر` | `futureAuthToken` | `await app.rpc("auth", "LogOut")` |
| `RecoverPassword` | `transactionHash` | `emailPattern` | `await app.rpc("auth", "RecoverPassword")` |
| `SendChangePhoneVerificationCode` | `بدون پارامتر` | `transactionHash، activationType` | `await app.rpc("auth", "SendChangePhoneVerificationCode")` |
| `SendDeleteAccountVerificationCode` | `بدون پارامتر` | `transactionHash، activationType` | `await app.rpc("auth", "SendDeleteAccountVerificationCode")` |
| `SetNewPassword` | `newPassword، transactionHash` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "SetNewPassword")` |
| `SignOut` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "SignOut")` |
| `SignUp` | `transactionHash، name، sex، password (+1)` | `user، config، jwt` | `await app.rpc("auth", "SignUp")` |
| `StartPhoneAuth` | `phoneNumber، appId، apiKey، deviceHash (+6)` | `transactionHash، isRegistered، activationType (+8)` | `await app.rpc("auth", "StartPhoneAuth")` |
| `TerminateAllSessions` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "TerminateAllSessions")` |
| `TerminateSession` | `id` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "TerminateSession")` |
| `ValidateCode` | `transactionHash، code، isJwt، futureAuthTokens (+1)` | `user، config، jwt` | `await app.rpc("auth", "ValidateCode")` |
| `ValidatePassword` | `transactionHash، password، isJwt، language` | `user، config، jwt` | `await app.rpc("auth", "ValidatePassword")` |
| `VerifyEmail` | `email، code` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "VerifyEmail")` |
| `VerifyPassword` | `password` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "VerifyPassword")` |
| `VerifyPasswordRecovery` | `code، transactionHash` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("auth", "VerifyPasswordRecovery")` |

## سرویس `bale.balebank.v1.GoldGiftPacket` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetWinnerIDs` | `giftPacketId` | `winners` | `await app.rpc("goldgiftpacket", "GetWinnerIDs")` |
| `OpenGoldGiftPacket` | `giftPacketId` | `openedCount، selfWinAmount، rank (+3)` | `await app.rpc("goldgiftpacket", "OpenGoldGiftPacket")` |
| `SendGoldGiftPacket` | `amount، count، description، givingType (+2)` | `giftPacketId` | `await app.rpc("goldgiftpacket", "SendGoldGiftPacket")` |

## سرویس `bale.balebank.v1.GoldWallet` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetBalance` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("goldwallet", "GetBalance")` |

## سرویس `bale.bank.v1.Bank` (17 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `BuyFastCharge` | `amount، phoneNumber، operator، chargeType` | `transactionDate، refrenceNumber، pin (+1)` | `await app.rpc("bank", "BuyFastCharge")` |
| `GetCardRemain` | `cardNumber، cvv2، expireDate، pin2` | `currentBalanceAmount، availableBalanceAmount` | `await app.rpc("bank", "GetCardRemain")` |
| `GetCardTransferToken` | `peerUserId، msgRid، description` | `requestEndPoint، token، destCardNo` | `await app.rpc("bank", "GetCardTransferToken")` |
| `GetOTPToken` | `cardNumberStartingSix` | `requestEndPoint، token` | `await app.rpc("bank", "GetOTPToken")` |
| `GetOTPTokenV2` | `messagePeer، msgRid، msgDate، peerUserId (+1)` | `requestEndPoint، token` | `await app.rpc("bank", "GetOTPTokenV2")` |
| `GetOrganizationPaymentToken` | `organizationId، invoiceId، amount` | `token، billHolderName، amount` | `await app.rpc("bank", "GetOrganizationPaymentToken")` |
| `GetPSProxyPaymentToken` | `paymentAmount، msg، description` | `endpoint، token` | `await app.rpc("bank", "GetPSProxyPaymentToken")` |
| `GetPSProxyToken` | `بدون پارامتر` | `endpoint، token` | `await app.rpc("bank", "GetPSProxyToken")` |
| `GetPayMoneyRequestToken` | `messagePeer، msgRid، msgDate، recipient (+1)` | `requestEndPoint، token` | `await app.rpc("bank", "GetPayMoneyRequestToken")` |
| `GetPaymentToken` | `msg، description، amount` | `token، endpoint، terminalId (+2)` | `await app.rpc("bank", "GetPaymentToken")` |
| `GetPayvandCard` | `index` | `card` | `await app.rpc("bank", "GetPayvandCard")` |
| `GetPayvandCardList` | `بدون پارامتر` | `payvandCards` | `await app.rpc("bank", "GetPayvandCardList")` |
| `GetRecentCharges` | `بدون پارامتر` | `recentCharges` | `await app.rpc("bank", "GetRecentCharges")` |
| `GetRemainToken` | `cardNumberStartingSix` | `requestEndPoint، token` | `await app.rpc("bank", "GetRemainToken")` |
| `GetSadadPSPPaymentToken` | `msg، paymentAmount، description` | `endpoint، token، terminalId (+1)` | `await app.rpc("bank", "GetSadadPSPPaymentToken")` |
| `GetTokenInvoice` | `service` | `endpoint، token` | `await app.rpc("bank", "GetTokenInvoice")` |
| `GrantBankiAccess` | `bot، serviceKey` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("bank", "GrantBankiAccess")` |

## سرویس `bale.bill.v1.Bill` (8 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CreateSavedBill` | `name، billType، billParameter` | `id` | `await app.rpc("bill", "CreateSavedBill")` |
| `DeleteSavedBills` | `ids` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("bill", "DeleteSavedBills")` |
| `GetBillHistory` | `count، page` | `bills` | `await app.rpc("bill", "GetBillHistory")` |
| `GetBillMenu` | `بدون پارامتر` | `items، otherBillsEnabled، usedDefaultMenu` | `await app.rpc("bill", "GetBillMenu")` |
| `GetSavedBills` | `count، page` | `bills` | `await app.rpc("bill", "GetSavedBills")` |
| `InquiryBill` | `billType، billParameters` | `bills، customerName` | `await app.rpc("bill", "InquiryBill")` |
| `PayBill` | `bill` | `paymentToken` | `await app.rpc("bill", "PayBill")` |
| `RenameSavedBill` | `id، name` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("bill", "RenameSavedBill")` |

## سرویس `bale.charnet.v1.CharnetService` (11 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `BuyCharge` | `walletToken، phoneNumber، amount، operatorType (+4)` | `paymentToken، receipt` | `await app.rpc("charnetservice", "BuyCharge")` |
| `BuyInternetBundle` | `walletToken، phoneNumber، bundleId، operatorType (+2)` | `paymentToken، receipt` | `await app.rpc("charnetservice", "BuyInternetBundle")` |
| `DeleteRecentChargeOrder` | `accessHash` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("charnetservice", "DeleteRecentChargeOrder")` |
| `DeleteRecentInternetBundleOrder` | `orderId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("charnetservice", "DeleteRecentInternetBundleOrder")` |
| `GetAvailableCharges` | `operator، chargeType` | `amounts، canBeOptional` | `await app.rpc("charnetservice", "GetAvailableCharges")` |
| `GetInternetBundleList` | `operatorType، simCardType، phoneNumber` | `bundleLists` | `await app.rpc("charnetservice", "GetInternetBundleList")` |
| `GetInternetBundlePaymentToken` | `operatorType، bundleId، phoneNumber، targetUserId` | `token` | `await app.rpc("charnetservice", "GetInternetBundlePaymentToken")` |
| `GetRecentChargeOrders` | `count، types` | `orders` | `await app.rpc("charnetservice", "GetRecentChargeOrders")` |
| `GetRecentInternetBundleOrders` | `count` | `orders` | `await app.rpc("charnetservice", "GetRecentInternetBundleOrders")` |
| `GetTopUpChargePaymentToken` | `providerCode، topupType، amount، targetPhoneNumber (+1)` | `token` | `await app.rpc("charnetservice", "GetTopUpChargePaymentToken")` |
| `GetVoucherChargePaymentToken` | `providerCode، amount، targetUserId` | `token` | `await app.rpc("charnetservice", "GetVoucherChargePaymentToken")` |

## سرویس `bale.crowdfunding.v1.CrowdFunding` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetParticipants` | `messageId، limit، offset` | `userPayments` | `await app.rpc("crowdfunding", "GetParticipants")` |
| `GetTotalPaidAmount` | `messageId` | `totalPaidAmount، creatorUserId` | `await app.rpc("crowdfunding", "GetTotalPaidAmount")` |

## سرویس `bale.evex.v1.Evex` (8 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetEvexCurrenciesList` | `بدون پارامتر` | `currencies، icmsWage` | `await app.rpc("evex", "GetEvexCurrenciesList")` |
| `GetEvexCurrencyPrice` | `currencyType، currencyAmount، reason، countryCode (+5)` | `currencyRate، orderId، amountToPay (+4)` | `await app.rpc("evex", "GetEvexCurrencyPrice")` |
| `GetEvexPaymentToken` | `orderId` | `token، paymentGatewayPrefix، terminalId` | `await app.rpc("evex", "GetEvexPaymentToken")` |
| `GetListOfEvexDeliveryStations` | `deliveryStationType، reason، ExitDate، bankType (+1)` | `stations` | `await app.rpc("evex", "GetListOfEvexDeliveryStations")` |
| `GetValidBanks` | `nationalCode، accountNationalCode` | `banks` | `await app.rpc("evex", "GetValidBanks")` |
| `LoadEvexHistory` | `بدون پارامتر` | `orders، approvalText` | `await app.rpc("evex", "LoadEvexHistory")` |
| `VerifyUserEvexAuthority` | `firstName، lastName، nationalCode، passportCode (+5)` | `approval` | `await app.rpc("evex", "VerifyUserEvexAuthority")` |
| `VerifyUserEvexExtraInfo` | `nakhodaInfo` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("evex", "VerifyUserEvexExtraInfo")` |

## سرویس `bale.exchange.v1.Exchange` (10 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetCurrenciesList` | `بدون پارامتر` | `currencies، icmsWage` | `await app.rpc("exchange", "GetCurrenciesList")` |
| `GetCurrencyPrice` | `currencyType، currencyAmount، reason، countryCode (+4)` | `currencyRate، orderId، amountToPay (+4)` | `await app.rpc("exchange", "GetCurrencyPrice")` |
| `GetExchangeOrderInfo` | `orderId` | `orderStatus` | `await app.rpc("exchange", "GetExchangeOrderInfo")` |
| `GetExchangePaymentToken` | `orderId، callBack` | `token` | `await app.rpc("exchange", "GetExchangePaymentToken")` |
| `GetInitialConfig` | `origin` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("exchange", "GetInitialConfig")` |
| `GetListOfDeliveryStations` | `deliveryStationType، reason، ExitDate` | `stations` | `await app.rpc("exchange", "GetListOfDeliveryStations")` |
| `GetTravelCurrencyOrderInDetail` | `phoneNumber، nationalCode، userId` | `orders` | `await app.rpc("exchange", "GetTravelCurrencyOrderInDetail")` |
| `GetUserIcmsInfo` | `nationalCode، birthDate` | `firstName، lastName، nationalCode (+6)` | `await app.rpc("exchange", "GetUserIcmsInfo")` |
| `LoadExchangeHistory` | `بدون پارامتر` | `orders، approvalText` | `await app.rpc("exchange", "LoadExchangeHistory")` |
| `VerifyUserExchangeAuthority` | `firstName، lastName، nationalCode، passportCode (+5)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("exchange", "VerifyUserExchangeAuthority")` |

## سرویس `bale.falake.v1.Falake` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetLinkStatus` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("falake", "GetLinkStatus")` |

## سرویس `bale.fanoos.v1.fanoos` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `Send` | `eventName، items، date` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("fanoos", "Send")` |
| `SendBatch` | `events` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("fanoos", "SendBatch")` |

## سرویس `bale.feedback.v1.FeedBack` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `SendFeedBack` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("feedback", "SendFeedBack")` |

## سرویس `bale.garson.v1.Garson` (11 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `EditCustomServices` | `items` | `customItems` | `await app.rpc("garson", "EditCustomServices")` |
| `GetAdvertisementBot` | `بدون پارامتر` | `bots` | `await app.rpc("garson", "GetAdvertisementBot")` |
| `GetBotBanners` | `بدون پارامتر` | `banners` | `await app.rpc("garson", "GetBotBanners")` |
| `GetBotsByCategory` | `categoryId، pagination` | `bots` | `await app.rpc("garson", "GetBotsByCategory")` |
| `GetCategorizedBots` | `بدون پارامتر` | `categorizedBots` | `await app.rpc("garson", "GetCategorizedBots")` |
| `GetCustomServices` | `بدون پارامتر` | `customItems` | `await app.rpc("garson", "GetCustomServices")` |
| `GetRecommendedBots` | `botId، pagination` | `bots، moreBotsUrl` | `await app.rpc("garson", "GetRecommendedBots")` |
| `GetServices` | `version` | `version، isChanged، data (+3)` | `await app.rpc("garson", "GetServices")` |
| `GetTrendBots` | `بدون پارامتر` | `bots` | `await app.rpc("garson", "GetTrendBots")` |
| `GetUserRepeatedBots` | `بدون پارامتر` | `bots` | `await app.rpc("garson", "GetUserRepeatedBots")` |
| `SearchServices` | `query، language، source` | `sections` | `await app.rpc("garson", "SearchServices")` |

## سرویس `bale.ghasedak.v1.GhasedakService` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetDiff` | `states، optimizations` | `updates، usersRefs، groupsRefs` | `await app.rpc("ghasedakservice", "GetDiff")` |
| `GetRoutesStates` | `groupPeers، optimizations` | `seqs` | `await app.rpc("ghasedakservice", "GetRoutesStates")` |

## سرویس `bale.giftpacket.v1.GiftPacket` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetGiftPacketPaymentToken` | `token، amount، peer، message` | `paymentToken` | `await app.rpc("giftpacket", "GetGiftPacketPaymentToken")` |
| `OpenGiftPacket` | `msgIdentifier، receiverWalletId، pageNo، orderType` | `giftReceivers، status، openedCount (+3)` | `await app.rpc("giftpacket", "OpenGiftPacket")` |
| `SendGiftPacketWithWallet` | `peer، randomId، message، sourceWalletId` | `seq، date، state (+2)` | `await app.rpc("giftpacket", "SendGiftPacketWithWallet")` |

## سرویس `bale.groups.v1.Groups` (50 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddDiscussionGroupAdmin` | `channel، discussionGroup` | `seq، date، state (+2)` | `await app.rpc("groups", "AddDiscussionGroupAdmin")` |
| `CreateGroup` | `rid، title، users، groupType (+3)` | `seq، state، group (+4)` | `await app.rpc("groups", "CreateGroup")` |
| `EditChannelNick` | `groupPeer، nick، randomId` | `seq، date، state (+2)` | `await app.rpc("groups", "EditChannelNick")` |
| `EditGroupAbout` | `groupPeer، rid، about، optimizations` | `seq، date، state (+2)` | `await app.rpc("groups", "EditGroupAbout")` |
| `EditGroupAvatar` | `groupPeer، fileLocation، rid، optimizations` | `avatar، seq، state (+1)` | `await app.rpc("groups", "EditGroupAvatar")` |
| `EditGroupDefaultCardNumber` | `groupPeer، cardNumber` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "EditGroupDefaultCardNumber")` |
| `EditGroupTitle` | `groupPeer، title، rid، optimizations` | `seq، date، state (+2)` | `await app.rpc("groups", "EditGroupTitle")` |
| `FetchGroupAdmins` | `groupOutPeer` | `users، admins` | `await app.rpc("groups", "FetchGroupAdmins")` |
| `GetBannedUsers` | `group` | `bannedUsers` | `await app.rpc("groups", "GetBannedUsers")` |
| `GetCanSeeMessages` | `groupPeer، userId` | `canSeeMessages` | `await app.rpc("groups", "GetCanSeeMessages")` |
| `GetFullGroup` | `peer` | `fullGroup` | `await app.rpc("groups", "GetFullGroup")` |
| `GetGroupDefaultCardNumber` | `groupPeerr` | `defaultCardNumber` | `await app.rpc("groups", "GetGroupDefaultCardNumber")` |
| `GetGroupInviteURL` | `groupPeer` | `url` | `await app.rpc("groups", "GetGroupInviteURL")` |
| `GetGroupMembersCount` | `group` | `membersCount` | `await app.rpc("groups", "GetGroupMembersCount")` |
| `GetGroupPreview` | `token، isOpenedOutsideBale` | `group، action` | `await app.rpc("groups", "GetGroupPreview")` |
| `GetGroupRecommendations` | `source` | `groups` | `await app.rpc("groups", "GetGroupRecommendations")` |
| `GetMemberPermissions` | `group، user` | `permissions` | `await app.rpc("groups", "GetMemberPermissions")` |
| `GetMutualGroups` | `peer` | `groups` | `await app.rpc("groups", "GetMutualGroups")` |
| `GetMyGroups` | `mode، isOwner، filters` | `groups` | `await app.rpc("groups", "GetMyGroups")` |
| `GetPins` | `groupPeer، page، limit` | `pins، count` | `await app.rpc("groups", "GetPins")` |
| `InviteUser` | `groupPeer، user، rid، optimizations (+1)` | `seq، date، state (+2)` | `await app.rpc("groups", "InviteUser")` |
| `InviteUsers` | `groupPeer، rid، users` | `notAddedUserPeers` | `await app.rpc("groups", "InviteUsers")` |
| `JoinGroup` | `token، optimizations` | `group، seq، state (+6)` | `await app.rpc("groups", "JoinGroup")` |
| `JoinPublicGroup` | `peer، optimizations` | `group، seq، state (+6)` | `await app.rpc("groups", "JoinPublicGroup")` |
| `KickUser` | `groupPeer، user، rid، optimizations` | `seq، date، state (+2)` | `await app.rpc("groups", "KickUser")` |
| `LeaveGroup` | `groupPeer، rid، optimizations، makeOrphan` | `seq، date، state (+2)` | `await app.rpc("groups", "LeaveGroup")` |
| `LoadFullGroups` | `groups` | `groups` | `await app.rpc("groups", "LoadFullGroups")` |
| `LoadGroupAvatars` | `peer` | `avatars` | `await app.rpc("groups", "LoadGroupAvatars")` |
| `LoadGroups` | `peers` | `groups` | `await app.rpc("groups", "LoadGroups")` |
| `LoadMembers` | `group، limit، next، condition` | `members، next` | `await app.rpc("groups", "LoadMembers")` |
| `MakeUserAdmin` | `groupPeer، userPeer، adminTitle` | `seq، date، state (+2)` | `await app.rpc("groups", "MakeUserAdmin")` |
| `PinMessage` | `senderUserId، groupPeer، date، msgRid` | `seq، date، state (+2)` | `await app.rpc("groups", "PinMessage")` |
| `RemoveDiscussionGroup` | `rid، channel` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "RemoveDiscussionGroup")` |
| `RemoveGroupAvatar` | `groupPeer، rid، optimizations، avaterId` | `seq، date، state (+2)` | `await app.rpc("groups", "RemoveGroupAvatar")` |
| `RemovePin` | `groupPeer` | `seq، date، state (+2)` | `await app.rpc("groups", "RemovePin")` |
| `RemoveSinglePin` | `groupPeer، msgRid، msgDate` | `seq، date، state (+2)` | `await app.rpc("groups", "RemoveSinglePin")` |
| `RemoveUserAdmin` | `groupPeer، userPeer` | `seq، date، state (+2)` | `await app.rpc("groups", "RemoveUserAdmin")` |
| `RevokeInviteURL` | `groupPeer` | `url` | `await app.rpc("groups", "RevokeInviteURL")` |
| `SetAvailableReactions` | `group، codes` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetAvailableReactions")` |
| `SetCanSeeHistory` | `groupPeer، canSeeHistory` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetCanSeeHistory")` |
| `SetCanSeeMessages` | `groupPeer، userId، canSeeMessages` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetCanSeeMessages")` |
| `SetDiscussionGroup` | `rid، channel` | `discussionGroup، group` | `await app.rpc("groups", "SetDiscussionGroup")` |
| `SetGroupDefaultPermissions` | `group، permissions` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetGroupDefaultPermissions")` |
| `SetMemberCustomTitle` | `groupId، memberId، title` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetMemberCustomTitle")` |
| `SetMemberPermissions` | `group، user، permissions` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetMemberPermissions")` |
| `SetRestriction` | `groupOutPeer، restriction، nick` | `seq، date، state (+2)` | `await app.rpc("groups", "SetRestriction")` |
| `SetSignMessages` | `groupPeer، signMessages` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetSignMessages")` |
| `SetSlowMode` | `group، seconds` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "SetSlowMode")` |
| `TransferOwnership` | `groupPeer، newOwner` | `seq، date، state (+2)` | `await app.rpc("groups", "TransferOwnership")` |
| `UnBanUser` | `groupPeer، user، optimizations` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("groups", "UnBanUser")` |

## سرویس `bale.ketf.v1.Ketf` (14 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetBotGroupPermissions` | `botUserId، groupId` | `hasAccessToMessages` | `await app.rpc("ketf", "GetBotGroupPermissions")` |
| `GetBotInfo` | `botUserId` | `botInfo` | `await app.rpc("ketf", "GetBotInfo")` |
| `GetBotWhiteList` | `botUserId` | `list` | `await app.rpc("ketf", "GetBotWhiteList")` |
| `GetBots` | `pagination` | `pageCount، bots` | `await app.rpc("ketf", "GetBots")` |
| `GetInlineBotResults` | `query، peer، botUserId، offset` | `results، nextOffset، queryId (+1)` | `await app.rpc("ketf", "GetInlineBotResults")` |
| `GetPaymentDetails` | `purchaseMessageId، invoiceIdentifier` | `title، totalAmount، paymentsHistory (+4)` | `await app.rpc("ketf", "GetPaymentDetails")` |
| `GetUserContext` | `botUserId` | `botUserId، userId، nonce (+1)` | `await app.rpc("ketf", "GetUserContext")` |
| `GetWebappHash` | `botUserId، data` | `hash، queryId، authDate` | `await app.rpc("ketf", "GetWebappHash")` |
| `InvokeCustomAction` | `id، messageId، peer، openDialogAction (+1)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ketf", "InvokeCustomAction")` |
| `MakePayment` | `paymentSessionId، paymentOptionId، wallet، gateway` | `gatewayRedirect، paymentReceipt` | `await app.rpc("ketf", "MakePayment")` |
| `SendAuthenticatedInlineCallBackData` | `templateMessageId، data` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ketf", "SendAuthenticatedInlineCallBackData")` |
| `SendInlineCallBackData` | `historyMessageIdentifier، data` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ketf", "SendInlineCallBackData")` |
| `SendInlineCallback` | `peer، messageId، data` | `answer` | `await app.rpc("ketf", "SendInlineCallback")` |
| `SendMiniAppData` | `botUserId، queryId، data، buttonText` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ketf", "SendMiniAppData")` |

## سرویس `bale.kifpool.v1.Kifpool` (30 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CashOut` | `requestId، token، amount، account (+2)` | `referenceNo` | `await app.rpc("kifpool", "CashOut")` |
| `Charge` | `paymentToken، referenceNo` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "Charge")` |
| `CheckChargePermission` | `paymentToken` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "CheckChargePermission")` |
| `CreateKifpool` | `nationalId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "CreateKifpool")` |
| `CryptoCashOut` | `requestId، amount، account، pan (+2)` | `referenceNo` | `await app.rpc("kifpool", "CryptoCashOut")` |
| `CryptoInvoice` | `token، pageSize، pageNumber` | `records` | `await app.rpc("kifpool", "CryptoInvoice")` |
| `CryptoPurchase` | `amount، srcToken، dstToken، description (+2)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "CryptoPurchase")` |
| `CryptoRefund` | `token، amount، approvalCode، trxRefSrc` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "CryptoRefund")` |
| `CryptoTransfer` | `amount، srcToken، dstToken، description (+1)` | `amount، date، approvalCode (+2)` | `await app.rpc("kifpool", "CryptoTransfer")` |
| `FeeInquiry` | `amount، transactionType، pocketType` | `amount، fee، responseData` | `await app.rpc("kifpool", "FeeInquiry")` |
| `GetChargePaymentToken` | `token، amount، callbackType` | `paymentToken` | `await app.rpc("kifpool", "GetChargePaymentToken")` |
| `GetCredit` | `بدون پارامتر` | `balance، hasCredit` | `await app.rpc("kifpool", "GetCredit")` |
| `GetCryptoChargePaymentToken` | `token، amount، receiverId` | `paymentToken` | `await app.rpc("kifpool", "GetCryptoChargePaymentToken")` |
| `GetCryptoWallets` | `بدون پارامتر` | `myCryptoWallets` | `await app.rpc("kifpool", "GetCryptoWallets")` |
| `GetKifpoolOwner` | `walletToken` | `firstName، lastName، walletStatus (+1)` | `await app.rpc("kifpool", "GetKifpoolOwner")` |
| `GetKifpoolPointBalance` | `token` | `pointBalanceInfo` | `await app.rpc("kifpool", "GetKifpoolPointBalance")` |
| `GetKifpoolPointDetails` | `token، count، page` | `pointDetailsInfo` | `await app.rpc("kifpool", "GetKifpoolPointDetails")` |
| `GetKifpoolPointSummery` | `token` | `pointSummeryInfo` | `await app.rpc("kifpool", "GetKifpoolPointSummery")` |
| `GetKifpoolTransactionPoint` | `transactionID، amount` | `calculatedPoint، point، unitAmount` | `await app.rpc("kifpool", "GetKifpoolTransactionPoint")` |
| `GetMyKifpools` | `invocationSpot، pocketType` | `myWallets، firstName، lastName` | `await app.rpc("kifpool", "GetMyKifpools")` |
| `Invoice` | `token، pageSize، pageNumber` | `records` | `await app.rpc("kifpool", "Invoice")` |
| `PayForMessage` | `amount، chargeAmount، message` | `status، paymentToken` | `await app.rpc("kifpool", "PayForMessage")` |
| `Purchase` | `amount، dstToken، srcToken، description (+4)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "Purchase")` |
| `PurchaseMessage` | `historyId، amount، description` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "PurchaseMessage")` |
| `PurchaseMessageWithCharge` | `historyId، amount، description، chargeAmount` | `paymentToken` | `await app.rpc("kifpool", "PurchaseMessageWithCharge")` |
| `PurchaseWithCharge` | `amount، dstToken، srcToken، description (+5)` | `paymentToken` | `await app.rpc("kifpool", "PurchaseWithCharge")` |
| `Transfer` | `sourceToken، destinationToken، destinationPhone، destinationUserid (+2)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("kifpool", "Transfer")` |
| `UpgradeKifpool` | `token، nationalId، cardNo، accountNo (+1)` | `level` | `await app.rpc("kifpool", "UpgradeKifpool")` |
| `VerifyCashOutKifpool` | `token` | `accountNo، firstName، lastName` | `await app.rpc("kifpool", "VerifyCashOutKifpool")` |
| `VerifyPurchaseMessage` | `historyId` | `amount، paymentTypeTitle، paymentTitle` | `await app.rpc("kifpool", "VerifyPurchaseMessage")` |

## سرویس `bale.llm_auth.v1.LLMAuthService` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetAuthToken` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("llmauthservice", "GetAuthToken")` |

## سرویس `bale.magazine.v1.Magazine` (9 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetMessageUpvoters` | `loadMoreState، message` | `loadMoreState، users` | `await app.rpc("magazine", "GetMessageUpvoters")` |
| `GetMyUpvotes` | `بدون پارامتر` | `upvotes` | `await app.rpc("magazine", "GetMyUpvotes")` |
| `GetSimilarPosts` | `message، loadMoreState` | `messages، loadMoreState، similarPosts` | `await app.rpc("magazine", "GetSimilarPosts")` |
| `LoadCategories` | `بدون پارامتر` | `categories` | `await app.rpc("magazine", "LoadCategories")` |
| `LoadCategoryFeedMessages` | `categoryId، loadMoreState` | `loadMoreState، messages` | `await app.rpc("magazine", "LoadCategoryFeedMessages")` |
| `LoadFeedMessages` | `loadMoreState` | `loadMoreState، messages` | `await app.rpc("magazine", "LoadFeedMessages")` |
| `LoadInternalFeedMessages` | `loadMoreState` | `loadMoreState، messages` | `await app.rpc("magazine", "LoadInternalFeedMessages")` |
| `RevokeUpvotedPost` | `message، albumId` | `upvotes` | `await app.rpc("magazine", "RevokeUpvotedPost")` |
| `UpvotePost` | `message، albumId` | `upvotes` | `await app.rpc("magazine", "UpvotePost")` |

## سرویس `bale.market.v1.Market` (26 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AcceptCampaignMarket` | `marketId، isPermanent` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "AcceptCampaignMarket")` |
| `AcceptMarketJoinRequest` | `marketPeerId، requestId، displayName، categoryId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "AcceptMarketJoinRequest")` |
| `CreateMarketJoinRequest` | `marketPeerId، displayName، categoryId، tagIds` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "CreateMarketJoinRequest")` |
| `CreateTag` | `title، categoryId` | `tag` | `await app.rpc("market", "CreateTag")` |
| `GetCategoriesList` | `categoryId، level، includeSampleMarkets، version` | `categories، version` | `await app.rpc("market", "GetCategoriesList")` |
| `GetCategoryMarkets` | `categoryId، pagination، version` | `markets، version` | `await app.rpc("market", "GetCategoryMarkets")` |
| `GetCategoryProducts` | `categoryId، pagination، version` | `products، version` | `await app.rpc("market", "GetCategoryProducts")` |
| `GetIndexedProducts` | `startDate، endDate، categoryId` | `products` | `await app.rpc("market", "GetIndexedProducts")` |
| `GetMarket` | `peerId، nickName` | `market، lastRequest` | `await app.rpc("market", "GetMarket")` |
| `GetMarketJoinRequests` | `بدون پارامتر` | `marketJoinRequests` | `await app.rpc("market", "GetMarketJoinRequests")` |
| `GetMarketsPendingJoinRequest` | `بدون پارامتر` | `requests` | `await app.rpc("market", "GetMarketsPendingJoinRequest")` |
| `GetNumberOfSales` | `peer` | `numberOfSales، isMarket` | `await app.rpc("market", "GetNumberOfSales")` |
| `GetOnboardingStatus` | `بدون پارامتر` | `status، categoryIds، gender` | `await app.rpc("market", "GetOnboardingStatus")` |
| `GetPendingCampaignMarkets` | `بدون پارامتر` | `markets` | `await app.rpc("market", "GetPendingCampaignMarkets")` |
| `GetStores` | `version` | `stores، version` | `await app.rpc("market", "GetStores")` |
| `GetTags` | `categoryId` | `tags` | `await app.rpc("market", "GetTags")` |
| `GetTopMarkets` | `ratingType، pagination` | `markets` | `await app.rpc("market", "GetTopMarkets")` |
| `GetYaldaStores` | `version` | `stores، version` | `await app.rpc("market", "GetYaldaStores")` |
| `RejectCampaignMarket` | `marketId، isPermanent` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "RejectCampaignMarket")` |
| `RejectMarketJoinRequest` | `marketPeerId، rejectCause، requestId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "RejectMarketJoinRequest")` |
| `SetGenericDeepLinks` | `links` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "SetGenericDeepLinks")` |
| `SetMarketBanners` | `banners` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "SetMarketBanners")` |
| `SetOnboardingData` | `categoryIds، gender، isSkipped` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "SetOnboardingData")` |
| `SetPopularSearches` | `items` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "SetPopularSearches")` |
| `SubmitMarketFeedback` | `rate، userOpinion، clientVersion، extraFields` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "SubmitMarketFeedback")` |
| `UpdateMarketInfo` | `peerId، displayName، primaryCategoryId، isBanned (+1)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("market", "UpdateMarketInfo")` |

## سرویس `bale.maviz.v1.MavizStream` (4 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetDifference` | `routeSequences، optimizations` | `groupEvents، usersRefs، groupsRefs` | `await app.rpc("mavizstream", "GetDifference")` |
| `SubscribeToThreadUpdates` | `peer، threadId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("mavizstream", "SubscribeToThreadUpdates")` |
| `SubscribeToUpdates` | `isMtProto` | `update، routeId، sequence (+4)` | `await app.rpc("mavizstream", "SubscribeToUpdates")` |
| `UnsubscribeFromThreadUpdates` | `peer، threadId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("mavizstream", "UnsubscribeFromThreadUpdates")` |

## سرویس `bale.meet.v1.Meet` (30 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AcceptCall` | `callId، inviteEnable` | `call، participants، seq (+2)` | `await app.rpc("meet", "AcceptCall")` |
| `AnswerCallJoinRequest` | `callId، requesterIdentifier، isAllowed` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "AnswerCallJoinRequest")` |
| `AskToJoinCall` | `callId، name` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "AskToJoinCall")` |
| `DeleteCallLogs` | `callIds، all، invert` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "DeleteCallLogs")` |
| `DeleteStream` | `streamUser` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "DeleteStream")` |
| `DiscardCall` | `callId، duration، reason، type` | `call، participants، seq (+2)` | `await app.rpc("meet", "DiscardCall")` |
| `GenerateCallLink` | `isPublic، callId، title` | `groupCall، linkExpirationPeriod` | `await app.rpc("meet", "GenerateCallLink")` |
| `GetCallLinkDetails` | `session` | `groupCall` | `await app.rpc("meet", "GetCallLinkDetails")` |
| `GetCallLogs` | `pageNumber، pageSize، afterDate، beforeDate` | `callLogs، total` | `await app.rpc("meet", "GetCallLogs")` |
| `GetCallState` | `callId` | `groupCall` | `await app.rpc("meet", "GetCallState")` |
| `GetGroupCall` | `peer` | `groupCall` | `await app.rpc("meet", "GetGroupCall")` |
| `GetOngoingCalls` | `pageNumber، pageSize` | `callLogs` | `await app.rpc("meet", "GetOngoingCalls")` |
| `GetWssURL` | `callId` | `url` | `await app.rpc("meet", "GetWssURL")` |
| `InviteToCall` | `callId، invitees` | `peerStates` | `await app.rpc("meet", "InviteToCall")` |
| `JoinGroupCall` | `callId، name` | `groupCall، states` | `await app.rpc("meet", "JoinGroupCall")` |
| `LeaveGroupCall` | `callId، end` | `groupCall، seq` | `await app.rpc("meet", "LeaveGroupCall")` |
| `MuteParticipant` | `callId، identity، trackId، revokePublishPermission` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "MuteParticipant")` |
| `ReceiveCall` | `callId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "ReceiveCall")` |
| `RemoveParticipant` | `callId، identity، blockFromCall` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "RemoveParticipant")` |
| `SendCallReaction` | `callId، reaction` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "SendCallReaction")` |
| `SendFanoosEvent` | `eventName، items، date` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "SendFanoosEvent")` |
| `SetLinkTitle` | `title، callId، linkUrl` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "SetLinkTitle")` |
| `StartCall` | `peer، rid، video، internalCall (+2)` | `call، participants، seq (+2)` | `await app.rpc("meet", "StartCall")` |
| `StartGroupCall` | `peer، randomId، video، mode (+1)` | `groupCall، seq` | `await app.rpc("meet", "StartGroupCall")` |
| `StartRecording` | `callId، layout، quality` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "StartRecording")` |
| `StartStream` | `streamUser، url، rtmpServer` | `streamKey` | `await app.rpc("meet", "StartStream")` |
| `StopRecording` | `callId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "StopRecording")` |
| `SubmitCallFeedback` | `callId، rate، userOpinion، client (+3)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "SubmitCallFeedback")` |
| `TakeCallAction` | `callId، lowerHand، raiseHand` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "TakeCallAction")` |
| `UpdateLayout` | `callId، requestedLayout` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("meet", "UpdateLayout")` |

## سرویس `bale.message_stream.v1.MessageStream` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CancelMessageStream` | `exPeer، messageId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messagestream", "CancelMessageStream")` |
| `ReceiveMessageStream` | `exPeer، messageId، fromChunkId` | `chunkTimeoutMillis` | `await app.rpc("messagestream", "ReceiveMessageStream")` |

## سرویس `bale.messaging.v2.Messaging` (43 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ArchiveDialogs` | `exPeers` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "ArchiveDialogs")` |
| `ClearChat` | `peer` | `seq، state، seqBig` | `await app.rpc("messaging", "ClearChat")` |
| `CreateFolder` | `name، peers` | `folderId، index، unreadPeers` | `await app.rpc("messaging", "CreateFolder")` |
| `CreateReservedFolder` | `folderId` | `index، unreadPeers` | `await app.rpc("messaging", "CreateReservedFolder")` |
| `CreateThread` | `peer، date، randomId، title` | `threadId` | `await app.rpc("messaging", "CreateThread")` |
| `CreateTopic` | `exPeer، title` | `topicId` | `await app.rpc("messaging", "CreateTopic")` |
| `DeleteChat` | `peer` | `seq، state، seqBig` | `await app.rpc("messaging", "DeleteChat")` |
| `DeleteFolder` | `folderId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "DeleteFolder")` |
| `DeleteMessage` | `peer، rids، dates، justMine` | `seq، state، seqBig` | `await app.rpc("messaging", "DeleteMessage")` |
| `DeleteTopic` | `exPeer، topicId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "DeleteTopic")` |
| `EditFolder` | `folderId، name، addedPeers، deletedPeers` | `unreadPeers` | `await app.rpc("messaging", "EditFolder")` |
| `EditTopic` | `exPeer، topicId، title` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "EditTopic")` |
| `FetchProtectedMessage` | `peer، messageId` | `history` | `await app.rpc("messaging", "FetchProtectedMessage")` |
| `ForwardMessages` | `peer، rid، forwardedMessages، groupedId (+1)` | `seq، date، state (+2)` | `await app.rpc("messaging", "ForwardMessages")` |
| `GetDiscussionMessage` | `peer، messageId` | `discussionMessage` | `await app.rpc("messaging", "GetDiscussionMessage")` |
| `GetMessagesRepliesInfo` | `peer، mids` | `containers` | `await app.rpc("messaging", "GetMessagesRepliesInfo")` |
| `GetTopicByID` | `exPeer، topicId` | `topic` | `await app.rpc("messaging", "GetTopicByID")` |
| `GetTopics` | `exPeer، minDate، limit` | `topics` | `await app.rpc("messaging", "GetTopics")` |
| `LoadDialogs` | `minDate، limit، optimizations، dialogType (+2)` | `groups، users، dialogs (+2)` | `await app.rpc("messaging", "LoadDialogs")` |
| `LoadFolderDialogs` | `minDate، limit، folderId، archiveFilter` | `dialogs` | `await app.rpc("messaging", "LoadFolderDialogs")` |
| `LoadFolders` | `includeMutedUnreadPeers، isNewUser` | `folders، unreadPeers` | `await app.rpc("messaging", "LoadFolders")` |
| `LoadGroupedDialogs` | `optimizations، archiveFilter` | `dialogs، users، groups (+4)` | `await app.rpc("messaging", "LoadGroupedDialogs")` |
| `LoadHistory` | `peer، date، loadMode، limit (+1)` | `history، users، userPeers (+2)` | `await app.rpc("messaging", "LoadHistory")` |
| `LoadPeerDialogs` | `peers` | `dialogs، groups، users (+2)` | `await app.rpc("messaging", "LoadPeerDialogs")` |
| `LoadPeers` | `بدون پارامتر` | `exPeers` | `await app.rpc("messaging", "LoadPeers")` |
| `LoadPinnedDialogs` | `folderId` | `dialogs` | `await app.rpc("messaging", "LoadPinnedDialogs")` |
| `LoadPinnedMessages` | `peer` | `pinnedMessages` | `await app.rpc("messaging", "LoadPinnedMessages")` |
| `LoadReplies` | `peer، threadId، date، loadMode (+1)` | `history، users، userPeers` | `await app.rpc("messaging", "LoadReplies")` |
| `MarkDialogsAsRead` | `peers` | `seq، state، seqBig` | `await app.rpc("messaging", "MarkDialogsAsRead")` |
| `MarkDialogsAsUnread` | `peers` | `seq، state، seqBig` | `await app.rpc("messaging", "MarkDialogsAsUnread")` |
| `MentionRead` | `peer، messageId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "MentionRead")` |
| `MessageRead` | `peer، date، exPeer` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "MessageRead")` |
| `MessageReceived` | `peer، date` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "MessageReceived")` |
| `PinDialogs` | `peers، folderId` | `dialogs، peers` | `await app.rpc("messaging", "PinDialogs")` |
| `PinMessage` | `peer، messageId، justMine` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "PinMessage")` |
| `ReorderFolders` | `folderIds` | `folderIds` | `await app.rpc("messaging", "ReorderFolders")` |
| `ReorderPinnedDialogs` | `peers، folderId` | `dialogs، peers` | `await app.rpc("messaging", "ReorderPinnedDialogs")` |
| `SendMessage` | `peer، rid، message، isOnlyForUser (+4)` | `seq، date، state (+2)` | `await app.rpc("messaging", "SendMessage")` |
| `SendMultiMediaMessage` | `peer، multiMedia، repliedMessage، groupedId` | `seq، date، state (+2)` | `await app.rpc("messaging", "SendMultiMediaMessage")` |
| `UnArchiveDialogs` | `exPeers` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "UnArchiveDialogs")` |
| `UnPinMessages` | `peer، messageIds، all` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "UnPinMessages")` |
| `UnpinDialogs` | `peers، folderId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("messaging", "UnpinDialogs")` |
| `UpdateMessage` | `peer، rid، updatedMessage` | `seq، date، state (+2)` | `await app.rpc("messaging", "UpdateMessage")` |

## سرویس `bale.microbanki.v1.MicroBanki` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetBamServiceToken` | `service` | `endpoint، token` | `await app.rpc("microbanki", "GetBamServiceToken")` |
| `GetMoneyRequestDetails` | `message` | `totalAmount، payCount، lastPayDate (+1)` | `await app.rpc("microbanki", "GetMoneyRequestDetails")` |
| `GetMoneyRequestPaymentList` | `message، loadMoreState` | `payment، loadMoreState، responseType (+2)` | `await app.rpc("microbanki", "GetMoneyRequestPaymentList")` |

## سرویس `bale.my_bank.v1.MyBank` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetMyBank` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("mybank", "GetMyBank")` |

## سرویس `bale.negah.v1.Negah` (1 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetMessageSeenList` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("negah", "GetMessageSeenList")` |

## سرویس `bale.organizations.v1.Organizations` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetUserOrganizationInfo` | `بدون پارامتر` | `userOrganization` | `await app.rpc("organizations", "GetUserOrganizationInfo")` |
| `GetUserOrganizationalContacts` | `بدون پارامتر` | `userPeers` | `await app.rpc("organizations", "GetUserOrganizationalContacts")` |

## سرویس `bale.pfm.v1.Pfm` (15 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddDetailToTransaction` | `id، detail` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "AddDetailToTransaction")` |
| `AddTransactionTags` | `id، tags` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "AddTransactionTags")` |
| `AddUserTags` | `tags` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "AddUserTags")` |
| `FilterTaggedTransactions` | `ids` | `idsWithTag` | `await app.rpc("pfm", "FilterTaggedTransactions")` |
| `GetSubTransactions` | `transactionId` | `transactionIds` | `await app.rpc("pfm", "GetSubTransactions")` |
| `GetTransactionTags` | `id` | `tags` | `await app.rpc("pfm", "GetTransactionTags")` |
| `GetUserAccounts` | `بدون پارامتر` | `accounts، config` | `await app.rpc("pfm", "GetUserAccounts")` |
| `GetUserTags` | `getUserTagType` | `tags` | `await app.rpc("pfm", "GetUserTags")` |
| `LoadTransactions` | `accountNumber، startDate، endDate، transactionType (+5)` | `transactions، totalAmounts، loadMoreState (+1)` | `await app.rpc("pfm", "LoadTransactions")` |
| `LoadTransactionsByIDs` | `transactionIds` | `transactions` | `await app.rpc("pfm", "LoadTransactionsByIDs")` |
| `RemoveTransaction` | `transactionIds` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "RemoveTransaction")` |
| `RemoveTransactionTags` | `id، tags` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "RemoveTransactionTags")` |
| `RemoveUserTags` | `tags` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "RemoveUserTags")` |
| `ReviveTransaction` | `transactionId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pfm", "ReviveTransaction")` |
| `SplitTransaction` | `transactionId، units` | `splitTransactionIds` | `await app.rpc("pfm", "SplitTransaction")` |

## سرویس `bale.pishvaz.v1.Pishvaz` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetMarketingToolsConfig` | `بدون پارامتر` | `inApp، eventBar، dialogListBanner` | `await app.rpc("pishvaz", "GetMarketingToolsConfig")` |
| `GetOnboardingPageData` | `بدون پارامتر` | `title، sections` | `await app.rpc("pishvaz", "GetOnboardingPageData")` |
| `SetMarketingToolAction` | `id، actionType` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("pishvaz", "SetMarketingToolAction")` |

## سرویس `bale.poll.v1.Poll` (5 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ClosePoll` | `pollId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("poll", "ClosePoll")` |
| `CreatePoll` | `pollMessage، createAt، expeer` | `pollId` | `await app.rpc("poll", "CreatePoll")` |
| `GetFullPollResult` | `pollId` | `fullPollResult` | `await app.rpc("poll", "GetFullPollResult")` |
| `GetPollResults` | `pollIds` | `pollResults` | `await app.rpc("poll", "GetPollResults")` |
| `Vote` | `pollId، isRetract، voteAt، optionIds` | `pollResult` | `await app.rpc("poll", "Vote")` |

## سرویس `bale.premium.v1.Premium` (7 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CalculateDiscountedPrice` | `packageId، couponCode` | `discountedPrice` | `await app.rpc("premium", "CalculateDiscountedPrice")` |
| `GetBadges` | `بدون پارامتر` | `categories` | `await app.rpc("premium", "GetBadges")` |
| `GetPackages` | `بدون پارامتر` | `packages، bundles` | `await app.rpc("premium", "GetPackages")` |
| `IsPremium` | `userId، withDetailOption` | `userStatus` | `await app.rpc("premium", "IsPremium")` |
| `IsPremiumBatch` | `userIds، withDetailOption` | `usersStatus` | `await app.rpc("premium", "IsPremiumBatch")` |
| `PurchasePackage` | `packageId، couponCode` | `sadadPaymentToken` | `await app.rpc("premium", "PurchasePackage")` |
| `SetUserBadge` | `badgeId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("premium", "SetUserBadge")` |

## سرویس `bale.presence.v1.Presence` (11 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetContactsPresences` | `limit` | `presences` | `await app.rpc("presence", "GetContactsPresences")` |
| `GetGroupMembersPresences` | `peer` | `presences` | `await app.rpc("presence", "GetGroupMembersPresences")` |
| `GetGroupOnlineCount` | `peer` | `count` | `await app.rpc("presence", "GetGroupOnlineCount")` |
| `GetUsersPresence` | `userIds` | `presences` | `await app.rpc("presence", "GetUsersPresence")` |
| `SetOnline` | `isOnline، timeout، deviceType، deviceCategory` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "SetOnline")` |
| `StopTyping` | `peer، typingType` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "StopTyping")` |
| `SubscribeFromGroupOnline` | `groups` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "SubscribeFromGroupOnline")` |
| `SubscribeFromOnline` | `users` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "SubscribeFromOnline")` |
| `SubscribeToGroupOnline` | `groups` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "SubscribeToGroupOnline")` |
| `SubscribeToOnline` | `users` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "SubscribeToOnline")` |
| `Typing` | `peer، typingType` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("presence", "Typing")` |

## سرویس `bale.ramz.v1.Ramz` (7 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `CheckPassword` | `password، servicesType` | `token` | `await app.rpc("ramz", "CheckPassword")` |
| `CheckPasswordSet` | `بدون پارامتر` | `hasSet، isSessionAuthorized` | `await app.rpc("ramz", "CheckPasswordSet")` |
| `DeletePassword` | `otp` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ramz", "DeletePassword")` |
| `ForgetPassword` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ramz", "ForgetPassword")` |
| `SendOTP` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ramz", "SendOTP")` |
| `SetPassword` | `password` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ramz", "SetPassword")` |
| `ValidateOTP` | `otp، servicesType` | `otpValid` | `await app.rpc("ramz", "ValidateOTP")` |

## سرویس `bale.recommender.v1.Recommender` (4 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetChannelRecommendations` | `بدون پارامتر` | `channels` | `await app.rpc("recommender", "GetChannelRecommendations")` |
| `GetGroupsRecommendation` | `source` | `groups` | `await app.rpc("recommender", "GetGroupsRecommendation")` |
| `GetRelatedChannels` | `exPeer` | `relatedChannels` | `await app.rpc("recommender", "GetRelatedChannels")` |
| `GetRelatedGroups` | `exPeer` | `relatedGroups` | `await app.rpc("recommender", "GetRelatedGroups")` |

## سرویس `bale.report.v1.Report` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ReportDismiss` | `exPeer` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("report", "ReportDismiss")` |
| `ReportInappropriateContent` | `report` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("report", "ReportInappropriateContent")` |

## سرویس `bale.sap.v1.Sap` (16 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddDestinationCards` | `cards` | `ids` | `await app.rpc("sap", "AddDestinationCards")` |
| `AddNewCards` | `cardInfo` | `cardId` | `await app.rpc("sap", "AddNewCards")` |
| `DeliverOtp` | `cardId، destinationPan، amount، accessAddress (+1)` | `isDone` | `await app.rpc("sap", "DeliverOtp")` |
| `EditCardExpirationDate` | `cardId، cardExpDate` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sap", "EditCardExpirationDate")` |
| `EnrollNewCard` | `origin` | `transactionId، url` | `await app.rpc("sap", "EnrollNewCard")` |
| `GetCardInfo` | `transactionId، cardInfo، cardId` | `cardId، maskedPan` | `await app.rpc("sap", "GetCardInfo")` |
| `GetCards` | `بدون پارامتر` | `userCards` | `await app.rpc("sap", "GetCards")` |
| `GetDefaultCard` | `بدون پارامتر` | `cardId` | `await app.rpc("sap", "GetDefaultCard")` |
| `GetDestinationCardInfo` | `cardId، destinationPan، amount، sourceAddress (+3)` | `cardHolderName، approvalCode` | `await app.rpc("sap", "GetDestinationCardInfo")` |
| `GetDestinationCards` | `بدون پارامتر` | `cards` | `await app.rpc("sap", "GetDestinationCards")` |
| `ReactivateApp` | `بدون پارامتر` | `transactionId، reactivationAddress` | `await app.rpc("sap", "ReactivateApp")` |
| `RemoveCard` | `cardId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sap", "RemoveCard")` |
| `RemoveDefaultCard` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sap", "RemoveDefaultCard")` |
| `RemoveDestinationCards` | `ids` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sap", "RemoveDestinationCards")` |
| `SetDefaultCard` | `cardId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sap", "SetDefaultCard")` |
| `TransferMoneyByCard` | `cardId، transferCode، destinationPan، amount (+11)` | `traceNumber، transactionTime` | `await app.rpc("sap", "TransferMoneyByCard")` |

## سرویس `bale.sarrafi.v1.Sarrafi` (9 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AuthenticateUser` | `nationalCode، accountNumber` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sarrafi", "AuthenticateUser")` |
| `CreateOrder` | `symbol، side، price، quantity` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("sarrafi", "CreateOrder")` |
| `GetChargeToken` | `currency، amount` | `tokenUrl` | `await app.rpc("sarrafi", "GetChargeToken")` |
| `GetDepth` | `symbol، limit` | `marketDepth` | `await app.rpc("sarrafi", "GetDepth")` |
| `GetOrder` | `orderId` | `order، trades` | `await app.rpc("sarrafi", "GetOrder")` |
| `GetOrders` | `بدون پارامتر` | `orders، limit، offset` | `await app.rpc("sarrafi", "GetOrders")` |
| `GetSession` | `symbol` | `openAt، closeAt، openingPrice (+4)` | `await app.rpc("sarrafi", "GetSession")` |
| `GetTickers` | `بدون پارامتر` | `usd، euro` | `await app.rpc("sarrafi", "GetTickers")` |
| `GetWallet` | `بدون پارامتر` | `wallet` | `await app.rpc("sarrafi", "GetWallet")` |

## سرویس `bale.schedule.v1.Scheduler` (6 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ExecuteTaskNow` | `taskID` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("scheduler", "ExecuteTaskNow")` |
| `ListTasks` | `exPeer، type، status` | `tasks` | `await app.rpc("scheduler", "ListTasks")` |
| `PeersWithScheduleTask` | `بدون پارامتر` | `exPeer` | `await app.rpc("scheduler", "PeersWithScheduleTask")` |
| `ReScheduleTask` | `taskID، scheduledAt، payload` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("scheduler", "ReScheduleTask")` |
| `ScheduleTask` | `exPeer، scheduledAt، payload` | `taskId` | `await app.rpc("scheduler", "ScheduleTask")` |
| `UnScheduleTask` | `taskIDs` | `failedTaskIDs` | `await app.rpc("scheduler", "UnScheduleTask")` |

## سرویس `bale.search.v1.Search` (12 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `RecommendPeer` | `exPeerType` | `peer` | `await app.rpc("search", "RecommendPeer")` |
| `SearchContent` | `query، contentType، loadMoreState` | `contentResults، loadMoreState، resultCount` | `await app.rpc("search", "SearchContent")` |
| `SearchDialog` | `query` | `dialogResults` | `await app.rpc("search", "SearchDialog")` |
| `SearchMarket` | `query، withCategory، loadMoreState` | `marketResults، category، loadMoreState (+1)` | `await app.rpc("search", "SearchMarket")` |
| `SearchMarketPopular` | `بدون پارامتر` | `popularResults` | `await app.rpc("search", "SearchMarketPopular")` |
| `SearchMedia` | `query، date، optimizations، loadMode` | `searchResults، users، groups (+4)` | `await app.rpc("search", "SearchMedia")` |
| `SearchMembers` | `query، exPeer، loadMoreState، users` | `users، loadMoreState` | `await app.rpc("search", "SearchMembers")` |
| `SearchMessageMore` | `loadMoreState، query، optimizations` | `searchResults، users، groups (+4)` | `await app.rpc("search", "SearchMessageMore")` |
| `SearchMessages` | `query، optimizations` | `searchResults، users، groups (+4)` | `await app.rpc("search", "SearchMessages")` |
| `SearchPeer` | `query، optimizations` | `searchResults، users، groups (+2)` | `await app.rpc("search", "SearchPeer")` |
| `SearchProduct` | `query، loadMoreState` | `productResults، loadMoreState، resultCount` | `await app.rpc("search", "SearchProduct")` |
| `UpdateSearchContentClick` | `messageId، searchTab` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("search", "UpdateSearchContentClick")` |

## سرویس `bale.shared_media.v1.SharedMediaService` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetActiveSharedMedia` | `exPeer` | `activeTab` | `await app.rpc("sharedmediaservice", "GetActiveSharedMedia")` |
| `LoadMedia` | `exPeer، date، contentType، loadMode (+1)` | `mediaResults` | `await app.rpc("sharedmediaservice", "LoadMedia")` |

## سرویس `bale.story.v1.Story` (24 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddBotStory` | `exPeer، mediaStory، textStory، tagIds (+1)` | `storyId` | `await app.rpc("story", "AddBotStory")` |
| `AddChannelStory` | `exPeer، mediaStory، hasReply، tagIds (+2)` | `storyId` | `await app.rpc("story", "AddChannelStory")` |
| `AddStory` | `mediaStory، textStory، tagIds، expirationType (+1)` | `storyId` | `await app.rpc("story", "AddStory")` |
| `CanAddBotStory` | `botUserId` | `canAddBotStory` | `await app.rpc("story", "CanAddBotStory")` |
| `CheckLinkValidity` | `exPeer، link` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("story", "CheckLinkValidity")` |
| `GetAllStories` | `بدون پارامتر` | `userStories، channelStories، botStories (+1)` | `await app.rpc("story", "GetAllStories")` |
| `GetBotStories` | `بدون پارامتر` | `result، popularityList` | `await app.rpc("story", "GetBotStories")` |
| `GetChannelStories` | `بدون پارامتر` | `result، popularityList` | `await app.rpc("story", "GetChannelStories")` |
| `GetDefaultStoryBackgrounds` | `بدون پارامتر` | `defaultStoryBackgrounds` | `await app.rpc("story", "GetDefaultStoryBackgrounds")` |
| `GetMostPopularStories` | `getSpecialStories، optimization` | `result، popularityList` | `await app.rpc("story", "GetMostPopularStories")` |
| `GetStories` | `getUnmutual` | `result، popularityList` | `await app.rpc("story", "GetStories")` |
| `GetStoriesByList` | `exPeers` | `userStories، channelStories، botStories` | `await app.rpc("story", "GetStoriesByList")` |
| `GetStoryById` | `storyId` | `result، channelStoryResult، botStoryResult` | `await app.rpc("story", "GetStoryById")` |
| `GetStoryReactionEmojis` | `بدون پارامتر` | `emojis` | `await app.rpc("story", "GetStoryReactionEmojis")` |
| `GetStoryTags` | `بدون پارامتر` | `tags` | `await app.rpc("story", "GetStoryTags")` |
| `GetStoryWidgets` | `storyId` | `widgets` | `await app.rpc("story", "GetStoryWidgets")` |
| `GetUserPrivacyConfig` | `بدون پارامتر` | `result` | `await app.rpc("story", "GetUserPrivacyConfig")` |
| `GetUserStoryConfig` | `key، exPeer` | `config` | `await app.rpc("story", "GetUserStoryConfig")` |
| `GetViewers` | `storyId، pagination` | `viewers، viewCount، likeCount (+3)` | `await app.rpc("story", "GetViewers")` |
| `GetViewersCount` | `storyId` | `viewCount، likeCount، linkClickCount (+2)` | `await app.rpc("story", "GetViewersCount")` |
| `ReactToStory` | `storyId، reaction، type، reactionType (+1)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("story", "ReactToStory")` |
| `RemoveStory` | `storyId` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("story", "RemoveStory")` |
| `SetUserPrivacyConfig` | `config` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("story", "SetUserPrivacyConfig")` |
| `SetUserStoryConfig` | `setType، config، exPeer` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("story", "SetUserStoryConfig")` |

## سرویس `bale.timche.v1.Timche` (5 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AskBotReviewCallback` | `botId، payload` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("timche", "AskBotReviewCallback")` |
| `GetBotPage` | `botId` | `name، nickname، activeUsers (+5)` | `await app.rpc("timche", "GetBotPage")` |
| `GetHomePage` | `بدون پارامتر` | `sections` | `await app.rpc("timche", "GetHomePage")` |
| `GetSectionPage` | `sectionId` | `sectionId، sectionName، bots` | `await app.rpc("timche", "GetSectionPage")` |
| `SubmitReview` | `botId، rating، comment، payload (+2)` | `shouldAskBaleReview، baleReviewText` | `await app.rpc("timche", "SubmitReview")` |

## سرویس `bale.tldr.v1.TLDR` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetLinkPreview` | `url` | `title، description، images` | `await app.rpc("tldr", "GetLinkPreview")` |
| `GetLinkSummary` | `url` | `summary` | `await app.rpc("tldr", "GetLinkSummary")` |

## سرویس `bale.top_peer.v1.TopPeer` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetTopPeer` | `بدون پارامتر` | `topPeers` | `await app.rpc("toppeer", "GetTopPeer")` |
| `RemovePeer` | `peer` | `isRemoved` | `await app.rpc("toppeer", "RemovePeer")` |

## سرویس `bale.turing.v1.AI` (2 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `GetTranscript` | `voice، outPeer، messageId` | `mustWait، downloadSource` | `await app.rpc("ai", "GetTranscript")` |
| `SendEvent` | `transcriptReactionEvent` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("ai", "SendEvent")` |

## سرویس `bale.users.v1.Users` (36 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddCard` | `bankCode` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "AddCard")` |
| `AddContact` | `uid، accessHash` | `seq، state، seqBig` | `await app.rpc("users", "AddContact")` |
| `BlockUser` | `peer` | `seq، state، seqBig` | `await app.rpc("users", "BlockUser")` |
| `ChangeDefaultCardNumber` | `defaultCardNumber` | `seq، state، seqBig` | `await app.rpc("users", "ChangeDefaultCardNumber")` |
| `ChangePhoneNumber` | `phoneNumber` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "ChangePhoneNumber")` |
| `CheckNickName` | `nickname` | `value` | `await app.rpc("users", "CheckNickName")` |
| `ConfirmPhoneNumber` | `code` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "ConfirmPhoneNumber")` |
| `EditAbout` | `about` | `seq، state، seqBig` | `await app.rpc("users", "EditAbout")` |
| `EditAvatar` | `fileLocation` | `avatar، seq، state` | `await app.rpc("users", "EditAvatar")` |
| `EditBirthDate` | `date` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "EditBirthDate")` |
| `EditMyPreferredLanguages` | `preferredLanguages` | `seq، state، seqBig` | `await app.rpc("users", "EditMyPreferredLanguages")` |
| `EditMyTimeZone` | `tz` | `seq، state، seqBig` | `await app.rpc("users", "EditMyTimeZone")` |
| `EditName` | `name` | `seq، state، seqBig` | `await app.rpc("users", "EditName")` |
| `EditNickName` | `nickname` | `seq، state، seqBig` | `await app.rpc("users", "EditNickName")` |
| `EditSex` | `sex` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "EditSex")` |
| `EditUserLocalName` | `uid، accessHash، name` | `seq، state، seqBig` | `await app.rpc("users", "EditUserLocalName")` |
| `GetContacts` | `contactsHash، optimizations` | `users، isNotChanged، userPeers` | `await app.rpc("users", "GetContacts")` |
| `GetFullUser` | `peer` | `fullUser` | `await app.rpc("users", "GetFullUser")` |
| `GetUserFullPrivacy` | `userId` | `privacy` | `await app.rpc("users", "GetUserFullPrivacy")` |
| `GetUserPrivacyStatus` | `userId، type` | `status` | `await app.rpc("users", "GetUserPrivacyStatus")` |
| `GetUsersDefaultCardNumber` | `userId` | `defaultCardNo` | `await app.rpc("users", "GetUsersDefaultCardNumber")` |
| `ImportContacts` | `phones، optimizations` | `users، seq، state (+1)` | `await app.rpc("users", "ImportContacts")` |
| `IsNameAllowed` | `name` | `value` | `await app.rpc("users", "IsNameAllowed")` |
| `LoadAvatars` | `peer` | `avatars` | `await app.rpc("users", "LoadAvatars")` |
| `LoadBlockedUsers` | `بدون پارامتر` | `userPeers` | `await app.rpc("users", "LoadBlockedUsers")` |
| `LoadFullUsers` | `userPeers` | `fullUsers` | `await app.rpc("users", "LoadFullUsers")` |
| `LoadFullUsersSequentially` | `userPeers` | `fullUsers` | `await app.rpc("users", "LoadFullUsersSequentially")` |
| `LoadUsers` | `peers` | `users` | `await app.rpc("users", "LoadUsers")` |
| `NotifyAboutDeviceInfo` | `preferredLanguages، timeZone` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "NotifyAboutDeviceInfo")` |
| `RemoveAvatar` | `avaterId` | `seq، state، seqBig` | `await app.rpc("users", "RemoveAvatar")` |
| `RemoveContact` | `uid، accessHash` | `seq، state، seqBig` | `await app.rpc("users", "RemoveContact")` |
| `RemoveDefaultCardNumber` | `بدون پارامتر` | `seq، state، seqBig` | `await app.rpc("users", "RemoveDefaultCardNumber")` |
| `ResetContacts` | `بدون پارامتر` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "ResetContacts")` |
| `SearchContacts` | `request، optimizations` | `users، userPeers، groups (+1)` | `await app.rpc("users", "SearchContacts")` |
| `SetUserPrivacyStatus` | `userId، type، status` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("users", "SetUserPrivacyStatus")` |
| `UnblockUser` | `peer` | `seq، state، seqBig` | `await app.rpc("users", "UnblockUser")` |

## سرویس `bale.v1.Configs` (3 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `EditParameter` | `key، value` | `seq، state، seqBig` | `await app.rpc("configs", "EditParameter")` |
| `GetInAppUpdate` | `بدون پارامتر` | `fileId، accessHash، fileSize` | `await app.rpc("configs", "GetInAppUpdate")` |
| `GetParameters` | `بدون پارامتر` | `parameters` | `await app.rpc("configs", "GetParameters")` |

## سرویس `bale.v1.Images` (10 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `AddGif` | `gif، thumb، mimeType` | `seq، state، seqBig` | `await app.rpc("images", "AddGif")` |
| `AddStickerCollection` | `id، accessHash` | `collections، seq، state` | `await app.rpc("images", "AddStickerCollection")` |
| `AddStickerPack` | `id` | `seq، state، seqBig` | `await app.rpc("images", "AddStickerPack")` |
| `GetSavedGifs` | `offset` | `gifs، offset` | `await app.rpc("images", "GetSavedGifs")` |
| `LoadOwnStickers` | `offset` | `ownStickers، offset` | `await app.rpc("images", "LoadOwnStickers")` |
| `LoadStickerCollection` | `id، accessHash` | `collection` | `await app.rpc("images", "LoadStickerCollection")` |
| `RemoveGif` | `gif` | `seq، state، seqBig` | `await app.rpc("images", "RemoveGif")` |
| `RemoveStickerCollection` | `id، accessHash` | `collections، seq، state` | `await app.rpc("images", "RemoveStickerCollection")` |
| `RemoveStickerPack` | `id` | `seq، state، seqBig` | `await app.rpc("images", "RemoveStickerPack")` |
| `UseGif` | `gif، usedAt` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("images", "UseGif")` |

## سرویس `bale.wallet.v1.Wallet` (13 متد)

| نام متد | ورودی‌ها (Arguments) | خروجی (Response) | نمونه کد فراخوانی |
| :--- | :--- | :--- | :--- |
| `ActivateWallet` | `nationalId، isAutoActivated` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("wallet", "ActivateWallet")` |
| `CashOutFromWallet` | `token، amount` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("wallet", "CashOutFromWallet")` |
| `GetMoneyRequestPaymentTokenByCard` | `msg، amount، regarding` | `token، endpoint، terminalId (+1)` | `await app.rpc("wallet", "GetMoneyRequestPaymentTokenByCard")` |
| `GetMyWallets` | `بدون پارامتر` | `wallets` | `await app.rpc("wallet", "GetMyWallets")` |
| `GetPaymentTokenByCard` | `targetWallet، amount، regarding` | `token، endpoint، terminalId (+1)` | `await app.rpc("wallet", "GetPaymentTokenByCard")` |
| `GetWalletChargeToken` | `walletId، amount` | `token، endpoint، terminalId (+1)` | `await app.rpc("wallet", "GetWalletChargeToken")` |
| `GetWalletContracts` | `بدون پارامتر` | `startDate، endDate، merchantCustomerUniqueValue (+3)` | `await app.rpc("wallet", "GetWalletContracts")` |
| `GetWalletInvoice` | `walletId، pageNumber` | `invoices` | `await app.rpc("wallet", "GetWalletInvoice")` |
| `PayByWallet` | `sourceWallet، targetWallet، amount، currency (+1)` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("wallet", "PayByWallet")` |
| `PayMoneyRequestByWallet` | `sourceWalletId، msg، amount، regarding` | `پاسخ تاییدیه پیش‌فرض` | `await app.rpc("wallet", "PayMoneyRequestByWallet")` |
| `VerifyCashOut` | `walletId، accountNo، nationalId` | `token، name` | `await app.rpc("wallet", "VerifyCashOut")` |
| `VerifyPeer` | `targetPeer` | `targetWalletName، targetUserId، walletId` | `await app.rpc("wallet", "VerifyPeer")` |
| `VerifyQRCode` | `targetWalletId` | `targetWalletName، targetUserId` | `await app.rpc("wallet", "VerifyQRCode")` |


# مرجع کامل RPCها

این مرجع شامل 690 ورودی registry است: 610 متد قبلی و 80 متد تازه.

هفت متد قدیمی برای سازگاری نگه داشته شده‌اند؛ بنابراین تعداد registry از ۶۸۳ descriptor فعال build رسمی بیشتر است.

## `ai.bale.pushak.Push`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `RegisterGooglePush` | `projectId: int64`، `token: string` | — | bundled |
| `RegisterPush` | `register: WebRegister`، `pushVersion: int32` | `encryptionKey: bytes` | bundled |
| `SetConfig` | `config: WebT_tl_91847` | — | bundled |
| `UnregisterAllPushCredentials` | — | — | bundled |
| `UnregisterGooglePush` | `token: string` | — | bundled |
| `UnregisterPush` | `unregister: WebUnregister` | — | bundled |

## `ai.bale.server.Files`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `FileUploadCancel` | `file: WebFileLocation` | `canceled: bool` | bundled |
| `GetNasimFilePublicUrl` | `peer: WebBot`، `file: WebFileLocation`، `filename: WebStringValue` | `fileUrl: WebFileUrl` | bundled |
| `GetNasimFileUploadResume` | `file: WebFileLocation` | `fileUrl: WebFileUrl`، `canResume: bool` | bundled |
| `GetNasimFileUploadUrl` | `expectedSize: int32`، `crc: int64`، `uid: int64`، `name: string`، `mimeType: string`، `exPeer: WebExPeer`، `sendType: WebSendType`، `chunkSize: int64` | `fileId: int64`، `url: string`، `duplicate: bool`، `chunkSize: int32`، `blockSize: int64` | bundled |
| `GetNasimFileUrl` | `file: WebFileLocation` | `fileUrl: WebFileUrl` | bundled |
| `GetNasimFileUrls` | `files: WebFileLocation[]` | `fileUrls: WebFileUrl[]` | bundled |
| `GetUploadLimits` | — | `uploadLimitBytes: int64`، `temporaryMaxBytes: int64`، `permanentMaxBytes: int64`، `boughtCapacityRemainingBytes: int64`، `boughtCapacityUnlimited: bool` | bundled |

## `bale.BankAccountPreferences.v1.BankAccountPreferences`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ActivateYaraMessaging` | `accountNumber: string` | — | web 5.5.1 |
| `EditPreference` | `preference: RecoveredMessage0093` | — | web 5.5.1 |
| `GetPreferences` | — | `accounts: RecoveredMessage0093[]` | web 5.5.1 |

## `bale.abacus.v1.Abacus`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `EnableShowReactionFlag` | — | — | bundled |
| `GetMessageReactionsList` | `peer: WebPeer`، `rid: int64`، `date: int64`، `code: string`، `page: int32`، `limit: int32` | `userReactions: WebUserReaction[]` | bundled |
| `GetMessagesReactions` | `peer: WebPeer`، `mids: WebMessageId[]`، `originPeer: WebPeer`، `originMids: WebMessageId[]` | `containers: WebContainer[]` | bundled |
| `GetMessagesViews` | `peer: WebPeer`، `mids: WebMessageId[]`، `increment: bool`، `correctMids: WebMessageId[]` | `containers: WebT_THn[]` | bundled |
| `GetShowReactionFlag` | — | `userId: int32`، `isEnable: bool` | bundled |
| `LoadReactions` | `peer: WebPeer`، `mids: WebMessageId[]`، `ignoreCountViews: bool` | `containers: WebContainer[]` | bundled |
| `MessageReactionsRead` | `peer: WebExPeer`، `messageId: WebMessageId` | — | bundled |
| `MessageRemoveReaction` | `peer: WebPeer`، `rid: int64`، `code: string`، `date: int64` | `seq: int32`، `reactions: WebReaction[]`، `state: bytes` | bundled |
| `MessageSetReaction` | `peer: WebPeer`، `rid: int64`، `code: string`، `date: int64` | `seq: int32`، `reactions: WebReaction[]`، `state: bytes` | bundled |

## `bale.advertisement.v1.Advertisement`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddCustomIncome` | `type: int32`، `amount: int64`، `description: string`، `customerUserId: int32`، `customerName: string`، `paymentMethod: int32`، `paymentDate: int64` | `id: string` | bundled |
| `BuildAudienceQuery` | `definition: RecoveredMessage0117` | `query: string`، `estimatedSize: int64` | web 5.5.1 |
| `CalculatePrice` | `spot: int32`، `viewCount: int64`، `clickCount: int64`، `link: string`، `isInstant: bool`، `tag1: int32`، `tag2: int32`، `targeting: RecoveredMessage0121` | `finalPrice: int64`، `clickUnitPrice: int64` | web 5.5.1 |
| `ChangeAccountState` | `state: int32`، `ownerId: int32`، `reason: string` | — | bundled |
| `ChangeAdState` | `adId: string`، `state: int32`، `reason: string` | — | bundled |
| `ChangeBonusCodeState` | `code: string`، `state: int32` | — | bundled |
| `ChangeCampaignContentState` | `campaignId: string`، `state: int32`، `reason: string` | — | bundled |
| `ChangeCampaignState` | `campaignId: string`، `state: int32`، `rejectionReason: string` | — | bundled |
| `ChangeChannelIncomeOwner` | `peerId: WebGroupPeer` | — | bundled |
| `ChangeChannelShowAdPermissions` | `peerId: WebGroupPeer`، `showAds: WebShowAds`، `timeRestrict: WebTimeRestrict`، `categoryFilter: WebCategoryFilter` | — | bundled |
| `ChangeStatusDialogAdOrder` | `id: string`، `targetStatus: int32`، `date: int64`، `rejectionReason: WebStringValue` | — | bundled |
| `ChangeUserDataState` | `ownerId: int32`، `state: int32`، `reason: int32` | — | bundled |
| `ChannelIncomeGetCredit` | `peerId: WebGroupPeer` | — | bundled |
| `ChannelIncomeKifTransfer` | `peerId: WebGroupPeer`، `payType: int32` | — | bundled |
| `ChannelIncomePayment` | `peerId: WebGroupPeer`، `payType: int32` | `factorHtml: string` | bundled |
| `ConvertIncome` | `convertToPoints: WebConvertToPoints`، `convertToGiftPacket: WebConvertToGiftPacket`، `convertToGiftPacketForChannelOwner: WebConvertToGiftPacketForChannelOwner` | — | bundled |
| `CreateAd` | `adData: WebAds`، `price: int64` | `adId: string` | bundled |
| `CreateAndStartChannelAd` | `title: string`، `description: string`، `link: string`، `platform: int32`، `viewCount: int32`، `clickCount: int32`، `startTime: int64` | `id: string` | bundled |
| `CreateAutomatedAudience` | `definition: RecoveredMessage0117`، `single: RecoveredMessage0113`، `randomGroups: RecoveredMessage0115` | `result: RecoveredMessage0116[]` | web 5.5.1 |
| `CreateBaleDialogCustomAd` | `pic: string`، `title: string`، `description: string`، `link: string`، `platform: int32` | `id: string` | bundled |
| `CreateBonusCode` | `data: WebT_tp_58187`، `autoGenerate: bool` | `code: string` | bundled |
| `CreateChannelIncomeFactor` | `peerId: WebGroupPeer`، `year: int32`، `month: int32` | `factorHtml: string` | bundled |
| `CreateCustomCampaignPackage` | `userId: int32`، `baseCredit: int64`، `creditExpireDays: int32`، `campaignDailyCapacity: int64`، `allowedConcurrentCampaign: int32`، `audienceId: int32`، `campaignViewCoef: int32`، `campaignClickCoef: int32` | — | bundled |
| `DeleteCustomIncome` | `id: string` | — | bundled |
| `EditAccount` | `account: WebData`، `isRestoreExpiredCredit: bool` | — | bundled |
| `EditAd` | `ad: WebAds` | — | bundled |
| `EditCampaignAd` | `ad: WebT_tE_58187` | — | bundled |
| `EditCampaignContent` | `campaign: WebCampaign` | — | bundled |
| `EstimateChannelSponsoredIncome` | `peerId: RecoveredMessage0086` | `estimatedViews: int64`، `estimatedIncome: int64` | web 5.5.1 |
| `FinishAd` | `id: string` | — | bundled |
| `FinishAdV2` | `adId: string` | — | bundled |
| `FinishChannelAd` | `id: string` | — | bundled |
| `GetAccountData` | `ownerId: int32` | `data: WebData` | bundled |
| `GetAccounts` | `pageData: WebPagingData` | `data: WebData[]` | bundled |
| `GetAccountsByState` | `state: int32`، `pageData: WebPagingData` | `data: WebData[]` | bundled |
| `GetActiveAds` | — | `ads: WebDialogAdOrder[]` | bundled |
| `GetActiveChannelAds` | — | `ads: WebOrder[]` | bundled |
| `GetAdData` | `adId: string` | `adData: WebAds` | bundled |
| `GetAdDetail` | `title: string`، `from: int64`، `to: int64` | `ads: WebT_rg_58187[]` | bundled |
| `GetAdProvider` | `peerId: WebGroupPeer`، `adType: int32`، `adSpot: int32`، `adCount: int64` | `content: WebContent[]` | bundled |
| `GetAdReport` | `adId: string` | `views: int64`، `clicks: int64`، `title: string`، `link: string` | bundled |
| `GetAdReportV2` | `adId: string` | `data: WebT_tu_58187` | bundled |
| `GetAdsBySpotAndPlatform` | `spot: int32`، `peerId: WebGroupPeer` | `data: WebT_tf_58187` | bundled |
| `GetAdsByStateAndSpot` | `pagingData: WebPagingData`، `state: int32`، `spot: int32` | `ads: WebAds[]` | bundled |
| `GetAllChannelIncomesFactor` | `year: int32`، `month: int32` | `factors: WebFactor[]` | bundled |
| `GetAllPaymentHistory` | `startDate: int64`، `endDate: int64` | `records: RecoveredMessage0118[]` | web 5.5.1 |
| `GetAvailableCampaignStartDate` | — | `date: int64` | bundled |
| `GetAwaitingToShowAds` | — | `ads: WebDialogAdOrder[]` | bundled |
| `GetAwaitingToShowChannelAds` | — | `ads: WebOrder[]` | bundled |
| `GetBaleCustomAd` | `adId: string` | `ad: WebAd` | bundled |
| `GetBonusCodeData` | `code: string` | `data: WebT_tp_58187` | bundled |
| `GetBonusCodes` | `pageData: WebPagingData` | `data: WebT_tp_58187[]` | bundled |
| `GetBusinessAds` | `pagingData: WebPagingData`، `state: int32` | `ads: WebUpdatedAd[]` | bundled |
| `GetCRMIssues` | `userIssue: WebUserIssue`، `allIssue: WebAllIssue` | `data: WebT_tw_58187[]` | bundled |
| `GetCampaignAds` | `pagingData: WebPagingData`، `state: int32` | `data: WebT_tN_58187[]` | bundled |
| `GetCampaignContentById` | `campaignId: string` | `campaign: WebCampaign` | bundled |
| `GetCampaignContents` | `pagingData: WebPagingData`، `state: int32` | `campaigns: WebCampaign[]` | bundled |
| `GetCampaignData` | `campaignId: string` | `data: WebT_tN_58187` | bundled |
| `GetChannelAds` | `groupId: WebPeer` | `ads: WebT_ez_58187[]` | bundled |
| `GetChannelEarnMoneyInfo` | `groupId: WebPeer` | `currentMonthIncome: double`، `notPaidIncome: double`، `adCount: int64`، `adCountUpdateDate: int64` | bundled |
| `GetChannelEarnMoneyStatus` | `groupId: WebPeer` | `status: int32` | bundled |
| `GetChannelGraphReport` | `peerId: WebGroupPeer`، `startTime: int64`، `endTime: int64` | `viewGraph: WebViewGraph[]` | bundled |
| `GetChannelIncomeReport` | `peerId: WebGroupPeer` | `incomeReports: WebIncomeReport[]` | bundled |
| `GetChannelOwnerBankInformation` | `channelId: WebGroupPeer` | `userId: int32`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string`، `firstName: string`، `lastName: string`، `phone: string`، `state: int32`، `reason: int32`، `channelNick: string` | bundled |
| `GetChannelShowAdCategoryFilter` | `peerId: WebGroupPeer` | `categories: WebCategory[]` | bundled |
| `GetChannelShowAdPermissions` | `peerId: WebGroupPeer` | `showSponsoredAd: bool`، `verifiedUserId: int32` | bundled |
| `GetChannelShowAdTimeRestrict` | `peerId: WebGroupPeer` | `data: WebT_tS_58187` | bundled |
| `GetChannelSponsoredIncomeReport` | `peerId: RecoveredMessage0086`، `startTime: int64`، `endTime: int64` | `totalViews: int64`، `totalIncome: int64`، `totalAdCount: int32`، `averageCtr: double`، `dailyReports: RecoveredMessage0120[]`، `categoryReports: RecoveredMessage0119[]` | web 5.5.1 |
| `GetChannelUndepositedIncomes` | `year: int32`، `month: int32` | `items: RecoveredMessage0042[]` | web 5.5.1 |
| `GetChannelsViewReport` | `startTime: int64`، `endTime: int64` | `channelsView: WebChannelsView[]` | bundled |
| `GetConfig` | — | `config: string` | bundled |
| `GetCreditHistory` | `ownerId: int32`، `startTime: int64`، `endTime: int64` | `creditHistories: WebCreditHistory[]` | bundled |
| `GetCreditableAccounts` | `pageData: WebPagingData` | `data: WebData[]` | bundled |
| `GetCustomIncomes` | `startTime: int64`، `endTime: int64` | `records: WebT_tV_58187[]` | bundled |
| `GetDialogAdOrderDetails` | — | `dialogAdOrder: WebDialogAdOrder[]` | bundled |
| `GetDialogAdOrderPaymentToken` | `id: string`، `rialAmount: int64`، `coinAmount: int64` | `token: string` | bundled |
| `GetFactorEligibleAds` | `tBegin: int64`، `tEnd: int64` | `ads: WebT_th_58187[]` | bundled |
| `GetInvoiceContent` | `invoiceRequestId: string` | `id: string`، `description: string[]`، `responseCode: string`، `data: RecoveredMessage0045` | web 5.5.1 |
| `GetLegalOrgChannels` | — | `channels: RecoveredMessage0061[]` | web 5.5.1 |
| `GetMyContactPopularChannels` | — | `channels: WebT_tk_58187[]` | bundled |
| `GetOnBoardingChannels` | — | `channels: WebChannel[]`، `showOnBoarding: bool` | bundled |
| `GetOnboardingPeers` | — | `peers: WebT_tm_58187[]` | bundled |
| `GetOnboardingPosts` | `categoryId: int32` | `posts: WebPost[]` | bundled |
| `GetOnboardingSpotData` | `onboardingSpot: int32`، `suggestedPeerType: int32` | `contactChannels: WebContactChannels`، `suggestedChannels: WebSuggestedChannels` | bundled |
| `GetOwnerIdByPhone` | `phoneNumber: string` | `userId: int32` | bundled |
| `GetPaidAdsByTime` | `pagingData: WebPagingData`، `startTime: int64`، `endTime: int64` | `ads: WebT_th_58187[]` | bundled |
| `GetPaymentData` | `adId: string` | `data: WebT_tI_58187` | bundled |
| `GetPeriodCapacityData` | `beginDate: int64`، `endDate: int64` | `data: WebT_te_58187[]` | bundled |
| `GetUserAds` | `pagingData: WebPagingData`، `userId: int32` | `ads: WebAds[]` | bundled |
| `GetUserAuthData` | `channelId: WebGroupPeer` | `userId: int32`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string`، `firstName: string`، `lastName: string`، `phone: string`، `state: int32`، `reason: int32`، `channelNick: string` | bundled |
| `GetUserCampaigns` | `pagingData: WebPagingData`، `userId: int32` | `data: WebT_tN_58187[]` | bundled |
| `GetUserOnboardingScenario` | — | `scenario: int32` | bundled |
| `GetUserStatus` | `userId: int64` | `status: int32` | bundled |
| `GetUsersAuthDataByState` | `state: int32` | `usersData: WebUsersData[]` | bundled |
| `GetVODContents` | — | `contents: WebT_tB_58187[]` | bundled |
| `MergeCustomIncomeRecords` | `customIncomeIds: string[]` | — | web 5.5.1 |
| `MergeIncreaseCreditRecords` | `increaseCreditIds: string[]` | — | web 5.5.1 |
| `ModifyCapacity` | `date: int64`، `val: int32` | — | bundled |
| `RegisterForEarnMoney` | `info: WebT_eY_58187` | — | bundled |
| `RetryFailedAutoSentInvoice` | `failedInvoiceRequestId: string` | — | web 5.5.1 |
| `SendAdminMessage` | `receiver: int32`، `messageText: string`، `fileId: int64`، `fileName: string` | — | bundled |
| `SendFactorMessage` | `channelId: int32`، `messageText: string`، `fileId: int64`، `fileName: string`، `year: int32`، `month: int32` | — | bundled |
| `SendInvoiceForPaymentHistoryRecord` | `recordId: string`، `depositTrackingId: RecoveredMessage0065`، `paymentHistoryType: int32` | `invoiceRequestId: string` | web 5.5.1 |
| `SendLegalOrgChannelIncome` | `channelId: int32` | `results: RecoveredMessage0048[]` | web 5.5.1 |
| `SetAdTarget` | `adId: string`، `targeting: WebTargeting` | — | bundled |
| `SetCapacityMaxViews` | `data: RecoveredMessage0114[]`، `spot: int32` | — | web 5.5.1 |
| `SetChannelInvoiceInfo` | `peerId: WebGroupPeer`، `nationalCode: string`، `address: string`، `postalCode: string`، `name: string`، `tag1: int32`، `tag2: int32`، `birthDate: string` | — | bundled |
| `SetChannelOwnerBankInformation` | `channelId: WebGroupPeer`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string` | — | bundled |
| `SetOnBoardingChannels` | `channels: WebChannel[]` | — | bundled |
| `SetUserAuthData` | `channelId: WebGroupPeer`، `nationalCode: string`، `birthDate: string`، `address: string`، `postalCode: string`، `melliAccountNumber: string` | — | bundled |
| `StartAd` | `adId: string`، `startTime: int64`، `platform: int32`، `autoFinish: bool` | — | bundled |
| `StartBaleCustomAd` | `id: string`، `platform: int32`، `pic: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int32`، `clickCount: int32` | `ad: WebAd` | bundled |
| `StartChannelAdFromOrder` | `id: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int32`، `clickCount: int32`، `platform: int32` | — | bundled |
| `StartFromOrder` | `id: string`، `platform: int32`، `pic: string`، `title: string`، `description: string`، `link: string`، `startTime: int64`، `viewCount: int64`، `clickCount: int64` | — | bundled |
| `StopAllBaleCustomAds` | — | — | bundled |
| `SubmitChannelAdOrder` | `order: WebOrder` | — | bundled |
| `SubmitDialogAdOrder` | `dialogAdOrder: WebDialogAdOrder` | — | bundled |
| `SubmitPhotoForBaleCustomAd` | `adId: string`، `pic: string` | `ad: WebAd` | bundled |
| `UpdateBusinessAd` | `updatedAd: WebUpdatedAd` | — | bundled |
| `UpdateCRMIssue` | `addIssue: WebAddIssue`، `addComment: WebAddComment`، `resolveIssue: WebResolveIssue`، `ignoreUser: WebIgnoreUser` | — | bundled |
| `UpdateClick` | `id: string`، `count: int32`، `peer: WebExPeer` | — | bundled |
| `UpdateGroupStatus` | `groupId: WebPeer` | — | bundled |
| `UpdateView` | `id: string`، `count: int32`، `peerId: WebGroupPeer` | `isSuccessful: bool` | bundled |

## `bale.anonymous_contact.v1.AnonymousContact`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetUserAnonymousContactPage` | `userId: int32`، `serviceMessageRid: int64`، `serviceMessageDate: int64` | `countryNumber: string`، `registerAccountTime: WebExtAnonymousContactInt64Value`، `lastTimeNameChanged: WebExtAnonymousContactInt64Value`، `lastTimeAvatarChanged: WebExtAnonymousContactInt64Value`، `commonGroups: WebExtAnonymousContactGroupPeer[]`، `extraInfo: WebExtAnonymousContactExtraInfo[]` | bundled |

## `bale.appzar.v1.Appzar`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetMenuButton` | `botUserId: int64` | `menuButton: WebT_LF` | bundled |
| `GetMiniAppUrl` | `botUserId: int64`، `screenMode: int64`، `themeParams: WebThemeParams`، `main: WebMain`، `menuButton: WebMenuButton`، `keyboardButton: WebKeyboardButton`، `directLink: WebDirectLink` | `url: bytes`، `screenMode: int64`، `queryId: WebStringValue` | bundled |
| `InvokeCustomMethod` | `botUserId: int64`، `method: bytes`، `params: bytes` | `data: bytes` | bundled |

## `bale.arbaeen.v1.Arbaeen`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CashPaymentCallback` | `paymentCode: string`، `nationalCode: string`، `userId: int32`، `orderId: int32` | `firstName: string`، `lastName: string` | web 5.5.1 |
| `GetAdminStationList` | — | `stations: RecoveredMessage0164[]` | web 5.5.1 |
| `GetArbaeenCurrenciesList` | — | `currencies: RecoveredMessage0159[]`، `icmsWage: int32` | web 5.5.1 |
| `GetArbaeenCurrencyPrice` | `currencyType: int32`، `currencyAmount: int32`، `reason: int32`، `countryCode: int32`، `exitDate: string`، `nationalCode: string`، `deliveryStationType: int32`، `stationId: string`، `bankType: int32` | `currencyRate: int32`، `orderId: int32`، `newCurrencyRate: string` | web 5.5.1 |
| `GetArbaeenPaymentToken` | `orderId: int32` | `token: string`، `paymentGatewayPrefix: string`، `terminalId: string`، `paymentUrl: string` | web 5.5.1 |
| `GetListOfArbaeenDeliveryStations` | `deliveryStationType: int32`، `reason: int32`، `ExitDate: string`، `bankType: int32`، `shouldReturnCapacity: RecoveredMessage0064` | `stations: RecoveredMessage0161[]` | web 5.5.1 |
| `GetListOfBoxOffice` | `stationId: string`، `exitDate: string` | `boxOffice: RecoveredMessage0164[]` | web 5.5.1 |
| `GetListOfBranches` | `stateId: string`، `exitDate: string` | `branches: RecoveredMessage0164[]` | web 5.5.1 |
| `GetListOfStates` | — | `states: RecoveredMessage0160[]` | web 5.5.1 |
| `GetRate` | — | `rate: float` | web 5.5.1 |
| `GetSuggestedGroups` | — | `suggestedGroups: RecoveredMessage0165[]` | web 5.5.1 |
| `GetValidArbaeenBanks` | `nationalCode: string`، `accountNationalCode: RecoveredMessage0065` | `banks: int32[]` | web 5.5.1 |
| `LoadArbaeenHistory` | — | `orders: RecoveredMessage0163[]`، `approvalText: string` | web 5.5.1 |
| `SendOTP` | `phoneNumber: string` | — | web 5.5.1 |
| `StartBot` | `peer: RecoveredMessage0087` | — | web 5.5.1 |
| `UserHasAccess` | — | `access: bool` | web 5.5.1 |
| `VerifyOTP` | `phoneNumber: string`، `code: string` | `verified: bool` | web 5.5.1 |
| `VerifyUserArbaeenAuthority` | `firstName: string`، `lastName: string`، `nationalCode: string`، `passportCode: string`، `postalCode: string`، `birthDate: string`، `fatherName: string`، `shId: string`، `bankType: int32`، `phoneNumber: string` | `approval: RecoveredMessage0162` | web 5.5.1 |
| `VerifyUserArbaeenExtraInfo` | `nakhodaInfo: RecoveredMessage0158` | — | web 5.5.1 |

## `bale.auth.v1.Auth`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ChangeLanguage` | `language: int32` | — | bundled |
| `ChangePhone` | `phoneNumber: int64`، `code: string`، `transactionHash: string` | — | bundled |
| `DeleteAccount` | `code: string`، `transactionHash: string` | — | bundled |
| `DisableTwoFactorAuthentication` | — | — | bundled |
| `EnableTwoFactorAuthentication` | `email: string`، `password: string` | — | bundled |
| `GetAuthSessions` | — | `userAuths: WebUserAuth[]` | bundled |
| `GetBajeBamTicket` | `expDateTime: int64`، `mobileNo: string` | `ticket: string` | bundled |
| `GetBaleTicket` | `expDateTime: int64`، `mobileNo: string`، `clientId: string` | `redirectUrl: string` | bundled |
| `GetJWTToken` | — | `jwt: WebStringValue` | bundled |
| `GetTicket` | `jsonRequest: string`، `jsonSign: string` | `redirectUrl: string` | bundled |
| `GetUserIdToken` | `ticket: string` | `token: string`، `userId: int32`، `source: int32`، `service: string` | bundled |
| `IsTwoFactorAuthenticationEnabled` | — | `isEnabled: bool` | bundled |
| `LogOut` | — | `futureAuthToken: WebStringValue` | bundled |
| `RecoverPassword` | `transactionHash: string` | `emailPattern: string` | bundled |
| `SendChangePhoneVerificationCode` | — | `transactionHash: string`، `activationType: int32` | bundled |
| `SendDeleteAccountVerificationCode` | — | `transactionHash: string`، `activationType: int32` | bundled |
| `SetNewPassword` | `newPassword: string`، `transactionHash: string` | — | bundled |
| `SignOut` | — | — | bundled |
| `SignUp` | `transactionHash: string`، `name: string`، `sex: int32`، `password: WebStringValue` | `user: WebUser`، `config: WebT_TS`، `jwt: WebStringValue` | bundled |
| `StartPhoneAuth` | `phoneNumber: int64`، `appId: int32`، `apiKey: string`، `deviceHash: bytes`، `deviceTitle: string`، `timeZone: WebStringValue`، `preferredLanguages: string[]`، `imeiList: WebValue`، `sendCodeType: int32`، `options: int32[]` | `transactionHash: string`، `isRegistered: bool`، `activationType: int32`، `isImeiOk: bool`، `sentCodeType: int32`، `codeExpirationDate: WebInt64Value_1`، `nextSendCodeType: int32`، `nextSendCodeWaitTime: WebInt64Value_1`، `codeTimeout: WebInt32Value_1`، `exInfoAddress: WebExInfoAddress[]`، `availableSendCodeTypes: int32[]` | bundled |
| `TerminateAllSessions` | — | — | bundled |
| `TerminateSession` | `id: int32` | — | bundled |
| `ValidateCode` | `transactionHash: string`، `code: string`، `isJwt: WebBoolValue_1`، `futureAuthTokens: string[]` | `user: WebUser`، `config: WebT_TS`، `jwt: WebStringValue` | bundled |
| `ValidatePassword` | `transactionHash: string`، `password: string`، `isJwt: WebBoolValue_1` | `user: WebUser`، `config: WebT_TS`، `jwt: WebStringValue` | bundled |
| `VerifyEmail` | `email: string`، `code: string` | — | bundled |
| `VerifyPassword` | `password: string` | — | bundled |
| `VerifyPasswordRecovery` | `code: string`، `transactionHash: string` | — | bundled |

## `bale.balebank.v1.GoldGiftPacket`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetWinnerIDs` | `giftPacketId: int64` | `winners: WebWinner[]` | bundled |
| `OpenGoldGiftPacket` | `giftPacketId: int64` | `openedCount: int64`، `selfWinAmount: int64`، `rank: int64`، `giftReceivers: WebGiftReceiver[]`، `status: int32`، `verificationDeadline: WebInt64Value` | bundled |
| `SendGoldGiftPacket` | `amount: int64`، `count: int64`، `description: string`، `givingType: int32`، `randomId: int64`، `peer: WebPeer` | `giftPacketId: int64` | bundled |

## `bale.balebank.v1.GoldWallet`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetBalance` | — | `balance: int64` | bundled |

## `bale.bank.v1.Bank`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `BuyFastCharge` | `amount: int64`، `phoneNumber: WebStringValue`، `operator: int32`، `chargeType: int32` | `transactionDate: int64`، `refrenceNumber: string`، `pin: WebStringValue`، `serial: WebStringValue` | bundled |
| `GetCardRemain` | `cardNumber: string`، `cvv2: string`، `expireDate: string`، `pin2: string` | `currentBalanceAmount: string`، `availableBalanceAmount: string` | bundled |
| `GetCardTransferToken` | `peerUserId: WebInt32Value`، `msgRid: WebInt64Value_1`، `description: WebStringValue` | `requestEndPoint: string`، `token: string`، `destCardNo: WebStringValue` | bundled |
| `GetOTPToken` | `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | bundled |
| `GetOTPTokenV2` | `messagePeer: WebBot`، `msgRid: int64`، `msgDate: int64`، `peerUserId: WebInt32Value`، `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | bundled |
| `GetOrganizationPaymentToken` | `organizationId: string`، `invoiceId: string`، `amount: int64` | `token: string`، `billHolderName: string`، `amount: double` | bundled |
| `GetPSProxyPaymentToken` | `paymentAmount: int64`، `msg: WebMsg`، `description: WebStringValue` | `endpoint: string`، `token: string` | bundled |
| `GetPSProxyToken` | — | `endpoint: string`، `token: string` | bundled |
| `GetPayMoneyRequestToken` | `messagePeer: WebBot`، `msgRid: int64`، `msgDate: int64`، `recipient: int32`، `description: WebStringValue` | `requestEndPoint: string`، `token: string` | bundled |
| `GetPaymentToken` | `msg: WebMsg`، `description: WebStringValue`، `amount: WebInt32Value` | `token: string`، `endpoint: string`، `terminalId: WebStringValue`، `cardAcqId: WebStringValue`، `orderId: WebInt64Value_1` | bundled |
| `GetPayvandCard` | `index: string` | `card: string` | bundled |
| `GetPayvandCardList` | — | `payvandCards: WebPayvandCard[]` | bundled |
| `GetRecentCharges` | — | `recentCharges: WebRecentCharge[]` | bundled |
| `GetRemainToken` | `cardNumberStartingSix: string` | `requestEndPoint: string`، `token: string` | bundled |
| `GetSadadPSPPaymentToken` | `msg: WebMsg`، `paymentAmount: int64`، `description: WebStringValue` | `endpoint: string`، `token: string`، `terminalId: string`، `merchantCode: string` | bundled |
| `GetTokenInvoice` | `service: int32` | `endpoint: string`، `token: string` | bundled |
| `GrantBankiAccess` | `bot: WebUserPeer`، `serviceKey: string` | — | bundled |

## `bale.bill.v1.Bill`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CreateSavedBill` | `name: string`، `billType: int32`، `billParameter: RecoveredMessage0152` | `id: int64` | web 5.5.1 |
| `DeleteSavedBills` | `ids: int64[]` | — | web 5.5.1 |
| `GetBillHistory` | `count: int32`، `page: int32` | `bills: RecoveredMessage0149[]` | web 5.5.1 |
| `GetBillMenu` | — | `items: RecoveredMessage0144[]`، `otherBillsEnabled: bool`، `usedDefaultMenu: bool` | web 5.5.1 |
| `GetSavedBills` | `count: int32`، `page: int32` | `bills: RecoveredMessage0151[]` | web 5.5.1 |
| `InquiryBill` | `billType: int32`، `billParameters: RecoveredMessage0152` | `bills: RecoveredMessage0149[]`، `customerName: string` | web 5.5.1 |
| `PayBill` | `bill: RecoveredMessage0149` | `paymentToken: string` | web 5.5.1 |
| `RenameSavedBill` | `id: int64`، `name: string` | — | web 5.5.1 |

## `bale.charnet.v1.CharnetService`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `BuyCharge` | `walletToken: bytes`، `phoneNumber: bytes`، `amount: int64`، `operatorType: int64`، `remaining: WebInt64Value_1`، `chargeType: int64`، `targetUserId: WebInt32Value`، `voucherId: WebInt32Value` | `paymentToken: WebOffset`، `receipt: WebReceipt` | bundled |
| `BuyInternetBundle` | `walletToken: bytes`، `phoneNumber: bytes`، `bundleId: int64`، `operatorType: int64`، `remaining: WebInt64Value_1`، `targetUserId: WebInt32Value` | `paymentToken: WebOffset`، `receipt: WebT_ei_76777` | bundled |
| `DeleteRecentChargeOrder` | `accessHash: bytes` | — | bundled |
| `DeleteRecentInternetBundleOrder` | `orderId: int64` | — | bundled |
| `GetAvailableCharges` | `operator: int64`، `chargeType: int64` | `amounts: int64[]`، `canBeOptional: int64` | bundled |
| `GetInternetBundleList` | `operatorType: int64`، `simCardType: int64` | `bundleLists: WebBundleList[]` | bundled |
| `GetInternetBundlePaymentToken` | `operatorType: int64`، `bundleId: int64`، `phoneNumber: bytes`، `targetUserId: WebInt32Value` | `token: bytes` | bundled |
| `GetRecentChargeOrders` | `count: int64`، `types: int64[]` | `orders: WebT_eo_76777[]` | bundled |
| `GetRecentInternetBundleOrders` | `count: int64` | `orders: WebT_en_76777[]` | bundled |
| `GetTopUpChargePaymentToken` | `providerCode: bytes`، `topupType: bytes`، `amount: int64`، `targetPhoneNumber: bytes`، `targetUserId: WebInt32Value` | `token: bytes` | bundled |
| `GetVoucherChargePaymentToken` | `providerCode: bytes`، `amount: int64`، `targetUserId: WebInt32Value` | `token: bytes` | bundled |

## `bale.crowdfunding.v1.CrowdFunding`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetParticipants` | `messageId: WebMsg`، `limit: int64`، `offset: int64` | `userPayments: WebUserPayment[]` | bundled |
| `GetTotalPaidAmount` | `messageId: WebMsg` | `totalPaidAmount: int64`، `creatorUserId: int64` | bundled |

## `bale.evex.v1.Evex`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetEvexCurrenciesList` | — | `currencies: RecoveredMessage0153[]`، `icmsWage: int32` | web 5.5.1 |
| `GetEvexCurrencyPrice` | `currencyType: int32`، `currencyAmount: int32`، `reason: int32`، `countryCode: int32`، `exitDate: string`، `nationalCode: string`، `deliveryStationType: int32`، `stationId: string`، `bankType: int32` | `currencyRate: int32`، `orderId: int32`، `amountToPay: int64`، `rialAmount: int64`، `melliWage: int64`، `iceWage: int64`، `otherWages: int64` | web 5.5.1 |
| `GetEvexPaymentToken` | `orderId: int32` | `token: string`، `paymentGatewayPrefix: string`، `terminalId: string` | web 5.5.1 |
| `GetListOfEvexDeliveryStations` | `deliveryStationType: int32`، `reason: int32`، `ExitDate: string`، `bankType: int32`، `shouldReturnCapacity: RecoveredMessage0064` | `stations: RecoveredMessage0154[]` | web 5.5.1 |
| `GetValidBanks` | `nationalCode: string`، `accountNationalCode: RecoveredMessage0065` | `banks: int32[]` | web 5.5.1 |
| `LoadEvexHistory` | — | `orders: RecoveredMessage0157[]`، `approvalText: string` | web 5.5.1 |
| `VerifyUserEvexAuthority` | `firstName: string`، `lastName: string`، `nationalCode: string`، `passportCode: string`، `postalCode: string`، `birthDate: string`، `fatherName: string`، `shId: string`، `bankType: int32` | `approval: RecoveredMessage0155` | web 5.5.1 |
| `VerifyUserEvexExtraInfo` | `nakhodaInfo: RecoveredMessage0156` | — | web 5.5.1 |

## `bale.exchange.v1.Exchange`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetCurrenciesList` | — | `currencies: RecoveredMessage0167[]`، `icmsWage: int32` | web 5.5.1 |
| `GetCurrencyPrice` | `currencyType: int32`، `currencyAmount: int32`، `reason: int32`، `countryCode: int32`، `exitDate: string`، `nationalCode: string`، `deliveryStationType: int32`، `stationId: string` | `currencyRate: int32`، `orderId: int32`، `amountToPay: int64`، `rialAmount: int64`، `melliWage: int64`، `iceWage: int64`، `otherWages: int64` | web 5.5.1 |
| `GetExchangeOrderInfo` | `orderId: int32` | `orderStatus: int32` | web 5.5.1 |
| `GetExchangePaymentToken` | `orderId: int32`، `callBack: string` | `token: string` | web 5.5.1 |
| `GetInitialConfig` | `origin: string` | — | web 5.5.1 |
| `GetListOfDeliveryStations` | `deliveryStationType: int32`، `reason: int32`، `ExitDate: string` | `stations: RecoveredMessage0168[]` | web 5.5.1 |
| `GetTravelCurrencyOrderInDetail` | `phoneNumber: string`، `nationalCode: string`، `userId: int32` | `orders: RecoveredMessage0179[]` | web 5.5.1 |
| `GetUserIcmsInfo` | `nationalCode: string`، `birthDate: string` | `firstName: string`، `lastName: string`، `nationalCode: string`، `passportCode: string`، `postalCode: string`، `birthDate: string`، `fatherName: string`، `shId: string`، `IsValid: bool` | web 5.5.1 |
| `LoadExchangeHistory` | — | `orders: RecoveredMessage0166[]`، `approvalText: string` | web 5.5.1 |
| `VerifyUserExchangeAuthority` | `firstName: string`، `lastName: string`، `nationalCode: string`، `passportCode: string`، `postalCode: string`، `birthDate: string`، `fatherName: string`، `shId: string`، `isValid: bool` | — | web 5.5.1 |

## `bale.falake.v1.Falake`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetLinkStatus` | `link: string` | `linkStatus: enum` | bundled |

## `bale.fanoos.v1.fanoos`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `Send` | `eventName: string`، `items: WebExtFanoosItems`، `date: int64` | — | bundled |
| `SendBatch` | `events: WebFanoosEvent[]` | — | bundled |

## `bale.feedback.v1.FeedBack`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `SendFeedBack` | `rate: int32`، `title: string`، `description: string`، `details: DetailsEntry[]`، `mtDetails: WebExtFeedBackMtDetails` | — | bundled |

## `bale.garson.v1.Garson`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `EditCustomServices` | — | `customItems: WebCustomItems` | bundled |
| `GetAdvertisementBot` | — | `bots: WebBots[]` | bundled |
| `GetBotBanners` | — | `banners: WebBanner[]` | bundled |
| `GetBotsByCategory` | `categoryId: int64`، `pagination: WebT_n8_51787` | `bots: WebCategorizedBot` | bundled |
| `GetCategorizedBots` | — | `categorizedBots: WebCategorizedBot[]` | bundled |
| `GetCustomServices` | — | `customItems: WebCustomItems` | bundled |
| `GetRecommendedBots` | `botId: int64`، `pagination: WebT_n8_51787` | `bots: WebBots[]`، `moreBotsUrl: WebStringValue` | bundled |
| `GetServices` | `version: int64` | `version: int64`، `isChanged: int64`، `data: bytes`، `banners: WebBanner[]`، `services: WebServices`، `sections: WebSection[]` | bundled |
| `GetTrendBots` | — | `bots: WebBots[]` | bundled |
| `GetUserRepeatedBots` | — | `bots: WebBots[]` | bundled |
| `SearchServices` | `query: RecoveredMessage0065`، `language: RecoveredMessage0065`، `source: int32` | `sections: RecoveredMessage0108[]` | web 5.5.1 |

## `bale.ghasedak.v1.GhasedakService`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetDiff` | `states: WebState[]`، `optimizations: int64[]` | `updates: WebT_tW_88717[]`، `usersRefs: WebUserPeer[]`، `groupsRefs: WebGroupPeer[]` | bundled |
| `GetRoutesStates` | `groupPeers: WebGroupPeer[]`، `optimizations: int64[]` | `seqs: WebState[]` | bundled |

## `bale.giftpacket.v1.GiftPacket`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetGiftPacketPaymentToken` | `token: bytes`، `amount: int64`، `peer: WebPeer`، `message: WebGiftPacketMessage` | `paymentToken: bytes` | bundled |
| `OpenGiftPacket` | `msgIdentifier: WebMsg`، `receiverWalletId: bytes`، `pageNo: WebInt32Value`، `orderType: int64` | `giftReceivers: WebGiftReceiver[]`، `status: int64`، `openedCount: int64`، `selfWinAmount: WebInt64Value_1`، `rank: WebInt32Value`، `userOutPeers: WebUserPeer[]` | bundled |
| `SendGiftPacketWithWallet` | `peer: WebPeer`، `randomId: int64`، `message: WebGiftPacketMessage`، `sourceWalletId: bytes` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |

## `bale.groups.v1.Groups`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddDiscussionGroupAdmin` | `channel: WebGroupPeer`، `discussionGroup: WebGroupPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `CreateGroup` | `rid: int64`، `title: string`، `users: WebUserPeer[]`، `groupType: int32`، `optimizations: int32[]`، `nick: WebStringValue`، `restriction: int32` | `seq: int32`، `state: bytes`، `group: WebGroup`، `users: WebUser[]`، `userPeers: WebUserPeer[]`، `notAddedUserPeers: WebUserPeer[]`، `inviteLink: string` | bundled |
| `EditChannelNick` | `groupPeer: WebGroupPeer`، `nick: string`، `randomId: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `EditGroupAbout` | `groupPeer: WebGroupPeer`، `rid: int64`، `about: WebStringValue`، `optimizations: int32[]` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `EditGroupAvatar` | `groupPeer: WebGroupPeer`، `fileLocation: WebFileLocation`، `rid: int64`، `optimizations: int32[]` | `avatar: WebAvatar`، `seq: int32`، `state: bytes`، `date: int64` | bundled |
| `EditGroupDefaultCardNumber` | `groupPeer: WebGroupPeer`، `cardNumber: string` | — | bundled |
| `EditGroupTitle` | `groupPeer: WebGroupPeer`، `title: string`، `rid: int64`، `optimizations: int32[]` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `FetchGroupAdmins` | `groupOutPeer: WebGroupPeer` | `users: WebUserPeer[]`، `admins: WebMember[]` | bundled |
| `GetBannedUsers` | `group: WebGroupPeer` | `bannedUsers: WebBannedUser[]` | bundled |
| `GetCanSeeMessages` | `groupPeer: WebGroupPeer`، `userId: int32` | `canSeeMessages: bool` | bundled |
| `GetFullGroup` | `peer: WebGroupPeer` | `fullGroup: WebFullGroup` | bundled |
| `GetGroupDefaultCardNumber` | `groupPeerr: WebGroupPeer` | `defaultCardNumber: string` | bundled |
| `GetGroupInviteURL` | `groupPeer: WebGroupPeer` | `url: string` | bundled |
| `GetGroupMembersCount` | `group: WebGroupPeer` | `membersCount: int32` | bundled |
| `GetGroupPreview` | `token: string`، `isOpenedOutsideBale: WebBoolValue_2` | `group: WebFullGroup`، `action: int32` | bundled |
| `GetGroupRecommendations` | `source: int32` | `groups: WebGroupPeer[]` | bundled |
| `GetMemberPermissions` | `group: WebGroupPeer`، `user: WebUserPeer` | `permissions: WebPermissions` | bundled |
| `GetMutualGroups` | `peer: WebUserPeer` | `groups: WebGroupPeer[]` | bundled |
| `GetMyGroups` | `mode: int32`، `isOwner: bool`، `filters: WebFilter[]` | `groups: WebGroupPeer[]` | bundled |
| `GetPins` | `groupPeer: WebGroupPeer`، `page: int32`، `limit: int32` | `pins: WebHistory[]`، `count: int32` | bundled |
| `InviteUser` | `groupPeer: WebGroupPeer`، `user: WebUserPeer`، `rid: int64`، `optimizations: int32[]`، `messageCount: WebInt32Value` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `InviteUsers` | `groupPeer: WebGroupPeer`، `rid: int64`، `users: WebUserPeer[]` | `notAddedUserPeers: WebUserPeer[]` | bundled |
| `JoinGroup` | `token: string`، `optimizations: int32[]` | `group: WebGroup`، `seq: int32`، `state: bytes`، `date: int64`، `users: WebUser[]`، `rid: int64`، `userPeers: WebUserPeer[]`، `inviterUserId: int32`، `groupSeq: int32` | bundled |
| `JoinPublicGroup` | `peer: WebBot`، `optimizations: int32[]` | `group: WebGroup`، `seq: int32`، `state: bytes`، `date: int64`، `users: WebUser[]`، `rid: int64`، `userPeers: WebUserPeer[]`، `inviterUserId: int32`، `groupSeq: int32` | bundled |
| `KickUser` | `groupPeer: WebGroupPeer`، `user: WebUserPeer`، `rid: int64`، `optimizations: int32[]` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `LeaveGroup` | `groupPeer: WebGroupPeer`، `rid: int64`، `optimizations: int32[]`، `makeOrphan: WebBoolValue_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `LoadFullGroups` | `groups: WebGroupPeer[]` | `groups: WebT_hI[]` | bundled |
| `LoadGroupAvatars` | `peer: WebGroupPeer` | `avatars: WebAvatars` | bundled |
| `LoadGroups` | `peers: WebGroupPeer[]` | `groups: WebGroup[]` | bundled |
| `LoadMembers` | `group: WebGroupPeer`، `limit: int32`، `next: WebBytesValue`، `condition: WebCondition` | `members: WebMember[]`، `next: WebBytesValue` | bundled |
| `MakeUserAdmin` | `groupPeer: WebGroupPeer`، `userPeer: WebUserPeer`، `adminTitle: WebStringValue` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `PinMessage` | `senderUserId: int32`، `groupPeer: WebGroupPeer`، `date: int64`، `msgRid: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `RemoveDiscussionGroup` | `rid: int64`، `channel: WebGroupPeer` | — | bundled |
| `RemoveGroupAvatar` | `groupPeer: WebGroupPeer`، `rid: int64`، `optimizations: int32[]`، `avaterId: WebInt64Value_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `RemovePin` | `groupPeer: WebGroupPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `RemoveSinglePin` | `groupPeer: WebGroupPeer`، `msgRid: int64`، `msgDate: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `RemoveUserAdmin` | `groupPeer: WebGroupPeer`، `userPeer: WebUserPeer` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `RevokeInviteURL` | `groupPeer: WebGroupPeer` | `url: string` | bundled |
| `SetAvailableReactions` | `group: WebGroupPeer`، `codes: string[]` | — | bundled |
| `SetCanSeeHistory` | `groupPeer: WebGroupPeer`، `canSeeHistory: bool` | — | bundled |
| `SetCanSeeMessages` | `groupPeer: WebGroupPeer`، `userId: int32`، `canSeeMessages: bool` | — | bundled |
| `SetDiscussionGroup` | `rid: int64`، `channel: WebGroupPeer` | `discussionGroup: WebGroupPeer`، `group: WebGroup` | bundled |
| `SetGroupDefaultPermissions` | `group: WebGroupPeer`، `permissions: WebPermissions` | — | bundled |
| `SetMemberCustomTitle` | `groupId: int32`، `memberId: int32`، `title: string` | — | bundled |
| `SetMemberPermissions` | `group: WebGroupPeer`، `user: WebUserPeer`، `permissions: WebPermissions` | — | bundled |
| `SetRestriction` | `groupOutPeer: WebGroupPeer`، `restriction: int32`، `nick: WebStringValue` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `SetSignMessages` | `groupPeer: RecoveredMessage0086`، `signMessages: bool` | — | web 5.5.1 |
| `SetSlowMode` | `group: RecoveredMessage0086`، `seconds: RecoveredMessage0063` | — | web 5.5.1 |
| `TransferOwnership` | `groupPeer: WebGroupPeer`، `newOwner: int32` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `UnBanUser` | `groupPeer: WebGroupPeer`، `user: WebUserPeer`، `optimizations: int32[]` | — | bundled |

## `bale.ketf.v1.Ketf`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetBotGroupPermissions` | `botUserId: int32`، `groupId: int32` | `hasAccessToMessages: bool` | bundled |
| `GetBotInfo` | `botUserId: int32` | `botInfo: WebBotInfo` | bundled |
| `GetBotWhiteList` | `botUserId: int32` | `list: WebList` | bundled |
| `GetBots` | `pagination: WebT_jq` | `pageCount: int32`، `bots: WebT_cC[]` | bundled |
| `GetInlineBotResults` | `query: string`، `peer: WebPeer`، `botUserId: int32`، `offset: string` | `results: WebT_L[]`، `nextOffset: WebOffset`، `queryId: WebInt64Value_1`، `isGallery: bool` | bundled |
| `GetPaymentDetails` | `purchaseMessageId: WebMsg`، `invoiceIdentifier: WebInvoiceIdentifier` | `title: string`، `totalAmount: int64`، `paymentsHistory: WebPaymentsHistory[]`، `session: WebSession`، `disapproved: WebDisapproved`، `description: string`، `labeledPrices: WebLabeledPrice[]` | bundled |
| `GetUserContext` | `botUserId: int32` | `botUserId: int32`، `userId: int32`، `nonce: string`، `sign: string` | bundled |
| `GetWebappHash` | `botUserId: int32`، `data: string` | `hash: string`، `queryId: string`، `authDate: int64` | bundled |
| `InvokeCustomAction` | `id: string`، `messageId: WebMessageId`، `peer: WebOutPeer`، `openDialogAction: WebOpenDialogAction`، `done: WebDone` | — | bundled |
| `MakePayment` | `paymentSessionId: string`، `paymentOptionId: string`، `wallet: WebT_yS`، `gateway: WebGateway` | `gatewayRedirect: WebGatewayRedirect`، `paymentReceipt: WebPaymentsHistory` | bundled |
| `SendAuthenticatedInlineCallBackData` | `templateMessageId: WebMsg`، `data: WebStringValue` | — | bundled |
| `SendInlineCallBackData` | `historyMessageIdentifier: WebMsg`، `data: WebStringValue` | — | bundled |
| `SendInlineCallback` | `peer: WebExPeer`، `messageId: WebMessageId`، `data: WebStringValue` | `answer: WebAnswer` | bundled |
| `SendMiniAppData` | `botUserId: int32`، `queryId: WebStringValue`، `data: WebStringValue`، `buttonText: WebStringValue` | — | bundled |

## `bale.kifpool.v1.Kifpool`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CashOut` | `requestId: bytes`، `token: bytes`، `amount: int64`، `account: WebStringValue`، `pan: WebStringValue` | `referenceNo: int64` | bundled |
| `Charge` | `paymentToken: bytes`، `referenceNo: int64` | — | bundled |
| `CheckChargePermission` | `paymentToken: bytes` | — | bundled |
| `CreateKifpool` | `nationalId: WebStringValue` | — | bundled |
| `CryptoCashOut` | `requestId: bytes`، `amount: int64`، `account: WebStringValue`، `pan: WebStringValue`، `pocketType: int64`، `isMerchant: WebBoolValue_1` | `referenceNo: int64` | bundled |
| `CryptoInvoice` | `token: bytes`، `pageSize: int64`، `pageNumber: int64` | `records: WebRecord[]` | bundled |
| `CryptoPurchase` | `amount: int64`، `srcToken: bytes`، `dstToken: bytes`، `description: bytes`، `terminalId: bytes`، `bornaTrxId: bytes` | — | bundled |
| `CryptoRefund` | `token: bytes`، `amount: int64`، `approvalCode: int64`، `trxRefSrc: bytes` | — | bundled |
| `CryptoTransfer` | `amount: int64`، `srcToken: bytes`، `dstToken: bytes`، `description: WebStringValue`، `dstPhoneNo: WebStringValue` | `amount: int64`، `date: int64`، `approvalCode: int64`، `srcToken: bytes`، `dstToken: bytes` | bundled |
| `FeeInquiry` | `amount: int64`، `transactionType: RecoveredMessage0063`، `pocketType: int32` | `amount: int64`، `fee: int64`، `responseData: RecoveredMessage0065` | web 5.5.1 |
| `GetChargePaymentToken` | `token: bytes`، `amount: int64`، `callbackType: int64` | `paymentToken: bytes` | bundled |
| `GetCredit` | — | `balance: WebInt64Value_1`، `hasCredit: int64` | bundled |
| `GetCryptoChargePaymentToken` | `token: bytes`، `amount: int64`، `receiverId: bytes` | `paymentToken: bytes` | bundled |
| `GetCryptoWallets` | — | `myCryptoWallets: WebCryptoPocket[]` | bundled |
| `GetKifpoolOwner` | `walletToken: bytes` | `firstName: WebStringValue`، `lastName: WebStringValue`، `walletStatus: int64`، `approvalCode: int64` | bundled |
| `GetKifpoolPointBalance` | `token: bytes` | `pointBalanceInfo: WebPointBalanceInfo[]` | bundled |
| `GetKifpoolPointDetails` | `token: bytes`، `count: int64`، `page: int64` | `pointDetailsInfo: WebPointDetailsInfo[]` | bundled |
| `GetKifpoolPointSummery` | `token: bytes` | `pointSummeryInfo: WebPointSummeryInfo[]` | bundled |
| `GetKifpoolTransactionPoint` | `transactionID: int64`، `amount: int64` | `calculatedPoint: int64`، `point: int64`، `unitAmount: int64` | bundled |
| `GetMyKifpools` | `invocationSpot: WebStringValue`، `pocketType: int64` | `myWallets: WebMyWallet[]`، `firstName: WebStringValue`، `lastName: WebStringValue` | bundled |
| `Invoice` | `token: bytes`، `pageSize: int64`، `pageNumber: int64` | `records: WebRecord[]` | bundled |
| `PayForMessage` | `amount: int64`، `chargeAmount: int64`، `message: WebMsg` | `status: int64`، `paymentToken: WebOffset` | bundled |
| `Purchase` | `amount: int64`، `dstToken: bytes`، `srcToken: bytes`، `description: bytes`، `useCredit: WebBoolValue_2`، `couponId: WebInt32Value`، `terminalNo: WebStringValue`، `stan: WebInt64Value` | — | bundled |
| `PurchaseMessage` | `historyId: WebMsg`، `amount: WebInt64Value_1`، `description: WebStringValue` | — | bundled |
| `PurchaseMessageWithCharge` | `historyId: WebMsg`، `amount: WebInt64Value_1`، `description: WebStringValue`، `chargeAmount: int64` | `paymentToken: bytes` | bundled |
| `PurchaseWithCharge` | `amount: int64`، `dstToken: bytes`، `srcToken: bytes`، `description: bytes`، `chargeAmount: int64`، `useCredit: WebBoolValue_2`، `couponId: WebInt32Value`، `terminalNo: WebStringValue`، `stan: WebInt64Value` | `paymentToken: bytes` | bundled |
| `Transfer` | `sourceToken: bytes`، `destinationToken: WebStringValue`، `destinationPhone: WebStringValue`، `destinationUserid: WebInt32Value`، `amount: int64`، `description: WebStringValue` | — | bundled |
| `UpgradeKifpool` | `token: bytes`، `nationalId: WebStringValue`، `cardNo: WebStringValue`، `accountNo: WebStringValue`، `remainReferenceNumber: bytes` | `level: int64` | bundled |
| `VerifyCashOutKifpool` | `token: bytes` | `accountNo: bytes`، `firstName: WebStringValue`، `lastName: WebStringValue` | bundled |
| `VerifyPurchaseMessage` | `historyId: WebMsg` | `amount: WebInt64Value_1`، `paymentTypeTitle: WebStringValue`، `paymentTitle: WebStringValue` | bundled |

## `bale.llm_auth.v1.LLMAuthService`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetAuthToken` | — | `token: string`، `url: string`، `expiresIn: int64` | bundled |

## `bale.magazine.v1.Magazine`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetMessageUpvoters` | `loadMoreState: WebBytesValue`، `message: WebMsg` | `loadMoreState: WebBytesValue`، `users: WebUserPeer[]` | bundled |
| `GetMyUpvotes` | — | `upvotes: WebUpvotes` | bundled |
| `GetSimilarPosts` | `message: WebMsg`، `loadMoreState: WebBytesValue` | `messages: WebT_A_54329[]`، `loadMoreState: WebBytesValue`، `similarPosts: WebSimilarPost[]` | bundled |
| `LoadCategories` | — | `categories: WebT_L_54329[]` | bundled |
| `LoadCategoryFeedMessages` | `categoryId: int64`، `loadMoreState: WebBytesValue` | `loadMoreState: WebBytesValue`، `messages: WebT_A_54329[]` | bundled |
| `LoadFeedMessages` | `loadMoreState: WebBytesValue` | `loadMoreState: WebBytesValue`، `messages: WebT_A_54329[]` | bundled |
| `LoadInternalFeedMessages` | `loadMoreState: WebBytesValue` | `loadMoreState: WebBytesValue`، `messages: WebT_A_54329[]` | bundled |
| `RevokeUpvotedPost` | `message: WebMsg`، `albumId: WebInt64Value_1` | `upvotes: WebUpvotes` | bundled |
| `UpvotePost` | `message: WebMsg`، `albumId: WebInt64Value_1` | `upvotes: WebUpvotes` | bundled |

## `bale.market.v1.Market`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AcceptCampaignMarket` | `marketId: int64`، `isPermanent: int64` | — | bundled |
| `AcceptMarketJoinRequest` | `marketPeerId: int64`، `requestId: int64`، `displayName: bytes`، `categoryId: int64` | — | bundled |
| `CreateMarketJoinRequest` | `marketPeerId: int64`، `displayName: bytes`، `categoryId: int64`، `tagIds: int64[]` | — | bundled |
| `CreateTag` | `title: bytes`، `categoryId: int64` | `tag: WebT_iR_88717` | bundled |
| `GetCategoriesList` | `categoryId: int64`، `level: WebInt32Value_1`، `includeSampleMarkets: WebBoolValue_2`، `version: WebInt32Value_1` | `categories: WebT_iE_88717[]`، `version: WebInt32Value_1` | bundled |
| `GetCategoryMarkets` | `categoryId: int64`، `pagination: WebPagination`، `version: int64` | `markets: WebMarketType[]`، `version: int64` | bundled |
| `GetCategoryProducts` | `categoryId: int64`، `pagination: WebPagination`، `version: int64` | `products: WebProduct[]`، `version: int64` | bundled |
| `GetIndexedProducts` | `startDate: int64`، `endDate: int64`، `categoryId: int64` | `products: WebProduct[]` | bundled |
| `GetMarket` | `peerId: int64`، `nickName: bytes` | `market: WebT_iS_88717`، `lastRequest: WebRequest` | bundled |
| `GetMarketJoinRequests` | — | `marketJoinRequests: WebRequest[]` | bundled |
| `GetMarketsPendingJoinRequest` | — | `requests: WebRequest[]` | bundled |
| `GetNumberOfSales` | `peer: WebPeer` | `numberOfSales: int64`، `isMarket: int64` | bundled |
| `GetOnboardingStatus` | — | `status: int64`، `categoryIds: int64[]`، `gender: int64` | bundled |
| `GetPendingCampaignMarkets` | — | `markets: WebT_iS_88717[]` | bundled |
| `GetStores` | `version: int64` | `stores: bytes`، `version: int64` | bundled |
| `GetTags` | `categoryId: int64` | `tags: WebT_iR_88717[]` | bundled |
| `GetTopMarkets` | `ratingType: int64`، `pagination: WebPagination` | `markets: WebMarketType[]` | bundled |
| `GetYaldaStores` | `version: int64` | `stores: bytes`، `version: int64` | bundled |
| `RejectCampaignMarket` | `marketId: int64`، `isPermanent: int64` | — | bundled |
| `RejectMarketJoinRequest` | `marketPeerId: int64`، `rejectCause: int64`، `requestId: int64` | — | bundled |
| `SetGenericDeepLinks` | `links: WebLink[]` | — | bundled |
| `SetMarketBanners` | `banners: WebT_ib_88717[]` | — | bundled |
| `SetOnboardingData` | `categoryIds: int64[]`، `gender: int64`، `isSkipped: WebBoolValue_1` | — | bundled |
| `SetPopularSearches` | `items: WebT_i__88717[]` | — | bundled |
| `SubmitMarketFeedback` | `rate: int64`، `userOpinion: WebOffset`، `clientVersion: WebOffset`، `extraFields: ExtraFieldsEntry[]` | — | bundled |
| `UpdateMarketInfo` | `peerId: int64`، `displayName: WebStringValue`، `primaryCategoryId: WebInt32Value`، `isBanned: WebBoolValue_1`، `isActive: WebBoolValue_1` | — | bundled |

## `bale.maviz.v1.MavizStream`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetDifference` | `routeSequences: WebRouteSequence[]`، `optimizations: int64[]` | `groupEvents: GroupEventsEntry[]`، `usersRefs: WebUserPeer[]`، `groupsRefs: WebGroupPeer[]` | bundled |
| `SubscribeToThreadUpdates` | `peer: WebExPeer`، `threadId: WebMessageId` | — | bundled |
| `SubscribeToUpdates` | `isMtProto: int64` | `update: WebUpdate`، `routeId: int64`، `sequence: int64`، `timestamp: int64`، `weakEvent: WebWeakEvent`، `mtupdate: WebMtupdate`، `updates: WebUpdates` | bundled |
| `UnsubscribeFromThreadUpdates` | `peer: WebExPeer`، `threadId: WebMessageId` | — | bundled |

## `bale.meet.v1.Meet`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AcceptCall` | `callId: int64`، `inviteEnable: WebBoolValue_2` | `call: WebCall`، `participants: WebPeer[]`، `seq: int32`، `sipCall: WebT_HS`، `isStream: WebBoolValue_2` | bundled |
| `AnswerCallJoinRequest` | `callId: int64`، `requesterIdentifier: string`، `isAllowed: bool` | — | bundled |
| `AskToJoinCall` | `callId: int64`، `name: string` | — | bundled |
| `DeleteCallLogs` | `callIds: WebInt64Value_1[]`، `all: bool`، `invert: bool` | — | bundled |
| `DeleteStream` | `streamUser: WebExPeer` | — | bundled |
| `DiscardCall` | `callId: int64`، `duration: int32`، `reason: int32`، `type: int32` | `call: WebCall`، `participants: WebPeer[]`، `seq: int32`، `sipCall: WebT_HS`، `isStream: WebBoolValue_2` | bundled |
| `GenerateCallLink` | `isPublic: bool`، `callId: WebInt64Value_1`، `title: WebOffset` | `groupCall: WebGroupCall`، `linkExpirationPeriod: int64` | bundled |
| `GetCallLinkDetails` | `session: string` | `groupCall: WebGroupCall` | bundled |
| `GetCallLogs` | `pageNumber: WebInt64Value_1`، `pageSize: WebInt64Value_1`، `afterDate: WebInt64Value_1`، `beforeDate: WebInt64Value_1` | `callLogs: WebCallLog[]`، `total: int32` | bundled |
| `GetCallState` | `callId: int64` | `groupCall: WebGroupCall` | bundled |
| `GetGroupCall` | `peer: WebOutPeer` | `groupCall: WebGroupCall` | bundled |
| `GetOngoingCalls` | `pageNumber: WebInt64Value_1`، `pageSize: WebInt64Value_1` | `callLogs: WebCallLog[]` | bundled |
| `GetWssURL` | `callId: int64` | `url: string` | bundled |
| `InviteToCall` | `callId: int64`، `invitees: WebOutPeer[]` | `peerStates: WebPeerState[]` | bundled |
| `JoinGroupCall` | `callId: int64`، `name: WebOffset` | `groupCall: WebGroupCall`، `states: WebPeerState[]` | bundled |
| `LeaveGroupCall` | `callId: int64`، `end: bool` | `groupCall: WebGroupCall`، `seq: int32` | bundled |
| `MuteParticipant` | `callId: int64`، `identity: string`، `trackId: string`، `revokePublishPermission: bool` | — | bundled |
| `ReceiveCall` | `callId: int64` | — | bundled |
| `RemoveParticipant` | `callId: int64`، `identity: string`، `blockFromCall: bool` | — | bundled |
| `SendCallReaction` | `callId: int64`، `reaction: string` | — | bundled |
| `SendFanoosEvent` | `eventName: string`، `items: WebExt`، `date: int64` | — | bundled |
| `SetLinkTitle` | `title: string`، `callId: WebInt64Value_1`، `linkUrl: WebOffset` | — | bundled |
| `StartCall` | `peer: WebPeer`، `rid: int64`، `video: bool`، `internalCall: WebInternalCall`، `sipCall: WebSipCall`، `liveKitCall: WebLiveKitCall` | `call: WebCall`، `participants: WebPeer[]`، `seq: int32`، `sipCall: WebT_HS`، `isStream: WebBoolValue_2` | bundled |
| `StartGroupCall` | `peer: WebOutPeer`، `randomId: int64`، `video: bool`، `mode: int32`، `invitees: WebOutPeer[]` | `groupCall: WebGroupCall`، `seq: int32` | bundled |
| `StartRecording` | `callId: int64`، `layout: string`، `quality: int32` | — | bundled |
| `StartStream` | `streamUser: WebExPeer`، `url: string`، `rtmpServer: string` | `streamKey: string` | bundled |
| `StopRecording` | `callId: int64` | — | bundled |
| `SubmitCallFeedback` | `callId: int64`، `rate: int32`، `userOpinion: WebOffset`، `client: int32`، `clientVersion: WebOffset`، `extraFields: ExtraFieldsEntry[]`، `isStream: WebBoolValue_2` | — | bundled |
| `TakeCallAction` | `callId: int64`، `lowerHand: WebLowerHand`، `raiseHand: WebRaiseHand` | — | bundled |
| `UpdateLayout` | `callId: int64`، `requestedLayout: string` | — | bundled |

## `bale.message_stream.v1.MessageStream`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CancelMessageStream` | `exPeer: WebExPeer`، `messageId: WebMessageId` | — | bundled |
| `ReceiveMessageStream` | `exPeer: WebExPeer`، `messageId: WebMessageId`، `fromChunkId: WebInt32Value` | `chunkTimeoutMillis: WebInt32Value` | bundled |

## `bale.messaging.v2.Messaging`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ArchiveDialogs` | `exPeers: WebExPeer[]` | — | bundled |
| `ClearChat` | `peer: WebPeer` | `seq: int32`، `state: bytes` | bundled |
| `CreateFolder` | `name: string`، `peers: WebExPeer[]` | `folderId: int32`، `index: int32`، `unreadPeers: WebExPeer[]` | bundled |
| `CreateReservedFolder` | `folderId: int32` | `index: int32`، `unreadPeers: WebExPeer[]` | bundled |
| `CreateThread` | `peer: WebOutPeer`، `date: int64`، `randomId: int64`، `title: string` | `threadId: int32` | bundled |
| `CreateTopic` | `exPeer: WebExPeer`، `title: string` | `topicId: WebMessageId` | bundled |
| `DeleteChat` | `peer: WebPeer` | `seq: int32`، `state: bytes` | bundled |
| `DeleteFolder` | `folderId: int32` | — | bundled |
| `DeleteMessage` | `peer: WebPeer`، `rids: int64[]`، `dates: WebT_LWL`، `justMine: WebBoolValue_1` | `seq: int32`، `state: bytes` | bundled |
| `DeleteTopic` | `exPeer: WebExPeer`، `topicId: WebMessageId` | — | bundled |
| `EditFolder` | `folderId: int32`، `name: string`، `addedPeers: WebExPeer[]`، `deletedPeers: WebExPeer[]` | `unreadPeers: WebExPeer[]` | bundled |
| `EditTopic` | `exPeer: WebExPeer`، `topicId: WebMessageId`، `title: string` | — | bundled |
| `FetchProtectedMessage` | `peer: WebOutPeer`، `messageId: WebMessageId` | `history: WebHistory` | bundled |
| `ForwardMessages` | `peer: WebOutPeer`، `rid: int64[]`، `forwardedMessages: WebQuotedMessageReference[]`، `groupedId: WebInt64Value_1` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `GetDiscussionMessage` | `peer: WebExPeer`، `messageId: WebMessageId` | `discussionMessage: WebHistory` | bundled |
| `GetMessagesRepliesInfo` | `peer: WebExPeer`، `mids: WebMessageId[]` | `containers: WebT_yze[]` | bundled |
| `GetTopicByID` | `exPeer: WebExPeer`، `topicId: WebMessageId` | `topic: WebTopic` | bundled |
| `GetTopics` | `exPeer: WebExPeer`، `minDate: int64`، `limit: int32` | `topics: WebTopic[]` | bundled |
| `LoadDialogs` | `minDate: int64`، `limit: int32`، `optimizations: int32[]`، `dialogType: int32`، `excludePinnedDialogs: bool`، `archiveFilter: int32` | `groups: WebGroup[]`، `users: WebUser[]`، `dialogs: WebDialog[]`، `userPeers: WebUserPeer[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `LoadFolderDialogs` | `minDate: int64`، `limit: int32`، `folderId: int32`، `archiveFilter: int32` | `dialogs: WebDialog[]` | bundled |
| `LoadFolders` | `includeMutedUnreadPeers: bool`، `isNewUser: bool` | `folders: WebFolder[]`، `unreadPeers: WebUnreadPeer[]` | bundled |
| `LoadGroupedDialogs` | `optimizations: int32[]`، `archiveFilter: int32` | `dialogs: WebT_wpU[]`، `users: WebUser[]`، `groups: WebGroup[]`، `showArchived: WebBoolValue_1`، `showInvite: WebBoolValue_1`، `userPeers: WebUserPeer[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `LoadHistory` | `peer: WebPeer`، `date: int64`، `loadMode: int32`، `limit: int32`، `optimizations: int32[]` | `history: WebHistory[]`، `users: WebUser[]`، `userPeers: WebUserPeer[]`، `groups: WebGroup[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `LoadPeerDialogs` | `peers: WebPeer[]` | `dialogs: WebDialog[]`، `groups: WebGroup[]`، `users: WebUser[]`، `userPeers: WebUserPeer[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `LoadPeers` | — | `exPeers: WebExPeer[]` | bundled |
| `LoadPinnedDialogs` | `folderId: int32` | `dialogs: WebDialog[]` | bundled |
| `LoadPinnedMessages` | `peer: WebExPeer` | `pinnedMessages: WebHistory[]` | bundled |
| `LoadReplies` | `peer: WebExPeer`، `threadId: WebMessageId`، `date: int64`، `loadMode: int32`، `limit: int32` | `history: WebHistory[]`، `users: WebUser[]`، `userPeers: WebUserPeer[]` | bundled |
| `MarkDialogsAsRead` | `peers: WebExPeer[]` | `seq: int32`، `state: bytes` | bundled |
| `MarkDialogsAsUnread` | `peers: WebExPeer[]` | `seq: int32`، `state: bytes` | bundled |
| `MentionRead` | `peer: WebExPeer`، `messageId: WebMessageId` | — | bundled |
| `MessageRead` | `peer: WebPeer`، `date: int64`، `exPeer: WebExPeer` | — | bundled |
| `MessageReceived` | `peer: WebPeer`، `date: int64` | — | bundled |
| `PinDialogs` | `peers: WebExPeer[]`، `folderId: int32` | `dialogs: WebDialog[]`، `peers: WebExPeer[]` | bundled |
| `PinMessage` | `peer: WebExPeer`، `messageId: WebMessageId`، `justMine: bool` | — | bundled |
| `ReorderFolders` | — | — | bundled |
| `ReorderPinnedDialogs` | `peers: WebExPeer[]`، `folderId: int32` | `dialogs: WebDialog[]`، `peers: WebExPeer[]` | bundled |
| `SendMessage` | `peer: WebPeer`، `rid: int64`، `message: WebMessage`، `isOnlyForUser: WebInt32Value`، `quotedMessageReference: WebQuotedMessageReference`، `exPeer: WebOutPeer`، `isSilent: bool`، `threadId: WebMessageId` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `SendMultiMediaMessage` | `peer: WebOutPeer`، `multiMedia: WebMultiMedia[]`، `repliedMessage: WebQuotedMessageReference`، `groupedId: int64` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |
| `UnArchiveDialogs` | `exPeers: WebExPeer[]` | — | bundled |
| `UnPinMessages` | `peer: WebExPeer`، `messageIds: WebMessageId[]`، `all: bool` | — | bundled |
| `UnpinDialogs` | `peers: WebExPeer[]`، `folderId: int32` | — | bundled |
| `UpdateMessage` | `peer: WebPeer`، `rid: int64`، `updatedMessage: WebMessage` | `seq: int32`، `date: int64`، `state: bytes`، `ext: ExtEntry[]` | bundled |

## `bale.microbanki.v1.MicroBanki`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetBamServiceToken` | `service: int64` | `endpoint: bytes`، `token: bytes` | bundled |
| `GetMoneyRequestDetails` | `message: WebMsg` | `totalAmount: int64`، `payCount: int64`، `lastPayDate: int64`، `responseType: int64` | bundled |
| `GetMoneyRequestPaymentList` | `message: WebMsg`، `loadMoreState: WebBytesValue` | `payment: WebPayment[]`، `loadMoreState: WebBytesValue`، `responseType: int64`، `userPeers: WebUserPeer[]`، `groupPeers: WebGroupPeer[]` | bundled |

## `bale.my_bank.v1.MyBank`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetMyBank` | — | `data: string`، `version: int32`، `itemsVersion: int32`، `isChanged: bool` | bundled |

## `bale.negah.v1.Negah`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetMessageSeenList` | `peer: WebExtNegahPeer`، `messageId: WebExtNegahMessageId`، `page: int32`، `limit: int32` | `usersSeen: WebExtNegahUserSeen[]`، `count: int32` | bundled |

## `bale.organizations.v1.Organizations`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetUserOrganizationInfo` | — | `userOrganization: WebUserOrganization` | bundled |
| `GetUserOrganizationalContacts` | — | `userPeers: WebUserPeer[]` | bundled |

## `bale.pfm.v1.Pfm`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddDetailToTransaction` | `id: WebId`، `detail: bytes` | — | bundled |
| `AddTransactionTags` | `id: WebId`، `tags: WebTags[]` | — | bundled |
| `AddUserTags` | `tags: WebTags[]` | — | bundled |
| `FilterTaggedTransactions` | `ids: WebId[]` | `idsWithTag: WebId[]` | bundled |
| `GetSubTransactions` | `transactionId: WebId` | `transactionIds: WebId[]` | bundled |
| `GetTransactionTags` | `id: WebId` | `tags: WebTags[]` | bundled |
| `GetUserAccounts` | — | `accounts: WebAccount[]`، `config: WebT_KW` | bundled |
| `GetUserTags` | `getUserTagType: int64` | `tags: WebTags[]` | bundled |
| `LoadTransactions` | `accountNumber: int64`، `startDate: WebInt64Value_1`، `endDate: WebInt64Value_1`، `transactionType: int64`، `label: WebTags[]`، `limit: int64`، `loadMoreState: WebOffset`، `loadMode: int64`، `userTagType: int64` | `transactions: WebTransaction[]`، `totalAmounts: WebTotalAmount[]`، `loadMoreState: WebOffset`، `totalAmountsPerDay: WebTotalAmountsPerDay[]` | bundled |
| `LoadTransactionsByIDs` | `transactionIds: WebId[]` | `transactions: WebTransaction[]` | bundled |
| `RemoveTransaction` | `transactionIds: WebId[]` | — | bundled |
| `RemoveTransactionTags` | `id: WebId`، `tags: WebTags[]` | — | bundled |
| `RemoveUserTags` | `tags: WebTags[]` | — | bundled |
| `ReviveTransaction` | `transactionId: WebId` | — | bundled |
| `SplitTransaction` | `transactionId: WebId`، `units: WebUnit[]` | `splitTransactionIds: WebId[]` | bundled |

## `bale.pishvaz.v1.Pishvaz`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetMarketingToolsConfig` | — | `inApp: RecoveredMessage0008`، `eventBar: RecoveredMessage0012`، `dialogListBanner: RecoveredMessage0003` | web 5.5.1 |
| `GetOnboardingPageData` | — | `title: string`، `sections: RecoveredMessage0021[]` | web 5.5.1 |
| `SetMarketingToolAction` | `id: int32`، `actionType: int32` | — | web 5.5.1 |

## `bale.poll.v1.Poll`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ClosePoll` | `pollId: int64` | — | bundled |
| `CreatePoll` | `pollMessage: WebPollMessage`، `createAt: int64`، `expeer: WebExPeer` | `pollId: int64` | bundled |
| `GetFullPollResult` | `pollId: int64` | `fullPollResult: WebFullPollResult[]` | bundled |
| `GetPollResults` | — | `pollResults: WebPollResult[]` | bundled |
| `Vote` | `pollId: int64`، `isRetract: int64`، `voteAt: int64`، `optionIds: int64[]` | `pollResult: WebPollResult` | bundled |

## `bale.premium.v1.Premium`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CalculateDiscountedPrice` | `packageId: int64`، `couponCode: string` | `discountedPrice: int64` | bundled |
| `GetBadges` | — | `categories: WebT__c[]` | bundled |
| `GetPackages` | — | `packages: WebPackage[]`، `bundles: BundlesEntry[]` | bundled |
| `IsPremium` | `userId: int32`، `withDetailOption: WebWithDetailOption` | `userStatus: WebUserStatus` | bundled |
| `IsPremiumBatch` | `userIds: int32[]`، `withDetailOption: WebWithDetailOption` | `usersStatus: WebUserStatus[]` | bundled |
| `PurchasePackage` | `packageId: int64`، `couponCode: WebStringValue` | `sadadPaymentToken: string` | bundled |
| `SetUserBadge` | `badgeId: int64` | — | bundled |

## `bale.presence.v1.Presence`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetContactsPresences` | `limit: WebInt32Value` | `presences: WebPresenceType[]` | bundled |
| `GetGroupMembersPresences` | `peer: WebGroupPeer` | `presences: WebPresenceType[]` | bundled |
| `GetGroupOnlineCount` | `peer: WebGroupPeer` | `count: int32` | bundled |
| `GetUsersPresence` | — | `presences: WebPresenceType[]` | bundled |
| `SetOnline` | `isOnline: bool`، `timeout: int64`، `deviceType: int32`، `deviceCategory: WebStringValue` | — | bundled |
| `StopTyping` | `peer: WebPeer`، `typingType: int32` | — | bundled |
| `SubscribeFromGroupOnline` | `groups: WebGroupPeer[]` | — | bundled |
| `SubscribeFromOnline` | `users: WebUserPeer[]` | — | bundled |
| `SubscribeToGroupOnline` | `groups: WebGroupPeer[]` | — | bundled |
| `SubscribeToOnline` | `users: WebUserPeer[]` | — | bundled |
| `Typing` | `peer: WebPeer`، `typingType: int32` | — | bundled |

## `bale.ramz.v1.Ramz`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `CheckPassword` | `password: string`، `servicesType: int32` | `token: string` | bundled |
| `CheckPasswordSet` | — | `hasSet: bool`، `isSessionAuthorized: bool` | bundled |
| `DeletePassword` | `otp: int32` | — | bundled |
| `ForgetPassword` | — | — | bundled |
| `SendOTP` | — | — | bundled |
| `SetPassword` | `password: string` | — | bundled |
| `ValidateOTP` | `otp: int32`، `servicesType: int32` | `otpValid: bool` | bundled |

## `bale.recommender.v1.Recommender`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetChannelRecommendations` | — | `channels: WebGroupPeer[]` | bundled |
| `GetGroupsRecommendation` | `source: int64` | `groups: WebGroupPeer[]` | bundled |
| `GetRelatedChannels` | `exPeer: WebExPeer` | `relatedChannels: WebRelatedChannel[]` | bundled |
| `GetRelatedGroups` | `exPeer: WebExPeer` | `relatedGroups: WebRelatedGroup[]` | bundled |

## `bale.report.v1.Report`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ReportDismiss` | `exPeer: WebExPeer` | — | bundled |
| `ReportInappropriateContent` | `report: WebReportType` | — | bundled |

## `bale.sap.v1.Sap`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddDestinationCards` | `cards: WebCard[]` | `ids: bytes[]` | bundled |
| `AddNewCards` | `cardInfo: WebCardInfo[]` | `cardId: bytes[]` | bundled |
| `DeliverOtp` | `cardId: bytes`، `destinationPan: bytes`، `amount: int64`، `accessAddress: bytes`، `approvalCode: bytes` | `isDone: WebBoolValue_2` | bundled |
| `EditCardExpirationDate` | `cardId: bytes`، `cardExpDate: WebCardExpDate` | — | bundled |
| `EnrollNewCard` | `origin: WebOffset` | `transactionId: bytes`، `url: bytes` | bundled |
| `GetCardInfo` | `transactionId: bytes`، `cardInfo: WebCardInfo`، `cardId: WebOffset` | `cardId: bytes`، `maskedPan: bytes` | bundled |
| `GetCards` | — | `userCards: WebUserCard[]` | bundled |
| `GetDefaultCard` | — | `cardId: WebOffset` | bundled |
| `GetDestinationCardInfo` | `cardId: bytes`، `destinationPan: bytes`، `amount: int64`، `sourceAddress: bytes`، `localize: int64`، `targetUserId: WebInt32Value_1`، `messageData: WebMsg` | `cardHolderName: bytes`، `approvalCode: bytes` | bundled |
| `GetDestinationCards` | — | `cards: WebCard[]` | bundled |
| `ReactivateApp` | — | `transactionId: bytes`، `reactivationAddress: bytes` | bundled |
| `RemoveCard` | `cardId: bytes` | — | bundled |
| `RemoveDefaultCard` | — | — | bundled |
| `RemoveDestinationCards` | `ids: bytes[]` | — | bundled |
| `SetDefaultCard` | `cardId: bytes` | — | bundled |
| `TransferMoneyByCard` | `cardId: bytes`، `transferCode: int64`، `destinationPan: bytes`، `amount: int64`، `pin: bytes`، `cvv2: bytes`، `expiryDate: bytes`، `sourceAddress: bytes`، `localize: int64`، `approvalCode: bytes`، `encryptedTransferInfo: WebOffset`، `messageData: WebMsg`، `targetUserId: WebInt32Value_1`، `description: WebOffset`، `ramzToken: WebOffset` | `traceNumber: bytes`، `transactionTime: bytes` | bundled |

## `bale.sarrafi.v1.Sarrafi`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AuthenticateUser` | `nationalCode: string`، `accountNumber: string` | — | web 5.5.1 |
| `CreateOrder` | `symbol: int32`، `side: int32`، `price: string`، `quantity: string` | — | web 5.5.1 |
| `GetChargeToken` | `currency: int32`، `amount: string` | `tokenUrl: string` | web 5.5.1 |
| `GetDepth` | `symbol: int32`، `limit: int32` | `marketDepth: RecoveredMessage0252` | web 5.5.1 |
| `GetOrder` | `orderId: string` | `order: RecoveredMessage0256`، `trades: RecoveredMessage0260[]` | web 5.5.1 |
| `GetOrders` | — | `orders: RecoveredMessage0256[]`، `limit: int32`، `offset: int32` | web 5.5.1 |
| `GetSession` | `symbol: int32` | `openAt: int64`، `closeAt: int64`، `openingPrice: string`، `brokerFeePercentage: string`، `marketFeePercentage: string`، `priceTolerancePercentage: string`، `quantityTickSize: string` | web 5.5.1 |
| `GetTickers` | — | `usd: RecoveredMessage0255`، `euro: RecoveredMessage0255` | web 5.5.1 |
| `GetWallet` | — | `wallet: RecoveredMessage0253` | web 5.5.1 |

## `bale.schedule.v1.Scheduler`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ExecuteTaskNow` | `taskID: int64` | — | bundled |
| `ListTasks` | `exPeer: WebExPeer`، `type: int64`، `status: int64` | `tasks: WebTask[]` | bundled |
| `PeersWithScheduleTask` | — | `exPeer: WebExPeer[]` | bundled |
| `ReScheduleTask` | `taskID: int64`، `scheduledAt: bytes`، `payload: WebT_Q_` | — | bundled |
| `ScheduleTask` | `exPeer: WebExPeer`، `scheduledAt: bytes`، `payload: WebT_Q_` | `taskId: int64` | bundled |
| `UnScheduleTask` | — | — | bundled |

## `bale.search.v1.Search`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `RecommendPeer` | `exPeerType: int64` | `peer: WebPeer[]` | bundled |
| `SearchContent` | `query: WebQuery`، `contentType: int64`، `loadMoreState: WebBytesValue` | `contentResults: WebContentResult[]`، `loadMoreState: WebBytesValue`، `resultCount: int64` | bundled |
| `SearchDialog` | `query: WebQuery` | `dialogResults: WebDialogResult[]` | bundled |
| `SearchMarket` | `query: WebQuery`، `withCategory: WebBoolValue_1`، `loadMoreState: WebBytesValue` | `marketResults: WebMarketResult[]`، `category: WebT_iE_88717`، `loadMoreState: WebBytesValue`، `resultCount: int64` | bundled |
| `SearchMarketPopular` | — | `popularResults: WebPopularResult[]` | bundled |
| `SearchMedia` | `query: WebAndQuery`، `date: WebInt64Value_1`، `optimizations: int64[]`، `loadMode: int64` | `searchResults: WebSearchResult[]`، `users: WebUser[]`، `groups: WebGroup[]`، `loadMoreState: WebBytesValue`، `userOutPeers: WebUserPeer[]`، `groupOutPeers: WebGroupPeer[]`، `resultCount: int64` | bundled |
| `SearchMembers` | `query: WebQuery`، `exPeer: WebExPeer`، `loadMoreState: WebBytesValue`، `users: WebUserPeer[]` | `users: WebUserPeer[]`، `loadMoreState: WebBytesValue` | bundled |
| `SearchMessageMore` | `loadMoreState: WebBytesValue`، `query: WebAndQuery`، `optimizations: int64[]` | `searchResults: WebSearchResult[]`، `users: WebUser[]`، `groups: WebGroup[]`، `loadMoreState: WebBytesValue`، `userOutPeers: WebUserPeer[]`، `groupOutPeers: WebGroupPeer[]`، `resultCount: int64` | bundled |
| `SearchMessages` | `query: WebAndQuery`، `optimizations: int64[]` | `searchResults: WebSearchResult[]`، `users: WebUser[]`، `groups: WebGroup[]`، `loadMoreState: WebBytesValue`، `userOutPeers: WebUserPeer[]`، `groupOutPeers: WebGroupPeer[]`، `resultCount: int64` | bundled |
| `SearchPeer` | `query: WebAndQuery[]`، `optimizations: int64[]` | `searchResults: WebT_I_[]`، `users: WebUser[]`، `groups: WebGroup[]`، `userPeers: WebUserPeer[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `SearchProduct` | `query: WebQuery`، `loadMoreState: WebBytesValue` | `productResults: WebProductResult[]`، `loadMoreState: WebBytesValue`، `resultCount: int64` | bundled |
| `UpdateSearchContentClick` | `messageId: WebMsg`، `searchTab: int64` | — | bundled |

## `bale.shared_media.v1.SharedMediaService`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetActiveSharedMedia` | `exPeer: WebExPeer` | — | bundled |
| `LoadMedia` | `exPeer: WebExPeer`، `date: WebInt64Value_1`، `contentType: int64`، `loadMode: int64`، `minimumResults: int64` | `mediaResults: WebMediaResult[]` | bundled |

## `bale.story.v1.Story`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddBotStory` | `exPeer: WebExPeer`، `mediaStory: WebStoryContent`، `textStory: WebTextStory`، `tagIds: int64[]`، `expirationType: int64` | `storyId: bytes` | bundled |
| `AddChannelStory` | `exPeer: WebExPeer`، `mediaStory: WebStoryContent`، `hasReply: int64`، `tagIds: int64[]`، `expirationType: int64`، `textStory: WebTextStory` | `storyId: bytes` | bundled |
| `AddStory` | `mediaStory: WebStoryContent`، `textStory: WebTextStory`، `tagIds: int64[]`، `expirationType: int64`، `exceptionType: int64` | `storyId: bytes` | bundled |
| `CanAddBotStory` | `botUserId: int64` | `canAddBotStory: int64` | bundled |
| `CheckLinkValidity` | `exPeer: WebExPeer`، `link: bytes` | — | bundled |
| `GetAllStories` | — | `userStories: RecoveredMessage0067[]`، `channelStories: RecoveredMessage0068[]`، `botStories: RecoveredMessage0069[]`، `popularityList: RecoveredMessage0066[]` | web 5.5.1 |
| `GetBotStories` | — | `result: WebBotStoryResult[]`، `popularityList: WebPopularityList[]` | bundled |
| `GetChannelStories` | — | `result: WebResult[]`، `popularityList: WebPopularityList[]` | bundled |
| `GetDefaultStoryBackgrounds` | — | `defaultStoryBackgrounds: WebStoryContent[]` | bundled |
| `GetMostPopularStories` | `getSpecialStories: WebBoolValue_1`، `optimization: int64` | `result: WebResult[]`، `popularityList: WebPopularityList[]` | bundled |
| `GetStories` | `getUnmutual: WebBoolValue_1` | `result: WebUserStory[]`، `popularityList: WebPopularityList[]` | bundled |
| `GetStoriesByList` | `exPeers: WebExPeer[]` | `userStories: WebUserStory[]`، `channelStories: WebResult[]`، `botStories: WebBotStoryResult[]` | bundled |
| `GetStoryById` | `storyId: bytes` | `result: WebUserStory`، `channelStoryResult: WebResult`، `botStoryResult: WebBotStoryResult` | bundled |
| `GetStoryReactionEmojis` | — | `emojis: WebEmoji[]` | bundled |
| `GetStoryTags` | — | `tags: WebT_vw[]` | bundled |
| `GetStoryWidgets` | `storyId: bytes` | `widgets: WebWidget[]` | bundled |
| `GetUserPrivacyConfig` | — | `result: WebPrivacyConfig[]` | bundled |
| `GetUserStoryConfig` | `key: int64[]`، `exPeer: WebExPeer` | `config: WebConfig[]` | bundled |
| `GetViewers` | `storyId: bytes`، `pagination: WebT_eC` | `viewers: WebViewer[]`، `viewCount: int64`، `likeCount: int64`، `linkClickCount: int64`، `emojiCount: int64`، `restoryCount: int64` | bundled |
| `GetViewersCount` | `storyId: bytes` | `viewCount: int64`، `likeCount: int64`، `linkClickCount: int64`، `emojiCount: int64`، `restoryCount: int64` | bundled |
| `ReactToStory` | `storyId: bytes`، `reaction: bytes`، `type: int64`، `reactionType: int64`، `reactionText: WebStringValue` | — | bundled |
| `RemoveStory` | `storyId: bytes` | — | bundled |
| `SetUserPrivacyConfig` | `config: WebPrivacyConfig` | — | bundled |
| `SetUserStoryConfig` | `setType: int64`، `config: WebConfig`، `exPeer: WebExPeer` | — | bundled |

## `bale.timche.v1.Timche`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AskBotReviewCallback` | `botId: int32`، `payload: string` | — | bundled |
| `GetBotPage` | `botId: int32` | `name: string`، `nickname: string`، `activeUsers: int32`، `averageRating: WebFloatValue`، `description: string`، `intro: string`، `avatar: WebAvatar`، `imageLinks: string[]` | bundled |
| `GetHomePage` | — | `sections: WebT_u_72802[]` | bundled |
| `GetSectionPage` | `sectionId: int32` | `sectionId: int32`، `sectionName: string`، `bots: WebT_c_72802[]` | bundled |
| `SubmitReview` | `botId: int32`، `rating: WebInt32Value`، `comment: WebStringValue`، `payload: WebStringValue`، `origin: int32`، `language: WebStringValue` | `shouldAskBaleReview: bool`، `baleReviewText: string` | bundled |

## `bale.tldr.v1.TLDR`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetLinkPreview` | `url: bytes` | `title: bytes`، `description: bytes`، `images: WebImage[]` | bundled |
| `GetLinkSummary` | `url: bytes` | `summary: bytes` | bundled |

## `bale.top_peer.v1.TopPeer`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetTopPeer` | — | `topPeers: WebTopPeerType[]` | bundled |
| `RemovePeer` | `peer: WebPeer` | `isRemoved: int64` | bundled |

## `bale.turing.v1.AI`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `GetTranscript` | `voice: WebMedia`، `outPeer: WebOutPeer`، `messageId: WebMessageId` | `mustWait: bool`، `downloadSource: WebDownloadSource` | bundled |
| `SendEvent` | `transcriptReactionEvent: WebTranscriptReactionEvent` | — | bundled |

## `bale.users.v1.Users`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddCard` | `bankCode: string` | — | bundled |
| `AddContact` | `uid: int32`، `accessHash: int64` | `seq: int32`، `state: bytes` | bundled |
| `BlockUser` | `peer: WebUserPeer` | `seq: int32`، `state: bytes` | bundled |
| `ChangeDefaultCardNumber` | `defaultCardNumber: WebStringValue` | `seq: int32`، `state: bytes` | bundled |
| `ChangePhoneNumber` | `phoneNumber: int64` | — | bundled |
| `CheckNickName` | `nickname: string` | `value: bool` | bundled |
| `ConfirmPhoneNumber` | `code: string` | — | bundled |
| `EditAbout` | `about: WebStringValue` | `seq: int32`، `state: bytes` | bundled |
| `EditAvatar` | `fileLocation: WebFileLocation` | `avatar: WebAvatar`، `seq: int32`، `state: bytes` | bundled |
| `EditBirthDate` | `date: int64` | — | bundled |
| `EditMyPreferredLanguages` | `preferredLanguages: string[]` | `seq: int32`، `state: bytes` | bundled |
| `EditMyTimeZone` | `tz: string` | `seq: int32`، `state: bytes` | bundled |
| `EditName` | `name: string` | `seq: int32`، `state: bytes` | bundled |
| `EditNickName` | `nickname: WebStringValue` | `seq: int32`، `state: bytes` | bundled |
| `EditSex` | `sex: int32` | — | bundled |
| `EditUserLocalName` | `uid: int32`، `accessHash: int64`، `name: string` | `seq: int32`، `state: bytes` | bundled |
| `GetContacts` | `contactsHash: string`، `optimizations: int32[]` | `users: WebUser[]`، `isNotChanged: bool`، `userPeers: WebUserPeer[]` | bundled |
| `GetFullUser` | `peer: WebUserPeer` | `fullUser: WebT_n4` | bundled |
| `GetUserFullPrivacy` | `userId: int32` | `privacy: WebPrivacy` | bundled |
| `GetUserPrivacyStatus` | `userId: int32`، `type: int32` | `status: int32` | bundled |
| `GetUsersDefaultCardNumber` | — | `defaultCardNo: WebDefaultCardNo[]` | bundled |
| `ImportContacts` | `phones: WebPhone[]`، `optimizations: int32[]` | `users: WebUser[]`، `seq: int32`، `state: bytes`، `userPeers: WebUserPeer[]` | bundled |
| `IsNameAllowed` | `name: string` | `value: bool` | bundled |
| `LoadAvatars` | `peer: WebUserPeer` | `avatars: WebAvatars` | bundled |
| `LoadBlockedUsers` | — | `userPeers: WebUserPeer[]` | bundled |
| `LoadFullUsers` | `userPeers: WebUserPeer[]` | `fullUsers: WebFullUser[]` | bundled |
| `LoadFullUsersSequentially` | `userPeers: WebUserPeer[]` | `fullUsers: WebFullUser[]` | bundled |
| `LoadUsers` | `peers: WebUserPeer[]` | `users: WebUser[]` | bundled |
| `NotifyAboutDeviceInfo` | `preferredLanguages: string[]`، `timeZone: WebStringValue` | — | bundled |
| `RemoveAvatar` | `avaterId: WebInt64Value_1` | `seq: int32`، `state: bytes` | bundled |
| `RemoveContact` | `uid: int32`، `accessHash: int64` | `seq: int32`، `state: bytes` | bundled |
| `RemoveDefaultCardNumber` | — | `seq: int32`، `state: bytes` | bundled |
| `ResetContacts` | — | — | bundled |
| `SearchContacts` | `request: string`، `optimizations: int32[]` | `users: WebUser[]`، `userPeers: WebUserPeer[]`، `groups: WebGroup[]`، `groupPeers: WebGroupPeer[]` | bundled |
| `SetUserPrivacyStatus` | `userId: int32`، `type: int32`، `status: int32` | — | bundled |
| `UnblockUser` | `peer: WebUserPeer` | `seq: int32`، `state: bytes` | bundled |

## `bale.v1.Configs`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `EditParameter` | `key: string`، `value: WebStringValue` | `seq: int32`، `state: bytes` | bundled |
| `GetInAppUpdate` | — | `fileId: int64`، `accessHash: int64`، `fileSize: int32` | bundled |
| `GetParameters` | — | `parameters: WebParameter[]` | bundled |

## `bale.v1.Images`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `AddGif` | `gif: WebFileLocation`، `thumb: bytes`، `mimeType: WebOffset` | `seq: int32`، `state: bytes` | bundled |
| `AddStickerCollection` | `id: int32`، `accessHash: int64` | `collections: WebCollection[]`، `seq: int32`، `state: bytes` | bundled |
| `AddStickerPack` | `id: int32` | `seq: int32`، `state: bytes` | bundled |
| `GetSavedGifs` | `offset: WebOffset` | `gifs: WebGifs[]`، `offset: WebOffset` | bundled |
| `LoadOwnStickers` | `offset: WebOffset` | `ownStickers: WebCollection[]`، `offset: WebOffset` | bundled |
| `LoadStickerCollection` | `id: int32`، `accessHash: int64` | `collection: WebCollection` | bundled |
| `RemoveGif` | `gif: WebFileLocation` | `seq: int32`، `state: bytes` | bundled |
| `RemoveStickerCollection` | `id: int32`، `accessHash: int64` | `collections: WebCollection[]`، `seq: int32`، `state: bytes` | bundled |
| `RemoveStickerPack` | `id: int32` | `seq: int32`، `state: bytes` | bundled |
| `UseGif` | `gif: WebFileLocation`، `usedAt: int64` | — | bundled |

## `bale.wallet.v1.Wallet`

| متد | ورودی | خروجی | منبع |
|---|---|---|---|
| `ActivateWallet` | `nationalId: string`، `isAutoActivated: WebBoolValue_1` | — | bundled |
| `CashOutFromWallet` | `token: string`، `amount: int64` | — | bundled |
| `GetMoneyRequestPaymentTokenByCard` | `msg: WebMsg`، `amount: WebInt64Value_1`، `regarding: WebStringValue` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | bundled |
| `GetMyWallets` | — | `wallets: WebWalletType[]` | bundled |
| `GetPaymentTokenByCard` | `targetWallet: string`، `amount: int64`، `regarding: WebStringValue` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | bundled |
| `GetWalletChargeToken` | `walletId: string`، `amount: int64` | `token: string`، `endpoint: string`، `terminalId: string`، `merchantId: string` | bundled |
| `GetWalletContracts` | — | `startDate: int64`، `endDate: int64`، `merchantCustomerUniqueValue: string`، `limitations: WebLimitation[]`، `agreementId: string`، `status: int32` | bundled |
| `GetWalletInvoice` | `walletId: string`، `pageNumber: WebInt32Value` | `invoices: WebInvoice[]` | bundled |
| `PayByWallet` | `sourceWallet: string`، `targetWallet: string`، `amount: int64`، `currency: int32`، `regarding: WebStringValue` | — | bundled |
| `PayMoneyRequestByWallet` | `sourceWalletId: string`، `msg: WebMsg`، `amount: WebInt64Value_1`، `regarding: WebStringValue` | — | bundled |
| `VerifyCashOut` | `walletId: string`، `accountNo: string`، `nationalId: string` | `token: string`، `name: string` | bundled |
| `VerifyPeer` | `targetPeer: WebBot` | `targetWalletName: string`، `targetUserId: WebInt32Value`، `walletId: string` | bundled |
| `VerifyQRCode` | `targetWalletId: string` | `targetWalletName: string`، `targetUserId: WebInt32Value` | bundled |

# Bale Web RPC API — Python coverage

All **607 RPCs** the Bale web client exposes, across **52 services**, are callable from `BaleClient` via per-service namespaces.

```python
client = BaleClient(token); await client.connect()
resp = await client.messaging.SendMessage(peer={'type':1,'id':uid}, rid=rid,
                                          message={'textMessage':{'text':'hi'}})
seen = await client.negah.GetMessageSeenList(peer={'type':2,'id':gid},
                                             messageId={'date':d,'rid':r,'seq':s})
```

- **607/607** fully typed · **1** server-streaming (stubbed). 8 long-tail schemas recovered into `bale_ext.proto`.

## `client.push` — ai.bale.pushak.Push  (6)
- `RegisterGooglePush` → pb.T_Ou
- `RegisterPush` → pb.RegisterPushResponse
- `SetConfig` → pb.T_Ou
- `UnregisterAllPushCredentials` → pb.T_Ou
- `UnregisterGooglePush` → pb.T_Ou
- `UnregisterPush` → pb.T_Ou

## `client.files` — ai.bale.server.Files  (6)
- `FileUploadCancel` → pb.FileUploadCancelResponse
- `GetNasimFilePublicUrl` → pb.GetNasimFilePublicUrlResponse
- `GetNasimFileUploadResume` → pb.GetNasimFileUploadResumeResponse
- `GetNasimFileUploadUrl` → pb.GetNasimFileUploadUrlResponse
- `GetNasimFileUrl` → pb.GetNasimFileUrlResponse
- `GetNasimFileUrls` → pb.GetNasimFileUrlsResponse

## `client.abacus` — bale.abacus.v1.Abacus  (9)
- `EnableShowReactionFlag` → pb.T_Ou
- `GetMessageReactionsList` → pb.GetMessageReactionsListResponse
- `GetMessagesReactions` → pb.GetMessagesReactionsResponse
- `GetMessagesViews` → pb.GetMessagesViewsResponse
- `GetShowReactionFlag` → pb.GetShowReactionFlagResponse
- `LoadReactions` → pb.LoadReactionsResponse
- `MessageReactionsRead` → pb.T_Ou
- `MessageRemoveReaction` → pb.T_p_29732
- `MessageSetReaction` → pb.T_p_29732

## `client.advertisement` — bale.advertisement.v1.Advertisement  (108)
- `AddCustomIncome` → pb.AddCustomIncomeResponse
- `ChangeAccountState` → pb.ChangeAccountStateResponse
- `ChangeAdState` → pb.T_Ou
- `ChangeBonusCodeState` → pb.T_Ou
- `ChangeCampaignContentState` → pb.T_Ou
- `ChangeCampaignState` → pb.T_Ou
- `ChangeChannelIncomeOwner` → pb.ChangeChannelIncomeOwnerResponse
- `ChangeChannelShowAdPermissions` → pb.T_Ou
- `ChangeStatusDialogAdOrder` → pb.T_Ou
- `ChangeUserDataState` → pb.T_Ou
- `ChannelIncomeGetCredit` → pb.T_Ou
- `ChannelIncomeKifTransfer` → pb.T_Ou
- `ChannelIncomePayment` → pb.ChannelIncomePaymentResponse
- `ConvertIncome` → pb.T_Ou
- `CreateAd` → pb.CreateAdResponse
- `CreateAndStartChannelAd` → pb.CreateAndStartChannelAdResponse
- `CreateBaleDialogCustomAd` → pb.CreateBaleDialogCustomAdResponse
- `CreateBonusCode` → pb.CreateBonusCodeResponse
- `CreateChannelIncomeFactor` → pb.CreateChannelIncomeFactorResponse
- `CreateCustomCampaignPackage` → pb.T_Ou
- `DeleteCustomIncome` → pb.T_Ou
- `EditAccount` → pb.T_Ou
- `EditAd` → pb.T_Ou
- `EditCampaignAd` → pb.T_Ou
- `EditCampaignContent` → pb.T_Ou
- `FinishAd` → pb.FinishAdResponse
- `FinishAdV2` → pb.T_Ou
- `FinishChannelAd` → pb.FinishChannelAdResponse
- `GetAccountData` → pb.GetAccountDataResponse
- `GetAccounts` → pb.GetAccountsResponse
- `GetAccountsByState` → pb.GetAccountsByStateResponse
- `GetActiveAds` → pb.GetActiveAdsResponse
- `GetActiveChannelAds` → pb.GetActiveChannelAdsResponse
- `GetAdData` → pb.GetAdDataResponse
- `GetAdDetail` → pb.GetAdDetailResponse
- `GetAdProvider` → pb.GetAdProviderResponse
- `GetAdReport` → pb.GetAdReportResponse
- `GetAdReportV2` → pb.GetAdReportV2Response
- `GetAdsBySpotAndPlatform` → pb.GetAdsBySpotAndPlatformResponse
- `GetAdsByStateAndSpot` → pb.GetAdsByStateAndSpotResponse
- `GetAllChannelIncomesFactor` → pb.GetAllChannelIncomesFactorResponse
- `GetAvailableCampaignStartDate` → pb.GetAvailableCampaignStartDateResponse
- `GetAwaitingToShowAds` → pb.GetAwaitingToShowAdsResponse
- `GetAwaitingToShowChannelAds` → pb.GetAwaitingToShowChannelAdsResponse
- `GetBaleCustomAd` → pb.GetBaleCustomAdResponse
- `GetBonusCodeData` → pb.GetBonusCodeDataResponse
- `GetBonusCodes` → pb.GetBonusCodesResponse
- `GetBusinessAds` → pb.GetBusinessAdsResponse
- `GetCRMIssues` → pb.GetCRMIssuesResponse
- `GetCampaignAds` → pb.T_oc_58187
- `GetCampaignContentById` → pb.GetCampaignContentByIdResponse
- `GetCampaignContents` → pb.GetCampaignContentsResponse
- `GetCampaignData` → pb.GetCampaignDataResponse
- `GetChannelAds` → pb.GetChannelAdsResponse
- `GetChannelEarnMoneyInfo` → pb.GetChannelEarnMoneyInfoResponse
- `GetChannelEarnMoneyStatus` → pb.GetChannelEarnMoneyStatusResponse
- `GetChannelGraphReport` → pb.GetChannelGraphReportResponse
- `GetChannelIncomeReport` → pb.GetChannelIncomeReportResponse
- `GetChannelOwnerBankInformation` → pb.GetChannelOwnerBankInformationResponse
- `GetChannelShowAdCategoryFilter` → pb.GetChannelShowAdCategoryFilterResponse
- `GetChannelShowAdPermissions` → pb.GetChannelShowAdPermissionsResponse
- `GetChannelShowAdTimeRestrict` → pb.GetChannelShowAdTimeRestrictResponse
- `GetChannelsViewReport` → pb.GetChannelsViewReportResponse
- `GetConfig` → pb.GetConfigResponse
- `GetCreditHistory` → pb.GetCreditHistoryResponse
- `GetCreditableAccounts` → pb.GetCreditableAccountsResponse
- `GetCustomIncomes` → pb.GetCustomIncomesResponse
- `GetDialogAdOrderDetails` → pb.GetDialogAdOrderDetailsResponse
- `GetDialogAdOrderPaymentToken` → pb.GetDialogAdOrderPaymentTokenResponse
- `GetFactorEligibleAds` → pb.GetFactorEligibleAdsResponse
- `GetMyContactPopularChannels` → pb.GetMyContactPopularChannelsResponse
- `GetOnBoardingChannels` → pb.GetOnBoardingChannelsResponse
- `GetOnboardingPeers` → pb.GetOnboardingPeersResponse
- `GetOnboardingPosts` → pb.GetOnboardingPostsResponse
- `GetOnboardingSpotData` → pb.GetOnboardingSpotDataResponse
- `GetOwnerIdByPhone` → pb.GetOwnerIdByPhoneResponse
- `GetPaidAdsByTime` → pb.GetPaidAdsByTimeResponse
- `GetPaymentData` → pb.GetPaymentDataResponse
- `GetPeriodCapacityData` → pb.GetPeriodCapacityDataResponse
- `GetUserAds` → pb.GetUserAdsResponse
- `GetUserAuthData` → pb.GetUserAuthDataResponse
- `GetUserCampaigns` → pb.T_oc_58187
- `GetUserOnboardingScenario` → pb.GetUserOnboardingScenarioResponse
- `GetUserStatus` → pb.GetUserStatusResponse
- `GetUsersAuthDataByState` → pb.GetUsersAuthDataByStateResponse
- `GetVODContents` → pb.GetVODContentsResponse
- `ModifyCapacity` → pb.ModifyCapacityResponse
- `RegisterForEarnMoney` → pb.T_Ou
- `SendAdminMessage` → pb.T_Ou
- `SendFactorMessage` → pb.T_Ou
- `SetAdTarget` → pb.T_Ou
- `SetChannelInvoiceInfo` → pb.T_Ou
- `SetChannelOwnerBankInformation` → pb.T_Ou
- `SetOnBoardingChannels` → pb.T_Ou
- `SetUserAuthData` → pb.T_Ou
- `StartAd` → pb.T_Ou
- `StartBaleCustomAd` → pb.StartBaleCustomAdResponse
- `StartChannelAdFromOrder` → pb.StartChannelAdFromOrderResponse
- `StartFromOrder` → pb.StartFromOrderResponse
- `StopAllBaleCustomAds` → pb.StopAllBaleCustomAdsResponse
- `SubmitChannelAdOrder` → pb.T_Ou
- `SubmitDialogAdOrder` → pb.T_Ou
- `SubmitPhotoForBaleCustomAd` → pb.SubmitPhotoForBaleCustomAdResponse
- `UpdateBusinessAd` → pb.T_Ou
- `UpdateCRMIssue` → pb.T_Ou
- `UpdateClick` → pb.UpdateClickResponse
- `UpdateGroupStatus` → pb.T_Ou
- `UpdateView` → pb.UpdateViewResponse

## `client.anonymous_contact` — bale.anonymous_contact.v1.AnonymousContact  (1)
- `GetUserAnonymousContactPage` → ext.ExtAnonymousContactGetUserAnonymousContactPageResponse

## `client.appzar` — bale.appzar.v1.Appzar  (3)
- `GetMenuButton` → pb.GetMenuButtonResponse
- `GetMiniAppUrl` → pb.GetMiniAppUrlResponse
- `InvokeCustomMethod` → pb.InvokeCustomMethodResponse

## `client.auth` — bale.auth.v1.Auth  (26)
- `ChangePhone` → pb.T_Ou
- `DeleteAccount` → pb.T_Ou
- `DisableTwoFactorAuthentication` → pb.T_Ou
- `EnableTwoFactorAuthentication` → pb.T_Ou
- `GetAuthSessions` → pb.GetAuthSessionsResponse
- `GetBajeBamTicket` → pb.GetBajeBamTicketResponse
- `GetBaleTicket` → pb.T_er_68945
- `GetJWTToken` → pb.GetJWTTokenResponse
- `GetTicket` → pb.T_er_68945
- `GetUserIdToken` → pb.GetUserIdTokenResponse
- `IsTwoFactorAuthenticationEnabled` → pb.IsTwoFactorAuthenticationEnabledResponse
- `LogOut` → pb.LogOutResponse
- `RecoverPassword` → pb.RecoverPasswordResponse
- `SendChangePhoneVerificationCode` → pb.SendChangePhoneVerificationCodeResponse
- `SendDeleteAccountVerificationCode` → pb.SendDeleteAccountVerificationCodeResponse
- `SetNewPassword` → pb.T_Ou
- `SignOut` → pb.T_Ou
- `SignUp` → pb.T_y_68945
- `StartPhoneAuth` → pb.StartPhoneAuthResponse
- `TerminateAllSessions` → pb.T_Ou
- `TerminateSession` → pb.T_Ou
- `ValidateCode` → pb.T_y_68945
- `ValidatePassword` → pb.T_y_68945
- `VerifyEmail` → pb.T_Ou
- `VerifyPassword` → pb.T_Ou
- `VerifyPasswordRecovery` → pb.T_Ou

## `client.gold_gift_packet` — bale.balebank.v1.GoldGiftPacket  (3)
- `GetWinnerIDs` → pb.GetWinnerIDsResponse
- `OpenGoldGiftPacket` → pb.OpenGoldGiftPacketResponse
- `SendGoldGiftPacket` → pb.SendGoldGiftPacketResponse

## `client.gold_wallet` — bale.balebank.v1.GoldWallet  (1)
- `GetBalance` → ext.ExtGoldWalletGetBalanceResponse

## `client.bank` — bale.bank.v1.Bank  (17)
- `BuyFastCharge` → pb.BuyFastChargeResponse
- `GetCardRemain` → pb.GetCardRemainResponse
- `GetCardTransferToken` → pb.GetCardTransferTokenResponse
- `GetOTPToken` → pb.GetOTPTokenResponse
- `GetOTPTokenV2` → pb.GetOTPTokenV2Response
- `GetOrganizationPaymentToken` → pb.GetOrganizationPaymentTokenResponse
- `GetPSProxyPaymentToken` → pb.GetPSProxyPaymentTokenResponse
- `GetPSProxyToken` → pb.GetPSProxyTokenResponse
- `GetPayMoneyRequestToken` → pb.GetPayMoneyRequestTokenResponse
- `GetPaymentToken` → pb.GetPaymentTokenResponse
- `GetPayvandCard` → pb.GetPayvandCardResponse
- `GetPayvandCardList` → pb.GetPayvandCardListResponse
- `GetRecentCharges` → pb.GetRecentChargesResponse
- `GetRemainToken` → pb.GetRemainTokenResponse
- `GetSadadPSPPaymentToken` → pb.GetSadadPSPPaymentTokenResponse
- `GetTokenInvoice` → pb.GetTokenInvoiceResponse
- `GrantBankiAccess` → pb.T_Ou

## `client.charnet_service` — bale.charnet.v1.CharnetService  (11)
- `BuyCharge` → pb.BuyChargeResponse
- `BuyInternetBundle` → pb.BuyInternetBundleResponse
- `DeleteRecentChargeOrder` → pb.T_Ou
- `DeleteRecentInternetBundleOrder` → pb.T_Ou
- `GetAvailableCharges` → pb.GetAvailableChargesResponse
- `GetInternetBundleList` → pb.GetInternetBundleListResponse
- `GetInternetBundlePaymentToken` → pb.GetInternetBundlePaymentTokenResponse
- `GetRecentChargeOrders` → pb.GetRecentChargeOrdersResponse
- `GetRecentInternetBundleOrders` → pb.GetRecentInternetBundleOrdersResponse
- `GetTopUpChargePaymentToken` → pb.GetTopUpChargePaymentTokenResponse
- `GetVoucherChargePaymentToken` → pb.GetVoucherChargePaymentTokenResponse

## `client.crowd_funding` — bale.crowdfunding.v1.CrowdFunding  (2)
- `GetParticipants` → pb.GetParticipantsResponse
- `GetTotalPaidAmount` → pb.GetTotalPaidAmountResponse

## `client.falake` — bale.falake.v1.Falake  (1)
- `GetLinkStatus` → ext.ExtFalakeGetLinkStatusResponse

## `client.fanoos` — bale.fanoos.v1.fanoos  (1)
- `Send` → pb.T_Ou

## `client.feed_back` — bale.feedback.v1.FeedBack  (1)
- `SendFeedBack` → pb.T_Ou

## `client.garson` — bale.garson.v1.Garson  (10)
- `EditCustomServices` → pb.EditCustomServicesResponse
- `GetAdvertisementBot` → pb.GetAdvertisementBotResponse
- `GetBotBanners` → pb.GetBotBannersResponse
- `GetBotsByCategory` → pb.GetBotsByCategoryResponse
- `GetCategorizedBots` → pb.GetCategorizedBotsResponse
- `GetCustomServices` → pb.GetCustomServicesResponse
- `GetRecommendedBots` → pb.GetRecommendedBotsResponse
- `GetServices` → pb.GetServicesResponse
- `GetTrendBots` → pb.GetTrendBotsResponse
- `GetUserRepeatedBots` → pb.GetUserRepeatedBotsResponse

## `client.ghasedak_service` — bale.ghasedak.v1.GhasedakService  (2)
- `GetDiff` → pb.GetDiffResponse
- `GetRoutesStates` → pb.GetRoutesStatesResponse

## `client.gift_packet` — bale.giftpacket.v1.GiftPacket  (3)
- `GetGiftPacketPaymentToken` → pb.GetGiftPacketPaymentTokenResponse
- `OpenGiftPacket` → pb.OpenGiftPacketResponse
- `SendGiftPacketWithWallet` → pb.T_pQ

## `client.groups` — bale.groups.v1.Groups  (48)
- `AddDiscussionGroupAdmin` → pb.T_pQ
- `CreateGroup` → pb.CreateGroupResponse
- `EditChannelNick` → pb.T_pQ
- `EditGroupAbout` → pb.T_pQ
- `EditGroupAvatar` → pb.EditGroupAvatarResponse
- `EditGroupDefaultCardNumber` → pb.T_Ou
- `EditGroupTitle` → pb.T_pQ
- `FetchGroupAdmins` → pb.FetchGroupAdminsResponse
- `GetBannedUsers` → pb.GetBannedUsersResponse
- `GetCanSeeMessages` → pb.GetCanSeeMessagesResponse
- `GetFullGroup` → pb.GetFullGroupResponse
- `GetGroupDefaultCardNumber` → pb.GetGroupDefaultCardNumberResponse
- `GetGroupInviteURL` → pb.T_ed_47679
- `GetGroupMembersCount` → pb.GetGroupMembersCountResponse
- `GetGroupPreview` → pb.GetGroupPreviewResponse
- `GetGroupRecommendations` → pb.GetGroupRecommendationsResponse
- `GetMemberPermissions` → pb.GetMemberPermissionsResponse
- `GetMutualGroups` → pb.GetMutualGroupsResponse
- `GetMyGroups` → pb.GetMyGroupsResponse
- `GetPins` → pb.GetPinsResponse
- `InviteUser` → pb.T_pQ
- `InviteUsers` → pb.InviteUsersResponse
- `JoinGroup` → pb.JoinGroupResponse
- `JoinPublicGroup` → pb.JoinPublicGroupResponse
- `KickUser` → pb.T_pQ
- `LeaveGroup` → pb.T_pQ
- `LoadFullGroups` → pb.LoadFullGroupsResponse
- `LoadGroupAvatars` → pb.LoadGroupAvatarsResponse
- `LoadGroups` → pb.LoadGroupsResponse
- `LoadMembers` → pb.LoadMembersResponse
- `MakeUserAdmin` → pb.T_pQ
- `PinMessage` → pb.T_pQ
- `RemoveDiscussionGroup` → pb.T_Ou
- `RemoveGroupAvatar` → pb.T_pQ
- `RemovePin` → pb.T_pQ
- `RemoveSinglePin` → pb.T_pQ
- `RemoveUserAdmin` → pb.T_pQ
- `RevokeInviteURL` → pb.T_ed_47679
- `SetAvailableReactions` → pb.T_Ou
- `SetCanSeeHistory` → pb.T_Ou
- `SetCanSeeMessages` → pb.T_Ou
- `SetDiscussionGroup` → pb.SetDiscussionGroupResponse
- `SetGroupDefaultPermissions` → pb.T_Ou
- `SetMemberCustomTitle` → pb.SetMemberCustomTitleResponse
- `SetMemberPermissions` → pb.T_Ou
- `SetRestriction` → pb.T_pQ
- `TransferOwnership` → pb.T_pQ
- `UnBanUser` → pb.UnBanUserResponse

## `client.ketf` — bale.ketf.v1.Ketf  (14)
- `GetBotGroupPermissions` → pb.GetBotGroupPermissionsResponse
- `GetBotInfo` → pb.GetBotInfoResponse
- `GetBotWhiteList` → pb.GetBotWhiteListResponse
- `GetBots` → pb.GetBotsResponse
- `GetInlineBotResults` → pb.GetInlineBotResultsResponse
- `GetPaymentDetails` → pb.GetPaymentDetailsResponse
- `GetUserContext` → pb.GetUserContextResponse
- `GetWebappHash` → pb.GetWebappHashResponse
- `InvokeCustomAction` → pb.InvokeCustomActionResponse
- `MakePayment` → pb.MakePaymentResponse
- `SendAuthenticatedInlineCallBackData` → pb.SendAuthenticatedInlineCallBackDataResponse
- `SendInlineCallBackData` → pb.T_Ou
- `SendInlineCallback` → pb.SendInlineCallbackResponse
- `SendMiniAppData` → pb.SendMiniAppDataResponse

## `client.kifpool` — bale.kifpool.v1.Kifpool  (29)
- `CashOut` → pb.CashOutResponse
- `Charge` → pb.ChargeResponse
- `CheckChargePermission` → pb.CheckChargePermissionResponse
- `CreateKifpool` → pb.CreateKifpoolResponse
- `CryptoCashOut` → pb.CryptoCashOutResponse
- `CryptoInvoice` → pb.CryptoInvoiceResponse
- `CryptoPurchase` → pb.CryptoPurchaseResponse
- `CryptoRefund` → pb.T_Ou
- `CryptoTransfer` → pb.CryptoTransferResponse
- `GetChargePaymentToken` → pb.T_v_98711
- `GetCredit` → pb.GetCreditResponse
- `GetCryptoChargePaymentToken` → pb.T_v_98711
- `GetCryptoWallets` → pb.GetCryptoWalletsResponse
- `GetKifpoolOwner` → pb.GetKifpoolOwnerResponse
- `GetKifpoolPointBalance` → pb.GetKifpoolPointBalanceResponse
- `GetKifpoolPointDetails` → pb.GetKifpoolPointDetailsResponse
- `GetKifpoolPointSummery` → pb.GetKifpoolPointSummeryResponse
- `GetKifpoolTransactionPoint` → pb.GetKifpoolTransactionPointResponse
- `GetMyKifpools` → pb.GetMyKifpoolsResponse
- `Invoice` → pb.InvoiceResponse
- `PayForMessage` → pb.PayForMessageResponse
- `Purchase` → pb.PurchaseResponse
- `PurchaseMessage` → pb.PurchaseMessageResponse
- `PurchaseMessageWithCharge` → pb.PurchaseMessageWithChargeResponse
- `PurchaseWithCharge` → pb.PurchaseWithChargeResponse
- `Transfer` → pb.TransferResponse
- `UpgradeKifpool` → pb.UpgradeKifpoolResponse
- `VerifyCashOutKifpool` → pb.VerifyCashOutKifpoolResponse
- `VerifyPurchaseMessage` → pb.VerifyPurchaseMessageResponse

## `client.llm_auth_service` — bale.llm_auth.v1.LLMAuthService  (1)
- `GetAuthToken` → ext.ExtLLMAuthServiceGetAuthTokenResponse

## `client.magazine` — bale.magazine.v1.Magazine  (9)
- `GetMessageUpvoters` → pb.GetMessageUpvotersResponse
- `GetMyUpvotes` → pb.GetMyUpvotesResponse
- `GetSimilarPosts` → pb.GetSimilarPostsResponse
- `LoadCategories` → pb.LoadCategoriesResponse
- `LoadCategoryFeedMessages` → pb.LoadCategoryFeedMessagesResponse
- `LoadFeedMessages` → pb.T_H_54329
- `LoadInternalFeedMessages` → pb.T_H_54329
- `RevokeUpvotedPost` → pb.RevokeUpvotedPostResponse
- `UpvotePost` → pb.UpvotePostResponse

## `client.market` — bale.market.v1.Market  (26)
- `AcceptCampaignMarket` → pb.T_Ou
- `AcceptMarketJoinRequest` → pb.T_Ou
- `CreateMarketJoinRequest` → pb.CreateMarketJoinRequestResponse
- `CreateTag` → pb.CreateTagResponse
- `GetCategoriesList` → pb.GetCategoriesListResponse
- `GetCategoryMarkets` → pb.GetCategoryMarketsResponse
- `GetCategoryProducts` → pb.GetCategoryProductsResponse
- `GetIndexedProducts` → pb.GetIndexedProductsResponse
- `GetMarket` → pb.GetMarketResponse
- `GetMarketJoinRequests` → pb.GetMarketJoinRequestsResponse
- `GetMarketsPendingJoinRequest` → pb.GetMarketsPendingJoinRequestResponse
- `GetNumberOfSales` → pb.GetNumberOfSalesResponse
- `GetOnboardingStatus` → pb.GetOnboardingStatusResponse
- `GetPendingCampaignMarkets` → pb.GetPendingCampaignMarketsResponse
- `GetStores` → pb.T_sG_88717
- `GetTags` → pb.GetTagsResponse
- `GetTopMarkets` → pb.GetTopMarketsResponse
- `GetYaldaStores` → pb.T_sG_88717
- `RejectCampaignMarket` → pb.T_Ou
- `RejectMarketJoinRequest` → pb.T_Ou
- `SetGenericDeepLinks` → pb.T_Ou
- `SetMarketBanners` → pb.T_Ou
- `SetOnboardingData` → pb.SetOnboardingDataResponse
- `SetPopularSearches` → pb.T_Ou
- `SubmitMarketFeedback` → pb.T_Ou
- `UpdateMarketInfo` → pb.T_Ou

## `client.maviz_stream` — bale.maviz.v1.MavizStream  (4)
- `GetDifference` → pb.GetDifferenceResponse
- `SubscribeToThreadUpdates` → pb.T_Ou
- `SubscribeToUpdates` → pb.SubscribeToUpdatesResponse _(streaming)_
- `UnsubscribeFromThreadUpdates` → pb.T_Ou

## `client.meet` — bale.meet.v1.Meet  (30)
- `AcceptCall` → pb.T_h_14892
- `AnswerCallJoinRequest` → pb.T_Ou
- `AskToJoinCall` → pb.T_Ou
- `DeleteCallLogs` → pb.T_Ou
- `DeleteStream` → pb.T_Ou
- `DiscardCall` → pb.T_h_14892
- `GenerateCallLink` → pb.GenerateCallLinkResponse
- `GetCallLinkDetails` → pb.GetCallLinkDetailsResponse
- `GetCallLogs` → pb.GetCallLogsResponse
- `GetCallState` → pb.GetCallStateResponse
- `GetGroupCall` → pb.GetGroupCallResponse
- `GetOngoingCalls` → pb.GetOngoingCallsResponse
- `GetWssURL` → pb.GetWssURLResponse
- `InviteToCall` → pb.InviteToCallResponse
- `JoinGroupCall` → pb.JoinGroupCallResponse
- `LeaveGroupCall` → pb.LeaveGroupCallResponse
- `MuteParticipant` → pb.T_Ou
- `ReceiveCall` → pb.T_Ou
- `RemoveParticipant` → pb.T_Ou
- `SendCallReaction` → pb.T_Ou
- `SendFanoosEvent` → pb.T_Ou
- `SetLinkTitle` → pb.T_Ou
- `StartCall` → pb.T_h_14892
- `StartGroupCall` → pb.StartGroupCallResponse
- `StartRecording` → pb.T_Ou
- `StartStream` → pb.StartStreamResponse
- `StopRecording` → pb.T_Ou
- `SubmitCallFeedback` → pb.T_Ou
- `TakeCallAction` → pb.TakeCallActionResponse
- `UpdateLayout` → pb.T_Ou

## `client.message_stream` — bale.message_stream.v1.MessageStream  (2)
- `CancelMessageStream` → pb.CancelMessageStreamResponse
- `ReceiveMessageStream` → pb.ReceiveMessageStreamResponse

## `client.messaging` — bale.messaging.v2.Messaging  (43)
- `ArchiveDialogs` → pb.T_Ou
- `ClearChat` → pb.T_B_
- `CreateFolder` → pb.CreateFolderResponse
- `CreateReservedFolder` → pb.CreateReservedFolderResponse
- `CreateThread` → pb.CreateThreadResponse
- `CreateTopic` → pb.CreateTopicResponse
- `DeleteChat` → pb.T_B_
- `DeleteFolder` → pb.T_Ou
- `DeleteMessage` → pb.T_B_
- `DeleteTopic` → pb.T_Ou
- `EditFolder` → pb.EditFolderResponse
- `EditTopic` → pb.T_Ou
- `FetchProtectedMessage` → pb.FetchProtectedMessageResponse
- `ForwardMessages` → pb.T_pQ
- `GetDiscussionMessage` → pb.GetDiscussionMessageResponse
- `GetMessagesRepliesInfo` → pb.GetMessagesRepliesInfoResponse
- `GetTopicByID` → pb.GetTopicByIDResponse
- `GetTopics` → pb.GetTopicsResponse
- `LoadDialogs` → pb.LoadDialogsResponse
- `LoadFolderDialogs` → pb.LoadFolderDialogsResponse
- `LoadFolders` → pb.LoadFoldersResponse
- `LoadGroupedDialogs` → pb.LoadGroupedDialogsResponse
- `LoadHistory` → pb.LoadHistoryResponse
- `LoadPeerDialogs` → pb.LoadPeerDialogsResponse
- `LoadPeers` → pb.LoadPeersResponse
- `LoadPinnedDialogs` → pb.LoadPinnedDialogsResponse
- `LoadPinnedMessages` → pb.LoadPinnedMessagesResponse
- `LoadReplies` → pb.LoadRepliesResponse
- `MarkDialogsAsRead` → pb.T_B_
- `MarkDialogsAsUnread` → pb.T_B_
- `MentionRead` → pb.T_Ou
- `MessageRead` → pb.T_Ou
- `MessageReceived` → pb.T_Ou
- `PinDialogs` → pb.PinDialogsResponse
- `PinMessage` → pb.T_Ou
- `ReorderFolders` → pb.ReorderFoldersResponse
- `ReorderPinnedDialogs` → pb.ReorderPinnedDialogsResponse
- `SendMessage` → pb.T_pQ
- `SendMultiMediaMessage` → pb.T_pQ
- `UnArchiveDialogs` → pb.T_Ou
- `UnPinMessages` → pb.T_Ou
- `UnpinDialogs` → pb.T_Ou
- `UpdateMessage` → pb.T_pQ

## `client.micro_banki` — bale.microbanki.v1.MicroBanki  (3)
- `GetBamServiceToken` → pb.GetBamServiceTokenResponse
- `GetMoneyRequestDetails` → pb.GetMoneyRequestDetailsResponse
- `GetMoneyRequestPaymentList` → pb.GetMoneyRequestPaymentListResponse

## `client.my_bank` — bale.my_bank.v1.MyBank  (1)
- `GetMyBank` → ext.ExtMyBankGetMyBankResponse

## `client.negah` — bale.negah.v1.Negah  (1)
- `GetMessageSeenList` → ext.ExtNegahGetMessageSeenListResponse

## `client.organizations` — bale.organizations.v1.Organizations  (2)
- `GetUserOrganizationInfo` → pb.GetUserOrganizationInfoResponse
- `GetUserOrganizationalContacts` → pb.GetUserOrganizationalContactsResponse

## `client.pfm` — bale.pfm.v1.Pfm  (15)
- `AddDetailToTransaction` → pb.T_Ou
- `AddTransactionTags` → pb.T_Ou
- `AddUserTags` → pb.T_Ou
- `FilterTaggedTransactions` → pb.FilterTaggedTransactionsResponse
- `GetSubTransactions` → pb.GetSubTransactionsResponse
- `GetTransactionTags` → pb.GetTransactionTagsResponse
- `GetUserAccounts` → pb.GetUserAccountsResponse
- `GetUserTags` → pb.GetUserTagsResponse
- `LoadTransactions` → pb.LoadTransactionsResponse
- `LoadTransactionsByIDs` → pb.LoadTransactionsByIDsResponse
- `RemoveTransaction` → pb.T_Ou
- `RemoveTransactionTags` → pb.T_Ou
- `RemoveUserTags` → pb.T_Ou
- `ReviveTransaction` → pb.T_Ou
- `SplitTransaction` → pb.SplitTransactionResponse

## `client.poll` — bale.poll.v1.Poll  (5)
- `ClosePoll` → pb.T_Ou
- `CreatePoll` → pb.CreatePollResponse
- `GetFullPollResult` → pb.GetFullPollResultResponse
- `GetPollResults` → pb.GetPollResultsResponse
- `Vote` → pb.VoteResponse

## `client.premium` — bale.premium.v1.Premium  (7)
- `CalculateDiscountedPrice` → pb.CalculateDiscountedPriceResponse
- `GetBadges` → pb.GetBadgesResponse
- `GetPackages` → pb.GetPackagesResponse
- `IsPremium` → pb.IsPremiumResponse
- `IsPremiumBatch` → pb.IsPremiumBatchResponse
- `PurchasePackage` → pb.PurchasePackageResponse
- `SetUserBadge` → pb.T_Ou

## `client.presence` — bale.presence.v1.Presence  (11)
- `GetContactsPresences` → pb.GetContactsPresencesResponse
- `GetGroupMembersPresences` → pb.GetGroupMembersPresencesResponse
- `GetGroupOnlineCount` → pb.GetGroupOnlineCountResponse
- `GetUsersPresence` → pb.GetUsersPresenceResponse
- `SetOnline` → pb.T_Ou
- `StopTyping` → pb.T_Ou
- `SubscribeFromGroupOnline` → pb.T_Ou
- `SubscribeFromOnline` → pb.T_Ou
- `SubscribeToGroupOnline` → pb.T_Ou
- `SubscribeToOnline` → pb.T_Ou
- `Typing` → pb.T_Ou

## `client.ramz` — bale.ramz.v1.Ramz  (7)
- `CheckPassword` → pb.CheckPasswordResponse
- `CheckPasswordSet` → pb.CheckPasswordSetResponse
- `DeletePassword` → pb.DeletePasswordResponse
- `ForgetPassword` → pb.ForgetPasswordResponse
- `SendOTP` → pb.SendOTPResponse
- `SetPassword` → pb.SetPasswordResponse
- `ValidateOTP` → pb.ValidateOTPResponse

## `client.recommender` — bale.recommender.v1.Recommender  (4)
- `GetChannelRecommendations` → pb.GetChannelRecommendationsResponse
- `GetGroupsRecommendation` → pb.GetGroupsRecommendationResponse
- `GetRelatedChannels` → pb.GetRelatedChannelsResponse
- `GetRelatedGroups` → pb.GetRelatedGroupsResponse

## `client.report` — bale.report.v1.Report  (2)
- `ReportDismiss` → pb.T_Ou
- `ReportInappropriateContent` → pb.T_Ou

## `client.sap` — bale.sap.v1.Sap  (16)
- `AddDestinationCards` → pb.AddDestinationCardsResponse
- `AddNewCards` → pb.AddNewCardsResponse
- `DeliverOtp` → pb.DeliverOtpResponse
- `EditCardExpirationDate` → pb.T_Ou
- `EnrollNewCard` → pb.EnrollNewCardResponse
- `GetCardInfo` → pb.GetCardInfoResponse
- `GetCards` → pb.GetCardsResponse
- `GetDefaultCard` → pb.GetDefaultCardResponse
- `GetDestinationCardInfo` → pb.GetDestinationCardInfoResponse
- `GetDestinationCards` → pb.GetDestinationCardsResponse
- `ReactivateApp` → pb.ReactivateAppResponse
- `RemoveCard` → pb.T_Ou
- `RemoveDefaultCard` → pb.T_Ou
- `RemoveDestinationCards` → pb.T_Ou
- `SetDefaultCard` → pb.T_Ou
- `TransferMoneyByCard` → pb.TransferMoneyByCardResponse

## `client.scheduler` — bale.schedule.v1.Scheduler  (6)
- `ExecuteTaskNow` → pb.T_Ou
- `ListTasks` → pb.ListTasksResponse
- `PeersWithScheduleTask` → pb.PeersWithScheduleTaskResponse
- `ReScheduleTask` → pb.T_Ou
- `ScheduleTask` → pb.ScheduleTaskResponse
- `UnScheduleTask` → pb.UnScheduleTaskResponse

## `client.search` — bale.search.v1.Search  (12)
- `RecommendPeer` → pb.RecommendPeerResponse
- `SearchContent` → pb.SearchContentResponse
- `SearchDialog` → pb.SearchDialogResponse
- `SearchMarket` → pb.SearchMarketResponse
- `SearchMarketPopular` → pb.SearchMarketPopularResponse
- `SearchMedia` → pb.SearchMediaResponse
- `SearchMembers` → pb.SearchMembersResponse
- `SearchMessageMore` → pb.T_iF_88717
- `SearchMessages` → pb.T_iF_88717
- `SearchPeer` → pb.SearchPeerResponse
- `SearchProduct` → pb.SearchProductResponse
- `UpdateSearchContentClick` → pb.T_Ou

## `client.shared_media_service` — bale.shared_media.v1.SharedMediaService  (2)
- `GetActiveSharedMedia` → pb.GetActiveSharedMediaResponse
- `LoadMedia` → pb.LoadMediaResponse

## `client.story` — bale.story.v1.Story  (23)
- `AddBotStory` → pb.T_u_70056
- `AddChannelStory` → pb.T_u_70056
- `AddStory` → pb.T_u_70056
- `CanAddBotStory` → pb.CanAddBotStoryResponse
- `CheckLinkValidity` → pb.T_Ou
- `GetBotStories` → pb.GetBotStoriesResponse
- `GetChannelStories` → pb.GetChannelStoriesResponse
- `GetDefaultStoryBackgrounds` → pb.GetDefaultStoryBackgroundsResponse
- `GetMostPopularStories` → pb.GetMostPopularStoriesResponse
- `GetStories` → pb.GetStoriesResponse
- `GetStoriesByList` → pb.GetStoriesByListResponse
- `GetStoryById` → pb.GetStoryByIdResponse
- `GetStoryReactionEmojis` → pb.GetStoryReactionEmojisResponse
- `GetStoryTags` → pb.GetStoryTagsResponse
- `GetStoryWidgets` → pb.GetStoryWidgetsResponse
- `GetUserPrivacyConfig` → pb.GetUserPrivacyConfigResponse
- `GetUserStoryConfig` → pb.GetUserStoryConfigResponse
- `GetViewers` → pb.GetViewersResponse
- `GetViewersCount` → pb.GetViewersCountResponse
- `ReactToStory` → pb.T_Ou
- `RemoveStory` → pb.T_Ou
- `SetUserPrivacyConfig` → pb.SetUserPrivacyConfigResponse
- `SetUserStoryConfig` → pb.SetUserStoryConfigResponse

## `client.timche` — bale.timche.v1.Timche  (5)
- `AskBotReviewCallback` → pb.AskBotReviewCallbackResponse
- `GetBotPage` → pb.GetBotPageResponse
- `GetHomePage` → pb.GetHomePageResponse
- `GetSectionPage` → pb.GetSectionPageResponse
- `SubmitReview` → pb.SubmitReviewResponse

## `client.tldr` — bale.tldr.v1.TLDR  (2)
- `GetLinkPreview` → pb.GetLinkPreviewResponse
- `GetLinkSummary` → pb.GetLinkSummaryResponse

## `client.top_peer` — bale.top_peer.v1.TopPeer  (2)
- `GetTopPeer` → pb.GetTopPeerResponse
- `RemovePeer` → pb.RemovePeerResponse

## `client.ai` — bale.turing.v1.AI  (2)
- `GetTranscript` → pb.GetTranscriptResponse
- `SendEvent` → pb.T_Ou

## `client.users` — bale.users.v1.Users  (36)
- `AddCard` → pb.T_Ou
- `AddContact` → pb.T_B_
- `BlockUser` → pb.T_B_
- `ChangeDefaultCardNumber` → pb.T_B_
- `ChangePhoneNumber` → pb.T_Ou
- `CheckNickName` → pb.BoolValue
- `ConfirmPhoneNumber` → pb.T_Ou
- `EditAbout` → pb.T_B_
- `EditAvatar` → pb.EditAvatarResponse
- `EditBirthDate` → pb.T_Ou
- `EditMyPreferredLanguages` → pb.T_B_
- `EditMyTimeZone` → pb.T_B_
- `EditName` → pb.T_B_
- `EditNickName` → pb.T_B_
- `EditSex` → pb.T_Ou
- `EditUserLocalName` → pb.T_B_
- `GetContacts` → pb.GetContactsResponse
- `GetFullUser` → pb.GetFullUserResponse
- `GetUserFullPrivacy` → pb.GetUserFullPrivacyResponse
- `GetUserPrivacyStatus` → pb.GetUserPrivacyStatusResponse
- `GetUsersDefaultCardNumber` → pb.GetUsersDefaultCardNumberResponse
- `ImportContacts` → pb.ImportContactsResponse
- `IsNameAllowed` → pb.BoolValue
- `LoadAvatars` → pb.LoadAvatarsResponse
- `LoadBlockedUsers` → pb.LoadBlockedUsersResponse
- `LoadFullUsers` → pb.T_q_53871
- `LoadFullUsersSequentially` → pb.T_q_53871
- `LoadUsers` → pb.LoadUsersResponse
- `NotifyAboutDeviceInfo` → pb.T_Ou
- `RemoveAvatar` → pb.T_B_
- `RemoveContact` → pb.T_B_
- `RemoveDefaultCardNumber` → pb.T_B_
- `ResetContacts` → pb.T_Ou
- `SearchContacts` → pb.SearchContactsResponse
- `SetUserPrivacyStatus` → pb.T_Ou
- `UnblockUser` → pb.T_B_

## `client.configs` — bale.v1.Configs  (3)
- `EditParameter` → pb.T_B_
- `GetInAppUpdate` → pb.GetInAppUpdateResponse
- `GetParameters` → pb.GetParametersResponse

## `client.images` — bale.v1.Images  (10)
- `AddGif` → pb.T_B_
- `AddStickerCollection` → pb.T_k_16349
- `AddStickerPack` → pb.T_B_
- `GetSavedGifs` → pb.GetSavedGifsResponse
- `LoadOwnStickers` → pb.LoadOwnStickersResponse
- `LoadStickerCollection` → pb.LoadStickerCollectionResponse
- `RemoveGif` → pb.T_B_
- `RemoveStickerCollection` → pb.T_k_16349
- `RemoveStickerPack` → pb.T_B_
- `UseGif` → pb.T_Ou

## `client.wallet` — bale.wallet.v1.Wallet  (13)
- `ActivateWallet` → pb.T_Ou
- `CashOutFromWallet` → pb.T_Ou
- `GetMoneyRequestPaymentTokenByCard` → pb.GetMoneyRequestPaymentTokenByCardResponse
- `GetMyWallets` → pb.GetMyWalletsResponse
- `GetPaymentTokenByCard` → pb.GetPaymentTokenByCardResponse
- `GetWalletChargeToken` → pb.GetWalletChargeTokenResponse
- `GetWalletContracts` → pb.GetWalletContractsResponse
- `GetWalletInvoice` → pb.GetWalletInvoiceResponse
- `PayByWallet` → pb.T_Ou
- `PayMoneyRequestByWallet` → pb.T_Ou
- `VerifyCashOut` → pb.VerifyCashOutResponse
- `VerifyPeer` → pb.VerifyPeerResponse
- `VerifyQRCode` → pb.VerifyQRCodeResponse

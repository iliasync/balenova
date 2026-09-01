"""Generated registry for RPCs recovered from the official Bale Web build."""

from typing import Any

from bale.proto import recovered_pb2 as _pb

pb: Any = _pb

RECOVERED_METHODS = {
    (
        'bale.BankAccountPreferences.v1.BankAccountPreferences',
        'ActivateYaraMessaging',
    ): (
        pb.RecoveredMessage0092,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.BankAccountPreferences.v1.BankAccountPreferences',
        'EditPreference',
    ): (
        pb.RecoveredMessage0090,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.BankAccountPreferences.v1.BankAccountPreferences',
        'GetPreferences',
    ): (
        pb.RecoveredMessage0091,
        pb.RecoveredMessage0089,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'BuildAudienceQuery',
    ): (
        pb.RecoveredMessage0029,
        pb.RecoveredMessage0032,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'CalculatePrice',
    ): (
        pb.RecoveredMessage0037,
        pb.RecoveredMessage0038,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'CreateAutomatedAudience',
    ): (
        pb.RecoveredMessage0030,
        pb.RecoveredMessage0031,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'EstimateChannelSponsoredIncome',
    ): (
        pb.RecoveredMessage0026,
        pb.RecoveredMessage0027,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'GetAllPaymentHistory',
    ): (
        pb.RecoveredMessage0047,
        pb.RecoveredMessage0058,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'GetChannelSponsoredIncomeReport',
    ): (
        pb.RecoveredMessage0028,
        pb.RecoveredMessage0025,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'GetChannelUndepositedIncomes',
    ): (
        pb.RecoveredMessage0039,
        pb.RecoveredMessage0051,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'GetInvoiceContent',
    ): (
        pb.RecoveredMessage0043,
        pb.RecoveredMessage0060,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'GetLegalOrgChannels',
    ): (
        pb.RecoveredMessage0040,
        pb.RecoveredMessage0052,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'MergeCustomIncomeRecords',
    ): (
        pb.RecoveredMessage0053,
        pb.RecoveredMessage0041,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'MergeIncreaseCreditRecords',
    ): (
        pb.RecoveredMessage0059,
        pb.RecoveredMessage0062,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'RetryFailedAutoSentInvoice',
    ): (
        pb.RecoveredMessage0034,
        pb.RecoveredMessage0033,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'SendInvoiceForPaymentHistoryRecord',
    ): (
        pb.RecoveredMessage0046,
        pb.RecoveredMessage0055,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'SendLegalOrgChannelIncome',
    ): (
        pb.RecoveredMessage0050,
        pb.RecoveredMessage0057,
    ),
    (
        'bale.advertisement.v1.Advertisement',
        'SetCapacityMaxViews',
    ): (
        pb.RecoveredMessage0035,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'CashPaymentCallback',
    ): (
        pb.RecoveredMessage0217,
        pb.RecoveredMessage0209,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetAdminStationList',
    ): (
        pb.RecoveredMessage0226,
        pb.RecoveredMessage0223,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetArbaeenCurrenciesList',
    ): (
        pb.RecoveredMessage0242,
        pb.RecoveredMessage0227,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetArbaeenCurrencyPrice',
    ): (
        pb.RecoveredMessage0239,
        pb.RecoveredMessage0206,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetArbaeenPaymentToken',
    ): (
        pb.RecoveredMessage0208,
        pb.RecoveredMessage0233,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetListOfArbaeenDeliveryStations',
    ): (
        pb.RecoveredMessage0231,
        pb.RecoveredMessage0241,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetListOfBoxOffice',
    ): (
        pb.RecoveredMessage0214,
        pb.RecoveredMessage0219,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetListOfBranches',
    ): (
        pb.RecoveredMessage0210,
        pb.RecoveredMessage0218,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetListOfStates',
    ): (
        pb.RecoveredMessage0220,
        pb.RecoveredMessage0213,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetRate',
    ): (
        pb.RecoveredMessage0225,
        pb.RecoveredMessage0211,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetSuggestedGroups',
    ): (
        pb.RecoveredMessage0215,
        pb.RecoveredMessage0224,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'GetValidArbaeenBanks',
    ): (
        pb.RecoveredMessage0228,
        pb.RecoveredMessage0236,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'LoadArbaeenHistory',
    ): (
        pb.RecoveredMessage0237,
        pb.RecoveredMessage0229,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'SendOTP',
    ): (
        pb.RecoveredMessage0240,
        pb.RecoveredMessage0221,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'StartBot',
    ): (
        pb.RecoveredMessage0222,
        pb.RecoveredMessage0212,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'UserHasAccess',
    ): (
        pb.RecoveredMessage0207,
        pb.RecoveredMessage0243,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'VerifyOTP',
    ): (
        pb.RecoveredMessage0234,
        pb.RecoveredMessage0216,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'VerifyUserArbaeenAuthority',
    ): (
        pb.RecoveredMessage0238,
        pb.RecoveredMessage0235,
    ),
    (
        'bale.arbaeen.v1.Arbaeen',
        'VerifyUserArbaeenExtraInfo',
    ): (
        pb.RecoveredMessage0232,
        pb.RecoveredMessage0230,
    ),
    (
        'bale.bill.v1.Bill',
        'CreateSavedBill',
    ): (
        pb.RecoveredMessage0137,
        pb.RecoveredMessage0135,
    ),
    (
        'bale.bill.v1.Bill',
        'DeleteSavedBills',
    ): (
        pb.RecoveredMessage0143,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.bill.v1.Bill',
        'GetBillHistory',
    ): (
        pb.RecoveredMessage0145,
        pb.RecoveredMessage0136,
    ),
    (
        'bale.bill.v1.Bill',
        'GetBillMenu',
    ): (
        pb.RecoveredMessage0142,
        pb.RecoveredMessage0139,
    ),
    (
        'bale.bill.v1.Bill',
        'GetSavedBills',
    ): (
        pb.RecoveredMessage0138,
        pb.RecoveredMessage0141,
    ),
    (
        'bale.bill.v1.Bill',
        'InquiryBill',
    ): (
        pb.RecoveredMessage0148,
        pb.RecoveredMessage0146,
    ),
    (
        'bale.bill.v1.Bill',
        'PayBill',
    ): (
        pb.RecoveredMessage0150,
        pb.RecoveredMessage0134,
    ),
    (
        'bale.bill.v1.Bill',
        'RenameSavedBill',
    ): (
        pb.RecoveredMessage0140,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.evex.v1.Evex',
        'GetEvexCurrenciesList',
    ): (
        pb.RecoveredMessage0195,
        pb.RecoveredMessage0192,
    ),
    (
        'bale.evex.v1.Evex',
        'GetEvexCurrencyPrice',
    ): (
        pb.RecoveredMessage0190,
        pb.RecoveredMessage0191,
    ),
    (
        'bale.evex.v1.Evex',
        'GetEvexPaymentToken',
    ): (
        pb.RecoveredMessage0203,
        pb.RecoveredMessage0204,
    ),
    (
        'bale.evex.v1.Evex',
        'GetListOfEvexDeliveryStations',
    ): (
        pb.RecoveredMessage0198,
        pb.RecoveredMessage0202,
    ),
    (
        'bale.evex.v1.Evex',
        'GetValidBanks',
    ): (
        pb.RecoveredMessage0200,
        pb.RecoveredMessage0197,
    ),
    (
        'bale.evex.v1.Evex',
        'LoadEvexHistory',
    ): (
        pb.RecoveredMessage0196,
        pb.RecoveredMessage0193,
    ),
    (
        'bale.evex.v1.Evex',
        'VerifyUserEvexAuthority',
    ): (
        pb.RecoveredMessage0194,
        pb.RecoveredMessage0201,
    ),
    (
        'bale.evex.v1.Evex',
        'VerifyUserEvexExtraInfo',
    ): (
        pb.RecoveredMessage0189,
        pb.RecoveredMessage0188,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetCurrenciesList',
    ): (
        pb.RecoveredMessage0177,
        pb.RecoveredMessage0170,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetCurrencyPrice',
    ): (
        pb.RecoveredMessage0187,
        pb.RecoveredMessage0182,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetExchangeOrderInfo',
    ): (
        pb.RecoveredMessage0185,
        pb.RecoveredMessage0173,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetExchangePaymentToken',
    ): (
        pb.RecoveredMessage0176,
        pb.RecoveredMessage0183,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetInitialConfig',
    ): (
        pb.RecoveredMessage0181,
        pb.RecoveredMessage0174,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetListOfDeliveryStations',
    ): (
        pb.RecoveredMessage0169,
        pb.RecoveredMessage0205,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetTravelCurrencyOrderInDetail',
    ): (
        pb.RecoveredMessage0184,
        pb.RecoveredMessage0186,
    ),
    (
        'bale.exchange.v1.Exchange',
        'GetUserIcmsInfo',
    ): (
        pb.RecoveredMessage0172,
        pb.RecoveredMessage0199,
    ),
    (
        'bale.exchange.v1.Exchange',
        'LoadExchangeHistory',
    ): (
        pb.RecoveredMessage0171,
        pb.RecoveredMessage0178,
    ),
    (
        'bale.exchange.v1.Exchange',
        'VerifyUserExchangeAuthority',
    ): (
        pb.RecoveredMessage0175,
        pb.RecoveredMessage0180,
    ),
    (
        'bale.garson.v1.Garson',
        'SearchServices',
    ): (
        pb.RecoveredMessage0085,
        pb.RecoveredMessage0084,
    ),
    (
        'bale.groups.v1.Groups',
        'SetSignMessages',
    ): (
        pb.RecoveredMessage0096,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.groups.v1.Groups',
        'SetSlowMode',
    ): (
        pb.RecoveredMessage0095,
        pb.RecoveredMessage0094,
    ),
    (
        'bale.kifpool.v1.Kifpool',
        'FeeInquiry',
    ): (
        pb.RecoveredMessage0098,
        pb.RecoveredMessage0097,
    ),
    (
        'bale.pishvaz.v1.Pishvaz',
        'GetMarketingToolsConfig',
    ): (
        pb.RecoveredMessage0020,
        pb.RecoveredMessage0001,
    ),
    (
        'bale.pishvaz.v1.Pishvaz',
        'GetOnboardingPageData',
    ): (
        pb.RecoveredMessage0014,
        pb.RecoveredMessage0011,
    ),
    (
        'bale.pishvaz.v1.Pishvaz',
        'SetMarketingToolAction',
    ): (
        pb.RecoveredMessage0018,
        pb.RecoveredMessage0004,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'AuthenticateUser',
    ): (
        pb.RecoveredMessage0257,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'CreateOrder',
    ): (
        pb.RecoveredMessage0248,
        pb.RecoveredMessage0133,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetChargeToken',
    ): (
        pb.RecoveredMessage0262,
        pb.RecoveredMessage0266,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetDepth',
    ): (
        pb.RecoveredMessage0250,
        pb.RecoveredMessage0244,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetOrder',
    ): (
        pb.RecoveredMessage0261,
        pb.RecoveredMessage0263,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetOrders',
    ): (
        pb.RecoveredMessage0265,
        pb.RecoveredMessage0264,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetSession',
    ): (
        pb.RecoveredMessage0247,
        pb.RecoveredMessage0246,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetTickers',
    ): (
        pb.RecoveredMessage0251,
        pb.RecoveredMessage0254,
    ),
    (
        'bale.sarrafi.v1.Sarrafi',
        'GetWallet',
    ): (
        pb.RecoveredMessage0259,
        pb.RecoveredMessage0258,
    ),
    (
        'bale.story.v1.Story',
        'GetAllStories',
    ): (
        pb.RecoveredMessage0112,
        pb.RecoveredMessage0111,
    ),
}

__all__ = ["RECOVERED_METHODS"]

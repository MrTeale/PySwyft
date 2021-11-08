""" Handle account endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints"""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Accounts, self).__init__(endpoint, method=self.METHOD)


@endpoint('user/')
class AccountDetails(Accounts):
    """AccountDetails - class to handle the account details endpoints"""
    def __init__(self):
        super(AccountDetails, self).__init__()


@endpoint('user/settings/', "POST", 200)
class AccountSettings(Accounts):
    """AccountSettings - class to handle the account settings endpoints"""
    def __init__(self, favouriteID=None, favouriteStatus=None, analyticsOptOut=None, toggleSMSRecovery=None):
        super(AccountSettings, self).__init__()

        data = {}
        if favouriteID is not None:
            data['favouriteAsset'] = {'assetId': favouriteID,
                                      'favStatus': favouriteStatus}

        if analyticsOptOut is not None:
            data['analyticsOptOut'] = analyticsOptOut

        if toggleSMSRecovery is not None:
            data['toggleSMSRecovery'] = toggleSMSRecovery

        self.data = {'data': data}


@endpoint('user/verification/')
class AccountVerificationInfo(Accounts):
    """AccountVerificationInfo - class to handle the account verification endpoints"""
    def __init__(self):
        super(AccountVerificationInfo, self).__init__()


@endpoint('user/verification/email/', "POST", 200)
class AccountStartVerificationEmail(Accounts):
    """AccountStartVerificationEmail - class to handle the account verification email endpoints"""
    def __init__(self):
        super(AccountStartVerificationEmail, self).__init__()


@endpoint('user/verification/email/')
class AccountCheckVerificationEmail(Accounts):
    """AccountCheckVerificationEmail - class to handle the account verification email endpoints"""
    def __init__(self):
        super(AccountCheckVerificationEmail, self).__init__()


@endpoint('user/verification/phone/')
class AccountCheckVerificationPhone(Accounts):
    """AccountCheckVerificationPhone - class to handle the account verification phone endpoints"""
    def __init__(self, token):
        super(AccountCheckVerificationPhone, self).__init__()
        self.params = {'token': token}


# TODO: Check this. Appears to be having some issues with this endpoint
@endpoint('user/verification/phone/', "POST", 200)
class AccountStartVerificationPhone(Accounts):
    """AccountStartVerificationPhone - class to handle the account verification phone endpoints"""
    def __init__(self, token):
        super(AccountStartVerificationPhone, self).__init__()
        self.params = {'token': token}


@endpoint('user/affiliations/')
class AccountAffiliations(Accounts):
    """AccountAffiliations - class to handle the account affiliations endpoints"""
    def __init__(self):
        super(AccountAffiliations, self).__init__()


@endpoint('user/balance/')
class AccountBalance(Accounts):
    """AccountBalance - class to handle the account balance endpoints"""
    def __init__(self):
        super(AccountBalance, self).__init__()


@endpoint('user/currency/', "POST", 200)
class AccountCurrency(Accounts):
    """Currency - class to handle the account currency endpoints"""
    def __init__(self, asset_number):
        super(AccountCurrency, self).__init__()
        self.data = {"profile": { "defaultAsset": asset_number}}


@endpoint('user/statistics/')
class AccountStatistics(Accounts):
    """AccountStatistics - class to handle the account statistics endpoints"""
    def __init__(self):
        super(AccountStatistics, self).__init__()


@endpoint('user/progress/')
class AccountProgress(Accounts):
    """AccountProgress - class to handle the account progress endpoints"""
    def __init__(self):
        super(AccountProgress, self).__init__()


@endpoint('user/promotions/')
class AccountPromotions(Accounts):
    """AccountPromotions - class to handle the account promotions endpoints"""
    def __init__(self):
        super(AccountPromotions, self).__init__()


@endpoint('user/taxReport/')
class AccountTaxReport(Accounts):
    """AccountTaxReport - class to handle the account tax report endpoints"""
    def __init__(self, from_data, offset, to_date, output_type):
        super(AccountTaxReport, self).__init__()
        self.params = {'from': from_date, 'offset': offset, 'to': to_date, 'type': output_type}
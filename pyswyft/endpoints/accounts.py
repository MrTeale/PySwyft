""" Handle account endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod

# TODO: Add Save Verification Info endpoints
# TODO: Add Start Email Verification endpoints
# TODO: Add verification phone number endpoints
# TODO: Add Tax Report

class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints"""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self, accountID=None):
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Accounts, self).__init__(endpoint, method=self.METHOD)


@endpoint('user/')
class AccountDetails(Accounts):
    """AccountDetails - class to handle the account details endpoints"""
    def __init__(self):
        super(AccountDetails, self).__init__()


@endpoint('user/settings/', "POST", 200)
class AccountSettings(Accounts):
    """AccountSettings - class to handle the account settings endpoints"""
    def __init__(self, data):
        super(AccountSettings, self).__init__()
        self.data = data


@endpoint('user/verification/')
class AccountVerificationInfo(Accounts):
    """AccountVerificationInfo - class to handle the account verification endpoints"""
    def __init__(self):
        super(AccountVerificationInfo, self).__init__()


@endpoint('user/verification/email/')
class AccountVerificationEmail(Accounts):
    """AccountVerificationEmail - class to handle the account verification email endpoints"""
    def __init__(self):
        super(AccountVerificationEmail, self).__init__()


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
    def __init__(self, data):
        super(AccountCurrency, self).__init__()
        self.data = data


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

""" Handle account endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints"""

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Accounts, self).__init__(endpoint, method=self.METHOD)


@endpoint('user/', "GET")
class AccountDetails(Accounts):
    """Send a request to Swyftx Profile API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/profile/get-profile
    URL: https://api.swyftx.com.au/user/
    Method: GET

    Returns:
        The user profile details
        e.g.
        {
            "profile": {
                "dob": 757346400000,
                "name": {
                    "first": "John",
                    "last": "Doe"
                },
                "email": "john.doe@example.com",
                "phone": "+614XXXXXXXX",
                "currency": {
                    "id": 1,
                    "code": "AUD"
                },
                "user_hash": "xxxx...xxxx",
                "metadata": {
                    "mfa_enabled": true,
                    "mfa_enrolled": true
                },
                "userSettings": {
                    "favouriteAssets": {
                        "assetId": true
                    },
                    "analyticsOptOut": true,
                    "activeAffil": true,
                    "disableSMSRecovery": false,
                    "dashboardSettings": [
                        {
                            "name": "favourites",
                            "display": false
                        },
                        {
                            "name": "announcement",
                            "display": true
                        }
                    ]
                }
            }
        }
    """
    def __init__(self):
        super(AccountDetails, self).__init__()


@endpoint('user/settings/', "POST", 200)
class AccountSettings(Accounts):
    """Send a request to Swyftx Account Settings API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/account-settings/account-settings
    URL: https://api.swyftx.com.au/user/settings/
    Method: POST

    Args:
        favouriteID (int): The asset ID of the favourite asset. Only required alongside FavouriteStatus
        favouriteStatus (bool): The status of the favourite asset. Only required alongside FavouriteID
        analyticsOptOut (bool): The status of the analytics opt out. Not Required
        toggleSMSRecovery (bool): The status of the SMS recovery. Not Required

    Returns:
        The user profile details
        e.g.
        {
            "profile": {
                "dob": 757346400000,
                "name": {
                    "first": "John",
                    "last": "Doe"
                },
                "email": "john.doe@example.com",
                "phone": "+614XXXXXXXX",
                "currency": {
                    "id": 1,
                    "code": "AUD"
                },
                "user_hash": "xxxx...xxxx",
                "metadata": {
                    "mfa_enabled": true,
                    "mfa_enrolled": true
                },
                "userSettings": {
                    "favouriteAssets": {
                        "assetId": true
                    },
                    "analyticsOptOut": true,
                    "activeAffil": true,
                    "disableSMSRecovery": false,
                    "dashboardSettings": [
                        {
                            "name": "favourites",
                            "display": false
                        },
                        {
                            "name": "announcement",
                            "display": true
                        }
                    ]
                }
            }
        }
    """
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


@endpoint('user/verification/', "GET")
class AccountVerificationInfo(Accounts):
    """Send a request to Swyftx Verification API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/verification/get-verification-info
    URL: https://api.swyftx.com.au/user/verification/
    Method: GET

    Returns:
        The user verification statuses
        e.g.
        {
            "verification": {
                "status": "unverified",
                "email": "verified",
                "mfa": "unverified",
                "phone": "verified",
                "identity": "unverified"
            }
        }
    """
    def __init__(self):
        super(AccountVerificationInfo, self).__init__()


@endpoint('user/verification/email/', "POST", 200)
class AccountStartVerificationEmail(Accounts):
    """Send a request to Swyftx Start Email Verification API endpoint
    triggering email to be sent to registered email

    Docs: https://docs.swyftx.com.au/#/reference/account/email-verification/start-email-verification
    URL: https://api.swyftx.com.au/user/verification/email/
    Method: POST

    Returns:
        The user email verification status
        e.g.
        {
            "success": true,
            "emailVerified": true,
            "msg": "Your email is verified"
        }
    """
    def __init__(self):
        super(AccountStartVerificationEmail, self).__init__()


@endpoint('user/verification/email/', "GET")
class AccountCheckVerificationEmail(Accounts):
    """Send a request to Swyftx Check Email Verification API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/email-verification/check-email-verification-status
    URL: https://api.swyftx.com.au/user/verification/email/
    Method: GET

    Returns:
        The user email verification status
        e.g.
        {
            "success": true,
            "emailVerified": true,
            "msg": "Your email is verified"
        }
    """
    def __init__(self):
        super(AccountCheckVerificationEmail, self).__init__()


@endpoint('user/verification/phone/', "GET")
class AccountCheckVerificationPhone(Accounts):
    """Send a request to Swyftx Check Phone Verification API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/verification/check-phone-verification-status
    URL: https://api.swyftx.com.au/user/verification/phone/{token}/
    Method: GET

    Args:
        token (str): The verification token

    Returns:
        The user phone verification status
        e.g.
        {
            "success": true,
            "phoneVerified": true,
            "msg": "Your email is verified"
        }
    """
    def __init__(self, token):
        super(AccountCheckVerificationPhone, self).__init__()
        self.params = {'token': token}


# TODO: Check this. Appears to be having some issues with this endpoint
@endpoint('user/verification/phone/', "POST", 200)
class AccountStartVerificationPhone(Accounts):
    """Send a request to Swyftx Check Start Phone Verification API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/phone-verification/start-phone-verification
    URL: https://api.swyftx.com.au/user/verification/phone/{token}/
    Method: POST

    Args:
        token (str): The verification token

    Returns:
        The user phone verification status
        e.g.
        {
            "success": true,
            "phoneVerified": true,
            "msg": "Your email is verified"
        }
    """
    def __init__(self, token):
        super(AccountStartVerificationPhone, self).__init__()
        self.params = {'token': token}


@endpoint('user/affiliations/', "GET")
class AccountAffiliations(Accounts):
    """Send a request to Swyftx Get Affiliation Info API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/affiliation/get-affiliation-info
    URL: https://api.swyftx.com.au/user/affiliations/
    Method: GET

    Returns:
        The user affiliation info
        e.g.
        {
        "referral_link": "https://swyftx.com.au/?ref=XXXXXXXXXXX",
        "referred_users": 1
        }
    """
    def __init__(self):
        super(AccountAffiliations, self).__init__()


@endpoint('user/balance/', "GET")
class AccountBalance(Accounts):
    """Send a request to Swyftx Get Account Balances API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/balance/get-account-balances
    URL: https://api.swyftx.com.au/user/balance/
    Method: GET

    Returns:
        The user currency balances
        e.g.
        [
        {"assetId": 1, "availableBalance": "100.2464"}
        ]
    """
    def __init__(self):
        super(AccountBalance, self).__init__()


@endpoint('user/currency/', "POST", 200)
class AccountCurrency(Accounts):
    """Send a request to Swyftx Set Currency API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/currency/set-currency
    URL: https://api.swyftx.com.au/user/currency/
    Method: POST

    Args:
        asset_number (str): The currency to set. e.g. 1, 3, 36

    Returns:
        The user currency balances
        e.g.
        [
        {"assetId": 1, "availableBalance": "100.2464"}
        ]
    """
    def __init__(self, asset_number):
        super(AccountCurrency, self).__init__()
        self.data = {"profile": { "defaultAsset": asset_number}}


@endpoint('user/statistics/', "GET")
class AccountStatistics(Accounts):
    """Send a request to Swyftx Account Statistics API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/statistics/statistics
    URL: https://api.swyftx.com.au/user/statistics/
    Method: GET

    Returns:
        The user account statistics regarding usage
        e.g.
        {
            "orders": 491,
            "traded": 20614.3484,
            "deposited": 5420.37,
            "withdrawn": 9400.58
        }
    """
    def __init__(self):
        super(AccountStatistics, self).__init__()


@endpoint('user/progress/', "GET")
class AccountProgress(Accounts):
    """Send a request to Swyftx Account Progress API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/progress/progress
    URL: https://api.swyftx.com.au/user/progress/
    Method: GET

    Returns:
        The user account progress for particular milestones
        e.g.
        {
            "signUp": true,
            "verified": true,
            "deposit": true,
            "trade": false,
            "refer": false,
            "completed": false
        }
    """
    def __init__(self):
        super(AccountProgress, self).__init__()


@endpoint('user/promotions/', "GET")
class AccountPromotions(Accounts):
    """Send a request to Swyftx Set Currency API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/promotions/promotions
    URL: https://api.swyftx.com.au/user/promotions/
    Method: GET

    Returns:
        Active promotions available on the account
        e.g.
        {
            "desc": "50% off fees first week",
            "ref": "bonusfee50",
            "expiry": 1593525600000
        }
    """
    def __init__(self):
        super(AccountPromotions, self).__init__()


@endpoint('user/taxReport/', "GET")
class AccountTaxReport(Accounts):
    """Send a request to Swyftx Get Tax Report API endpoint

    Docs: https://docs.swyftx.com.au/#/reference/account/tax-report/get-tax-report
    URL: https://api.swyftx.com.au/user/taxReport/
    Method: GET

    Args:
        from_date (str): The start date of the tax report
        to_date (str): The end date of the tax report
        type (str): The filetype to be outputted
        offset (int): Optional time zone offset in ms from UTC

    Returns:
        The user account tax report
        e.g.
        {
            "cryptoStatement": [
                {
                    "date": "4/06/2020",
                    "time": "14:21:03",
                    "event": "sell",
                    "asset": "AUD",
                    "amount": "500.00000000",
                    "currency": "USD",
                    "value": "343.35520439",
                    "rate": "0.68671041",
                    "audValue": "500.00000000",
                    "feeAmount": "null",
                    "feeAsset": "null",
                    "feeAudValue": "null",
                    "gst": "null",
                    "exGST": "null",
                    "depositedTo": "null",
                    "withdrawnTo": "null",
                    "withdrawalFee": "null",
                    "reference": "null",
                    "txId": "null",
                    "uuid": "null"
                }
            ],
            "fiatStatement": [
                {
                    "date": "4/06/2020",
                    "time": "14:21:03",
                    "event": "sell",
                    "asset": "AUD",
                    "amount": "500.00000000",
                    "currency": "USD",
                    "value": "343.35520439",
                    "rate": "0.68671041",
                    "audValue": "500.00000000",
                    "feeAmount": "null",
                    "feeAsset": "null",
                    "feeAudValue": "null",
                    "gst": "null",
                    "exGST": "null",
                    "depositedTo": "null",
                    "withdrawnTo": "null",
                    "withdrawalFee": "null",
                    "reference": "null",
                    "txId": "null",
                    "uuid": "null"
                }
            ],
            "openingStatements": {
                "cryptoStatement": [
                    {
                        "date": "30/06/2020",
                        "time": "23:59:59",
                        "event": "open position",
                        "asset": "USDT",
                        "amount": "23.84373701",
                        "currency": "null",
                        "value": "null",
                        "rate": "null",
                        "audValue": "33.04021869"
                    }
                ],
                "fiatStatement": [
                    {
                        "date": "30/06/2020",
                        "time": "23:59:59",
                        "event": "open position",
                        "asset": "USDT",
                        "amount": "23.84373701",
                        "currency": "null",
                        "value": "null",
                        "rate": "null",
                        "audValue": "33.04021869"
                    }
                ]
            },
            "closingStatements": {
                "cryptoStatement": [
                    {
                        "date": "30/06/2020",
                        "time": "23:59:59",
                        "event": "open position",
                        "asset": "USDT",
                        "amount": "23.84373701",
                        "currency": "null",
                        "value": "null",
                        "rate": "null",
                        "audValue": "33.04021869"
                    }
                ],
                "fiatStatement": [
                    {
                        "date": "30/06/2020",
                        "time": "23:59:59",
                        "event": "open position",
                        "asset": "USDT",
                        "amount": "23.84373701",
                        "currency": "null",
                        "value": "null",
                        "rate": "null",
                        "audValue": "33.04021869"
                    }
                ]
            }
        }
    """
    def __init__(self, from_date, to_date, output_type, offset=0):
        super(AccountTaxReport, self).__init__()
        self.params = {'from': from_date, 'offset': offset, 'to': to_date, 'type': output_type}
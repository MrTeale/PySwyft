""" Handle History endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class History(APIRequest):
    """History - class to handle the History endpoints"""

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(History, self).__init__(endpoint, method=self.METHOD)


@endpoint('history/withdraw/', 'GET')
class HistoryCurrencyWithdraw(History):
    """Send a request to Swyftx Currency Withdraw History API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/currency-withdraw-history/get-currency-withdraw-history
    URL: https://api.swyftx.com.au/history/withdraw/
    Method: GET

    Args:
        asset_code (str): The asset code to get the history for.
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of Withdraw events for a Currency.
        e.g.
        {
            "id": 1,
            "time": 1517458855347,
            "quantity": "1231.123",
            "address_id": 1,
            "status": 1
        }
    """
    def __init__(self, asset_code, limit=None, page=None, sortby=None):
        super(HistoryCurrencyWithdraw, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code) + '/'
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/deposit/', 'GET')
class HistoryCurrencyDeposit(History):
    """Send a request to Swyftx Currency Deposit History API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/currency-deposit-history/get-currency-deposit-history
    URL: https://api.swyftx.com.au/history/deposit/
    Method: GET

    Args:
        asset_code (str): The asset code to get the history for.
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of Deposit events for a Currency.
        e.g.
        {
            "id": 1,
            "time": 1517458855347,
            "quantity": "1231.123",
            "address_id": 1,
            "status": 1
        }
    """
    def __init__(self, asset_code, limit=None, page=None, sortby=None):
        super(HistoryCurrencyDeposit, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code) + '/'
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/withdraw/', 'GET')
class HistoryAllWithdraw(History):
    """Send a request to Swyftx Currency All Withdraw History API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/all-withdraw-history/get-all-withdraw-history
    URL: https://api.swyftx.com.au/history/withdraw/
    Method: GET

    Args:
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of All Withdraw events.
        e.g.
        {
            "id": 1,
            "time": 1517458855347,
            "quantity": "1231.123",
            "address_id": 1,
            "status": 1
        }
    """
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAllWithdraw, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/deposit/', 'GET')
class HistoryAllDeposit(History):
    """Send a request to Swyftx Currency All Deposit History API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/all-deposit-history/get-all-deposit-history
    URL: https://api.swyftx.com.au/history/deposit/
    Method: GET

    Args:
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of All Deposit events.
        e.g.
        {
            "id": 1,
            "time": 1517458855347,
            "quantity": "1231.123",
            "address_id": 1,
            "status": 1
        }
    """
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAllDeposit, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/all/', 'GET')
class HistoryAll(History):
    """Send a request to Swyftx Currency All History API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/currency-deposit-history/get-history
    URL: https://api.swyftx.com.au/history/all/
    Method: GET

    Args:
        type (str): The type of history to get.
        assetId (str): The asset code to get the history for.
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of All events.
        e.g.
        [
            {
                "asset": "5",
                "amount": 1.234,
                "updated": 15326574115,
                "actionType": "Deposit",
                "status": "Failed"
            },
            {
                "asset": "1",
                "amount": 1.234,
                "updated": 15326574115,
                "actionType": "Withdrawal",
                "status": "Pending"
            }
        ]
    """
    def __init__(self, type, assetId, limit=None, page=None, sortby=None):
        super(HistoryAll, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(type) + '/' + str(assetId) + '/'
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/affiliate/', 'GET')
class HistoryAffiliate(History):
    """Send a request to Swyftx Currency All affiliate API Endpoint

    Docs: https://docs.swyftx.com.au/#/reference/history/affiliate-payout-history/get-affiliate-payout-history
    URL: https://api.swyftx.com.au/history/affiliate/
    Method: GET

    Args:
        limit (int): The number of results to return.
        page (int): The page number to return.
        sortby (str): The field to sort the results by.

    Returns:
        List of All Deposit events for a Currency.
        e.g.
        [
            {
                "asset": "36",
                "amount": "1",
                "updated": "1600055580000",
                "actionType": "Affiliate Payout",
                "status": 1
            }
        ]
    """
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAffiliate, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}
""" Handle History endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class History(APIRequest):
    """History - class to handle the accounts endpoints"""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(History, self).__init__(endpoint, method=self.METHOD)


@endpoint('history/withdraw/')
class HistoryCurrencyWithdraw(History):
    """HistoryCurrencyWithdraw - class to handle the curreny withdraw endpoints"""
    def __init__(self, asset_code, limit=None, page=None, sortby=None):
        super(HistoryCurrencyWithdraw, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code) + "/"
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/deposit/')
class HistoryCurrencyDeposit(History):
    """HistoryCurrencyDeposit - class to handle the curreny deposit endpoints"""
    def __init__(self, asset_code, limit=None, page=None, sortby=None):
        super(HistoryCurrencyDeposit, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code) + "/"
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/withdraw/')
class HistoryAllWithdraw(History):
    """HistoryAllWithdraw - class to handle the curreny withdraw endpoints"""
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAllWithdraw, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/deposit/')
class HistoryAllDeposit(History):
    """HistoryAllDeposit - class to handle the curreny deposit endpoints"""
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAllDeposit, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/all/')
class HistoryAll(History):
    """HistoryAll - class to handle the all history endpoints"""
    def __init__(self, type, assetId, limit=None, page=None, sortby=None):
        super(HistoryAll, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(type) + "/" + str(assetId) + "/"
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}


@endpoint('history/affiliate/')
class HistoryAffiliate(History):
    """HistoryAffiliate - class to handle the affiliate history endpoints"""
    def __init__(self, limit=None, page=None, sortby=None):
        super(HistoryAffiliate, self).__init__()
        self.params = {'limit': limit, 'page': page, 'sortby': sortby}
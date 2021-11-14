""" Handle Markets endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class Markets(APIRequest):
    """Markets - class to handle the Markets endpoints"""

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Markets, self).__init__(endpoint, method=self.METHOD)


@endpoint('live-rates/', 'GET')
class MarketsLiveRates(Markets):
    """MarketsLiveRates - class to handle the live-rates endpoints"""
    def __init__(self, asset_code):
        super(MarketsLiveRates, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code) + "/"


@endpoint('markets/assets/', 'GET')
class MarketsAssets(Markets):
    """MarketsAssets - class to handle the markets/assets endpoints"""
    def __init__(self):
        super(MarketsAssets, self).__init__()


@endpoint('markets/info/basic/', 'GET')
class MarketsInfoBasic(Markets):
    """MarketsInfoBasic - class to handle the markets/info/basic endpoints"""
    def __init__(self, asset_code):
        super(MarketsInfoBasic, self).__init__()
        self.ENDPOINT = self.ENDPOINT + asset_code + "/"


@endpoint('markets/info/detail/', 'GET')
class MarketsInfoDetail(Markets):
    """MarketsInfoDetail - class to handle the markets/info/detail endpoints"""
    def __init__(self, asset_code):
        super(MarketsInfoDetail, self).__init__()
        self.ENDPOINT = self.ENDPOINT + asset_code + "/"
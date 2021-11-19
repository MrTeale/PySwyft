""" Handle Candles endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod
from datetime import datetime


class Candles(APIRequest):
    """Candles - class to handle the Candles endpoints"""

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Candles, self).__init__(endpoint, method=self.METHOD)


@endpoint('charts/getBars/', 'GET')
class CandlesGetBars(Candles):
    """CandlesGetBars - class to handle the CandlesGetBars endpoint"""
    def __init__(self, primary, secondary, side, resolution, timeEnd, timeStart):
        super(CandlesGetBars, self).__init__()

        converted_timeEnd = int((timeEnd - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)         # convert to milliseconds since epoch
        converted_timeStart = int((timeStart - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)     # convert to milliseconds since epoch

        self.ENDPOINT = self.ENDPOINT + str(primary) + '/' + str(secondary) + '/' + str(side) + '/'
        self.params = {'resolution': resolution, 'timeEnd': converted_timeEnd, 'timeStart': converted_timeStart}


@endpoint('charts/getLatestBar/', 'GET')
class CandlesGetLatestBar(Candles):
    """CandlesGetLatestBar - class to handle the CandlesGetLatestBar endpoint"""
    def __init__(self, primary, secondary, side, resolution):
        super(CandlesGetLatestBar, self).__init__()

        self.ENDPOINT = self.ENDPOINT + str(primary) + '/' + str(secondary) + '/' + str(side) + '/'
        self.params = {'resolution': resolution}
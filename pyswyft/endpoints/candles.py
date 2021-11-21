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
    """Send a request to Swyftx Tradingview Chart API Endpoint

    Docs: None Available. Undocumented Endpoint
    URL: https://api.swyftx.com.au/charts/getBars/
    Method: GET

    Args:
        primary (str): Primary currency
        secondary (str): Secondary currency
        side (str): Side of the trade
        resolution (str): Resolution of the candles
        timeEnd (datetime): End time of the candles
        timeStart (datetime): Start time of the candles

    Returns:
        The candles between the start and end time at the desired resolution.
        e.g.
        {'candles': [
            {
                'close': 6018.03078889,
                'high': 6119.11916734,
                'low': 6006.76506452,
                'name': '4h',
                'open': 6114.5597655,
                'time': 1637452800000,
                'volume': None
            },
            {
                'close': 6025.15327637,
                'high': 6070.54874137,
                'low': 5995.74876578,
                'name': '4h',
                 'open': 6018.50192619,
                 'time': 1637467200000,
                 'volume': None
            }
        ]}
    """
    def __init__(self, primary, secondary, side, resolution, timeEnd, timeStart):
        super(CandlesGetBars, self).__init__()

        converted_timeEnd = int((timeEnd - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)         # convert to milliseconds since epoch
        converted_timeStart = int((timeStart - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)     # convert to milliseconds since epoch

        self.ENDPOINT = self.ENDPOINT + str(primary) + '/' + str(secondary) + '/' + str(side) + '/'
        self.params = {'resolution': resolution, 'timeEnd': converted_timeEnd, 'timeStart': converted_timeStart}


@endpoint('charts/getLatestBar/', 'GET')
class CandlesGetLatestBar(Candles):
    """Send a request to Swyftx Tradingview Lastest Bar API Endpoint

    Docs: None Available. Undocumented Endpoint
    URL: https://api.swyftx.com.au/charts/getLatestBar/
    Method: GET

    Args:
        primary (str): Primary currency
        secondary (str): Secondary currency
        side (str): Side of the trade
        resolution (str): Resolution of the candles

    Returns:
        The latest candle at the desired resolution.
        e.g.
        {
            'close': '6010.2431663833561285082664603855',
            'high': '6053.241373914440973290462808762',
            'low': '6007.51334141280385186563266142525',
            'open': '6025.56898576117753950701256488875',
            'resolution': '1h',
            'side': 'ask',
            'time': 1637481600000,
            'volume': False
        }
    """
    def __init__(self, primary, secondary, side, resolution):
        super(CandlesGetLatestBar, self).__init__()

        self.ENDPOINT = self.ENDPOINT + str(primary) + '/' + str(secondary) + '/' + str(side) + '/'
        self.params = {'resolution': resolution}
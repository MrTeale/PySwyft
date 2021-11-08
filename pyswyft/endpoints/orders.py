""" Handle Orders endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class Orders(APIRequest):
    """Orders - class to handle the orders endpoints"""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Orders, self).__init__(endpoint, method=self.METHOD)


@endpoint('orders/rate/')
class OrdersExchangeRate(Orders):
    """OrdersExchangeRate - class to handle the orders exchange rate endpoints"""
    def __init__(self, buy, sell, amount=None, limit=None):
        super(OrdersExchangeRate, self).__init__()
        data = {'buy': buy, 'sell': sell}

        if amount is not None:
            data['amount'] = amount
    
        if limit is not None:
            data['limit'] = limit

        self.data = data


@endpoint('orders/')
class OrdersListAll(Orders):
    """OrdersListAll - class to handle the orders list all endpoint"""
    def __init__(self, asset_code="", limit=None, page=None):
        super(OrdersListAll, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(asset_code)
        self.params = {'limit': limit, 'page': page}


@endpoint('orders/byId/')
class OrdersGetOrder(Orders):
    """OrdersGetOrder - class to handle the specific order endpoint"""
    def __init__(self, orderID):
        super(OrdersGetOrder, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(orderID)


@endpoint('orders/', 'POST', 200)
class OrdersCreate(Orders):
    """OrdersCreate - class to handle the orders create endpoint"""
    def __init__(self, primary, secondary, quantity, assetQuantity, orderType, trigger=None):
        super(OrdersCreate, self).__init__()
        data = {'primary': primary, 'secondary': secondary, 'quantity': quantity, 'assetQuantity': assetQuantity, 'orderType': orderType}

        if trigger is not None:
            data['trigger'] = trigger

        self.data = data


@endpoint('orders/', 'PUT', 200)
class OrdersUpdate(Orders):
    """OrdersUpdate - class to handle the orders update endpoint"""
    def __init__(self, orderID, quantity, assetQuantity, trigger=None):
        super(OrdersUpdate, self).__init__()
        data = {'orderUuid': orderID, 'quantity': quantity, 'assetQuantity': assetQuantity}

        if trigger is not None:
            data['trigger'] = trigger

        self.data = data


@endpoint('user/balance/dust/', 'POST', 200)
class OrdersDust(Orders):
    """OrdersDust - class to handle the dust endpoint"""
    def __init__(self, primary, selected):
        super(OrdersDust, self).__init__()
        self.data = {'selected': selected, 'primary': primary}


@endpoint('orders/', 'DELETE', 200)
class OrdersCancel(Orders):
    """OrdersCancel - class to handle the orders cancel endpoint"""
    def __init__(self, orderID):
        super(OrdersCancel, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(orderID)
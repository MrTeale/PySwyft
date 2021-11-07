""" Handling of API Requests """

import six
from abc import ABCMeta, abstractmethod


@six.add_metaclass(ABCMeta)
class APIRequest(object):
    """ Base Class for API-request classes"""

    @abstractmethod
    def __init__(self, endpoint, method="GET", expected_status=200):
        """"""
        self._expected_status = expected_status
        self._status_code = None
        self._response = None

        self._endpoint = endpoint
        self.method = method
    
    @property
    def expected_status(self):
        return self._expected_status
    
    @property
    def status_code(self):
        return self._status_code
    
    @status_code.setter
    def status_code(self, value):
        if value != self._expected_status:
            raise ValueError("{} {} {:d}".format(self, self.method, value))
            
        self._status_code = value
    
    @property
    def response(self):
        """Response - get the response of the request"""
        return self._response
    
    @response.setter
    def response(self, value):
        """Response - set the response of the request"""
        self._response = value
    
    def __str__(self):
        """ Return the endpoint"""
        return self._endpoint
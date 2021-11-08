# -*- coding: utf-8 -*-
""" Swyftx API wrapper for Swyftx's API """

import requests
import json
import logging
from .exceptions import PySwyftError

TRADING_ENVIRONMENTS = {
    'live': 'https://api.swyftx.com.au',
    'demo': 'https://api.demo.swyftx.com.au'
}

DEFAULT_HEADERS = {
    'Content-Type': 'application/json'
}

logger = logging.getLogger(__name__)

class API(object):
    """"""
    def __init__(self, access_token, environment='demo', headers=None, request_params=None):
        """"""
        logger.info("setting up API-client for environment %s", environment)

        try:
            TRADING_ENVIRONMENTS[environment]
        except KeyError:
            logger.error("invalid environment specified: %s", environment)
            raise KeyError("invalid environment specified: %s" % environment)
        else:
            self.environment = environment
        
        self.access_token = access_token
        self.client = requests.Session()
        self._request_params = request_params if request_params else {}

        # personal token authentication
        if self.access_token:
            self.client.headers.update({'Authorization': 'Bearer %s' % self.access_token})

        self.client.headers.update(DEFAULT_HEADERS)
        if headers:
            self.client.headers.update(headers)
            logger.info('applying headers %s', ",".join(headers.keys()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

    def close(self):
        """"""
        self.client.close()

    @property
    def request_params(self):
        """request parameters"""
        return self._request_params
    
    def _request(self, method, url, requests_args, headers=None):
        """"""
        func = getattr(self.client, method)
        headers = headers if headers else {}
        response = None
        try:
            logger.info("requesting %s %s", method, url)
            response = func(url, headers=headers, **requests_args)
        except requests.exceptions.RequestException as e:
            logger.error("request %s failed: %s", url, e)
            raise e
        
        # Handle error responses
        if response.status_code >= 400:
            logger.error("request %s failed: [%d, %s]", url, response.status_code, response.content.decode('utf-8'))
            raise PySwyftError(response.status_code, response.content.decode('utf-8'))
    
        return response

    def request(self, endpoint):
        """Perform a request for the APIRequest instance 'endpoint'."""

        method = endpoint.method
        method = method.lower()
        params = None

        try:
            params =getattr(endpoint, "params")
        except AttributeError:
            # request does not have params
            params = {}
        
        headers = {}
        if hasattr(endpoint, "HEADERS"):
            headers = getattr(endpoint, "HEADERS")

        requests_args = {}
        if method == 'get':
            requests_args['params'] = params
        elif hasattr(endpoint, "data"):
            requests_args['json'] = endpoint.data

        # if any parameter for request then merge them
        requests_args.update(self.request_params)

        # Which API to access?
        url = "{}/{}".format(TRADING_ENVIRONMENTS[self.environment], endpoint.ENDPOINT)
        print(url)
        response = self._request(method, url, requests_args, headers=headers)
        content = response.content.decode('utf-8')
        content = json.loads(content)

        # update endpoint
        endpoint.response = content
        endpoint.status_code = response.status_code
    
        return content
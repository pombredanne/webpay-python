from .api import Account, Charges, Customers, Events
import requests
import json

class WebPay:
    """Main interface of webpay library.
    See `API reference<https://webpay.jp/docs/api/python>`.
    """

    _headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def __init__(self, key, api_base = 'https://api.webpay.jp/v1'):
        """Instantiate WebPay API client

        Attributes:
        - `key`: secret API key which is in `https://webpay.jp/settings`.
        - `api_base`: optional. Specify full URL of api base. Default is `https://api.webpay.jp/v1`.
        """
        self.key = key
        self.api_base = api_base
        self.account = Account(self)
        self.charges = Charges(self)
        self.customers = Customers(self)
        self.events = Events(self)

    def post(self, path, params):
        r = requests.post(self.api_base + path, auth = (self.key, ''), data = json.dumps(params), headers = self._headers)
        return r.json()

    def get(self, path, params = {}):
        r = requests.get(self.api_base + path, auth = (self.key, ''), data = json.dumps(params), headers = self._headers)
        return r.json()

    def delete(self, path, params = {}):
        r = requests.delete(self.api_base + path, auth = (self.key, ''), data = json.dumps(params), headers = self._headers)
        return r.json()

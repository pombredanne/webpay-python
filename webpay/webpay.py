from .api import Account, Charges, Customers
import requests
import json

class WebPay:
    """Main interface of webpay library.
    See `API reference<https://webpay.jp/docs/api/python>`.
    """
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

    def post(self, path, params):
        r = requests.post(self.api_base + path, auth = (self.key, ''), data = json.dumps(params))
        return r.json()

    def get(self, path, params = {}):
        r = requests.get(self.api_base + path, auth = (self.key, ''), params = params)
        return r.json()

    def delete(self, path, params = {}):
        r = requests.delete(self.api_base + path, auth = (self.key, ''), data = json.dumps(params))
        return r.json()

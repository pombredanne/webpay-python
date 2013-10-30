from .api import Account, Charges
import requests

class WebPay:
    def __init__(self, key, api_base = 'https://api.webpay.jp/v1'):
        self.key = key
        self.api_base = api_base
        self.account = Account(self)
        self.charges = Charges(self)

    def post(self, path, params):
        r = requests.post(self.api_base + path, auth = (self.key, ''), params = params)
        return r.json()

    def get(self, path, params = {}):
        r = requests.get(self.api_base + path, auth = (self.key, ''), params = params)
        return r.json()

    def delete(self, path, params = {}):
        r = requests.delete(self.api_base + path, auth = (self.key, ''), params = params)
        return r.json()

from webpay.model.card import Card
from .model import Model

class Token(Model):
    def __init__(self, client, data):
        Model.__init__(self, client, data, lambda k: Card if k == 'card' else None)

from webpay.model.card import Card

class Token:
    def __init__(self, client, data):
        self.__client = client
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = Card(client, v) if k == 'card' else v

from webpay.model.card import Card

class Customer:
    def __init__(self, client, data):
        self.__client = client
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = Card(client, v) if k == 'active_card' else v

    def _update_attributes(self, new_customer):
        for k, v in new_customer.__data.items():
            self.__dict__[k] = Card(self.__client, v) if k == 'active_card' else v

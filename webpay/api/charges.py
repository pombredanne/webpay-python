from webpay.model.charge import Charge

class Charges:
    def __init__(self, webpay):
        self.__client = webpay

    def create(self, **params):
        return Charge(self.__client, self.__client.post('/charges', params))

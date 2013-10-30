from webpay.model.charge import Charge
from webpay.model.entity_list import EntityList
import webpay.errors

def assertId(id):
    if id is None or id.strip() == '':
        raise webpay.errors.InvalidRequestError.empty_id_error()

class Charges:
    def __init__(self, webpay):
        self.__client = webpay

    def create(self, **params):
        return Charge(self.__client, self.__client.post('/charges', params))

    def retrieve(self, id):
        assertId(id)
        return Charge(self.__client, self.__client.get('/charges/' + id))

    def all(self, **params):
        return EntityList(self.__client, self.__client.get('/charges', params))

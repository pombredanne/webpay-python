from webpay.model.customer import Customer
from webpay.model.entity_list import EntityList
from .helpers import assertId

class Customers:
    def __init__(self, webpay):
        self.__client = webpay

    def create(self, **params):
        return Customer(self.__client, self.__client.post('/customers', params))

    def retrieve(self, id):
        assertId(id)
        return Customer(self.__client, self.__client.get('/customers/' + id))

    def all(self, **params):
        return EntityList(self.__client, self.__client.get('/customers', params))

    def save(self, id, **params):
        """Update attributes of the customer identified by `id`
        """
        assertId(id)
        return Customer(self.__client, self.__client.post('/customers/' + id, params))

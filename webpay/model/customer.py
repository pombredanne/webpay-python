from webpay.model.card import Card
from .model import Model


class Customer(Model):

    def __init__(self, client, data):
        conversion = lambda k: Card if k == 'active_card' else None
        Model.__init__(self, client, data, conversion)

    def is_deleted(self):
        """ Always returns `False`
        """
        return False

    def save(self):
        """Save updated data to WebPay server.

        Following fields are updated:
        - `email`
        - `description`
        - `new_card`: `active_card` is a Card object, `new_card` is a dict. Setting new card info as a dict to `active_card` has no effect.
        """

        params = {}
        if hasattr(self, 'email') and self._data['email'] != self.email:
            params['email'] = self.email
        if hasattr(self, 'description') and self._data['description'] != self.description:
            params['description'] = self.description
        if hasattr(self, 'new_card') and self.new_card is not None:
            params['card'] = self.new_card
            self.new_card = None

        self._update_attributes(self._client.customers.save(self.id, **params))

    def delete(self):
        """Delete this customer from WebPay
        """
        return self._client.customers.delete(self.id)

    def _update_attributes(self, new_customer):
        self._data = new_customer._data
        for k, v in new_customer._data.items():
            self.__dict__[k] = \
                Card(self._client, v) if k == 'active_card' else v

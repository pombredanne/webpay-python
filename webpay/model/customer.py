from webpay.model.card import Card

class Customer:
    def __init__(self, client, data):
        self.__client = client
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = Card(client, v) if k == 'active_card' else v

    def save(self):
        """Save updated data to WebPay server.

        Following fields are updated:
        - `email`
        - `description`
        - `new_card`: `active_card` is a Card object, `new_card` is a dict. Setting new card info as a dict to `active_card` has no effect.
        """

        params = {}
        if hasattr(self, 'email') and self.__data['email'] != self.email:
            params['email'] = self.email
        if hasattr(self, 'description') and self.__data['description'] != self.description:
            params['description'] = self.description
        if hasattr(self, 'new_card') and self.new_card is not None:
            params['card'] = self.new_card
            self.new_card = None

        self._update_attributes(self.__client.customers.save(self.id, **params))

    def delete(self):
        """Delete this customer from WebPay
        """
        return self.__client.customers.delete(self.id)

    def _update_attributes(self, new_customer):
        self.__data = new_customer.__data
        for k, v in new_customer.__data.items():
            self.__dict__[k] = Card(self.__client, v) if k == 'active_card' else v

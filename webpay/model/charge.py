from webpay.model.card import Card

class Charge:
    def __init__(self, client, data):
        self.__client = client
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = Card(client, v) if k == 'card' else v

    def refund(self, amount = None):
        """Refund this charge.

        Arguments:
        - `amount`: amount to refund.  If `amount` is not given or `None`, refund all.
          If `amount` is less than this charge's amount, refund partially.
        """
        self._update_attributes(self.__client.charges.refund(self.id, amount))

    def capture(self, amount = None):
        """Capture this charge.
        This charge should be uncaptured (created with capture=false) and not yet expired.

        Arguments:
        - `amount`: amount to capture.  If `amount` is not given or `None`, use `this.amount`.
        """
        self._update_attributes(self.__client.charges.capture(self.id, amount))

    def _update_attributes(self, new_charge):
        for k, v in new_charge.__data.items():
            self.__dict__[k] = Card(self.__client, v) if k == 'card' else v

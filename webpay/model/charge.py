from webpay.model.card import Card
from .model import Model

class Charge(Model):
    def __init__(self, client, data):
        Model.__init__(self, client, data, lambda k: Card if k == 'card' else None)

    def refund(self, amount = None):
        """Refund this charge.

        Arguments:
        - `amount`: amount to refund.  If `amount` is not given or `None`, refund all.
          If `amount` is less than this charge's amount, refund partially.
        """
        self._update_attributes(self._client.charges.refund(self.id, amount))

    def capture(self, amount = None):
        """Capture this charge.
        This charge should be uncaptured (created with capture=false) and not yet expired.

        Arguments:
        - `amount`: amount to capture.  If `amount` is not given or `None`, use `this.amount`.
        """
        self._update_attributes(self._client.charges.capture(self.id, amount))

    def _update_attributes(self, new_charge):
        for k, v in new_charge._data.items():
            self.__dict__[k] = Card(self._client, v) if k == 'card' else v

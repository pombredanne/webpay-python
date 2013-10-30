from webpay.webpay import WebPay
from httmock import HTTMock
import pytest

import tests.helper as helper
import webpay.errors as errors

class TestCharges:
    def test_create(self):
        with HTTMock(helper.mock_api('/charges', 'charges/create.txt')):
            charge = WebPay('test_key').charges.create(
                amount = 1000,
                currecy = 'jpy',
                card = {
                    'number': '4242-4242-4242-4242',
                    'exp_month': 12,
                    'exp_year': 2015,
                    'cvc': 123,
                    'name': 'YUUKO SHIONJI'
                    },
                description = 'Test Charge from Java',
                )

        assert charge.id == 'ch_2SS17Oh1r8d2djE'
        assert charge.description == 'Test Charge from Java'
        assert charge.card.name == 'YUUKO SHIONJI'

    def test_retrieve(self):
        id = 'ch_bWp5EG9smcCYeEx'
        with HTTMock(helper.mock_api('/charges/' + id, 'charges/retrieve.txt')):
            charge = WebPay('test_key').charges.retrieve(id)

        assert charge.id == id
        assert charge.description == 'アイテムの購入'
        assert charge.card.name == 'KEI KUBO'

    def test_retrieve_without_id(self):
        with pytest.raises(errors.InvalidRequestError) as excinfo:
            charge = WebPay('test_key').charges.retrieve('')
        exc = excinfo.value
        assert exc.type == 'invalid_request_error'
        assert exc.param == 'id'

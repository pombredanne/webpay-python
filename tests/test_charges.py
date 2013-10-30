from webpay.webpay import WebPay
from httmock import HTTMock
import tests.helper as helper

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

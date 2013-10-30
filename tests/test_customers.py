# coding: utf-8
from webpay.webpay import WebPay
from httmock import HTTMock
import pytest

import tests.helper as helper
import webpay.errors as errors

class TestCustomers:
    def test_create(self):
        with HTTMock(helper.mock_api('/customers', 'customers/create.txt')):
            customer = WebPay('test_key').customers.create(
                description = 'Test Customer from Java',
                email = 'customer@example.com',
                card = {
                    'number': '4242-4242-4242-4242',
                    'exp_month': 12,
                    'exp_year': 2015,
                    'cvc': 123,
                    'name': 'YUUKO SHIONJI'
                    },
                )

        assert customer.id == 'cus_39o4Fv82E1et5Xb'
        assert customer.description == 'Test Customer from Java'
        assert customer.active_card.name == 'YUUKO SHIONJI'

    def test_retrieve(self):
        id = 'cus_39o4Fv82E1et5Xb'
        with HTTMock(helper.mock_api('/customers/' + id, 'customers/retrieve.txt')):
            customer = WebPay('test_key').customers.retrieve(id)

        assert customer.id == id
        assert customer.active_card.name == 'YUUKO SHIONJI'

    def test_retrieve_without_id(self):
        with pytest.raises(errors.InvalidRequestError) as excinfo:
            customer = WebPay('test_key').customers.retrieve('')
        exc = excinfo.value
        assert exc.type == 'invalid_request_error'
        assert exc.param == 'id'

    def test_all(self):
        with HTTMock(helper.mock_api('/customers', 'customers/all.txt')):
            customers = WebPay('test_api').customers.all(count = 3, offset = 0, created = {'gt': 1378000000})

        assert customers.url == '/v1/customers'
        assert customers.data[0].description == 'Test Customer from Java'
        assert customers.data[0].active_card.name == 'YUUKO SHIONJI'

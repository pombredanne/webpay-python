from webpay import WebPay
from httmock import HTTMock, urlmatch
import pytest

import tests.helper as helper
import webpay.errors as errors


class TestWebpay:

    def test_request_raises_not_found_with_ja_language(self):
        webpay = WebPay('test_key')
        webpay.accept_language('ja')

        @urlmatch(scheme='https', netloc='api.webpay.jp', path='/v1/customers/cus_eS6dGfa8BeUlbS')
        def mock(url, request):
            assert request.headers['Accept-Language'] == 'ja'
            return helper.response_from_file('errors/not_found_ja.txt', request)

        with pytest.raises(errors.InvalidRequestError) as excinfo:
            with HTTMock(mock):
                webpay.customers.retrieve('cus_eS6dGfa8BeUlbS')
        exc = excinfo.value
        assert exc.__str__() == '該当する顧客がありません: cus_eS6dGfa8BeUlbS'

    def test_request_raises_not_found_with_default_language(self):
        webpay = WebPay('test_key')

        @urlmatch(scheme='https', netloc='api.webpay.jp', path='/v1/charges/foo')
        def mock(url, request):
            assert request.headers['Accept-Language'] == 'en'
            return helper.response_from_file('errors/not_found.txt', request)

        with pytest.raises(errors.InvalidRequestError) as excinfo:
            with HTTMock(mock):
                webpay.charges.retrieve('foo')
        exc = excinfo.value
        assert exc.__str__() == 'No such charge: foo'

from webpay.webpay import WebPay
from httmock import urlmatch, HTTMock, response
from os import path

class TestCharges:
    def test_create(self):
        @urlmatch(scheme = 'https', netloc = 'api.webpay.jp', path = '/v1/charges')
        def create_charge_mock(url, request):
            dump = path.dirname(path.abspath(__file__)) + '/mock/charges/create.txt'
            file = open(dump)
            lines = file.readlines()
            file.close

            status = 0
            headers = {}
            body = ''
            body_started = False

            for i in range(len(lines)):
                line = lines[i]
                if i == 0:
                    status = int(line.split(' ')[1])
                elif body_started:
                    body += line
                elif (line.strip() == ''):
                    body_started = True
                else:
                    key, value = line.split(':', 1)
                    headers[key] = value.strip()

            return response(status, content = body.encode('utf-8'), headers = headers, request = request)

        webpay = WebPay('test_key')
        with HTTMock(create_charge_mock):
            charge = webpay.charges.create(
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

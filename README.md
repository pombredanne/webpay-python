webpay-python is a client library for python of [WebPay](https://webpay.jp).

# Installation

    $ pip install webpay

# Usage

```python
from webpay.webpay import WebPay
webpay = WebPay('YOUR_TEST_SECRET_KEY')

webpay.charges.create(
  amount=400,
  currency="jpy",
  card={
    'number': '4242-4242-4242-4242',
    'exp_month': '11',
    'exp_year': '2014',
    'cvc': '123',
    'name': 'FOO BAR'
  }
  )
```

See [Python API document](https://webpay.jp/docs/api/python) on WebPay official page for more details.

# Dependencies

- [kennethreitz/requests](https://github.com/kennethreitz/requests)

# Development

## Testing

    $ pip install -r dev-requirements.txt
    $ py.test

# License

[The MIT License (MIT)](http://opensource.org/licenses/mit-license.html)

Copyright (c) 2013 WebPay.

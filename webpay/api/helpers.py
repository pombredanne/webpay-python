import webpay.errors

def assertId(id):
    if id is None or id.strip() == '':
        raise webpay.errors.InvalidRequestError.empty_id_error()

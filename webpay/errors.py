class WebPayError(RuntimeError):
    """Base class for errors related to webpay library.
    """
    def __init__(self, message, status, error_info):
        RuntimeError.__init__(self, message)
        self.status = status
        self.error_info = error_info

class ApiConnectionError(WebPayError):
    """Error raised when something is wrong while connecting to WebPay API.
    """
    def __init__(self, message, status, error_info, cause):
        WebPayError.__init__(self, message, status, error_info)
        self.cause = cause

class ApiError(WebPayError):
    """Error raised when WebPay API returns error status (500, 503, etc).
    """
    def __init__(self, status, error_info):
        WebPayError.__init__(self, error_info['message'], status, error_info)
        self.type = error_info['type']

class AuthenticationError(WebPayError):
    """Error raised when authentication failed.
    In most cases, the API key is invalid.
    """

    def __init__(self, status, error_info):
        WebPayError.__init__(self, error_info['message'], status, error_info)

class CardError(WebPayError):
    """Error raised when given card information is invalid.
    A system should make its end user check input information.
    """

    def __init__(self, status, error_info):
        WebPayError.__init__(self, error_into['message'], status, error_info)
        self.type = error_info['type']
        self.code = error_info['code']
        self.param = error_info['param']

class InvalidRequestError(WebPayError):
    """Error raised when given parameters have an invalid field.
    """

    def __init__(self, status, error_info):
        WebPayError.__init__(self, error_info['message'], status, error_info)
        self.type = error_info['type']
        self.param = error_info['param'] if 'param' in error_info else None

    @staticmethod
    def empty_id_error():
        return InvalidRequestError(None, {
                'message': 'id must not be empty',
                'type': 'invalid_request_error',
                'param': 'id'
                })
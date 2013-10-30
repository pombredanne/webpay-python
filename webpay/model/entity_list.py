import webpay.model as model
import webpay.errors

def data_to_object_converter(client):
    """Return a function to convert entity dict data to entity object
    """

    def converter(data):
        object = data['object']
        if object == 'charge':
            return model.charge.Charge(client, data)
        elif object == 'customer':
            return model.charge.Customer(client, data)
        elif object == 'event':
            return model.charge.Event(client, data)
        elif object == 'token':
            return model.charge.Token(client, data)
        elif object == 'account':
            return model.charge.Account(client, data)
        else:
            raise webpay.errors.APIConnectionError('Unknown object type ' + object, None, None, None)

    return converter

class EntityList(object):
    """List of the same entities.
    This list is the return value of ``all()``.
    """

    def __init__(self, client, data):
        self.__client = client

        for k, v in data.items():
            self.__dict__[k] = list(map(data_to_object_converter(client), v)) if k == 'data' else v

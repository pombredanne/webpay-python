from .helpers import data_to_object_converter

class EntityList(object):
    """List of the same entities.
    This list is the return value of ``all()``.
    """

    def __init__(self, client, data):
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = list(map(data_to_object_converter(client), v)) if k == 'data' else v

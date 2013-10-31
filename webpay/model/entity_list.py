from .helpers import data_to_object_converter
from .model import Model

class EntityList(Model):
    """List of the same entities.
    This list is the return value of ``all()``.
    """

    def __init__(self, client, data):
        Model.__init__(self, client, data, lambda k: (lambda c, v: list(map(data_to_object_converter(c), v))) if k == 'data' else None)

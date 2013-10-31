from .helpers import data_to_object_converter
from .model import Model

class Event(Model):
    def __init__(self, client, data):
        Model.__init__(self, client, data, lambda k: EventData if k == 'data' else None)

class EventData(Model):
    def __init__(self, client, data):
        Model.__init__(self, client, data, lambda k: (lambda c, v: data_to_object_converter(c)(v)) if k == 'object' else None)

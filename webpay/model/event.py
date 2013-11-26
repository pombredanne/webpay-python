from .helpers import data_to_object_converter
from .model import Model


class Event(Model):

    def __init__(self, client, data):
        conversion = lambda k: EventData if k == 'data' else None
        Model.__init__(self, client, data, conversion)


class EventData(Model):

    def __init__(self, client, data):
        convert_object = lambda c, v: data_to_object_converter(c)(v)
        conversion = lambda k: convert_object if k == 'object' else None
        Model.__init__(self, client, data, conversion)

from .helpers import data_to_object_converter

class Event:
    def __init__(self, client, data):
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = EventData(client, v) if k == 'data' else v

class EventData:
    def __init__(self, client, data):
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = data_to_object_converter(client)(v) if k == 'object' else v

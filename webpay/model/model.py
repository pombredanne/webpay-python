import json

class Model:
    def __init__(self, client, data, conversion = None):
        self._client = client
        self._data = data

        for k, v in data.items():
            if conversion is None:
                self.__dict__[k] = v
            else:
                conv = conversion(k)
                self.__dict__[k] = v if conv is None else conv(client, v)

    def __str__(self):
        t = type(self)
        return '<%s.%s> %s' % (t.__module__, t.__name__, json.dumps(self._data, indent = 4, sort_keys = True))

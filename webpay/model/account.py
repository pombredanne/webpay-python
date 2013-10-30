class Account:
    def __init__(self, client, data):
        self.__client = client
        self.__data = data

        for k, v in data.items():
            self.__dict__[k] = v

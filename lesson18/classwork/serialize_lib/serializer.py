#  Each provider_class should realize some interface. serialize()

class Serializer:
    def __init__(self, provider_class):
        self.provider_class = provider_class

    def execute(self, data):
        self.provider_class.serialize(data)

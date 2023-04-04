#  Each provider_class should realize some interface. serialize()
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import ProviderProtocol
    from providers import InputData


class Serializer:
    def __init__(self, provider_class: 'ProviderProtocol') -> None:
        self.provider_class = provider_class

    def execute(self, data: 'InputData') -> None:
        self.provider_class.serialize(data)

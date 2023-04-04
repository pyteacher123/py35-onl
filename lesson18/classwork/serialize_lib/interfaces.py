from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from providers import InputData


class ProviderProtocol(Protocol):
    def serialize(self, data: 'InputData') -> None:
        raise NotImplementedError

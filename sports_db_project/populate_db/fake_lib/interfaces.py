from typing import Protocol, Any


class ProviderProtocol(Protocol):
    def __call__(self) -> Any:
        raise NotImplementedError

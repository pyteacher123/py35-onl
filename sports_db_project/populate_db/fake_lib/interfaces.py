from typing import Protocol


class ProviderProtocol(Protocol):
    def generate(self) -> str:
        raise NotImplementedError
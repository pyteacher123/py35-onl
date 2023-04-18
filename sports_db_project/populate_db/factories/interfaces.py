from typing import Protocol


class FakeFactoryProtocol(Protocol):
    def generate(self) -> object:
        raise NotImplementedError

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import ProviderProtocol



class FakeFactory:
    def __init__(self, provider_class: ProviderProtocol) -> None:
        self._provider_class = provider_class
    
    def 
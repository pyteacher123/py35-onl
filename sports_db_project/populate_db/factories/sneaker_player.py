from __future__ import annotations
from data_access.dto import SneakerPlayerDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class SneakerPlayerFactory:
    def __init__(
            self,
            sneaker_id_provider: RandomValueFromListProvider,
            player_id_provider: RandomValueFromListProvider
    ):
        self._sneaker_id_provider = sneaker_id_provider
        self._player_id_provider = player_id_provider
    
    def generate(self) -> SneakerPlayerDTO:
        return SneakerPlayerDTO(
            sneaker_id=self._sneaker_id_provider(),
            player_id=self._player_id_provider()
        )

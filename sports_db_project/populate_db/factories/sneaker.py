from __future__ import annotations
from data_access.dto import SneakerDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers.word import WordProvider
    from fake_lib.providers.price import PriceProvider
    from fake_lib.providers.random_value import RandomValueFromListProvider
    from fake_lib.providers.color import ColorProvider


class SneakerFactory:
    def __init__(
            self,
            word_provider: WordProvider,
            price_provider: PriceProvider,
            random_value_provider: RandomValueFromListProvider,
            color_provider: ColorProvider
    ) -> None:
        self._word_provider = word_provider
        self._price_provider = price_provider
        self._random_value_provider = random_value_provider
        self._color_provider = color_provider

    def generate(self) -> SneakerDTO:
        return SneakerDTO(
            model=self._word_provider(),
            color=self._color_provider(),
            price=self._price_provider(),
            producer_id=self._random_value_provider()
        )

from __future__ import annotations
from data_access.dto import ProducerDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers.random_value import RandomValueFromListProvider
    from fake_lib.providers.text import TextProvider
    from fake_lib.providers.sport_company import SportwareCompanyProvider


class ProducerFactory:
    def __init__(
            self,
            random_value_provider: RandomValueFromListProvider,
            text_provider: TextProvider,
            sports_company_provider: SportwareCompanyProvider
    ):
        self._random_value_provider = random_value_provider
        self._text_provider = text_provider
        self._sports_company_provider = sports_company_provider
    
    def generate(self) -> ProducerDTO:
        return ProducerDTO(
            country_id=self._random_value_provider(),
            name=self._sports_company_provider(),
            description=self._text_provider()
        )

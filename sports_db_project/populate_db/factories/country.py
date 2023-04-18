from __future__ import annotations
from data_access.dto import CountryDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers.country import CountryProvider


class CountryFactory:
    def __init__(
            self,
            country_provider: CountryProvider
    ):
        self._country_provider = country_provider
    
    def generate(self) -> CountryDTO:
        return CountryDTO(
            name=self._country_provider()
        )

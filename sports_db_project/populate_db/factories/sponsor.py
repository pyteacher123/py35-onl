from __future__ import annotations
from data_access.dto import SponsorDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (
        CompanyProvider,
        RandomValueFromListProvider,
        TextProvider
    )


class SponsorFactory:
    def __init__(
            self,
            name_provider: CompanyProvider,
            country_id_provider: RandomValueFromListProvider,
            description_provider: TextProvider
    ):
        self._name_provider = name_provider
        self._country_id_provider = country_id_provider
        self._description_provider = description_provider
    
    def generate(self) -> SponsorDTO:
        return SponsorDTO(
            name=self._name_provider(),
            country_id=self._country_id_provider(),
            description=self._description_provider()
        )

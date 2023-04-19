from __future__ import annotations
from data_access.dto import TeamDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (
        WordProvider,
        RandomValueFromListProvider,
        TextProvider
    )


class TeamFactory:
    def __init__(
            self,
            name_provider: WordProvider,
            country_id_provider: RandomValueFromListProvider,
            description_provider: TextProvider,
            sport_type_id_provider: RandomValueFromListProvider
    ):
        self._name_provider = name_provider
        self._country_id_provider = country_id_provider
        self._description_provider = description_provider
        self._sport_type_id_provider = sport_type_id_provider

    def generate(self) -> TeamDTO:
        return TeamDTO(
            name=self._name_provider(),
            country_id=self._country_id_provider(),
            description=self._description_provider(),
            sport_type_id=self._sport_type_id_provider()
        )

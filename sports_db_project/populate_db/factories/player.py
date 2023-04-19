from __future__ import annotations
import random
from data_access.dto import PlayerDTO, ProfileDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (
        RandomValueFromListProvider,
        EmailProvider,
        PhoneProvider,
        NameProvider,
        SurnameProvider,
        TextProvider
    )


class PlayerFactory:
    def __init__(
            self,
            phone_provider: PhoneProvider,
            name_provider: NameProvider,
            surname_provider: SurnameProvider,
            email_provider: EmailProvider,
            description_provider: TextProvider,
            age_provider: RandomValueFromListProvider,
            height_provider: RandomValueFromListProvider,
            weight_provider: RandomValueFromListProvider,
            country_id_provider: RandomValueFromListProvider,
            sport_type_id_provider: RandomValueFromListProvider,
            team_id_provider: RandomValueFromListProvider
    ) -> None:
        self._phone_provider = phone_provider
        self._name_provider = name_provider
        self._surname_provider = surname_provider
        self._email_provider = email_provider
        self._description_provider = description_provider
        self._age_provider = age_provider
        self._height_provider = height_provider
        self._weight_provider = weight_provider
        self._country_id_provider = country_id_provider
        self._sport_type_id_provider = sport_type_id_provider
        self._team_id_provider = team_id_provider
    
    def generate(self) -> PlayerDTO:
        name = self._name_provider()
        username = name.lower() + str(random.choice(range(1111, 99999)))
        
        profile = ProfileDTO(
            phone=self._phone_provider(),
            username=username,
            age=self._age_provider(),
            description=self._description_provider(),
            height=self._height_provider(),
            weight=self._weight_provider()
        )

        return PlayerDTO(
            email=self._email_provider(),
            name=name,
            surname=self._surname_provider(),
            country_id=self._country_id_provider(),
            sport_type_id=self._sport_type_id_provider(),
            team_id=self._team_id_provider(),
            profile=profile
        )

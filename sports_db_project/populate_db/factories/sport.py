from __future__ import annotations
from data_access.dto import SportDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (
        SportProvider,
        IsTeamProvider
    )


class SportFactory:
    def __init__(
            self,
            sport_provider: SportProvider,
            is_team_provider: IsTeamProvider
    ):
        self._sport_provider = sport_provider
        self._is_team_provider = is_team_provider
    
    def generate(self) -> SportDTO:
        return SportDTO(
            name=self._sport_provider(),
            is_team=self._is_team_provider()
        )

from __future__ import annotations
from data_access.dto import SponsorTeamDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (
        RandomValueFromListProvider,
        DatesRangeProvider
    )


class SponsorTeamFactory:
    def __init__(
            self,
            sponsor_type_id_provider: RandomValueFromListProvider,
            team_id_provider: RandomValueFromListProvider,
            dates_range_provider: DatesRangeProvider 
    ) -> None:
        self._sponsor_type_id_provider = sponsor_type_id_provider
        self._team_id_provider = team_id_provider
        self._dates_range_provider = dates_range_provider
    
    def generate(self) -> SponsorTeamDTO:
        start_date, end_date = self._dates_range_provider()
        return SponsorTeamDTO(
            sponsor_id=self._sponsor_type_id_provider(),
            team_id=self._team_id_provider(),
            start_date=start_date,
            end_date=end_date
        )

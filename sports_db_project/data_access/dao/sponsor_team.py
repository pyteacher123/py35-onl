from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import SponsorTeamDTO


class SponsorTeamDAO(BaseDAO):
    def create(self, data: SponsorTeamDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO sponsors_teams (sponsor_id, team_id, start_year, end_year) VALUES "
                                        "(?, ?, ?, ?);", (data.sponsor_id, data.team_id, data.start_date, data.end_date))
        self._db_gateway.connection.commit()

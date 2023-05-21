from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import TeamDTO


class TeamDAO(BaseDAO):
    def create(self, data: TeamDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO teams (name, country_id, description, sport_type_id) VALUES (?, ?, ?, ?);",
                                        (data.name, data.country_id, data.description, data.sport_type_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM producers;")
        return result.fetchall()

from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import PlayerDTO


class PlayerDAO(BaseDAO):
    def create(self, data: PlayerDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO profiles (phone, username, description, age, height, weight) "
                                        "VALUES (?, ?, ?, ?, ?, ?);", 
                                        (data.profile.phone, data.profile.username, data.profile.description,
                                         data.profile.age, data.profile.height, data.profile.weight))
        profile_id = self._db_gateway.cursor.lastrowid
        self._db_gateway.cursor.execute("INSERT INTO players (email, name, surname, country_id, sport_type_id, "
                                        "team_id, profile_id) VALUES (?, ?, ?, ?, ?, ?, ?);",
                                        (data.email, data.name, data.surname, data.country_id, data.sport_type_id,
                                         data.team_id, profile_id))
        self._db_gateway.connection.commit()

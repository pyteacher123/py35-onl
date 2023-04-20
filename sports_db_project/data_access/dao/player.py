from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING, Any
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
    
    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM players;")
        return result.fetchall()
    
    def get_list(self) -> list[tuple]:
        result = self._db_gateway.cursor.execute("SELECT players.id, players.name, players.surname, profiles.age, countries.name, teams.name "
                                                 "FROM players JOIN profiles ON players.profile_id = profiles.id JOIN countries ON "
                                                 "players.country_id = countries.id JOIN teams ON players.team_id = teams.id;")
        return result.fetchall()

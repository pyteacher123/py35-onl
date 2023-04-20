from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import SportDTO


class SportDAO(BaseDAO):
    def create(self, data: SportDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO sport_types (name, is_team) VALUES (?, ?);", 
                                        (data.name, data.is_team))
        self._db_gateway.connection.commit()
    
    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM sport_types;")
        return result.fetchall()

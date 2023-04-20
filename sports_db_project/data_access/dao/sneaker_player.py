from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import SneakerPlayerDTO


class SneakerPlayerDAO(BaseDAO):
    def create(self, data: SneakerPlayerDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO sneakers_players (sneaker_id, player_id) VALUES (?, ?);", 
                                        (data.sneaker_id, data.player_id))
        self._db_gateway.connection.commit()

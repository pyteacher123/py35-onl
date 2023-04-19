from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import ProducerDTO


class ProducerDAO(BaseDAO):
    def create(self, data: ProducerDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO producers (country_id, name, description) VALUES (?, ?, ?);", 
                                        (data.country_id, data.name, data.description))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM producers;")
        return result.fetchall()

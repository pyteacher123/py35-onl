from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import CountryDTO


class CountryDAO(BaseDAO):    
    def create(self, data: CountryDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO countries (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()
    
    def get_ids_list(self) -> list[int]:
        result = self._db_gateway.cursor.execute("SELECT id FROM countries;")
        return result.fetchall()

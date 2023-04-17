from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import DAOProtocol
    from dto import CountryDTO


class RecordsGenerator:
    def __init__(
            self, 
            records_number: int, 
            dao: DAOProtocol,
            dto: list[CountryDTO]
    ) -> None:
        self._number = records_number
        self._dao = dao
        self._dto = dto
    
    def generate(self):
        for _ in self._number:
            self._dao.create(data=self._dto)
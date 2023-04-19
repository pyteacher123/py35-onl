from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import SponsorDTO


class SponsorDAO(BaseDAO):
    def create(self, data: SponsorDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO sponsors (name, country_id, description) VALUES (?, ?, ?);",
                                        (data.name, data.country_id, data.description))
        self._db_gateway.connection.commit()

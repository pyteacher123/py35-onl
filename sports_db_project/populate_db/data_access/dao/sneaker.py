from __future__ import annotations
from .base import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import SneakerDTO


class SneakerDAO(BaseDAO):
    def create(self, data: SneakerDTO) -> None:
        print(data)
        self._db_gateway.cursor.execute("INSERT INTO sneakers (model, color, price, producer_id) VALUES (?, ?, ?, ?);",
                                        (data.model, data.color, data.price, data.producer_id))
        self._db_gateway.connection.commit()

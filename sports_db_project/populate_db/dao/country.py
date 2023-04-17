from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import CountryDTO
    from interfaces import GatewayProtocol


class CountryDAO:
    def __init__(self, db_gateway: GatewayProtocol) -> None:
        self._db_gateway = db_gateway

    def create(self, data: CountryDTO) -> None:
        self._db_gateway.cursor.execute("INSERT INTO countries (name) VALUES (?);", (data.name, ))
        self._db_gateway.connection.commit()

from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class DBGatewayProtocol(Protocol):
    connection: Connection
    cursor: Cursor


class CreateRecordProtocol(Protocol):
    def create(self, data: object) -> None:
        raise NotImplementedError


class GetIdsListProtocol(Protocol):
    def get_ids_list(self) -> list[int]:
        raise NotImplementedError

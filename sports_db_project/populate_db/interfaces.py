from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class GatewayProtocol(Protocol):
    connection: Connection
    cursor: Cursor

    def __init__(self, db_name: str) -> None:
        raise NotImplementedError


class DAOProtocol(Protocol):
    def __init__(self, db_gateway: GatewayProtocol) -> None:
        raise NotImplementedError

    def create(self, data: None) -> None:
        raise NotImplementedError

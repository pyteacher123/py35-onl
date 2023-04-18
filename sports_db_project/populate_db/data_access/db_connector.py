from __future__ import annotations
import sqlite3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class SqliteGateway:
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self.connection = self._create_connection()
        self.cursor = self._create_cursor()
    
    def _create_connection(self) -> Connection:
        return sqlite3.connect(self._db_name)
    
    def _create_cursor(self) -> Cursor:
        return self.connection.cursor()

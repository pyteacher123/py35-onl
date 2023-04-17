from __future__ import annotations
import sqlite3

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class DbGateway:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = self._create_connection()
        self.cursor = self._create_cursor()
    
    @property
    def db_name(self) -> None:
        raise NotImplementedError
    
    @db_name.setter
    def db_name(self, value: str) -> None:
        if value.split('.')[1] != 'db':
            raise ValueError('Invalid DB name.')
        
        self._db_name = value
    
    def _create_connection(self) -> Connection:
        return sqlite3.connect(self.db_name)
    
    def _create_cursor(self) -> None:
        self._cursor =  self.connection.cursor()

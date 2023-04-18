from __future__ import annotations
from sqlite3 import IntegrityError
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.interfaces import CreateRecordProtocol
    from factories.interfaces import FakeFactoryProtocol

class PopulateTable:
    def __init__(
            self,
            records_number: int,
            dao: CreateRecordProtocol,
            fake_factory: FakeFactoryProtocol
    ):
        self._records_number = records_number
        self._dao = dao
        self._fake_factory = fake_factory
    
    def execute(self) -> None:
        for _ in range(self._records_number):
            new_record = self._fake_factory.generate()
            try:
                self._dao.create(data=new_record)
            except IntegrityError as err:
                print(err)
                continue

from data_access import CSVStorage, JSONStorage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import StorageProto


#  Абстрактная фабрика
def provide_db(db_type: str, db_file: str) -> 'StorageProto':
    if db_type == "csv":
        return CSVStorage(db_file)
    elif db_type == "json":
        return JSONStorage(db_file)
    else:
        raise ValueError("Unsupported DB type.")

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from data_access import CompaniesList


class StorageProto(Protocol):
    def get_all_records(self) -> 'CompaniesList':
        raise NotImplementedError

    def record_exists(self, company_name: str) -> bool:
        raise NotImplementedError

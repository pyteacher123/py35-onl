import csv
import json
from typing import TypeAlias


RecordsList: TypeAlias = list[dict[str, str | int | float]]


class CSVStorage:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "csv":
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def get_all_records(self) -> RecordsList:
        with open(self.file_name) as db_file:
            return list(csv.DictReader(db_file))

    def record_exists(self, company_name: str) -> bool:
        with open(self.file_name) as db_file:
            for row in csv.DictReader(db_file):
                if company_name == row["Name"]:
                    return True
        return False


class JSONStorage:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "json":
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def get_all_records(self) -> RecordsList:
        with open(self.file_name) as db_file:
            return list(json.load(db_file))

    def record_exists(self, company_name: str) -> bool:
        with open(self.file_name) as db_file:
            for row in json.load(db_file):
                if company_name == row["Name"]:
                    return True
        return False

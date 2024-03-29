import csv
import json
from dataclasses import dataclass
from typing import TypeAlias


@dataclass
class CompanyDTO:
    symbol: str
    name: str
    sector: str
    price: float


CompaniesList: TypeAlias = list[CompanyDTO]


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

    def get_all_records(self) -> CompaniesList:
        with open(self.file_name) as db_file:
            res = []
            for row in csv.DictReader(db_file):
                res.append(CompanyDTO(
                    symbol=row['Symbol'],
                    name=row['Name'],
                    sector=row['Sector'],
                    price=float(row['Price'])
                ))
            return res

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

    def get_all_records(self) -> CompaniesList:
        with open(self.file_name) as db_file:
            res = []
            for row in json.load(db_file):
                res.append(CompanyDTO(
                    symbol=row['Symbol'],
                    name=row['Name'],
                    sector=row['Sector'],
                    price=float(row['Price'])
                ))
            return res

    def record_exists(self, company_name: str) -> bool:
        with open(self.file_name) as db_file:
            for row in json.load(db_file):
                if company_name == row["Name"]:
                    return True
        return False

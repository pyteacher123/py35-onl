import csv
import json
from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_all_records(self):
        raise NotImplementedError

    @abstractmethod
    def record_exists(self, company_name):
        raise NotImplementedError


class CSVStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value.split(".")[1] != "csv":
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def get_all_records(self):
        with open(self.file_name) as db_file:
            return list(csv.DictReader(db_file))

    def record_exists(self, company_name):
        with open(self.file_name) as db_file:
            for row in csv.DictReader(db_file):
                if company_name == row["Name"]:
                    return True
        return False


class JSONStorage(IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value.split(".")[1] != "json":
            raise ValueError("Invalid file extension.")

        self._file_name = value

    def get_all_records(self):
        with open(self.file_name) as db_file:
            return json.load(db_file)

    def record_exists(self, company_name):
        with open(self.file_name) as db_file:
            for row in json.load(db_file):
                if company_name == row["Name"]:
                    return True
        return False

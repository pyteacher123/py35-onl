import csv
import openpyxl
import json
from errors import InvalidDataError
from typing import Any, TypeAlias


InputData: TypeAlias = list[dict[str, Any]]


class BaseProvider:
    """
    NOT FOR CREATING OBJECTS!
    """
    AVAILABLE_EXTENSIONS: tuple[str, ...]

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] not in self.AVAILABLE_EXTENSIONS:
            raise ValueError("Invalid file extension.")

        self._file_name = value


class ConvertDataMixin:
    def _convert_data(self, data: InputData) -> list[list[Any]]:
        res = []
        res.append(list(data[0].keys()))
        for element in data:
            if list(element.keys()) != res[0]:
                raise InvalidDataError("Can't serialize this data.")

            res.append(list(element.values()))

        return res


class CSVProvider(BaseProvider, ConvertDataMixin):
    AVAILABLE_EXTENSIONS = ('csv',)

    def serialize(self, data: InputData) -> None:
        data_converted = self._convert_data(data)
        with open(self.file_name, "w") as file:
            writer = csv.writer(file, delimiter=",")
            for row in data_converted:
                writer.writerow(row)


class ExcelProvider(BaseProvider, ConvertDataMixin):
    AVAILABLE_EXTENSIONS = ('xlsx', 'xls')

    def serialize(self, data: InputData) -> None:
        data_converted = self._convert_data(data)
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for row in data_converted:
            worksheet.append(row)
        workbook.save(self.file_name)


class JsonProvider(BaseProvider):
    AVAILABLE_EXTENSIONS = ('json',)

    def serialize(self, data: InputData) -> None:
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

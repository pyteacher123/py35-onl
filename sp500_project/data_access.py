import csv


class RecordAlreadyExists(Exception):
    ...


def get_all_records():
    with open("sp500.csv") as db_file:
        return list(csv.DictReader(db_file))


def record_exist(company_name):
    with open("sp500.csv") as db_file:
        for row in csv.DictReader(db_file):
            if company_name == row["Name"]:
                raise RecordAlreadyExists("Company already exists.")

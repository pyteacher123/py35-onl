import csv


def get_all_records():
    with open("sp500.csv") as db_file:
        return list(csv.DictReader(db_file))

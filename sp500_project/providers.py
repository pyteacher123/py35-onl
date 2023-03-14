from data_access import CSVStorage, JSONStorage


#  Абстрактная фабрика
def provide_db(db_type, db_file):
    if db_type == "csv":
        return CSVStorage(db_file)
    elif db_type == "json":
        return JSONStorage(db_file)
    else:
        raise ValueError("Unsupported DB type.")

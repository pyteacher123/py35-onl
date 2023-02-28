# Контекстный менеджер


class DatabaseStub:
    def __init__(self, db_url):
        self.db_url = db_url

    def open_db(self):
        print("Open db connection")

    def close(self):
        print("Close db connection")

    def __enter__(self):
        print("__enter__ calls")
        self.open_db()
        return self

    def __exit__(self, *args, **kwargs):
        print("__exit__ calls")
        self.close()


# f = open("test.txt")
# print(f)

# with open("test.txt") as file:
#     print(file)


# db = DatabaseStub("http:\\localhost:5432")
# db.open()
# raise KeyError
# db.close()


with DatabaseStub("http:\\localhost:5432") as db:
    print(db)
    raise KeyError

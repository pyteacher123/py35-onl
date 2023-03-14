from time import time


cache_storage = {}


def cache(cache_time=5):
    def inner(func):
        def wrapper(*args, **kwargs):
            value, expiration_time = cache_storage.get(args, (None, None))
            if value and time() <= expiration_time:
                return value

            res = func(*args, **kwargs)
            expiration_time = time() + cache_time
            cache_storage[args] = (res, expiration_time)
            return res
        return wrapper
    return inner


@cache(cache_time=10)
def find_info_by_name(company_name, db_connector):
    data = db_connector.get_all_records()
    result = []
    for row in data:
        if company_name.lower() in row.get("Name").lower():
            result.append({
                "Symbol": row.get("Symbol"),
                "Name": row.get("Name"),
                "Sector": row.get("Sector"),
                "Stock Price": row.get("Price")
                }
            )
    return result

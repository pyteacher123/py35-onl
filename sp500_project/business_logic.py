from time import time
from typing import Any, Callable, TypeVar, ParamSpec, TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import StorageProto


RT = TypeVar('RT')
P = ParamSpec('P')


cache_storage: dict[tuple, tuple] = {}


def cache(cache_time: int = 5) -> Callable[[Callable[P, RT]], Callable[P, RT]]:
    def inner(func: Callable[P, RT]) -> Callable[P, RT]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT | Any:
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
def find_info_by_name(
    company_name: str,
    db_connector: StorageProto
) -> list[dict[str, Any]]:
    data = db_connector.get_all_records()
    result = []
    for row in data:
        if company_name.lower() in row.name.lower():
            result.append({
                "Symbol": row.symbol,
                "Name": row.name,
                "Sector": row.sector,
                "Stock Price": row.price
                }
            )
    return result

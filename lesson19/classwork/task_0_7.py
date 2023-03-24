from time import time
from typing import Callable, TypeVar, ParamSpec


RT = TypeVar('RT')
P = ParamSpec('P')


def speed_test(func: Callable[P, RT]) -> Callable[P, RT]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Func executed {end - start} sec.")
        return res
    return wrapper


@speed_test
def test(a: str) -> None:
    print(a)


test(10)

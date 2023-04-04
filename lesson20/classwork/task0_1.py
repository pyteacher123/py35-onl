from typing import TypeVar


T = TypeVar('T', int, str)


def sum_of_obj(a: T, b: T) -> T:
    return a + b


sum_of_obj(1, 2)
sum_of_obj("1", "2")
sum_of_obj(1, "2")

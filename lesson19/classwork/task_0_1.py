# Дженерик тип - это возможность указать у типа-контейнера то, какие
# типы он может хранить внутри себя.
# list[int]
from typing import Any


class A:
    pass


class B(A):
    pass


def some_func(a: A) -> None:
    pass


some_func(B())


a: list[int] = [1, 2, 3]
b: list[str] = ['1', '2', '3']
c = [1, '2', [1, 2, 3]]


def test1(a: list[int]) -> None:
    pass


test1([1, 2, 3])


def test2(a: Any) -> None:
    pass


a: tuple(int, int) = (2, 2)

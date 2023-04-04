from typing import Generic, TypeVar


T = TypeVar('T')
V = TypeVar('V')


class A(Generic[T, V]):
    variable: T
    variable2: V

    def __init__(self, variable: T, variable2: V) -> None:
        self.variable = variable
        self.variable2 = variable2


def test(a: A[str, int]) -> None:
    pass


def test1(a: A[int, int]) -> None:
    pass


test(A("10", 10))
test(A("10", 20))

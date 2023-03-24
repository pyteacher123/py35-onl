from typing import Optional


def test(a: int | float | str) -> int | float | str:
    return a


test(10)
test(10.0)
test("Hello")


class Test:
    def __init__(self, value: Optional(str) = None) -> None:
        self.value = value

from typing import Generic, TypeVar, Any


T = TypeVar('T')


class Array(list, Generic[T]):
    t: T | type[int]

    def __init__(
            self,
            i: list[T] = [],
            t: T | type[int] = int,
            *args: Any,
            **kwargs: Any
    ) -> None:
        super().__init__(i)
        self.t = t

    # TODO: check isinstance type hint.
    def append(self, element: T) -> None:
        if type(element) != self.t:
            raise ValueError(f"Element must be {self.t}")
        super().append(element)


# l1 = [1, 2, 3]
# # l1.append("str")


# # l1 = list("str")
# # print(l1)

a1: Array[int] = Array(t=int)
a1.append(5)
a1.append(2)
a1.append('10')


# print(sorted(a1))


def test(arr: Array[int]) -> None:
    raise NotImplementedError


test(Array(i=[1, 2, 3], t=int))

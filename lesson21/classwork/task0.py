from typing import TypeAlias, Iterator


SelfPoint: TypeAlias = 'Point'


class Point:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __iter__(self) -> SelfPoint:
        self.counter = 0
        return self

    def __next__(self) -> float:
        if self.counter == 0:
            res = self.coord_x
        elif self.counter == 1:
            res = self.coord_y
        else:
            raise StopIteration

        self.counter += 1
        return res


def iterate(obj: Iterator[float]) -> None:
    for i in obj:
        print(i)


iterate(Point(10.0, 20.0))
#  List - iterable
#  list_iterator - iterator
print(iter([1, 2, 3]))

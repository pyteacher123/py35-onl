from typing import Optional, TypeAlias


Result: TypeAlias = Optional[tuple[int, int]]

a = [11, 15, 2, 8, -2]
target = 9


def solution(data: list[int], target: int) -> Result:
    buf: dict[int, int] = {}
    for index1, first_number in enumerate(data):
        try:
            second_number = target - first_number
            index2 = buf[second_number]
            return index2, index1
        except KeyError:
            buf[first_number] = index1
    return None


print(solution(a, target))

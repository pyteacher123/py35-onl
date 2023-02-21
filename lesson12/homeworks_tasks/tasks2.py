"""
args = (P1, P2, P3)
P1 -> P2 -> P3 -> None

"""


def calculate_route_length(*args):
    length = 0
    for index, point in enumerate(args[:-1]):
        x1, y1 = point
        x2, y2 = args[index+1]
        length += round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

    return length


res = calculate_route_length((1, 1), (1, 2), (1, 3))
print(res)

"""
Fibonacci task
n -> [0, 10000]

n = 3
fib_number(n) -> 2

0, 1, 1, 2, 3, 5, 8, 13, ...
0, 1, 2, 3, 4, 5, 6, 7
"""


def fib_number_rec(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    return fib_number_rec(n-1) + fib_number_rec(n-2)


def fib_number_gen(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    pointer1 = 0
    pointer2 = 1
    index = 2
    while index <= n:
        new_number = pointer1 + pointer2
        pointer1 = pointer2
        pointer2 = new_number
        index += 1
    return pointer2


print(fib_number_gen(10000))

# 1. Итерационный протокол
# 2. Итерируемые объекты
# 3. Объекты итераторы


class FibonacciIterator:  # Итераторы
    def __init__(self, max_index, first, second, index):
        self.max_index = max_index
        self.first = first
        self.second = second
        self.index = index

    def __next__(self):
        if self.index == self.max_index:
            raise StopIteration

        if self.index in (0, 1):
            result = self.index
        else:
            result = self.first + self.second
            self.first, self.second = self.second, result

        self.index += 1
        return result


class Fibonacci:  # Итерируемыми объектами
    def __init__(self, max_index):
        self.max_index = max_index

    def __iter__(self):
        self.first = 0
        self.second = 1
        self.index = 0
        return FibonacciIterator(self.max_index, self.first,
                                 self.second, self.index)


f = Fibonacci(10)

for number in f:
    print(number)

# f_iter = iter(f)
# print(f_iter)
# print(next(f))

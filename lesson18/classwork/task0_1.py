class Example:
    # def test(self, a, b):
    #     print(a, b)

    def test(self, a, b, c):
        print(a, b, c)


# Все атрибуты и методы класса сохраняются в памяти ввиде словаря
# print(Example.__dict__)


class A:
    __slots__ = ("a", "b", "c")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self):
        return self.a + self.b


print(A.__dict__)
a = A(1, 2)
print(a.__slots__)
print(a.c)
print(a.__slots__)

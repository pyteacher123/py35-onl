# Магические (дандер) методы
# Метод = функция, определённая внутри класса.
# Атрибуты объекта класса - это переменные, которые мы определяем и
# храним в объекте какого-то класса и
# можем получить к ним доступ через оператор точка (".").


def fib_gen():
    print("Hello")


class Rectangle:
    # В СВОИХ КЛАССАХ НЕ ОПРЕДЕЛЯЕМ
    def __new__(cls, *args, **kwargs):  # конструктор
        # print("__new__ calls")
        # print(cls)
        res = super().__new__(cls)
        # print(res)
        return res

    def __init__(self, a, b, c, d):  # инициализатор
        print("__init__ calls")
        self.a = a
        self.b = b
        self.c = c
        self.d = d


r1 = Rectangle(2, 4, 2, 4)
print(r1.a)
print(r1.b)

r2 = Rectangle(3, 5, 3, 5)
print(r2.a)
print(r2.b)

class A:
    pass


# a1 = A()  # a - переменная, которая ссылается на объект класса A.
# print(a1)  # A - это название класса.
# print(type(a1))

# # A - это переменная, которая хранит объект класса type.
# # print(type(A))

# # Создание объекта в python
# # Создаётся объект класса type -> создаётся объекта класса A
# # Объект класса type, который хранится в переменной A создаёт метакласс.
# # Иными словами метакласс - это класс, объекты которого тоже классы.
# # type - метакласс, который создаёт другие классы.

# B = type("B", (), {})
# b1 = B()
# print(b1)
# print(type(b1))


class Meta(type):
    def __new__(cls, *args, **kwargs):
        print("__new__ of Metaclass calls")
        print(args)
        print(kwargs)
        res = super().__new__(cls, *args, **kwargs)
        print(res)
        return res

    def __init__(cls, *args, **kwargs):
        print("__init__ of Metaclass calls")
        print(args)
        print(kwargs)
        res = super().__init__(*args, **kwargs)
        print(res)
        return res

    def __call__(cls, *args, **kwargs):
        print("__call__ of Metaclass calls")
        print(args)
        print(kwargs)
        return super().__call__(*args, **kwargs)


class C(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("__new__ of C calls")
        print(args)
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, a, b):
        print("__init__ of C calls")
        self.a = a
        self.b = b


c1 = C(1, 2)
print(f"C OBJECT CREATED: {c1}")

# инкапсуляция - это свойство класса, проявляющееся в том, что он как бы
# служит "контейнером", то есть объединяет в себе и данные и методы работы
# над этими данными.


class Rectangle:
    LIMITS = range(1, 1000)

    def __init__(self, a, b, c, d):
        self.a = a  # атрибут объекта
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):  # bound method
        return self.a + self.b + self.c + self.d

    def square(self):
        return self.a * self.b

    @classmethod
    def check_in_limit(cls, value):  # class method
        print(cls)
        return value in cls.LIMITS

    @staticmethod
    def print_hello_world():  # static method
        print("Hello World")


res = Rectangle.check_in_limit(10)
print(res)

Rectangle.print_hello_world()

r1 = Rectangle(2, 4, 2, 4)
res = r1.perimetr()
res1 = r1.square()
print(res)
print(res1)

r2 = Rectangle(3, 5, 3, 5)
res = r2.perimetr()
res1 = r2.square()
print(res)
print(res1)

class Rectangle:
    def __init__(self, a, b, c, d):
        self.a = a  # атрибут объекта
        self.b = b
        self.c = c
        self.d = d

    def __eq__(self, other):
        print("__eq__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() == other.perimetr()

    def __ne__(self, other):
        print("__ne__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() != other.perimetr()

    def __gt__(self, other):
        print("__gt__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() > other.perimetr()

    def __lt__(self, other):
        print("__lt__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() < other.perimetr()

    def __ge__(self, other):
        print("__ge__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() >= other.perimetr()

    def __le__(self, other):
        print("__le__ calls")
        print(self)
        print(other)
        if not isinstance(other, Rectangle):
            raise ValueError("The second object must be Rectangle")
        return self.perimetr() <= other.perimetr()

    def perimetr(self):  # bound method
        return self.a + self.b + self.c + self.d


r1 = Rectangle(2, 6, 2, 6)
r2 = Rectangle(2, 7, 2, 7)

print(r1 <= r2)  # синтаксический сахар

# Класс B является подтипом класса A.
# Цепочка наследования образует иерархию типов в программе.

class A:  # классом-родителем или базовым классом
    def __init__(self, text):
        self.text = text

    def hello(self):
        print("Hello World!")


class B(A):  # классом-потомком или дочерним классом или наследником
    def __init__(self, text, m):
        self.text = text
        self.m = m


class C(B):
    pass


c = C(text=20)
c.hello()

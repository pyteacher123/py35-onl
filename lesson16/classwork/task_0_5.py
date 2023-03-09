# python2: C -> A -> A1 -> object -> B -> B1 -> object
# object class has a method __init__
# python3: C -> A -> A1 -> B -> B1 -> object
# В python3 внедрён новый алгоритм построения иерархии наследования.

class A1:
    pass


class B1:
    pass


class A(A1):
    pass


class B(B1):
    def __init__(self, text):
        self.text = text


class C(A, B):
    pass


c = C(text=10)
print(c)
print(C.__mro__)

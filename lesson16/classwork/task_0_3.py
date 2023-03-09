class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


b1 = B(10, 10)
print(b1.b)
print(b1.a)

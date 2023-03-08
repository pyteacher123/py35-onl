class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b


ex1 = Example(1, 1)
print(ex1.a)
print(getattr(ex1, 'a'))
ex1.a = 10
print(ex1.a)
setattr(ex1, 'a', 20)
print(ex1.a)

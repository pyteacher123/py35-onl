class A:
    def hello(self):
        print("Hello world")


class B:
    def hello(self):
        print("Hello Maxim")


a = A()
b = B()


def print_func(obj):
    obj.hello()


print_func(a)
print_func(b)

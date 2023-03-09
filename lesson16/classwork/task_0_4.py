class A:
    def hello(self):
        print("Hello World")


class B:
    def hello(self):
        print("Lorem Ipsum")


class C(A, B):
    pass


c = C()
c.hello()

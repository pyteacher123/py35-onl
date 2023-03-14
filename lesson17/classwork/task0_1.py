from abc import ABC, abstractmethod


class AbstractHello(ABC):
    @abstractmethod
    def hello(self):
        ...


class A(AbstractHello):
    def hello(self):
        print("Hello world")


class B(AbstractHello):
    def hello(self):
        print("Hello Maxim")


class C(AbstractHello):
    pass


a = A()
b = B()
a.hello()
b.hello()
c = C()
c.hello()

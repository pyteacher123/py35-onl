# Аcсоциация - HAS A
# Наследование - IS A


class A:
    pass


class B:
    def __init__(self, a):
        self.b = a


a1 = A()
b1 = B(a1)


class Profile:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class User:
    def __init__(self, name, surname, profile):
        self.name = name
        self.surname = surname
        self.profile = profile

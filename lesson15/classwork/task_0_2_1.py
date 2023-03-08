# Дескриптор - класс, который реализует протокол дескриптора.
# Протокол дескриптора - это реализация в каком-то классе магических методов
# __get__, __set__, __delete__
# Класс дескриптор может управлять атрибутами другого класса.
# __set_name__ - метод для получения названия атрибута

class ValidationError(Exception):
    ...


class Coordinate:
    def __set_name__(self, owner, name):
        print("__set_name__ calls")
        print(self)
        print(owner)
        print(name)
        self.name = "_" + name

    def __get__(self, instance, owner):
        print("__get__ calls")
        print(self)
        print(instance)
        print(owner)
        print(self.name)
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print("__set__ calls")
        print(self)
        print(instance)
        print(value)
        print(self.name)
        if value < 0:
            raise ValidationError(f"{self.name} must be more than 0.")
        setattr(instance, self.name, value)


class Point:
    coord_x = Coordinate()
    coord_y = Coordinate()

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


class Point3D:
    coord_x = Coordinate()
    coord_y = Coordinate()
    coord_z = Coordinate()

    def __init__(self, coord_x, coord_y, coord_z):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z


p1 = Point3D(0, 0, 0)
print("++++++", p1)
p2 = Point3D(0, 0, -10)

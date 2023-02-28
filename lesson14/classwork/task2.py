# Инкапсуляция
# Сокрытие (атрибутов, методов)
# Атрибуты могут быть: public - доступны внутри класса и вне класса
#                      private - доступны внутри класса, но не снаружи

# Как "сделать" private атрибут в python:
# СПОСОБ 1: указать перед названием атрибута или метода нижнее подчёркивание
# Например self.coord_x - публичный атрибут
#          self._coord_x - приватный атрибут
# Это договоренность между разработчиками на языке python,
# что если атрибут назван с нижнего подчёркивания - то этот атрибут считается
# private. То есть этот атрибут нельзя вызывать или изменять напрямую вне
# класса
# СПОСОБ 2: указать перед названием атрибута или метода 2 нижних подчёркивания
# Например self.coord_x - публичный атрибут
#          self.__coord_x - приватный атрибут
# Геттеры, сеттеры
# метод-свойство (property) - альтернатива в python для реализации механизмов
# геттера и сеттера.

class ValidationError(Exception):
    ...


class Point:
    def __init__(self, coord_x, coord_y):
        if coord_x < 0 or coord_y < 0:
            raise ValidationError("coord must be positive.")
        self._coord_x = coord_x
        self._coord_y = coord_y

    def get_coord_x(self):
        return self._coord_x

    def set_coord_x(self, value):
        if value < 0:
            raise ValidationError("coord_x must be positive.")
        self._coord_x = value


class Point3D:
    def __init__(self, coord_x, coord_y, coord_z):
        if coord_x < 0 or coord_y < 0 or coord_z < 0:
            raise ValidationError("coord must be positive.")
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z


class Circle:
    def __init__(self, c_point, radius):
        self.c_point = c_point
        self.radius = radius


class Rectagle:
    def __init__(self, point_a, point_b, point_c, point_d):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d


p1 = Point(0, 0)
print(p1.get_coord_x())
p1.set_coord_x(-10)
print(p1.get_coord_x())


# c1 = Circle(p1, 10)
# print(c1)
# print(c1.c_point)

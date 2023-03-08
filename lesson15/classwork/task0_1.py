# Методы-свойства - это метод, который можно вызывать как свойство.
# 1. Чтобы сделать метод методом-свойством, его надо обернуть во
# встроенный декоратор property.


class ValidationError(Exception):
    ...


class Example:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def _validate_coord(self, value):
        if value < 0:
            raise ValidationError("coord must be positive.")

    @property
    def coord_x(self):  # Аналог геттера
        print("coord_x getter property calls")
        return self._coord_x

    @coord_x.setter
    def coord_x(self, value):
        print("coord_x setter property calls")
        self._validate_coord(value)
        self._coord_x = value

    @property
    def coord_y(self):
        print("coord_y getter property calls")
        return self._coord_y

    @coord_y.setter
    def coord_y(self, value):
        print("coord_y setter property calls")
        self._validate_coord(value)
        self._coord_y = value


p1 = Point(0, 0)
print(p1.coord_x)
p1.coord_x = 10
print(p1.coord_x)
print(p1.coord_y)
p1.coord_y = -10

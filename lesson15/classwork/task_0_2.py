# Дескриптор - класс, который реализует протокол дескриптора.
# Протокол дескриптора - это реализация в каком-то классе магических методов
# __get__, __set__, __delete__
# Класс дескриптор может управлять атрибутами другого класса.


class ValidationError(Exception):
    ...


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


class Point3D:
    def __init__(self, coord_x, coord_y, coord_z):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z

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

    @property
    def coord_z(self):
        print("coord_z getter property calls")
        return self._coord_z

    @coord_z.setter
    def coord_z(self, value):
        print("coord_z setter property calls")
        self._validate_coord(value)
        self._coord_z = value


p1 = Point3D(0, 0, 0)
print(p1)
p2 = Point3D(0, 0, -10)

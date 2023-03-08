class ValidationError(Exception):
    ...


class Point:
    def __init__(self, coord_x, coord_y):
        self.set_coord_x(coord_x)
        self.set_coord_y(coord_y)

    def _validate_coord(self, value):
        if value < 0:
            raise ValidationError("coord must be positive.")

    def get_coord_x(self):
        return self._coord_x

    def set_coord_x(self, value):
        self._validate_coord(value)
        self._coord_x = value

    def get_coord_y(self):
        return self._coord_y

    def set_coord_y(self, value):
        self._validate_coord(value)
        self._coord_y = value


p1 = Point(0, 0)
print(p1.get_coord_x())
p1.set_coord_x(10)
print(p1.get_coord_x())

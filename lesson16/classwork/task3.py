from math import pi


class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            res = self.coord_x
        elif self.counter == 1:
            res = self.coord_y
        else:
            raise StopIteration

        self.counter += 1
        return res


class Figure:
    def __init__(self, color):
        self.color = color

    def draw(self):
        return self.__dict__


class Line(Figure):
    def __init__(self, color, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        super().__init__(color)

    def length(self):
        x1, y1 = tuple(self.point_a)
        x2, y2 = tuple(self.point_b)
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


class Triangle(Figure):
    def __init__(self, color, point_a, point_b, point_c):
        super().__init__(color)
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimetr(self):
        x1, y1 = tuple(self.point_a)
        x2, y2 = tuple(self.point_b)
        x3, y3 = tuple(self.point_c)
        res = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 + \
            ((x3 - x2)**2 + (y3 - y2)**2)**0.5 + \
            ((x1 - x3)**2 + (y1 - y3)**2)**0.5
        return res


class Circle(Figure):
    def __init__(self, color, centre, radius):
        super().__init__(color)
        self.centre = centre
        self.radius = radius

    def length(self):
        return pi * self.radius**2


class Rectangle(Figure):
    def __init__(self, color, point_a, point_b, point_c, point_d):
        super().__init__(color)
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def perimetr(self):
        x1, y1 = tuple(self.point_a)
        x2, y2 = tuple(self.point_b)
        x3, y3 = tuple(self.point_c)
        x4, y4 = tuple(self.point_d)
        res = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 + \
            ((x3 - x2)**2 + (y3 - y2)**2)**0.5 + \
            ((x4 - x3)**2 + (y4 - y3)**2)**0.5 + \
            ((x1 - x4)**2 + (y1 - y4)**2)**0.5
        return res


r1 = Rectangle("red", Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
print(r1.perimetr())
print(r1.draw())

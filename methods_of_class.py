import math


class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 0

    def set_center(self, x, y):
        self.x = x
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def get_distance(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)


class Student:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Poligon:
    def set_sides(self, sides_list: list):
        self.sides = sides_list

    def get_perimeter(self):
        return sum(self.sides)


poligon = Poligon()

sides_string = input('sides: ')
poligon.set_sides(
    [int(side) for side in sides_string.split(', ')]
)
print(poligon.get_perimeter())

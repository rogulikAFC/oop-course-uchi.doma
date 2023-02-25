from math import pi


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * self.radius * pi

    def get_perimeter(self):
        return 2 * pi * self.r


class Number:
    ALPHABET = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def __init__(self, number, base):
        result = ''
        while number != 0:
            digit = number % base
            if digit >= 10:
                digit = self.ALPHABET[digit]
            result += str(digit)
            number //= base
        self.value = result[::-1]

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'

    def to_dec(self):
        return int(self.number, self.base)


class Bin(Number):
    def __init__(self, number):
        super().__init__(number, 2)

    def __add__(self, other):
        dec_num = self.to_dec() + other.to_dec()
        return self(dec_num, 2)

    def __sub__(self, other):
        dec_num = self.to_dec() - other.to_dec()
        return self(dec_num, 2)

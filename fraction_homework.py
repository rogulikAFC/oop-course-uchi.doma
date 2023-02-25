import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(int(num), int(den))

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    @staticmethod
    def get_reduced_fraction(num, den):
        """Принимает числитель и знаменатель дроби
        и возвращает кортеж: числитель и знаменатель сокращенной дроби."""
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """Принимает знаменатель первой и знаменатель второй дроби и
        возвращает общий знаменатель."""
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __add__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num + common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __sub__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num - common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __lt__(self, other):
        final_fraction = self - other
        return final_fraction.num < 0

    def __eq__(self, other):
        return self.den == other.den and self.num == other.num

    def __le__(self, other):
        is_less = self.__lt__(other)
        is_eq = self.__eq__(other)
        return is_less or is_eq

    def __ge__(self, other):
        is_greater = other.__lt__(self)
        is_eq = self.__eq__(other)
        return is_greater or is_eq


frac1_input = input('1: ').split()
frac1 = Fraction(
    frac1_input[0], frac1_input[1]
)

frac2_input = input('2: ').split()
frac2 = Fraction(
    frac2_input[0], frac2_input[1]
)

oper = input('operation: ')

if oper == '==':
    print(frac1 == frac2)

elif oper == '!=':
    print(frac1 != frac2)

elif oper == '>':
    print(frac1 > frac2)

elif oper == '>=':
    print(frac1 >= frac2)

elif oper == '<':
    print(frac1 < frac2)

elif oper == '<=':
    print(frac1 <= frac2)

elif oper == '+':
    print(frac1 + frac2)

elif oper == '-':
    print(frac1 - frac2)

elif oper == '*':
    print(frac1 * frac2)

elif oper == '/':
    print(frac1 / frac2)

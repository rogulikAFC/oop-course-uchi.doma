class Point:
    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return f'Точка с координатами {self.coords}'


class Sequence:
    def __init__(self, *args):
        self.elements = list(args)

    def __str__(self):
        return f'Последовательность {self.elements}'

    def __len__(self):
        return len(self.elements)


class RomanNumber:
    def __init__(self, num: str = None):
        self.num = num

    def __str__(self):
        return f'Число {self.num}'

    def __len__(self):
        return len(self.num)

    def __bool__(self):
        return bool(self.num)


class PrimeNumbers:
    def __init__(self, n):
        number = 2
        numbers = []

        while len(numbers) < n:
            for d in range(2, number - 1):
                if number % d == 0:
                    break
            else:
                numbers.append(number)
            number += 1

        self.numbers = numbers

    def __str__(self):
        return f'Последовательность из {len(self.numbers)} простых чисел {self.numbers}'

    def total(self):
        return sum(self.numbers)

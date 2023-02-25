class Date:
    def __init__(self, d, m, y):
        self.d = int(d)
        self.m = int(m)
        self.y = int(y)

    def __eq__(self, other):
        if self.y == other.y:
            if self.m == other.m:
                if self.d == other.d:
                    return True

        return False

    def __lt__(self, other):
        if self.y < other.y:
            return True

        elif self.y > other.y:
            return False

        else:
            if self.m < other.m:
                return True

            elif self.m > other.m:
                return False

            else:
                if self.d < other.d:
                    return True

                elif self.d > other.d:
                    return False


date1 = Date(*map(int, input().split('.')))
date2 = Date(*map(int, input().split('.')))

if date1 < date2:
    print('Второй старше')

elif date1 == date2:
    print('Одного возраста')

elif date1 > date2:
    print('Первый старше')

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __eq__(self, other):
        return self.y, self.m, self.y == other.y, other.m, other.d

    def __lt__(self, other):
        return self.y, self.m, self.y < other.y, other.m, other.d


date1 = Date(10, 10, 2000)
date2 = Date(10, 10, 2000)

print(date1 == date2)

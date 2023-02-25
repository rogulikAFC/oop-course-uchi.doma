class OddEvenList(list):
    def get_even(self):
        return [num for num in self if num % 2 == 1]

    def get_odd(self):
        return [num for num in self if num % 2 != 1]


new_list = OddEvenList()
n = input('n: ')

for num in range(int(n)):
    number = int(input('num: '))
    new_list.append(number)

print(new_list)
print(new_list.get_even())
print(new_list.get_odd())

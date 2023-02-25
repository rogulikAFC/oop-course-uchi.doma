n = int(input('n: '))
array = [value for value in map(int, input('list: ').split())]

for i in range(n):
    for j in range(1, n-i):
        if array[j-1] < array[j]:
            array[j], array[j-1] = array[j-1], array[j]

    print(' '.join(str(el) for el in array))

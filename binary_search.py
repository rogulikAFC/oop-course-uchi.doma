n = int(input('n: '))
array = [value for value in map(int, input('list: ').split())]
# n = len(array)
x = int(input('x: '))

left = 0
right = n

while left < right:
    mid = (left + right) // 2

    if array[mid] == x:
        print(mid)
        break

    elif array[mid] < x:
        left = mid + 1

    else:
        right = mid

else:
    print(-1)

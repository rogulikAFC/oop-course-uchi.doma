set = {int(num) for num in input('set: ').split()}
total = int(input('gives: '))


def get_gives():
    for current in set:
        for second_num in set:
            if current + second_num == total:
                if second_num != current:
                    return {current, second_num}


try:
    print(' '.join(str(num) for num in get_gives()))

except:
    print('None')

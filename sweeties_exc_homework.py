try:
    sweeties1, sweeties2, friends = map(int, input().split())
    sweeties = sweeties1 + sweeties2

    print(sweeties // friends)

except Exception as e:
    print(e.__class__.__name__)

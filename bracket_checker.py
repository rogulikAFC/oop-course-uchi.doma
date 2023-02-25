s = input('brackets: ')
stack = []


def is_valid():
    for char in s:
        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack or stack[-1] != '(':
                return False

            stack.pop()

    return not stack


print(is_valid())

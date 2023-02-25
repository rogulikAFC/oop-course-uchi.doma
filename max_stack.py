class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def __str__(self):
        ' '.join(str(el) for el in self.stack)

    def push(self, item):
        self.stack.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        del (self.stack[0])

    def size(self):
        print(len(self.stack))

    def get_max(self):
        print(self.max_stack[-1] if self.max_stack else None)


# Считываем количество команд
n = int(input())

# Создаем объект класса StackMax
stack = StackMax()

# Обрабатываем команды
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'size':
        stack.size()
    elif command[0] == 'get_max':
        stack.get_max()

    print(stack)

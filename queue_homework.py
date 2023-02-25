class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items.pop(0)
        print(item)

    def size(self):
        print(len(self.items))


queue = Queue()

n = int(input('n'))

for i in range(n):
    command = input('command: ')

    try:
        command, data = command.split()

        if command == 'push':
            queue.push(data)

        else:
            continue

    except:
        if command == 'pop':
            queue.pop()

        elif command == 'size':
            queue.size()

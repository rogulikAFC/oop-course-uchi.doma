class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def get_position(node, value, n):
    if node.next != None:
        if node.value == value:
            return n

        else:
            get_position(node.next, value, n)

# class Node:
#    def __init__(self, value, next):
#        self.value = value
#        self.next = next

# def search(vertex, string):
#     count = 1
#     while vertex:
#         if vertex.value == string:
#             print(count)
#             return True
#         vertex = vertex.next
#         count += 1
#     print(1)


n4 = Node('apple', None)
n3 = Node('banana', n4)
n2 = Node('orange', n3)
n1 = Node('grapes', n2)

search(n1, 'banana')


n4 = Node('apple', None)
n3 = Node('banana', n4)
n2 = Node('orange', n3)
n1 = Node('grapes', n2)

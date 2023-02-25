head_node = None


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


def print_linked_list(vertex):
    while vertex:
        print(vertex, end=" -> ")
        vertex = vertex.next

    # print("None")


def remove_node(head, index):
    if index != 0:
        temp = head

        for i in range(1, index):
            if temp != None:
                temp = temp.next

        if temp != None and temp.next != None:
            node_to_delete = temp.next
            temp.next = temp.next.next
            node_to_delete = None

    elif index == 0:
        global head_node
        head_node = head.next
        head = None


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)
head_node = n1

el_to_delete = int(input())

# print(print_linked_list(n1))
remove_node(head_node, el_to_delete)
print(print_linked_list(head_node))

class Node():
    """A class for a node in the linked list"""

    def __init__(self, given_data):
        self.data = given_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    """A class for the linked list"""

    def __init__(self):
        """Constructor method"""
        self.head = None  # Initialise to None as the linked list is empty

    def insert_at_front(self, data):
        """Insert a node to the front of the list"""

        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.head is None:
            self.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.set_next(self.head)
            self.head = new_node

    def traverse(self):
        """Traverse the list and output the data from each node"""

        # Set the current node as the head
        current = self.head

        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()


def insert_test_data(my_list):
    my_list.insert_at_front("Julie")
    my_list.insert_at_front("Rey")
    my_list.insert_at_front("Habib")
    my_list.insert_at_front("Sabrina")
    my_list.insert_at_front("Mina")


if __name__ == '__main__':
    my_list = LinkedList()
    print("\nInsert test data into the linked list in order:")
    insert_test_data(my_list)
    my_list.traverse()
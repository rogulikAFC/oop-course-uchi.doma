from collections import deque


def breadth_first_search(graph, start_node, target_node):
    # Initialisation
    queue = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False

    # Repeat while there are items in the queue
    # and the target node has not been found
    while len(queue) != 0 and found == False:

        # Set the current node to the first item in the queue
        current_node = queue[0]

        # Remove the current node from the start of the queue
        queue = queue[1:]

        # Get the current node's list of neighbours
        neighbours = graph[current_node]

        # Repeat for each node in the neighbours list
        for node in neighbours:
            print(f"node is {node}")
            # Check if the node has not already been discovered
            if node not in discovered:
                # Check if the target node has been found
                if node == target_node:
                    found = True
                else:
                    # Add the node to the stack
                    # and to the discovered list
                    queue.append(node)
                    discovered.append(node)
    print(f"queue: {queue}")
    print(f"neighbours: {neighbours}")
    return found


def depth_first_search(graph, start_node, target_node):


    # Initialisation
    stack = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False

    # Repeat while there are items in the stack
    # and the target node has not been found
    while len(stack) != 0 and found == False:

        # Pop the top item from the stack to be the current node
        current_node = stack.pop()

        # Get the current node's list of neighbours
        neighbours = graph[current_node]

        # Testing
        print(f"Curent node: {current_node}")
        print(f"\nStack: {stack}")
        print(f"Discovered: {discovered}")
        print(f"Neighbours: {neighbours}")

        # Repeat for each node in the neighbours list
        for node in neighbours:
            # Check if the node has not already been discovered
            if node not in discovered:
                # Check if the target node has been found
                if node == target_node:
                    found = True
                else:
                    # Push the node onto the stack
                    # and add it to the discovered list
                    stack.append(node)
                    discovered.append(node)

                    # Testing
                    print(f"\nStack: {stack}")
                    print(f"Discovered: {discovered}")
                    print(f"Neighbours: {neighbours}")

    return

def find_shortest_path(graph, start, end, path=[]):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)

test_graph = {
    "0": ["1"],
    "1": ["0", "2", "9"],
    "2": ["1"],
    "3": ["4", "5", "6", "9"],
    "4": ["3"],
    "5": ["3", "8"],
    "6": ["3", "7"],
    "7": ["6", "8", "9"],
    "8": ["5", "7"],
    "9": ["1", "3", "7"]
}



# Search for a value and return True if it has been found
item_to_find = "8"
start = "0"
found = breadth_first_search(test_graph, start, item_to_find)

# Output the search result
print(f"\nThe target node is {item_to_find}")
depth_first_search(test_graph,start,item_to_find)
print(find_shortest_path(test_graph,"0","9"))

if found == True:
    print(f"{item_to_find} was found in the graph")
else:
    print(f"{item_to_find} was NOT found in the graph")
graph = [
    ["A", "B", 15],
    ["A", "D", 15],
    ["A", "E", 5],
    ["B", "C", 10],
    ["B", "E", 5],
    ["C", "D", 15],
    ["C", "F", 15],
    ["C", "E", 5],
    ["D", "F", 5],
    ["E", "F", 25],
]

# CREATE stack
# MARK startingNode as VISITED AND PUSH currentNode onto stack
# WHILE stack NOT EMPTY
# 	currentNode = topOfStack
# 	WHILE currentNode has (unvisited) neighbour
# 		MARK neighbourNode as VISITED AND PUSH onto stack
# 		currentNode = topOfStack
# 	POP topOfStack
#


def stack_traverse_graph(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for node in graph:
                if node[0] == current_node and node[1] not in visited:
                    stack.append(node[1])
    return visited


print(stack_traverse_graph(graph, "A"))


# CREATE queue
# MARK startingNode as VISITED AND ENQUEUE startingNode into queue
# WHILE queue NOT EMPTY
# 	DEQUEUE startOfQueue
# 	MARK and ENQUEUE (unvisited) neighbour(s) of dequeuedNode


def queue_traverse_graph(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    while len(stack) > 0:
        current_node = stack.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            for node in graph:
                if node[0] == current_node and node[1] not in visited:
                    stack.append(node[1])
    return visited


print(queue_traverse_graph(graph, "A"))

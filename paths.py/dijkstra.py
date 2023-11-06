# graph data structure
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}


# dijkstra's algorithm
def dijkstra(graph, start, goal):
    shortest_distance = {}
    infinite = 9999999
    path = []
    privious_node = {}

    for i in graph:
        shortest_distance[i] = infinite
    shortest_distance[start] = 0

    while graph:
        min_node = None
        for node in graph:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                privious_node[child_node] = min_node
        graph.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = privious_node[current_node]
        except KeyError:
            print("Path not reachable")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinite:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("And the path is " + str(path))


dijkstra(graph, "A", "F")

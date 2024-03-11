from collections import defaultdict 


class Graph:
    def __init__(graph):
        graph.dict = defaultdict(list)
    
    def add(graph,node,adjacent_node): 
        graph.dict[node].append(adjacent_node)

    def view(graph):
        return graph.dict
    
    def bfs(graph, start,goal):
        visited = []
        queue = []
        if start == goal:
            return start
        visited.append(start)
        queue.append(start)
        while len (queue) > 0:
            v = queue.pop(0) #dequeue tjhe first ellement then find all of its neighbour
            for neighbour in graph.dict[v]:
                
                queue.append(neighbour)
                visited.append(neighbour)
                if neighbour == goal:
                    return visited
        return visited
    
    def dfs(graph, start):
        stack = []
        visited = []
        stack.append(start)
        while len(stack) > 0:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for neighbour in graph.dict[v]:
                    stack.append(neighbour)

        return visited
    
    



tree = Graph()
tree.add("A", "B")
tree.add("A", "C")
tree.add("B", "D")
tree.add("B", "E")
tree.add("D", "F")
tree.add("F", "G")
tree.add("G", "H")
print(tree.view())
print(tree.dfs("A"))



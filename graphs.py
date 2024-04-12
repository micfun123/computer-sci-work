import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def save_to_file(self, filename):
        nx.write_adjlist(self.graph, filename)

    @staticmethod
    def load_from_file(filename):
        graph = Graph()
        graph.graph = nx.read_adjlist(filename)
        return graph

    def visualize(self, shortest_path=None):
        pos = nx.spring_layout(self.graph)  # Position nodes using Fruchterman-Reingold force-directed algorithm
        nx.draw_networkx_nodes(self.graph, pos, node_size=700)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos)

        if shortest_path:
            edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
            nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color='r', width=2)

        plt.show()

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source=source, target=target)

    def __str__(self):
        return str(dict(self.graph.adjacency()))

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

print("Original graph:")
print(g)

# Save graph to file
g.save_to_file('graph.txt')

# Load graph from file
loaded_graph = Graph.load_from_file('graph.txt')
print("\nLoaded graph:")
print(loaded_graph)

# Visualize the loaded graph
loaded_graph.visualize()

# Find shortest path
source = 'A'
target = 'D'
shortest_path = loaded_graph.shortest_path(source, target)
print(f"Shortest path between {source} and {target}: {shortest_path}")

# Visualize the loaded graph with shortest path highlighted
loaded_graph.visualize(shortest_path=shortest_path)

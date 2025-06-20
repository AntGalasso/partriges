from itertools import combinations

from urllib3.util import is_connection_dropped


#   input: G(V, E) and k integer
#   question: is there a subset S of V such that:
#
#           for each u, v to subset are linked by an edge in E with |S| = k
#
# [+]

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        if to_node not in self.graph[from_node]:
            self.graph[from_node].append(to_node)
        if from_node not in self.graph[to_node]:
            self.graph[to_node].append(from_node)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} --> {self.graph[node]}")

    def get_nodes(self):
        return list(self.graph.keys())

    def is_complete(self, nodes_subset=None):
        if nodes_subset is None:
            nodes_subset = self.get_nodes()
        n = len(nodes_subset)
        if n <= 1:
            return True
        for u, v in combinations(nodes_subset, 2):
            if v not in self.graph[u] or u not in self.graph[v]:
                return False
        return True

def myClique(graph_obj, k):
    nodes = graph_obj.get_nodes()
    if k > len(nodes):
        return False
    for subset in combinations(nodes, k):
        # Call is_complete on subset
        if graph_obj.is_complete(subset):
            return True
    return False


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("A", "C")
    g.add_edge("C", "D")

    g.print_graph()

    print("Is whole graph complete?", g.is_complete())    # False
    print("Is there a 3-clique?", myClique(g, 3))          # True (A,B,C)
    print("Is there a 4-clique?", myClique(g, 4))          # False



class Graph:
    def __init__(self):
        self.grafo = {}
    def aggiungiNodo(self, node):
        if node not in self.grafo:
            self.grafo[node] = []
    def aggiungiArco(self, from_node, to_node):
        self.aggiungiNodo(from_node)
        self.aggiungiNodo(to_node)

        if to_node not in self.grafo[from_node]:
            self.grafo[from_node] = [to_node]
    def printGrafo(self):
        for nodo in self.grafo:
            print(f"f: {nodo} --> {self.grafo[nodo]}")





graph = Graph()
n1 = "A"
n2 = "B"
n3 = "C"

graph.aggiungiArco(n1, n2)
graph.aggiungiArco(n3, n2)
graph.printGrafo()


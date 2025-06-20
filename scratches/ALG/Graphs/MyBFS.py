
class Graph:
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0
        self.num_links = 0


    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            self.num_vertices += 1

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)

        if vertex2 not in self.graph:
            self.add_vertex(vertex2)


        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
            self.num_links += 1

        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
            self.num_links += 1

    def get_first_vertex(self):
        if self.num_vertices != 0:
            return list(self.graph.keys())[0]

    def get_neighbours(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

        """ le chiavi associate al grafo - tutti i vertici 
            il grafo ha una visualizzazione del tipo
            
            {
            1: [2],  # il vertice 1 è connesso al vertice 2
            2: [1, 3],  # il vertice 2 è connesso ai vertici 1 e 3
            3: [2]   # il vertice 3 è connesso al vertice 2
        }

        """



    def my_bfs(self):
        l0 = list()
        l0.append(self.get_first_vertex())

        for i in range(self.num_vertices):
            for u in l0:
                for v in self.get_neighbours(u):
                    if v not in l0:
                        l0.append(v)
        print(l0)

    """
    def queue_bfs(self):
        q = deque()
        q.append(self.get_first_vertex())
        visited = set()
        visited.add(self.get_first_vertex())

        while q:
            el = q.popleft()
            for v in self.get_neighbours(el):
                if v not in q:
                    visited.add(el)
                    q.append(el)"""

    def my_dfs(self, vertex, visited, r):
        visited.add(vertex)
        r.append(vertex)

        for v in self.get_neighbours(vertex):
            if v not in visited:
                self.my_dfs(v, visited, r)


    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {', '.join(map(str, neighbors))}")
        print(f"Total vertices: {self.num_vertices}")
        print(f"Total edges: {self.num_links}")


# Test the Graph and BFS
# Creazione del grafo più dettagliato
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(4, 8)
g.add_edge(5, 9)
g.add_edge(6, 10)
g.add_edge(7, 11)
g.add_edge(8, 12)
g.add_edge(9, 13)

# Stampa del grafo
print("\nGrafo:")
g.print_graph()

print("\nBFS Traversal:")
g.my_bfs()  # Call the BFS method to see the traversal


# Inizializzazione della DFS
visited = set()
dfs_result = []

# Chiamata al DFS
print("\nDFS Traversal:")
start_vertex = g.get_first_vertex()
g.my_dfs(start_vertex, visited, dfs_result)

# Stampa il risultato del DFS
print("Ordine di visita DFS:", dfs_result)






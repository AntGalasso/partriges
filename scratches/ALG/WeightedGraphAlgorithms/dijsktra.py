import heapq

def my_dijkstra(graph, start ):
	S = set()
	d = {v: float('inf') for v in graph}
	d[start] = 0

	while S != set(graph):
		u = min((v for v in graph if v not in S), key = lambda v: d[v])
		S.add(u)

		for v, weight in graph[u]:
			if v not in S and d[v] > d[u] + weight:
				d[v] = d[u] + weight

	return d

def heapqDijkstra(g, s):

    #inizializziamo la coda, le distance a infinito e quella a se stesso = 0

    d = {node: float('inf') for node in g}
    d[s] = 0
    Q = [(0, s)]

    #fetchiamo la coda con ogni vicino di s e cosi via, finche non diventerà = V
    while Q:
        (current_distance, current_node) = heapq.heappop(Q)
        if current_distance > d[current_node]:
            continue

        for (neighbor, neighbor_cost) in g[current_node]:
            new_d = current_distance + neighbor_cost
            if new_d < d[neighbor]:
                d[neighbor] = new_d
                heapq.heappush(Q, (new_d , neighbor))


    return d
# Grafo rappresentato come dizionario:
# Ogni chiave è un nodo, ogni valore è una lista di tuple (vicino, peso)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distanze = my_dijkstra(graph, 'C')
print(distanze)
# Output atteso: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

distanze_heap = heapqDijkstra(graph, 'A')
print(distanze_heap)

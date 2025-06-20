import heapq

def myPrim(g, s):
    visited = set()
    min_heap = [(0, s, s)]
    mst = []
    tot_cost = 0

    while min_heap and len(visited) < len(g):
        (current_cost, from_node, to_node) = heapq.heappop(min_heap)
        if to_node not in visited:
            visited.add(to_node)
            tot_cost += current_cost
            mst.append((from_node, to_node, current_cost))  # ordine: from → to

            min_cost = float('inf')
            for (neighbor_node, neighbor_cost) in g[to_node]:  # CORRETTO ordine
                if neighbor_node not in visited and neighbor_cost < min_cost:
                    min_cost = neighbor_cost

            for (neighbor_node, neighbor_cost) in g[to_node]:  # STESSO ordine corretto
                if neighbor_node not in visited and neighbor_cost == min_cost:
                    heapq.heappush(min_heap, (neighbor_cost, to_node, neighbor_node))

    return mst, tot_cost

# Grafo non orientato rappresentato come lista di adiacenza
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst, cost = myPrim(graph, 'A')
print("Albero di copertura minimo:")
for u, v, w in mst:
    print(f"{u} --({w})--> {v}")
print(f"Costo totale: {cost}")



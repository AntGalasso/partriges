def kruskal(edges, nodes):
    mst = []
    tot_cost = 0
    components = {nodes: i for i, nodes in enumerate(nodes)}

    edges = sorted(edges, key=lambda x:x[2])

    for u, v, cost in edges:
        if components[v] != components[u]:
            mst.append(u, v, cost)
            tot_cost = tot_cost + cost

            old_component = components[v]
            new_component = components[u]

            for node in components:
                if components[node] == old_component:
                    components[node] = new_component

    return mst, tot_cost
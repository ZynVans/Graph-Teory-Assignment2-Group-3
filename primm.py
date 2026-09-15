# Graph based on the picture (adjacency list: vertex -> list of (neighbor, weight))
graph = {
    'A': [('B', 7), ('C', 6), ('G', 5), ('F', 10)],
    'B': [('A', 7), ('C', 5), ('D', 7), ('E', 9)],
    'C': [('A', 6), ('B', 5), ('F', 9), ('E', 7)],
    'D': [('B', 7), ('E', 5)],
    'E': [('B', 9), ('C', 7), ('D', 5), ('F', 5)],
    'F': [('A', 10), ('C', 9), ('G', 6), ('E', 5)],
    'G': [('A', 5), ('F', 6)],
}

def prim_mst(graph, start):

    visited = {start}      # vertices already included in the tree
    mst_edges = []          # stores the resulting MST edges
    total_cost = 0

    # repeat until all vertices are included in the tree
    while len(visited) < len(graph):
        min_weight = None   # smallest weight found so far
        min_edge = None     # the (u, v) edge with that smallest weight

        # step 3: check all edges connecting the tree to the outside
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited:
                    # step 4: compare, keep it if it's smaller
                    if min_weight is None or weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v)

        # if no edge can be used anymore, the graph is not connected
        if min_edge is None:
            print("Graph is not connected, not all vertices are reachable.")
            break

        # step 5: add the edge and vertex to the spanning tree
        u, v = min_edge
        visited.add(v)
        mst_edges.append((u, v, min_weight))
        total_cost += min_weight

    return mst_edges, total_cost


if __name__ == "__main__":
    mst, cost = prim_mst(graph, 'A')  # can start from any vertex

    print("Selected edges for the Minimum Spanning Tree (Prim's Algorithm):")
    for u, v, w in mst:
        print(f"{u}-{v} = {w}")

    print(f"\nTotal MST cost: {cost}")
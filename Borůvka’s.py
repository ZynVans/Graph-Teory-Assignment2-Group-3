def find(parent, x):
    # Find the component of vertex x
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    # Join two different components
    a, b = find(parent, a), find(parent, b)
    if a != b:
        parent[b] = a
        return True
    return False


def boruvka(vertices, edges):
    # Initially, every vertex is a separate component
    parent = {v: v for v in vertices}
    mst = []
    total = 0

    while len(mst) < len(vertices) - 1:
        # Store the cheapest edge for each component
        cheapest = {}

        for u, v, w in edges:
            a, b = find(parent, u), find(parent, v)

            if a == b:
                continue

            if a not in cheapest or w < cheapest[a][2]:
                cheapest[a] = (u, v, w)

            if b not in cheapest or w < cheapest[b][2]:
                cheapest[b] = (u, v, w)

        # Add the selected edges to the MST
        for u, v, w in cheapest.values():
            if union(parent, u, v):
                mst.append((u, v, w))
                total += w

    return mst, total


# Graph from the homework
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

edges = [
    ('A','B',7), ('A','C',6), ('A','G',5),
    ('A','F',10), ('G','F',6), ('F','C',9),
    ('F','B',9), ('F','E',5), ('C','B',5),
    ('C','E',7), ('E','B',9), ('E','D',5),
    ('B','D',7)
]

mst, total = boruvka(vertices, edges)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Weight:", total)
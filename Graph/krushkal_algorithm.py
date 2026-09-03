class DisjoinSet:

    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [0] * (n + 1)

        for i in range(n + 1):
            self.parent[i] = i

    def findPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        ParU = self.findPar(u)
        ParV = self.findPar(v)

        if ParU == ParV:
            return False

        if self.size[ParV] > self.size[ParU]:
            self.parent[ParU] = ParV
            self.size[ParV] += self.size[ParU]

        else:
            self.parent[ParV] = ParU
            self.size[ParU] += self.size[ParV]

        return True


def kruskal(n, edges):

    # Sort edges according to weight
    edges.sort()

    ds = DisjoinSet(n)

    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:

        # If they belong to different components,
        # adding this edge will not create a cycle
        if ds.unionBySize(u, v):

            mst_weight += weight
            mst_edges.append((u, v, weight))

            # MST contains n-1 edges
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges

if __name__ == "__main__":

    n = 7

    edges = [
        (1, 1, 2),
        (2, 2, 3),
        (3, 1, 4),
        (4, 3, 4),
        (5, 2, 5),
        (6, 4, 5),
        (7, 5, 6),
        (8, 6, 7)
    ]

    mst_weight, mst_edges = kruskal(n, edges)

    print("MST Weight:", mst_weight)
    print("MST Edges:", mst_edges)

# time complexity = > 
# Sorting edges:

# O(E log E)

# DSU operations:

# O(E × α(V)) ≈ O(E)

# Therefore:

# Time: O(E log E)

# Space: O(V) for the Disjoint Set.
m,n = map(int, input("Enter number of vertices and edges: ").split())


# 1) store graph as adjacency matrix


# graph = [[0]*m for _ in range(m)]

# for _ in range(n):

#     u,v = map(int, input("Enter edge u,v: ").split())

#     graph[u][v] = 1
#     graph[v][u] = 1


# print("\nAdjacency matrix")

# for row in graph:
#     print(*row)

# 2) store as adjacency List

graph = [[] for _ in range(m)]

for _ in range(n):

    u,v = map(int,input("Enter Edge U,V: ").split())

    graph[u].append(v)
    graph[v].append(u)

print("\nAdjacency List")

print(graph)
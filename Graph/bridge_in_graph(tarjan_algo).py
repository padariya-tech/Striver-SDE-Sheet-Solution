from typing import List
# Tarjan's algorithm — it's simply a way to check for the presence of a back edge. 
# The low value of a node helps us determine whether there's an alternate path (a back edge) to one of its ancestors in the DFS tree. 
# If such a back edge exists, it means that node is not the root of a strongly connected component (SCC), 
# because we can reach an earlier ancestor without having to backtrack through it
class Solution:

    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, edges, tin, low, bridges):

        vis[node] = 1

        tin[node] = self.timer
        low[node] = self.timer

        self.timer += 1

        for neighbour in edges[node]:

            # Ignore the edge we came from
            if neighbour == parent:
                continue

            # Forward/tree edge
            if vis[neighbour] == 0:

                self.dfs(
                    neighbour,
                    node,
                    vis,
                    edges,
                    tin,
                    low,
                    bridges
                )

                low[node] = min(low[node], low[neighbour])

                # Bridge condition
                if low[neighbour] > tin[node]:
                    bridges.append([node, neighbour])

            # Back edge
            else:

                low[node] = min(low[node], tin[neighbour])

    def criticalConnections(
        self,
        n: int,
        connections: List[List[int]]
    ) -> List[List[int]]:

        adj_list = [[] for _ in range(n)]

        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n

        bridges = []

        for i in range(n):
            if vis[i] == 0:
                self.dfs(
                    i,
                    -1,
                    vis,
                    adj_list,
                    tin,
                    low,
                    bridges
                )

        return bridges
    
if __name__ == "__main__":
    n = 4 
    connections = [[0,1],[1,2],[2,0],[1,3]] 
    sol = Solution() 
    answer = sol.criticalConnections(n,connections) 
    print(answer)
from typing import List

class Solution:

    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, edges, tin, low, marked):

        vis[node] = 1

        tin[node] = self.timer
        low[node] = self.timer
        child = 0
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
                    marked
                )

                low[node] = min(low[node], low[neighbour])

                # Bridge condition
                if low[neighbour] >= tin[node] and parent != -1:
                    marked[node] = 1
                child += 1
            # Back edge
            else:
                low[node] = min(low[node], tin[neighbour])

        if parent == -1 and child > 1:
            marked[node] = 1

    def articulationPoints(
        self,
        n: int,
        connections: List[List[int]]
    ) -> List[int]:

        
        adj_list = [[] for _ in range(n)]

        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        marked = [0] * n


        for i in range(n):
            if vis[i] == 0:
                self.dfs(
                    i,
                    -1,
                    vis,
                    adj_list,
                    tin,
                    low,
                    marked
                )
        ans = []
        for i in range(n):
            if marked[i] == 1:
                ans.append(i)
        return ans

if __name__ == "__main__":
    n = 5 
    connections = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
    sol = Solution() 
    answer = sol.articulationPoints(n,connections) 
    print(answer)
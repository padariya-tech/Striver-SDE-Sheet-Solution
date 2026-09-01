# Bellman-Ford Algorithm
# when graph has negative edge -> dijkstra fails
# this helps to detect negative cycle as well
# it will work only in directed graph
# it is single source shortest path algorithm
# relax all the edges V-1 times
# if we can relax any edge in Vth iteration then negative cycle is present
# edge relaxation : if dist[u] + weight < dist[v] then update dist[v] = dist[u] + weight
# why V-1 times : because in worst case we can have V-1 edges in a path from source to destination
# and to reach the destination we need to relax all the edges in the path
# Time Complexity : O(V*E)
class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:

        dist = [float('inf')] * V
        dist[src] = 0
        for i in range(V-1):
            for it in edges:
                u = it[0]
                v = it[1]
                wt = it[2]

                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        for it in edges:
                u = it[0]
                v = it[1]
                wt = it[2]

                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    return [-1]
                
        return dist


        


if __name__ == "__main__":
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    src = 0
    sol = Solution()
    answer = sol.bellmanFord(V, edges, src)
    print(answer)
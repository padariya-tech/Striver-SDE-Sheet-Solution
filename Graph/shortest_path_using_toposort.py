# step 1 ===> find a topological sort
# step 2 ===> take node out of the stack one by one and relax the edges (distance array with infinite)
# intuition ==> if i raech any node than i have already computed for previous node 
# Dijkstra's does work for this particular question, but topo sort is preferred because it's a DAG. 
# This topo sort method has a much better TC - O(V + E) compared to Dijkstra's O(E LogV). However, '
# 'topo sort wouldn't work if there were cycles present in the graph. That's when you use Dijkstra's. 
# If the graph has both a cycle and a negative weight in the cycle, both won't work! That's when you resort to Bellman Ford.
# Shortest path from any src :
# 1.Perform toposort and store the order in a stack
# 2.Once the source node is given, pop the elements in the stack until the stack's top is the source 
# 3. Rest is the same .

class Solution:
    def dfs(self,node,vis,adj,ans):

        vis[node] = 1
        for neighbors in adj[node]:
            neigh = neighbors[0]

            if vis[neigh] == 0:
                self.dfs(neigh,vis,adj,ans)

        ans.append(node)
            
    def topoShort(self,adj):

        st= []
        n = len(adj)
        vis = [0] * n
        ans = []
        for i in range(n):
            if vis[i] == 0:
                self.dfs(i,vis,adj,ans)


        return ans
        
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            weight = edges[i][2]

            adj[u].append([v,weight])
        
        print(adj)
        
        stack = self.topoShort(adj)

        dist = [float('inf')] * V

        dist[0] = 0

        while stack:

            node = stack.pop()

            for neighbor in adj[node]:

                v = neighbor[0]
                val = neighbor[1]

                if dist[node] + val < dist[v]:

                    dist[v] = dist[node] + val


        return dist

if __name__ == "__main__":

    V = 6
    edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
    sol = Solution()

    answer = sol.shortestPath(V,edges)

    print(answer)
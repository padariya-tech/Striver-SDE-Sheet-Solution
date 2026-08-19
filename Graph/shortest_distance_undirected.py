# we have undirected graph with unit weights 
# we have to find shortest distance between two nodes

from collections import deque
class Solution:

    def shortestPath(self, V, edges, src, dst):

        adj_list = [[] for _ in range(V)]

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]

            adj_list[u].append(v)
            adj_list[v].append(u)

        
        dist = [-1] * V
        
        dist[src] = 0
        
        q = deque()
        q.append(src)
        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
                if dist[node] + 1 < dist[neighbor]: # from node by adding one is less than the dist required previously to reach neighbor, 
                                                                # then update distance of the neighbor 
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)


        print(dist)
        return dist[dst]
        # return dist

        

 

if __name__ == "__main__":

    V = 9
    edges = [[0, 3], [1, 3]]
    src = 0
    dst = 8
    sol = Solution()

    answer = sol.shortestPath(V,edges,src,dst)


    print(answer)
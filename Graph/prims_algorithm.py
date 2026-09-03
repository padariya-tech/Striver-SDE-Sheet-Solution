import heapq
class Solution:
    def prims_alogrithm(self,V,edges):
        # Code implementation here
        vis = [0] * V
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        # Further implementation of the algorithm
        q= []
        # weight, node
        heapq.heappush(q,(0,0))
        ans = 0 # minimum spanning tree cost
        while q:
            dist , node = heapq.heappop(q)
            if vis[node]:
                continue
            vis[node] = 1
            ans += dist
            for neighbour in adj[node]:
                adjNode = neighbour[0]
                edW = neighbour[1]

                if vis[adjNode] == 0:
                    heapq.heappush(q,(edW,adjNode))

        return ans

if __name__ == "__main__":
    s = Solution()
    V = 9
    edges = [[0,1,4],[1,2,8],[2,3,7],[3,4,9],[4,5,10],[5,6,2],[6,7,1],[7,8,7],[7,0,8],[2,8,2],[2,5,4],[3,5,14],[1,7,11],[8,6,6]]
    ans = s.prms(V,edges)
    print(ans)
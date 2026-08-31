from collections import deque
import heapq
class Solution:
    def countPaths(self, n,arr):

        adj_list = [[] for _ in range(n)]

        for node in arr:
            adj_list[node[0]].append([node[1],node[2]])
            adj_list[node[1]].append([node[0],node[2]])

        q = []
        heapq.heappush(q,[0,0])
        dist = [float('inf')] * n
        ways = [-1] * n
        ways[0] = 1
        dist[0] = 0
        mod = 1000000007
        while q:

            dis , node = heapq.heappop(q)

            for neigh in adj_list[node]:

                adjNode = neigh[0]
                edW = neigh[1]

                if edW + dis < dist[adjNode]:
                    dist[adjNode] = edW + dis
                    ways[adjNode] = ways[node]
                    heapq.heappush(q,[dist[adjNode],adjNode])
                
                elif edW + dis == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

        return ways

if __name__ == "__main__":
    n = 7
    arr = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

    sol = Solution()
    ans = sol.countPaths(n,arr)

    print(ans)
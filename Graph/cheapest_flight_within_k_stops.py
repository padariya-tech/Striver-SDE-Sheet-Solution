from collections import deque
class Solution:
    def flights_within_k_stops(self,n,flights,src,dst,k):

        adj_list = [[] for _ in range(n)]
        for node in flights:
            adj_list[node[0]].append([node[1],node[2]])

        q = deque()

        q.append([0,src,0])
        dist = [float('inf')] * n

        while q:
            step ,node,cost = q.popleft()
            for neighbor in adj_list[node]:

                if step > k:
                    continue
                adjNode = neighbor[0]
                edW = neighbor[1]

                if dist[adjNode] > cost + edW and step <= k:

                    dist[adjNode] = cost + edW
                    q.append([step+1,adjNode,dist[adjNode]])
        return dist

if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 2
    sol = Solution()
    ans = sol.flights_within_k_stops(4,flights,src,dst,k)

    print(ans)
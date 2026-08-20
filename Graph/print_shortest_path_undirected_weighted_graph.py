import heapq
class Solution:
    def shortestPath(self,n,m,adj_list):

        q = []
        dist = [float('inf')] * (n + 1)
        parent = [-1] * (n + 1)

        dist[1] = 0 # stores the current best distance from source to node
        parent[1] = -1
        heapq.heappush(q,(0,1)) # distance , node

        while q:
            top_element = heapq.heappop(q)
            distance = top_element[0]
            node = top_element[1]

            for neighbor in adj_list[node]:
                if dist[neighbor[0]] > neighbor[1] + distance:
                    dist[neighbor[0]] = neighbor[1] + distance
                    parent[neighbor[0]] = node
                    heapq.heappush(q,(dist[neighbor[0]],neighbor[0])) #(shortest distance known at that moment, node)

        # reconstruct path from source to destination
        path = []
        node = n

        while node != -1:
            path.append(node)
            node = parent[node]

        path.reverse()

        print("Path:", path)

        return dist

if __name__ == "__main__":

    adj_list = [[],
    [[2,2],[4,1]],              # 1
    [[5,5],[3,4]],              # 2
    [[5,1]],                    # 3
    [[3,3],[5,3]],              # 4
    [] ] # node , distance
    n = 5
    m = 6
    sol = Solution()
    answer = sol.shortestPath(n,m,adj_list)
    print(answer)
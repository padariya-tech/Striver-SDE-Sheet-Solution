import heapq
class Solution:

    def dijkstra(self,adj_list):

        q = []

        heapq.heappush(q,(0,0))
        dist = [float('inf')] * len(adj_list)
        dist[0] = 0

        while q:  # runs for V time
            node,w = heapq.heappop(q) # log ( heap size)
            for neighbor in adj_list[node]:
                if dist[neighbor[0]] > dist[node] + neighbor[1]: # all the edges ( V-1 if it is dence graph )
                    # number of edges of every node above part
                    dist[neighbor[0]] = dist[node] + neighbor[1]
                    heapq.heappush(q,(dist[neighbor[0]],neighbor[0])) # log(heap size)

        return dist


if __name__ == "__main__":
    adj_list = [[[1,4],[2,4]],[[0,4],[2,2]],[[0,4],[1,2],[3,3],[4,1],[5,6]],[[2,3],[5,2]],[[2,1],[5,3]],[[2,6],[3,2],[4,3]]]
    sol = Solution()
    answer = sol.dijkstra(adj_list)
    print(answer)


# Time Complexity: O(ElogV)
# Space Complexity: O(V)

# dijkstra algorithm is a single source shortest path algorithm , 
# which is used to find the shortest path from a source to all the other vertices in a graph.
# it is not work if there are negative weight edges present in the graph because it will go forever in a loop


######################################################################################################################################################

# Time Complexity Explanation

# 1) Why Not Queue 
# ans : unneccesary more path exploration , it will give answer 
#         but priority queue will take min (greedy) each time 
#         for new node selection , 

# 2) why time complexity (ElogV) , where E => total no of edges , v == > total vertices

# check first tc of each operation

# 0( v * (log (heap size) + no of edges of each node * log(heap size)))
# o( v * (log(heap_size) * (no of edges of each node + 1)))  #no of edges of each node = V - 1

# o ( v * (log(heap_size) * V))
# o(V^2 * (log(heap_size)))

# # heap size worst case => V^2 => every node pushing the edges 

# o(v^2 * log (v^2))

# # V^2 => every node have v-1 edges so total edges => v * (v-1) = V^2 = total edges = E

# O(Elog(V))
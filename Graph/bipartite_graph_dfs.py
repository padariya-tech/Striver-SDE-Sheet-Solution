# Bipartite Graph == > color the graph with two color such that no adjacent node have same color

# linear graph are always bipartite
# graph having even cycle are bipartite

# graph with odd length never bipartite

from collections import deque
class Solution:
    def dfs(self,node,adj_list,color):

        color[node] = 1

        for neighbor in adj_list[node]:
            if color[neighbor] == -1:
                if self.dfs(neighbor,adj_list,color) == False:
                    return False
            if color[neighbor] == color[node]:
                return False
        return True
    
    def isBipartite(self, adj_list):
        n = len(adj_list)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if self.dfs(i, adj_list, color) == False:
                    return False

        return True
        # q = deque()

        # color[0] = 1
        # q.append(0)
        # while q:
        #     node = q.popleft()
            
        #     for neighbor in adj_list[node]:
        #         if color[neighbor] == -1:
        #             q.append(neighbor)
        #             color[neighbor]=1-color[node]

        #         if color[neighbor] == color[node]:
        #             return False
                
        # return True

                

    

if __name__ == "__main__":

    adj_list = [[1],[0,2,4],[1,3],[2,5,6],[1,5],[3,4],[3]]
    sol = Solution()
    answer = sol.isBipartite(adj_list)
    print(answer)
class Solution:
    def dfs(self, node, adj_list, vis,path_vis):

        vis[node] = 1
        path_vis[node] = 1

        for neighbor in adj_list[node]:
            if vis[neighbor] == 0:
                if self.dfs(neighbor,adj_list,vis,path_vis) == True:
                    return True

            elif vis[neighbor] == path_vis[neighbor]:
                return True
            
        
        path_vis[node] = 0
        return False

    def findCycle(self,adj_list):
        n = len(adj_list)
        vis = [0] * n
        path_vis = [0] * n

        for i in range(n):
            if vis[i] == 0:
                if self.dfs(i,adj_list,vis,path_vis) == True:
                    return True

        return False
if __name__ == "__main__":

    adj_list = [[1,2],[2],[3],[]]
    sol = Solution()
    answer = sol.findCycle(adj_list)
    print(answer)
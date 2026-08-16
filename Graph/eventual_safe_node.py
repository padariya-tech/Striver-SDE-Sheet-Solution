from typing import List
class Solution:
    # all the path should be ended up at terminal node ( terminal node=> node with outdegree zero)
    # anyone who is part of the cycle or leads to cycle is not leads to eventual safe state
    # same as cycle detection problem addon condition is check[node] = 0 and if not cycle then mark check[node] = 1
    def dfs(self, node, adj_list, vis,path_vis,check):

        vis[node] = 1
        path_vis[node] = 1
        check[node] = 0
        for neighbor in adj_list[node]:
            if vis[neighbor] == 0:
                if self.dfs(neighbor,adj_list,vis,path_vis,check) == True:
                    check[node] = 0
                    return True

            elif vis[neighbor] == path_vis[neighbor]:
                check[node] = 0
                return True
            
        check[node] = 1
        path_vis[node] = 0
        return False

    def eventualSafeNodes(self,adj_list):
        n = len(adj_list)
        vis = [0] * n
        path_vis = [0] * n
        check = [0] * n
        safenodes = []
        for i in range(n):
            if vis[i] == 0:
                self.dfs(i,adj_list,vis,path_vis,check)

        for i in range(n):
            if check[i] == 1:
                safenodes.append(i)
        return safenodes
        

if __name__ == "__main__":

    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    obj = Solution()
    print(obj.eventualSafeNodes(graph))



from collections import deque
class Solution:

    def dfs_cycle(self,node,parent,vis,edges):
        vis[node] = 1

        for neighbor in edges[node]:

            if vis[neighbor] == 0:
                if self.dfs_cycle(neighbor,node,vis,edges) == True:
                    return True
            elif neighbor != parent:
                return True
            
        return False
    
        # q = deque([[src,-1]])

        # while q:
        #     # print(q)
        #     node,parent = q.popleft()
        #     print(node,parent)
            
        #     for neighbor in edges[node]:
                
        #         if vis[neighbor] == 0:
        #             vis[neighbor] = 1
        #             q.append([neighbor,node])
        #         elif parent != neighbor:
        #             return True
                
        # return False
            

     
    def isCycle(self, V, edges):
        vis = [0] * V
        
        adj_list = [[] for _ in range(V)]
        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])
            
        print(adj_list)


        for i in range(V):
              if vis[i] == 0:
                # print(i)
                if self.dfs_cycle(i,-1,vis,adj_list) == True:
                        return True
        
        return False

	    
		

if __name__ == "__main__":
    V = 4
    E = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    sol = Solution()
    answer = sol.isCycle(V,edges)
    print(answer)
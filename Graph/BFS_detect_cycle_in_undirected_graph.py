from collections import deque
class Solution:

    def bfs_cycle(self,src,vis,edges):
        print(edges)
        vis[src] = 1

        q = deque([[src,-1]])

        while q:
            # print(q)
            node,parent = q.popleft()
            print(node,parent)
            
            for neighbor in edges[node]:
                
                if vis[neighbor] == 0:
                    vis[neighbor] = 1
                    q.append([neighbor,node])
                elif parent != neighbor:
                    return True
                
        return False
            

     
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
                if self.bfs_cycle(i,vis,adj_list) == True:
                        return True
        
        return False

	    
		

if __name__ == "__main__":
    V = 4
    E = 3
    edges = [[0, 1], [1, 2], [2, 3]]

    sol = Solution()
    answer = sol.isCycle(V,edges)
    print(answer)
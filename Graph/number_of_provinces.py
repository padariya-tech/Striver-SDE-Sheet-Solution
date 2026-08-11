from collections import deque


class Solution:

    def bfs(self,node,adj_list,vis):
        q = deque([node])
        
        vis[node] = 1

        while q:
            element = q.popleft()

            # print(element)

            for node in adj_list[element]:
                if vis[node] == 0:
                    vis[node] = 1
                    q.append(node)
                    
        return 

if __name__ == "__main__":
    adj_list =[[1], [0,2], [1],[4],[3,5],[4],[7],[6]]
    sol = Solution()
    n = len(adj_list)
    vis = [0]*n
    ans = 0
    for i in range(n):
        if vis[i] == 0:
            ans += 1
            print(i)
            sol.bfs(i,adj_list,vis)
    print(ans)
    
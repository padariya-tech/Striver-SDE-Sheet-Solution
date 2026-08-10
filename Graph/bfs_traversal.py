from collections import deque


class Solution:

    def bfs(self,adj_list):
        n = len(adj_list)
        q = deque([0])
        
        vis = [0] * n
        vis[0] = 1
        
        while q:
            top = q.popleft()
            print(top)
            for node in adj_list[top]:
                if vis[node] == 0:
                    vis[node] = 1
                    q.append(node)

        return 

if __name__ == "__main__":
    adj_list =[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    sol = Solution()
    sol.bfs(adj_list)
    
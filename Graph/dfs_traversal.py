from collections import deque


class Solution:

    def traversal(self,node,vis,adj_list):

        vis[node] = 1
        print(node)
        for adj in adj_list[node]:
            if vis[adj] == 0:
                self.traversal(adj,vis,adj_list)

    def dfs(self,adj_list):
        n = len(adj_list)

        vis = [0] * n
        self.traversal(0,vis,adj_list)

if __name__ == "__main__":
    adj_list =[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    sol = Solution()
    sol.dfs(adj_list)
    
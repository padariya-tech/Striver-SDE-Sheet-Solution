class Solution:
    def dfs(self,node,edges,vis,st):

        vis[node] = 1
        for neighbour in edges[node]:
            if vis[neighbour] == 0:
                self.dfs(neighbour,edges,vis,st)

        st.append(node)
    def dfs2(self,node,vis,edges):

        vis[node] = 1
        for neighbour in edges[node]:
            if vis[neighbour] == 0:
                self.dfs2(neighbour,vis,edges)

    def countSCC(self, v, edges):

        vis = [0] * v
        adj_lsit = [[] for _ in range(v)]
        reverse_adj_list = [[] for _ in range(v)]
        for i in range(len(edges)):
            u = edges[i][0]
            node = edges[i][1]

            adj_lsit[u].append(node)
            reverse_adj_list[node].append(u)
        st = []
        for i in range(v):
            if vis[i] == 0:
                self.dfs(i,adj_lsit,vis,st)

        for i in range(v):
            vis[i] = 0
        ans = 0
        while st:
            node = st.pop()
            if vis[node] == 0:
                ans += 1
                self.dfs2(node,vis,reverse_adj_list)

        return ans

if __name__ == "__main__":
    V = 6
    edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 3], [4, 5]]
    sol = Solution()
    answer = sol.countSCC(V, edges)
    print(answer)
# it only exist on DAG
# linear order of vertices such that if there is an edge from u to v then u comes before v in this order
# intuition => 
class Solution:
    def dfs(self,node,graph,vis,stack):

        vis[node] = 1
        for neighbor in graph[node]:

            if vis[neighbor] == 0:
                self.dfs(neighbor,graph,vis,stack)
            
        stack.append(node)


    def topological_sort(self,graph):
        n = len(graph)
        vis = [0] * n
        stack= []
        for i in range(n):
            if vis[i] == 0:
                self.dfs(i,graph,vis,stack)
        
        ans = []
        for i in range(len(stack)):
            ans.append(stack.pop())

        return ans


if __name__ == "__main__":

    graph = [[],[],[3],[1],[0,1],[0,2]]
    obj = Solution()
    print(obj.topological_sort(graph))
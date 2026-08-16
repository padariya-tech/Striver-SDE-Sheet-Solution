# it only exist on DAG
# linear order of vertices such that if there is an edge from u to v then u comes before v in this order
# intuition => to maintain order u -> v then u is before v , stack. is used
from collections import deque

class Solution:
    def topological_sort(self,graph):
        n = len(graph)
        
        indegree_node = [0] * n
        for i in range(n):
            for j in graph[i]:
                indegree_node[j]+= 1

        q = deque()
        ans = []
        for i in range(n):
            if indegree_node[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                    indegree_node[neighbor]-=1
                    if indegree_node[neighbor] == 0:
                        q.append(neighbor)

        

        return ans


if __name__ == "__main__":

    graph = [[],[],[3],[1],[0,1],[0,2]]
    obj = Solution()
    print(obj.topological_sort(graph))
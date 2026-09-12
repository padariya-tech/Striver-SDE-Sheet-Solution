class Solution:
    def possible_to_color(self,node_color,node,edges,color):

        n = len(color)
        for neighbour in edges[node]:
            if color[neighbour] == node_color:
                return False

        return True
    def graphColoring(self, node,color,v,edges,m):
        
        if node == v:
            return True
        
        for node_color in range(1,m+1):
            
            if self.possible_to_color(node_color,node,edges,color):

                color[node] = node_color

                if self.graphColoring(node+1,color,v,edges,m):
                    return True
                
                color[node] = 0

        return False


if __name__ == "__main__":

    v = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    m = 2

    sol = Solution()
    color = [0] * v
    adj_list = [[] for _ in range(v)]

    for i in range(len(edges)):
        u = edges[i][0]
        v_ = edges[i][1]

        adj_list[u].append(v_)
        adj_list[v_].append(u)
    print(adj_list)
    ans = sol.graphColoring(0,color,v,adj_list,m)
    print(ans)
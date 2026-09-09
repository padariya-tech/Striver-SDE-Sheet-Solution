from typing import List
class Disjoint:
    def __init__(self,n):
        self.size = [1] * (n+1)
        self.parent = [0] * (n+1)
        for i in range(n+1):
            self.parent[i] = i

    def findUPar(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self,u,v):

        ParU = self.findUPar(u)
        ParV = self.findUPar(v)

        if ParU == ParV:
            return 
        
        if self.size[ParU] < self.size[ParV]:
            self.size[ParV] += self.size[ParU]
            self.parent[ParU] = ParV
        else:
            self.size[ParU] += self.size[ParV]
            self.parent[ParV] = ParU

class Solution:
    def numOfIslands(self, n: int, m: int,
                     operators: List[List[int]]) -> List[int]:
        
        dst = Disjoint(n*m)
        print(n,m)
        vis = [[0]*m for _ in range(n)]
        ans=[]
        cnt = 0
        for edges in operators:
            u = edges[0]
            v = edges[1]

            if vis[u][v] == 1: # condition if edges are repeated
                ans.append(cnt)
                continue

            vis[u][v] = 1
            cnt += 1

            dr = [-1,0,1,0]
            dc = [0,1,0,-1]
            for i in range(4):
                newr = dr[i] + u
                newc = dc[i] + v
                if 0 <= newr < n and 0 <= newc < m:
                    if vis[newr][newc] == 1:
                        nodeNo = u * m + v
                        newnodeNo = newr * m + newc
                        if dst.findUPar(nodeNo) != dst.findUPar(newnodeNo):
                            cnt -= 1
                            dst.unionBySize(nodeNo,newnodeNo)
        
            ans.append(cnt)

    
        return ans

if __name__ == "__main__":

    n = 5
    m = 5
    operators= [[1,1],[0,1],[3,3],[3,4],[2,2],[3,1],[4,0],[3,2],[3,0]]
    sol = Solution()
    answer = sol.numOfIslands(n,m,operators)
    print(answer)
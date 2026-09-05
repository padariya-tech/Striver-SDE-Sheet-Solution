from typing import List
class DisjointSet:
    
    def __init__(self,n):
        self.rank = [0] * (n+1) # n +1 size for 0 and 1 based indexing
        self.size = [1] * (n+1)
        self.parent = [0] * (n+1)
        for i in range(n+1):
            self.parent[i] = i

    def findUPar(self,node):
        if node == self.parent[node]:
            return node
        # below logic is for path compression

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self,u,v):

        ParU = self.findUPar(u)
        ParV = self.findUPar(v)

        if ParU == ParV:
            return
        
        if self.rank[ParU] > self.rank[ParV]:
            self.parent[ParV] = ParU
        elif self.rank[ParU] < self.rank[ParV]:
            self.parent[ParU] = ParV
        else:
            self.rank[ParU] += 1
            self.parent[ParV] = ParU
    
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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dst = DisjointSet(n*m)
        vis = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                else:
                    dr = [-1,0,1,0]
                    dc = [0,1,0,-1]
                    for k in range(4):
                        newr = dr[k] + i
                        newc = dc[k] + j
                        if 0<=newr<n and 0<=newc<m:
                                if grid[newr][newc] == 1:
                                    nodeNo = i * m + j
                                    newnodeNo = newr * m + newc
                                    if dst.findUPar(nodeNo) != dst.findUPar(newnodeNo):
                                        dst.unionBySize(nodeNo,newnodeNo)


        maxSize = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dr = [-1,0,1,0]
                    dc = [0,1,0,-1]
                    unique_ultimate_parents = set()
                    for k in range(4):
                        newr = dr[k] + i
                        newc = dc[k] + j
                        if 0<=newr<n and 0<=newc<m:
                                if grid[newr][newc] == 1:
                                    
                                    newnodeNo = newr * m + newc
                                    unique_ultimate_parents.add(dst.findUPar(newnodeNo))
                    sizeTotal = 1
                    for par in unique_ultimate_parents:
                        sizeTotal += dst.size[par]

                    maxSize=max(maxSize,sizeTotal)

        for i in range(n*m):
            maxSize = max(maxSize,dst.size[dst.findUPar(i)])

        for i in range(n*m):
            maxSize = max(maxSize,dst.size[dst.findUPar(i)])

        return maxSize

if __name__ == "__main__":
    grid = [[1,1],[1,1]]
    sol = Solution()
    ans = sol.largestIsland(grid)
    print(ans)
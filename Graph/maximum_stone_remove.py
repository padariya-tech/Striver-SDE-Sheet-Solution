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
    def removeStones(self, stones: List[List[int]],n:int) -> int:
        maxRow = 0
        maxCol = 0
        for it in stones:
            maxRow = max(maxRow,it[0])
            maxCol = max(maxCol,it[1])

        dst = DisjointSet(maxRow+maxCol+1) # +1 is for safety

        stoneNodes = {}
        for edges in stones:
            nodeRow = edges[0]
            nodeCol = edges[1] + maxRow + 1
            dst.unionBySize(nodeRow,nodeCol)
            stoneNodes[nodeRow]=1
            stoneNodes[nodeCol]=1

        cnt = 0
        print(stoneNodes)
        for index,val in stoneNodes.items():
            if dst.findUPar(index) == index:
                cnt += 1

        return n - cnt


if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    n = len(stones)
    sol = Solution()
    ans = sol.removeStones(stones,n)
    print(ans)
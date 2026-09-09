# used to check if two elements belong to same set or not and also used to union two sets
# used where graph is changing dynamically and we want to check if two nodes are connected or not
# # find parent of a node and union two nodes 
# Union → easy ✅
# Find → easy ✅
# Delete edge / split component → not directly supported ❌
# Handle deletions by processing backwards → often possible ✅
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



if __name__ == "__main__":
    sol = DisjointSet(7)
    # sol.unionByRank(1,2)
    # sol.unionByRank(2,3)
    # sol.unionByRank(4,5)
    # sol.unionByRank(6,7)
    # sol.unionByRank(5,6)
    # not same parent
    # print(sol.findUPar(3))
    # print(sol.findUPar(7))
    # sol.unionByRank(3,7)
    # parent same
    # print(sol.findUPar(3))
    # print(sol.findUPar(7))

    # 2 ===>> union by size

    sol.unionBySize(1,2)
    sol.unionBySize(2,3)
    sol.unionBySize(4,5)
    sol.unionBySize(6,7)
    sol.unionBySize(5,6)
    # not same parent
    print(sol.findUPar(3))
    print(sol.findUPar(7))
    sol.unionBySize(3,7)
    # parent same
    print(sol.findUPar(3))
    print(sol.findUPar(7))
  
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        email_to_index = {}

        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email in email_to_index:
                    ds.unionBySize(email_to_index[email],i)
                else:
                    email_to_index[email] = i

        merged_accounts = {}
        for email, index in email_to_index.items():
            root = ds.findUPar(index)
            print(f"Email: {email}, Index: {index}, Root: {root}")
            if root not in merged_accounts:

                merged_accounts[root] = []
            merged_accounts[root].append(email)

        result = []
        print("Email to Index Mapping:", email_to_index)
        print("Merged Accounts:", merged_accounts)
        for emails in merged_accounts.values():
            name = accounts[email_to_index[emails[0]]][0]
            result.append([name] + sorted(emails))

        return result



if __name__ == "__main__":
    accounts = [["John","j1@mail.com","j2@mail.com"],["John","j1@mail.com","j0@mail.com"],["Mary","mary@mail.com"],["John","j3@mail.com"]]

    sol = Solution()
    print(sol.accountsMerge(accounts))

        
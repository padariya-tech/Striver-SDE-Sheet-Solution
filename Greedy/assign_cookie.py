from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        g = sorted(g)
        s = sorted(s)
        i,j = 0,0
        ans = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
                j += 1
                ans += 1
            else:
                j += 1
        
        return ans
    

if __name__ == "__main__":

    sol = Solution()
    g = [1,2,3]
    s = [1,1]
    ans = sol.findContentChildren(g,s)
    print(ans)
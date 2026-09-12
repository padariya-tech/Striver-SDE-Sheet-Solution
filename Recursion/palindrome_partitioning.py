class Solution:
    def isPalindrome(self,start,end,s):
        i =start
        j = end
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def partition(self,ind,temp,ans,s):
        if ind == len(s):
            ans.append(temp.copy())
            return 
        
        for i in range(ind,len(s)):
            if self.isPalindrome(ind,i,s):
                temp.append(s[ind:i+1])
                self.partition(i+1,temp,ans,s)
                temp.pop()


if __name__ == "__main__":

    s = "aabb"
    sol = Solution()
    ans = []
    sol.partition(0,[],ans,s)
    print(ans)
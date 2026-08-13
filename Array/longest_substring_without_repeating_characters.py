class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        n = len(s)
        mapp = {}
        answer = 0
        i , j = 0,0
        while j < n:
            answer = max(answer,len(mapp))
            if s[j] in mapp:
                while mapp.get(s[j]):
                    mapp[s[i]] = mapp.get(s[i],0) - 1
                    if mapp.get(s[i]) == 0:
                        mapp.pop(s[i])
                    i += 1

            mapp[s[j]] = mapp.get(s[j],0)+ 1
            j += 1
        answer = max(answer,len(mapp))
        return answer

if __name__ == "__main__":

    s="babababaabcabcbb"
    sol = Solution()
    answer = sol.lengthOfLongestSubstring(s)
    print(answer)
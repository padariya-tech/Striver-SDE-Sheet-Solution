class Solution:
    def zeroSumSubarray(self,nums):
        n = len(nums)
        mapp= {}
        summ = 0
        ans = 0
        for i in range(n):
            summ += nums[i]
            if summ == 0:
                ans = max(ans,i+1)
            if summ in mapp:
                ans = max(ans,i - mapp.get(summ))
            else:
                mapp[summ]=i
        return ans 



if __name__ == "__main__":

    nums = [1,0,3]
    sol = Solution()
    answer = sol.zeroSumSubarray(nums)
    print(answer)
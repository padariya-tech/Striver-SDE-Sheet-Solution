class Solution:
    def getPermutation(self, n, k):

        fact = 1
        nums = []
        for i in range(1,n):
            fact *= i
            nums.append(i)
        nums.append(n)
        ans = ""
        k = k-1
        while True:

            ans += str(nums[k // fact])
            nums.pop(k // fact)
            if len(nums) == 0:
                break

            k = k%fact
            fact = fact // len(nums)


        return ans
        
        
        


if __name__ == "__main__":

    n = 3
    k = 3
    sol = Solution()
    ans = sol.getPermutation(n,k)
    print(ans)
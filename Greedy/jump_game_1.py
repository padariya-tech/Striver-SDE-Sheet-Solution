class Solution:
    def canJump(self, nums):
        n = len(nums)

        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach,i + nums[i])

        return True


if __name__ == "__main__":

    sol = Solution()
    nums = [3,2,1,0,4]

    ans = sol.canJump(nums)
    print(ans)


# minimum jumps to reach last index . 
class Solution:
    def canJump(self, nums):
        n = len(nums)

        near = far = jumps = 0

        while far < n - 1: # r is less than n - 1 

            farthest = 0
            for i in range(near,far + 1):
                farthest = max(farthest,i+nums[i])

            near = far + 1
            far = farthest
            jumps += 1

        return jumps


if __name__ == "__main__":

    sol = Solution()
    nums = [2,3,1,1,1,1,4]

    ans = sol.canJump(nums)
    print(ans)


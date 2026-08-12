class Solution(object):
    def twoSum(self, nums, target):
        mapp = {}
        n = len(nums)
        nums = sorted(nums)
        i = 0
        j = n - 1
        for i in range(n):
            if nums[i] not in mapp:
                mapp[nums[i]] = i
        
        for i in range(n):
            remaining = target - nums[i]
            if remaining in mapp and mapp[remaining] != i:
                return [i,mapp[remaining]]
        return [-1,-1]


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    answer = solution.twoSum(nums,target)
    print(answer)
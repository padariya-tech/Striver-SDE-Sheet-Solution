from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        if n == 1:
            return nums[0]
        largest_sum = float('-inf')
        for i in range(n):
            summ += nums[i]
            largest_sum = max(largest_sum,summ) # to handle negative also
            if summ <= 0:
                summ = 0
            

        return largest_sum




if __name__ == "__main__":

    nums = [-1]
    solution = Solution()
    answer = solution.maxSubArray(nums)
    print(answer)
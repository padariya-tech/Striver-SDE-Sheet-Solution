from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n-2
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n-1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]

        nums[i+1:] = reversed(nums[i+1:])
        return nums
    

if __name__ == "__main__":
    nums=[3,5,4,3,2,1]
    solution = Solution()
    answer = solution.nextPermutation(nums)
    print(answer)

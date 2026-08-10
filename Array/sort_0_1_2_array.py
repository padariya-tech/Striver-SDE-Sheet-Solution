class Solution:
    def sortArray(self,nums):
        n = len(nums)
        lo=0
        mid = 0
        hi = n-1
        while mid <= hi:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[mid],nums[lo] = nums[lo],nums[mid]
                mid += 1
                lo += 1
            else:
                nums[mid],nums[hi] = nums[hi],nums[mid]
                hi -= 1
        return nums


if __name__ == "__main__":

    sol = Solution()
    nums=[0,0,1,2,1,2,0,0,1]
    answer = sol.sortArray(nums)
    print(answer)
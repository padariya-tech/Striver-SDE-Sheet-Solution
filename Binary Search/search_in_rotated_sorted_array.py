class Solution:
    def search(self,nums,target):
        n = len(nums)

        lo = 0
        hi = n-1

        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]: # left part sorted
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: # right part sorted
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
                

        return -1


if __name__ == "__main__":

    nums = [1,2,3,4,5,6]
    target = 5

    sol = Solution()
    element_index = sol.search(nums,target)
    print(element_index)
    # for i in range(len(nums)):
            
    #     element_index = sol.search(nums,nums[i])
    #     print(element_index)

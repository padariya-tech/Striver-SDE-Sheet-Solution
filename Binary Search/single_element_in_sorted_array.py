class Solution:

    # using XOR operator => tc = o(n)
    # def singleNonDuplicate(self,nums):
    #     n = len(nums)
    #     ans = 0
    #     for i in range(n):
    #         ans = ans ^ nums[i]

    #     return ans

    # using binary search => tc = o(log(n))
    def singleNonDuplicate(self,nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        lo = 1
        hi = n - 2

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if ((mid %2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 ==1 and nums[mid-1] == nums[mid])):
                lo = mid + 1

            else:
                hi = mid - 1

        return -1



if __name__ == "__main__":
    nums = [2,2,3,3,4,5,5]
    find_single_element = Solution()
    ans = find_single_element.singleNonDuplicate(nums)
    print(ans)
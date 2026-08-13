from typing import List
class Solution:
    def mergeAlgo(self,i,mid,end,nums):
        start = i
        ans = []
        result = 0
        j = mid
        while i < mid and j <= end:
            if nums[i] <= nums[j]:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                result += (mid - i)
                j += 1

        while i < mid:
            ans.append(nums[i])
            i += 1

        while j <= end:
            ans.append(nums[j])
            j += 1

        nums[start:end + 1] = ans

        return result
    def mergeSort(self,i,j,nums: List[int]) -> int:
        
        ans = 0
        if i < j:
            mid = (i + j) // 2
            ans += self.mergeSort(i,mid,nums)
            ans += self.mergeSort(mid+1,j,nums)
            ans += self.mergeAlgo(i,mid+1,j,nums)

        return ans

if __name__ == "__main__":

    nums=[5,4,3,2,1]
    sol = Solution()
    answer = sol.mergeSort(0,len(nums)-1,nums)
    print(answer)
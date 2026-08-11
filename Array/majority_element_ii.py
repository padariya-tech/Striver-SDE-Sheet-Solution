from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele1 = ele2 = None
        c1 = c2 = 0
        for num in nums:
            if ele1 == num:
                c1 += 1
            elif ele2 == num:
                c2 += 1
            elif c1 == 0:
                ele1 = num
                c1 += 1

                
            elif c2 == 0:
                ele2 = num
                c2 += 1

            else:
                c1 -= 1   
                c2 -= 1

        ans = []
        c1 = c2 = 0
        for i in range(len(nums)):
            if nums[i] == ele1:
                c1 += 1
            if nums[i] == ele2:
                c2 += 1

        if c1 > (len(nums) // 3):
            ans.append(ele1)
        if c2 > (len(nums) // 3):
            ans.append(ele2)

        return ans
    
if __name__ == "__main__":

    nums = [1,2,2,2,1,1,4,4,4,4,4,4,4]
    solution = Solution()
    answer = solution.majorityElement(nums)
    print(answer)
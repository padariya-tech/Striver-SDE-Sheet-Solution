from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        ele1 = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                ele1 = num
                cnt = 1
            elif num == ele1:
                cnt += 1
            else:
                cnt -= 1

        for i in range(n):
            if nums[i] == ele1:
                cnt += 1
        ans = -1
        if cnt > (n // 2):
            ans = ele1
        return ans            

        
if __name__ == "__main__":

    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    answer = solution.majorityElement(nums)
    print(answer)
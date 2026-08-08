from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        print("hello")
        print(slow,fast)
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            print(slow,fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


if __name__ == "__main__":

    nums = [1,3,2,4,2]
    duplicate = Solution()
    answer = duplicate.findDuplicate(nums)

    print(answer)
    
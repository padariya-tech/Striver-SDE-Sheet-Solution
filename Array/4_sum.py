from typing import List
class Solution:

    # 1) ==> using hashmap / set

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     n = len(nums)
    #     ans = set()
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             seen = set()
    #             for k in range(j+1,n):
    #                 remaining = target - nums[i] - nums[j] - nums[k]
    #                 if remaining in seen:
    #                     temp = tuple(sorted([nums[i],nums[j],nums[k],remaining]))
    #                     ans.add(temp)
    #                 seen.add(nums[k])


    #     return [list(quad) for quad in ans]
    

    # 2) ==> using sorted Array
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > 0 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans



if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1,1, 0, -1, 0,0,0,0,0,0, -2, 2,2,2,2,2,2,2,2]
    target = 3
    sol = Solution()
    answer = sol.fourSum(nums,target)
    print(answer)
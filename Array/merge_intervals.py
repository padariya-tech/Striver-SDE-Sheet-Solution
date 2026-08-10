class Solution:
    def merge(self, nums):
        nums.sort(key=lambda x: x[0])

        ans = [nums[0]]
        last_val = nums[0][1]

        j = 0  # index of last interval in ans

        for i in range(1, len(nums)):

            if nums[i][0] <= last_val:
                last_val = max(last_val, nums[i][1])
                ans[j][1] = last_val

            else:
                ans.append([nums[i][0], nums[i][1]])
                j += 1
                last_val = nums[i][1]

        return ans


if __name__ == "__main__":

    sol = Solution()
    nums=[[1,3],[8,10],[15,18],[2,6]]
    answer = sol.merge(nums)
    print(answer)
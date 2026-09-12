class Solution:
    def combination_sum(self, i, temp, curr_sum, arr, k, ans):

        # Target reached
        if curr_sum == k:
            ans.append(temp.copy())
            return

        # Out of bounds or sum exceeded
        if i == len(arr) or curr_sum > k:
            return

        # TAKE
        temp.append(arr[i])

        self.combination_sum(
            i + 1,                  # move to next index
            temp,
            curr_sum + arr[i],
            arr,
            k,
            ans
        )

        temp.pop()

        # NOT TAKE
        # Skip duplicate values at the same recursion level
        next_i = i + 1

        while next_i < len(arr) and arr[next_i] == arr[i]:
            next_i += 1

        self.combination_sum(
            next_i,
            temp,
            curr_sum,
            arr,
            k,
            ans
        )


if __name__ == "__main__":

    arr = [1, 1, 2]
    k = 3

    arr.sort()

    ans = []

    sol = Solution()

    sol.combination_sum(
        0,
        [],
        0,
        arr,
        k,
        ans
    )

    print(ans)



# class Solution:
#     def combinationSum2(self, candidates, target):
#         candidates.sort()
#         ans = []

#         def backtrack(start, curr_sum, temp):

#             if curr_sum == target:
#                 ans.append(temp.copy())
#                 return

#             if curr_sum > target:
#                 return

#             for i in range(start, len(candidates)):

#                 # Skip duplicate choices at the same level
#                 if i > start and candidates[i] == candidates[i - 1]:
#                     continue

#                 temp.append(candidates[i])

#                 # i + 1 because each element can be used only once
#                 backtrack(
#                     i + 1,
#                     curr_sum + candidates[i],
#                     temp
#                 )

#                 temp.pop()

#         backtrack(0, 0, [])

#         return ans
class Solution:
    def count_pairs(self, nums, x):
        n = len(nums)
        mapp = {0:1} # if we initilize with map = {} , then we will not able to capture the subarray with starting index 0 , bcz we do not have any 0 value as remaining

        cnt =  0
        xor_sum = 0

        for i in range(len(nums)):
            xor_sum = xor_sum ^ nums[i]
            remaining = xor_sum ^ x
            if remaining in mapp:
                cnt += mapp.get(remaining)
            mapp[xor_sum] = mapp.get(xor_sum,0) + 1

        return cnt

if __name__ == "__main__":

    sol = Solution()
    nums = [4,2,2,6,4]
    k = 6
    answer = sol.count_pairs(nums, k)
    print(answer)
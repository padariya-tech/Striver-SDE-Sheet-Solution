from typing import List
class Solution:
    def find_sequence_length(self,element,nums,mapp):
        cnt = 1
        while element + 1 in mapp:
            element = element + 1
            cnt += 1
        return cnt

    def longestConsecutive(self, nums: List[int]) -> int:

        ans = 0
        temp = 0

        mapp = set(nums)
        # mapp(nums)
        # print(mapp)
        n = len(nums)
        sequence_length = 0
        for num in mapp:
            if num - 1 not in mapp:
                sequence_length = self.find_sequence_length(num,nums,mapp)
            ans = max(ans,sequence_length)

        return ans
        

if __name__ == "__main__":

    sol = Solution()
    nums=[100,4,200,1,3,2]
    answer = sol.longestConsecutive(nums)
    print(answer)
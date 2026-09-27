
class Solution:

    def remove_k_digits(self, nums, k):

        if k >= len(nums):
            return "0"

        st = []

        for digit in nums:

            while st and k > 0 and st[-1] > digit:
                st.pop()
                k -= 1

            st.append(digit)

        # If removals are still remaining,
        # remove from the end
        if k > 0:
            st = st[:-k]

        # Remove leading zeros
        result = ''.join(st).lstrip('0')

        return result if result else "0"

if __name__ == "__main__":

    nums = "12341"
    k = 3
    sol = Solution()
    ans = sol.remove_k_digits(nums,k)
    print(ans)
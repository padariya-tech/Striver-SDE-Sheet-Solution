class Solution:

    def next_smaller_element(self,arr):
        st = []
        n = len(arr)
        ans = [-1] * n
        for i in range(n):
            while st and st[-1] >= arr[i]:
                st.pop()
            if st:
                ans[i] = st[-1]

            st.append(arr[i])
        
        return ans


if __name__ == "__main__":
    arr = [5,4,3,10,9]
    sol = Solution()
    ans = sol.next_smaller_element(arr)
    print(ans)
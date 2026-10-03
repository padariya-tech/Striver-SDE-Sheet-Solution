class Solution:

    def next_greater_element(self,arr):
        st = []
        n = len(arr)
        ans = [-1] * n
        for i in range(n-1,-1,-1):
            while st and st[-1] <= arr[i]:
                st.pop()
            if st:
                ans[i] = st[-1]

            st.append(arr[i])
        
        return ans


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    sol = Solution()
    ans = sol.next_greater_element(arr)
    print(ans)
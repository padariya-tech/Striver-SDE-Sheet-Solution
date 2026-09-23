class Solution:

    def next_greater_element(self,arr):
        st = []
        n = len(arr)
        ans = [-1] * n
        st.append(arr[n-1])
        for i in range(n-2,-1,-1):

            if arr[i] < st[-1]:
                ans[i] = st[-1]
                

            else:
                while st and st[-1] <= arr[i]:
                    st.pop()
                if st:
                    ans[i] = st[-1]

            st.append(arr[i])
        
        return ans


if __name__ == "__main__":
    arr = [3,2,1]
    sol = Solution()
    ans = sol.next_greater_element(arr)
    print(ans)
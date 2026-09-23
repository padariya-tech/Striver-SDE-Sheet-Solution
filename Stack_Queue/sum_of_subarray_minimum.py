class Solution:
    def previous_smaller_equal_element(self,arr):
        st = []
        n = len(arr)
        ans = [-1] * n
        st.append(0)
        for i in range(1,n):

            if arr[i] > arr[st[-1]]:
                ans[i] = arr[st[-1]]
                

            else:
                while st and arr[st[-1]] > arr[i]:
                    st.pop()
                if st:
                    ans[i] = arr[st[-1]]

            st.append(i)
        
        return ans
    
    def next_smaller_element(self,arr):
        st = []
        n = len(arr)
        ans = [n] * n
        st.append(n-1)
        for i in range(n-1,-1,-1):

            if arr[i] > arr[st[-1]]:
                ans[i] = arr[st[-1]]
                

            else:
                while st and arr[st[-1]] >= arr[i]:
                    st.pop()
                if st:
                    ans[i] = arr[st[-1]]

            st.append(i)
        
        return ans


if __name__ == "__main__":
    arr = [3,1,2,4]
    sol = Solution()
    nse = sol.next_smaller_element(arr)
    psee = sol.previous_smaller_equal_element(arr)
    total = 0
    for i in range(len(arr)):

        left = i - psee[i]
        right = nse[i] - i

        ans = left * right * arr[i]
        total += ans

    print(total)
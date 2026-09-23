class Solution:

    def next_greater_element_right(self,arr):
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
    arr = [2,10,12,1,11]
    new_arr = arr + arr
    sol = Solution()
    ans1 = sol.next_greater_element_right(new_arr)
    
    ans = [-1] * len(arr)
    for i in range(len(arr)):
            ans[i] = ans1[i]
    print(ans)
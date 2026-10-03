class Solution:
    def aestroid_collision(self,arr):
        n = len(arr)
        st = []
        i = 0
        for curr_val in arr:

            while st:
                if curr_val < 0 and st[-1] > 0:

                    if abs(st[-1]) < abs(curr_val):
                        st.pop()
                        

                    elif abs(st[-1]) > abs(curr_val):
                        curr_val = 0
                        break

                    else:
                        st.pop()
                        curr_val = 0
                        break

                else:
                    break

            if curr_val != 0:
                st.append(curr_val)

        return (st)

if __name__ == "__main__":

    # arr = [1,2,3,4,5,6,-6,-35]
    arr = [-3,1,-2]

    sol = Solution()
    ans = sol.aestroid_collision(arr)
    print(ans)
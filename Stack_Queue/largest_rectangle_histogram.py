class Solution:
    def largest_rectangle(self, arr):
        n = len(arr)
        # logic is arr[i] * (nse - pse - 1)
        # we are going from left to right 
        # pse will calculate on the fly and when popping
        # we will take that min as nse for popped element

        st = []
        max_area = float('-inf')
        for i in range(n):

            while st and arr[st[-1]] >= arr[i]:
                curr = st.pop()
                nse = i
                pse = st[-1] if st else -1
                curr_area = arr[curr] * (nse - pse - 1)
                max_area = max(max_area,curr_area)

            st.append(i)

        while st:
            curr = st.pop()
            nse = n
            pse = st[-1] if st else -1
            curr_area = arr[curr] * (nse - pse - 1)
            max_area = max(max_area, curr_area)


        return max_area

if __name__ == '__main__':
    heights = [1,2,3,4,5]
    s = Solution()
    answer = s.largest_rectangle(heights)
    print(answer)

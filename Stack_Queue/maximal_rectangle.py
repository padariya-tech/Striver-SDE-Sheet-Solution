class Solution:

    def largest_rectangle(self,arr):
        n = len(arr)
        st = []
        max_area = float('-inf')
        for i in range(n):

            while st and arr[st[-1]] >= arr[i]:
                curr = st.pop()
                nse = i
                pse = st[-1] if st else -1
                curr_area = arr[curr] * (nse - pse - 1)
                max_area = max(max_area , curr_area)

            st.append(i)

        while st:
            curr = st.pop()
            nse = n
            pse = st[-1] if st else -1
            curr_area = arr[curr] * (nse - pse - 1)
            max_area = max(max_area , curr_area)
            
        return max_area

    def maximalRectangle(self,mat):

        # change the matrix to prefix sum array for input in 
        # largest rectangle in histogram function
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])

        for i in range(1,n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i-1][j]
                else:
                    mat[i][j] = 0
        
        max_area = float('-inf')
        for i in range(n):
            curr_row_area = self.largest_rectangle(mat[i])
            max_area = max(max_area,curr_row_area)

        return max_area


if __name__ == "__main__":

    sol = Solution()
    mat = [
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0]
    ]
    answer = sol.maximalRectangle(mat)
    print(answer)
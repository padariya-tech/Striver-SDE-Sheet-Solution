class Solution:

    # Previous Smaller or Equal INDEX
    def previous_smaller_equal_element(self, arr):
        st = []
        n = len(arr)
        ans = [-1] * n

        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()

            if st:
                ans[i] = st[-1]

            st.append(i)

        return ans

    # Next Smaller INDEX
    def next_smaller_element(self, arr):
        st = []
        n = len(arr)
        ans = [n] * n

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                ans[i] = st[-1]

            st.append(i)

        return ans

    # Previous Greater INDEX
    def previous_greater_element(self, arr):
        st = []
        n = len(arr)
        ans = [-1] * n

        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()

            if st:
                ans[i] = st[-1]

            st.append(i)

        return ans

    # Next Greater or Equal INDEX
    def next_greater_equal_element(self, arr):
        st = []
        n = len(arr)
        ans = [n] * n

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                st.pop()

            if st:
                ans[i] = st[-1]

            st.append(i)

        return ans

    def sum_of_subarray_ranges(self, arr):

        n = len(arr)

        # For minimum contribution
        nse = self.next_smaller_element(arr)
        psee = self.previous_smaller_equal_element(arr)

        min_total = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i

            min_total += left * right * arr[i]

        # For maximum contribution
        pge = self.previous_greater_element(arr)
        ngee = self.next_greater_equal_element(arr)

        max_total = 0

        for i in range(n):
            left = i - pge[i]
            right = ngee[i] - i

            max_total += left * right * arr[i]

        print(" ")
        print("original ",arr) 
        print("nse ",nse) 
        print("psee ",psee) 
        print("pge ",pge) 
        print("ngee ",ngee) 
        print(max_total , min_total)
        return max_total - min_total


if __name__ == "__main__":

    arr = [1, 4, 3, 2]

    sol = Solution()

    answer = sol.sum_of_subarray_ranges(arr)

    print(answer)
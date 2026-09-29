class Solution:

    def find_celebrity(self, arr):
        n = len(arr)

        # Find candidate
        candidate = 0

        for i in range(1, n):

            # candidate knows i
            # => candidate cannot be celebrity
            print(candidate,i)
            if arr[candidate][i] == 1:
                candidate = i

        # Verify candidate
        for i in range(n):

            if i == candidate:
                continue

            # Celebrity knows nobody
            if arr[candidate][i] == 1:
                return -1

            # Everybody must know celebrity
            if arr[i][candidate] == 0:
                return -1

        return candidate

if __name__ == "__main__":

    arr = [[0,1,1,1],[0,0,0,1],[0,1,0,1],[0,0,0,0]]

    sol = Solution()
    # celebrity ===> known by all , not knowing anyone
    ans = sol.find_celebrity(arr)
    print(ans)
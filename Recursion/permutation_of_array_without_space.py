class Solution:
    def permutation(self, start, arr, ans):

        if start == len(arr):
            ans.append(arr.copy())
            return

        for i in range(start, len(arr)):

            # Put arr[i] at position start
            arr[start], arr[i] = arr[i], arr[start]

            self.permutation(start + 1, arr, ans)

            # Undo
            arr[start], arr[i] = arr[i], arr[start]


if __name__ == "__main__":

    ans = []
    arr = [1, 2, 3]

    sol = Solution()
    sol.permutation(0, arr, ans)

    print(ans)
class Solution:

    def trapping_water(self,arr):
        leftmax , rightmax , total = 0,0,0
        l = 0
        r = len(arr) - 1
        while l <= r:

            if leftmax <= rightmax:

                if arr[l] >= leftmax:
                    leftmax = arr[l]
                else:
                    total += leftmax - arr[l]

                l += 1

            else:

                if arr[r] >= rightmax:
                    rightmax = arr[r]
                else:
                    total += rightmax - arr[r]

                r -= 1

        return total



if __name__ == "__main__":
    # arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    arr= [4,2,0,3,2,5]
    sol = Solution()
    ans = sol.trapping_water(arr)
    print(ans)
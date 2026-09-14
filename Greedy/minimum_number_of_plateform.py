class Solution:
    def minPlatform(self, arr, dept):
        n = len(arr)
        arr = sorted(arr)
        dept = sorted(dept)

        i,j = 0,0
        cnt = 0
        max_count = -1
        while i < n and j < n :

            if arr[i] <= dept[j]:

                cnt += 1
                i += 1

            else:
                cnt -= 1
                j += 1

            max_count = max(max_count,cnt)

        return max_count
        

if __name__ == "__main__":

    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    sol = Solution()
    ans = sol.minPlatform(arr,dep)

    print(ans)




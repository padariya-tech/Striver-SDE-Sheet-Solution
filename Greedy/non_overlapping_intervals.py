class Solution:
    def minRemoval(self, intervals):
        # code here
        n = len(intervals)
        # Sort by finish time
        intervals.sort(key = lambda x: [1])

        cnt = 1
        end = intervals[0][1]
        ans = []
        ans.append([intervals[0][0],end])
        for i in range(1, n):

            start = intervals[i][0]
            finish = intervals[i][1]
            
            if start >= end:
                ans.append([start,finish])
                cnt += 1
                end = finish

        print(ans)
        return n - len(ans)


if __name__ == "__main__":

    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    sol = Solution()
    ans = sol.minRemoval(intervals)
    print(ans)
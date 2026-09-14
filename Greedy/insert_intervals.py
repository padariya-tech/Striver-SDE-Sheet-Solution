class Solution:
    def insertInterval(self, intervals, newInterval):

        intervals.append(newInterval)

        # Sort based on start time
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0].copy()]

        for i in range(1, len(intervals)):

            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            # Overlapping
            if curr_start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], curr_end)

            # Non-overlapping
            else:
                ans.append(intervals[i].copy())

        return ans


if __name__ == "__main__":

    intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
    newInterval = [5, 6]

    sol = Solution()
    ans = sol.insertInterval(intervals, newInterval)

    print(ans)
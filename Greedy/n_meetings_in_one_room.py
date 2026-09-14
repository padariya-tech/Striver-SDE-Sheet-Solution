class Solution:
    def maxMeetings(self, s, f):
        n = len(s)

        if n == 0:
            return 0

        # (finish_time, start_time)
        meetings = list(zip(f, s))

        # Sort by finish time
        meetings.sort()

        cnt = 1
        end = meetings[0][0]
        ans = []
        ans.append([meetings[0][1],end])
        for i in range(1, n):

            start = meetings[i][1]
            finish = meetings[i][0]
            
            if start > end:
                ans.append([start,finish])
                cnt += 1
                end = finish

        print(ans)
        return cnt


if __name__ == "__main__":

    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]

    sol = Solution()
    ans = sol.maxMeetings(s, f)

    print(ans)
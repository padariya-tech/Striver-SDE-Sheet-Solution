class Solution:
    def solve(self, bt):
        # code here
        ans = 0
        bt = sorted(bt)
        ct = 0
        wt = 0
        n = len(bt)
        for i in range(len(bt)):
            ct += bt[i]
            wt += (ct - bt[i])

        # print(wt)
        return wt // n

if __name__ == "__main__":

    bt = [4,3,7,1,2]
    sol = Solution()
    ans = sol.solve(bt)
    print(ans)
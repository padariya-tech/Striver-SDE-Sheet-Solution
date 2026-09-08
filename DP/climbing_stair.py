class Solution:
    def helper(self,n,dp):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n <= 0:
            return 0

        return self.helper(n-1) + self.helper(n-2)
    
    def climbStairs(self, n: int) -> int:
        dp = {}

        ans = self.helper(n,dp)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 5
    answer = sol.climbStairs(n)

    print(answer)
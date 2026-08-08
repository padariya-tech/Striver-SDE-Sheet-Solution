from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_val = prices[0]
        max_profit = 0
        for i in range(n):
            min_val = min(min_val,prices[i])
            max_profit = max(max_profit,prices[i] - min_val)

        return max_profit


if __name__ == "__main__":

    prices = [7,6,4,3,1]
    solution = Solution()
    answer = solution.maxProfit(prices)
    print(answer)
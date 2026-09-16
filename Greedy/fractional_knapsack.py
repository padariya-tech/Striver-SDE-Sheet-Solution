class Solution:
    def fractionalKnapsack(self, val, wt, capacity):

        n = len(val)
        items = list(zip(val,wt))

        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        total_profit = 0
        for v,w in items:
            if w <= capacity:
                capacity -= w
                total_profit += v
            else:
                fraction = capacity/w
                total_profit += v*fraction
                break

        return round(total_profit,6)


if __name__ == "__main__":
    val = [500]
    wt = [30]
    capacity = 10
    sol = Solution()
    ans = sol.fractionalKnapsack(val,wt,capacity)
    print(ans)
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
class Solution:
    def candy(self, arr):
        n = len(arr)
        sum = 1
        i = 1
        while i < n:

            if arr[i] == arr[i-1]:
                sum += 1
                i+=1
                continue

            peak = 1
            while i < n and arr[i] > arr[i-1]:
                peak += 1
                sum += peak
                i+= 1
            
            down = 1
            while i < n and arr[i] < arr[i-1]:
                sum += down
                i += 1
                down += 1

            if down > peak:
                sum += (down-peak)

        return sum

if __name__ == "__main__":

    arr = [2,1,1,1]
    sol = Solution()
    ans = sol.candy(arr)
    print(ans)


from collections import deque
class Solution:
    def sliding_window_max(self,arr,k):
        # keep track of k elements
        # we are having monotonic decreasing queue
        # using decreasing to get max of window in constant time

        dq = deque()
        ans = []

        for i in range(len(arr)):
            
            # remove element outside the current window
            while dq and dq[0] <= i-k:
                dq.popleft()

            # remmove smaller elements from the back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # add current index
            dq.append(i)

            if i >= k-1:
                ans.append(arr[dq[0]])

        return ans


if __name__ == "__main__":

    sol = Solution()
    arr = [1,3,-1,-3,5,3,2,1,6]
    k = 9
    ans = sol.sliding_window_max(arr,k)
    print(ans)
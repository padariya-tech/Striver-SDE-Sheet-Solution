from collections import deque

class Solution:
    def minimum_multiplication(self, start, end, arr):
        n = len(arr)
        MOD = 100000

        if start == end:
            return 0

        q = deque()
        dist = [-1] * MOD

        q.append(start)
        dist[start] = 0

        while q:
            top = q.popleft()

            for i in range(n):
                nxt = (top * arr[i]) % MOD

                if dist[nxt] == -1:
                    dist[nxt] = dist[top] + 1

                    if nxt == end:
                        return dist[nxt]

                    q.append(nxt)

        return -1


if __name__ == "__main__":
    start = 7
    end = 66175
    arr = [3, 4, 65]

    sol = Solution()
    ans = sol.minimum_multiplication(start, end, arr)

    print(ans)
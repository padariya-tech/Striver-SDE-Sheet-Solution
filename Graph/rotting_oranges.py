from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        rows = [-1,0,1,0]
        cols = [0,1,0,-1]

        freshcount = 0
        vis = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                    vis[i][j]=1
                elif grid[i][j] == 0:
                    vis[i][j] = 0
                else:
                    freshcount += 1
        
        tm = 0
        while q:
            r,c,t = q.popleft()
            tm = max(tm,t)
            for i in range(4):
                new_r = r + rows[i]
                new_c = c + cols[i]
                if 0 <= new_c < m and 0 <=new_r < n and grid[new_r][new_c] == 1 and vis[new_r][new_c] == 0:
                    vis[new_r][new_c] = 1
                    freshcount -= 1
                    grid[new_r][new_c] = 2
                    q.append([new_r,new_c,t+1])

        if freshcount > 0:
            return -1
        return tm

        
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    sol = Solution()
    answer = sol.orangesRotting(grid)
    print(answer)
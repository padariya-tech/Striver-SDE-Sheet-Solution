from typing import List
from collections import deque
class Solution:
    def bfs(self,i,j,grid,vis):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        q.append([i,j])
        rows = [-1,0,1,0]
        cols = [0,1,0,-1]
        vis[i][j] = 1
        while q:
            elements = q.popleft()
            x = elements[0]
            y = elements[1]
            for k in range(4):
                new_row = x + rows[k]
                new_col = y + cols[k]
                if new_row >=0 and new_row <n and new_col >=0 and new_col < m and grid[new_row][new_col] == '1' and vis[new_row][new_col] == 0:
                    vis[new_row][new_col] = 1
                    q.append([new_row,new_col])

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis= [[0]*m for _ in range(n)]

        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    # print(i,j)
                    ans += 1
                    self.bfs(i,j,grid,vis)
        return ans

if __name__ == "__main__":
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    sol = Solution()
    answer = sol.numIslands(grid)
    print(answer)
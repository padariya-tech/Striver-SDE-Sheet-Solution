from collections import deque
class Solution:
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()
        vis = [[0]*m for _ in range(n)]
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    vis[i][j] = 1
                    ans[i][j] = 0
                    q.append([i,j])
        
        rows = [-1,0,1,0]
        cols = [0,1,0,-1]

        while q:
            elements = q.popleft()
            row = elements[0]
            col = elements[1]

            for i in range(4):
                new_r = row + rows[i]
                new_c = col + cols[i]

                if 0 <= new_c < m and 0 <= new_r < n and vis[new_r][new_c] == 0 and grid[new_r][new_c] == 0:
                    vis[new_r][new_c] = 1
                    ans[new_r][new_c] = ans[row][col] + 1
                    q.append([new_r,new_c])

        return ans




if __name__ == "__main__":

    sol = Solution()

    grid = [[1, 0, 1], 
                [1, 1, 0], 
                [1, 0, 0]]
    
    answer = sol.nearest(grid)

    print(answer)
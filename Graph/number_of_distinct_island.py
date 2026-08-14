from collections import deque
class Solution:
    def bfs(self,i,j,vis,grid):

        q = deque()
        q.append([i,j])
        shape = []
        n = len(grid)
        m = len(grid[0])
        vis[i][j] = 1
        shape.append((0,0))  # we are storing the relative position not the actual position (a-i,b-j) for start (a-a = 0,b-b = 0)
        rows = [-1,0,1,0]
        cols = [0,1,0,-1]

        while q:

            row,col = q.popleft()

            for k in range(4):
                new_row = row + rows[k]
                new_col = col + cols[k]

                if new_row >=0 and new_row <n and new_col >=0 and new_col < m and grid[new_row][new_col] == 1 and vis[new_row][new_col] == 0:
                    vis[new_row][new_col] = 1
                    shape.append((new_row - i, new_col - j))
                    q.append([new_row,new_col])

        return tuple(shape) # list is not allowed in set so convert it in tuple and then add in set 
    def countDistinctIslands(self,grid):
        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]
        ans_set = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    shape = self.bfs(i,j,vis,grid)
                    ans_set.add(shape)
        print(ans_set)
        return len(ans_set)

if __name__ == "__main__":

    grid = [
    [1, 1, 0,1,1],
    [1, 0, 0,0, 0],
    [0, 0, 0,1, 1],
    [1,1, 0,1, 0]
    ]

    sol = Solution()
    answer = sol.countDistinctIslands(grid)
    print(answer)
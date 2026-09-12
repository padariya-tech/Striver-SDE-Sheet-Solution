class Solution:

    def ratInMaze(self, i, j, temp, maze, vis, ans):

        n = len(maze)
        m = len(maze[0])

        # Destination
        if i == n - 1 and j == m - 1:
            ans.append(temp)
            return

        vis[i][j] = 1

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        direction = ['u','r','d','l']

        for k in range(4):

            new_r = i + dr[k]
            new_c = j + dc[k]

            if 0 <= new_r < n and 0 <= new_c < m:

                if maze[new_r][new_c] == 1 and vis[new_r][new_c] == 0:

                    # TAKE
                    temp += direction[k]

                    self.ratInMaze(
                        new_r,
                        new_c,
                        temp,
                        maze,
                        vis,
                        ans
                    )

                    # UNDO
                    temp=temp[:-1]

        # UNDO VISITED
        vis[i][j] = 0


if __name__ == "__main__":

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    sol = Solution()

    n = len(maze)
    m = len(maze[0])

    vis = [[0 for _ in range(m)] for _ in range(n)]

    ans = []

    sol.ratInMaze(
        0,
        0,
        "",
        maze,
        vis,
        ans
    )
    ans = sorted(ans)
    print(ans)
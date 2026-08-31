import heapq
class Solution:
    def binary_maze(self,grid):

        n = len(grid)
        m = len(grid[0])

        dist = [[float('inf')]* m for _ in range(n)]

        q = []
        heapq.heappush(q,(0,0,0))
        dist[0][0]=0

        row_array = [-1,0,1,0]
        col_array = [0,1,0,-1]
        while q:

            elements = heapq.heappop(q)
            distance = elements[0]
            i = elements[1]
            j = elements[2]

            for k in range(4):
                new_row = row_array[k] + i
                new_col = col_array[k] + j

                if  0<=new_row < n and 0<=new_col<m and grid[new_row][new_col] == 1:
                    if dist[new_row][new_col] > distance + 1:
                        dist[new_row][new_col] = distance + 1
                        heapq.heappush(q,(dist[new_row][new_col],new_row,new_col))
        
        return dist


if __name__ == "__main__":

    grid = [[1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,0,0],
            [1,0,0,0]]
    
    sol = Solution()
    ans = sol.binary_maze(grid)
    print(ans)
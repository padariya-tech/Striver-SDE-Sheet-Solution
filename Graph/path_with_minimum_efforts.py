import heapq
class Solution:
    def minimum_efforts(self,grid):
        n = len(grid)
        m = len(grid[0])
        
        dist = [[float('inf')]*m for _ in range(n) ]

        q = []
        heapq.heappush(q,(0,0,0))
        dist[0][0] = 0
        row_array = [-1,0,1,0]
        col_array = [0,1,0,-1]
        while q:

            diff , i , j = heapq.heappop(q)
            # print(diff,i,j)

            for k in range(4):

                new_row = row_array[k] + i
                new_col = col_array[k] + j
                # print(new_row,new_col)
                if 0<=new_row<n and 0<=new_col<m:
                    difference = abs(grid[new_row][new_col] - grid[i][j])
                    # print(difference)
                    if dist[new_row][new_col] > max(diff,difference):
                        dist[new_row][new_col] = max(diff,difference)
                        # print("hello")
                        heapq.heappush(q,(dist[new_row][new_col],new_row,new_col))

        return dist


if __name__ == "__main__":

    grid = [
            [1,2,2],
            [3,8,2],
            [5,3,5]
        ]
    sol = Solution()

    answer = sol.minimum_efforts(grid)
    print(answer)
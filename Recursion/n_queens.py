
class Solution:
    def isSafe(self,row,col,n,board):
        
        # check for same row
        for i in range(col,-1,-1):
            # print(row,i)
            if board[row][i] == 1:
                return False

        r,c = row,col
        while r >=0 and c>=0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1

        r,c = row,col
        while r < n and c>=0:
            if board[r][c] == 1:
                return False
            r += 1
            c -= 1
        
        return True
    def solveNQueens(self,col,n,board,ans):

        if col == n:
            ans.append([row.copy() for row in board])
            return
        
        for row in range(n):
            if self.isSafe(row,col,n,board):

                board[row][col] = 1
                self.solveNQueens(col+1,n,board,ans)

                board[row][col] = 0
        return

if __name__ == "__main__":

    n = 10
    sol = Solution()
    ans = []
    board = [[0]*n for i in range(n)]
    sol.solveNQueens(0,n,board,ans)

    print(ans)

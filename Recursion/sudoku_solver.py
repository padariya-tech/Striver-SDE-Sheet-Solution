class Solution:
    def isValid(self,k,row,col,board):

        for i in range(9):
            if board[row][i] == k:
                return False
            
            if board[i][col] == k:
                return False
            
            if board[3 * (row//3) + (i//3)][3 * (col//3)+(i%3)] == k:
                return False
            
        return True
    def solveSudoku(self, board):

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == ".":
                    for k in "123456789":
                        if self.isValid(k,i,j,board):
                            board[i][j] = k
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
                
        return True


if __name__ == "__main__":

    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    n = len(board)
    sol.solveSudoku(board)

    print(board)



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




# class Solution {
#     public List<List<String>> solveNQueens(int n) {
#         char[][] board = new char[n][n]; // basically used for storing result
#         for(char[] row : board){
#             Arrays.fill(row,'.');
#         }  
#         List<List<String>> res = new ArrayList<>();
#         int[] leftRow = new int[n];
#         int[] upperDiagonal = new int[2*n-1];
#         int[] lowerDiagonal = new int[2*n-1];

#         solve(0,board,res,leftRow,upperDiagonal,lowerDiagonal);

#         return res;
#     }
#     static List < String > construct(char[][] board) {
#         List < String > res = new LinkedList < String > ();
#         for (int i = 0; i < board.length; i++) {
#             String s = new String(board[i]);
#             res.add(s);
#         }
#         return res;
#     }
#     public void solve(int col,char[][] board,List < List < String >> res, int leftRow[], int upperDiagonal[], int lowerDiagonal[]) {
#        if(col==board.length)
#        {
#        res.add(construct(board));
#            return;
#        }
#        for(int row = 0;row < board.length;row++){
#             if(leftRow[row]==0 && lowerDiagonal[row+col]==0 && upperDiagonal[board.length - 1 + col - row]==0){
#                 board[row][col]='Q';
#                 leftRow[row]=1; // 0(1) lookup 
#                 lowerDiagonal[row+col]=1;
#                 upperDiagonal[board.length-1+col-row]=1;
#                 solve(col+1,board,res,leftRow,upperDiagonal,lowerDiagonal);
#                 board[row][col]='.';
#                 leftRow[row]=0;
#                 lowerDiagonal[row+col]=0;
#                 upperDiagonal[board.length-1+col-row]=0;
#             }
#        }

#     }
# }
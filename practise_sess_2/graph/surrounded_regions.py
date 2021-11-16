import numpy as np
class Solution:
    def solve(self, board):
        board = np.array(board)
        R,C = board.shape
        def dfs(row, col):
            if (row<0 or col<0 or row>=R or col>=C or board[row][col] == 'X' or board[row][col] == 'A'):
                return
            board[row][col] = 'A'
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row+1,col)
            dfs(row,col+1)

        for i in range(R):
            for j in range(C):
                if (i == 0 or i ==R-1 or j == 0 or j==C-1) and board[i][j] == 'O':
                    dfs(i,j)
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
        print(board)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
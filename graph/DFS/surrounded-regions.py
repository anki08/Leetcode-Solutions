import numpy as np


def solve(board) -> None:
    board = np.array(board)
    R, C = board.shape

    def dfs(board, row, col):
        if board[row][col] != 'O':
            return
        board[row][col] = 'A'
        if row + 1 < R: dfs(board, row + 1, col)
        if col + 1 < C: dfs(board, row, col + 1)
        if row - 1 > 0: dfs(board, row - 1, col)
        if col - 1 > 0: dfs(board, row, col - 1)


    for i in range(R):
        dfs(board, i, 0)
        dfs(board, i, C-1)
    for i in range(C):
        dfs(board, 0, i)
        dfs(board, R-1, i)

    print(board)

    for i in range(R):
        for j in range(C):
            if board[i][j] != 'A': board[i][j] = 'X'
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'A': board[i][j] = 'O'
    print(board)





if __name__ == '__main__':
    solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])

import numpy as np
def numEnclaves(grid) -> int:
    grid = np.array(grid)
    R,C = grid.shape
    def dfs(board, row, col):
        if board[row][col] != 1:
            return
        board[row][col] = 9
        if row + 1 < R: dfs(board, row + 1, col)
        if col + 1 < C: dfs(board, row, col + 1)
        if row - 1 > 0: dfs(board, row - 1, col)
        if col - 1 > 0: dfs(board, row, col - 1)


    for i in range(R):
        dfs(grid, i, 0)
        dfs(grid, i, C - 1)
    for i in range(C):
        dfs(grid, 0, i)
        dfs(grid, R - 1, i)

    print(grid)
    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1: count+=1
    print(count)



if __name__ == '__main__':
    numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
    numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])

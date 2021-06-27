import numpy as np


def numIslands(grid) -> int:
    if (grid == None or len(grid) == 0):
        return 0

    grid = np.array(grid)
    nr = grid.shape[0]
    nc = grid.shape[1]
    num_islands = 0
    for i in range(nr):
        for j in range(nc):
            if (grid[i][j] == '1'):
                dfs(grid, i, j)
                num_islands += 1

    return num_islands


def dfs(grid, r, c):
    if (r < 0 or c < 0 or r >= grid.shape[0] or c >= grid.shape[1] or grid[r][c] == '0'):
        return

    grid[r][c] = '0'
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))

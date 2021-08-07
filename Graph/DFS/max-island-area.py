import numpy as np
global max_area
max_area = 0
def maxAreaOfIsland(grid) -> int:
    global max_area
    grid = np.array(grid)
    R,C = grid.shape

    def dfs(grid, row, col):
        global max_area
        if (row < 0 or col < 0 or row > R - 1 or col > C - 1 or grid[row][col] == 0):
            return 0
        # print(area)
        # max_area = max(area, max_area)
        grid[row][col] = "0"
        return (1+ dfs(grid, row + 1, col)+
        dfs(grid, row, col + 1)+
        dfs(grid, row - 1, col)+
        dfs(grid, row, col - 1))

    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                count = max(dfs(grid, i, j), count)


    return count



if __name__ == '__main__':
    maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
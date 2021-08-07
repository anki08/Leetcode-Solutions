import numpy as np
def closedIsland(grid) -> int:
    grid = np.array(grid)
    # R,C = len(grid), len(grid[0])
    R,C = grid.shape
    print(grid)

    def dfs(grid, row, col):
        if(row<0 or row> R-1 or col<0 or col>C-1 or grid[row][col]==1):
            return
        grid[row][col]=1
        dfs(grid, row + 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row - 1, col)
        dfs(grid, row, col - 1)

    for i in range(R):
        for j in range(C):
            if(i==0 or j==0 or i==R-1 or j==C-1):
                dfs(grid, i, j)
    print(grid)

    ans = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                dfs(grid, i, j)
                ans += 1
    return ans



if __name__ == '__main__':
    print(closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
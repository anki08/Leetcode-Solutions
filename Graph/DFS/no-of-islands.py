import numpy as np
def numIslands(grid) -> int:
    grid = np.array(grid)
    R,C  = grid.shape
    ans = 0
    print(grid)
    def dfs(grid, row, col):
        if(row<0 or col<0 or row>R-1 or col>C-1 or grid[row][col]=="0"):
            return
        grid[row][col] = "0"
        dfs(grid, row + 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row - 1, col)
        dfs(grid, row, col - 1)


    for i in range(R):
        for j in range(C):
            if(grid[i][j] == "1"):
                dfs(grid, i , j)
                ans +=1
                # print(grid)
    return ans


if __name__ == '__main__':
    print(numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
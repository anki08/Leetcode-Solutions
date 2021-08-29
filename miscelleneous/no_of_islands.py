import numpy as np
class Solution:
    def __init__(self):
        self.count = 0
    def numIslands(self, grid):
        count = 0
        grid = np.array(grid)
        R,C = grid.shape
        visited = np.full((R,C), False)
        def dfs(row, col):
            if row<0 or row>=R or col<0 or col>=C or visited[row][col] == True or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            visited[row][col] = True
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        # print(gri)
        print(count)


if __name__ == '__main__':
    sol = Solution()
    sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
    sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

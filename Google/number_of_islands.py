class Solution:
    def numIslands(self, grid):
        count = 0
        R, C = len(grid), len(grid[0])
        def util( row, col):
            if row < 0 or row>R-1 or col<0 or col>C-1 or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            util(row-1, col)
            util(row, col-1)
            util(row+1, col)
            util(row, col+1)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    count += 1
                    util(i, j)
        return count



if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands( grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

    print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
class Solution(object):

    def dfs(self, row, col, grid, visited):
        cell_pos = str(row) + str(col)
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or cell_pos in visited:
            return 0
        if grid[row][col] == '0':
            return 0
        else:

            visited.append(cell_pos)
            self.dfs(row, col + 1, grid, visited)
            self.dfs(row + 1, col, grid, visited)
            self.dfs(row - 1, col, grid, visited)
            self.dfs(row, col - 1, grid, visited)

            return 1

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        visited  = []
        for row in range(self.rows):
            for col in range(self.cols):
                ans += self.dfs(row, col, grid, visited)

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    print(sol.numIslands(grid= [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

import numpy as np
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R,C = np.array(image).shape
        oldColor = image[sr][sc]
        visited = np.full((R+1, C+1), False)
        def dfs(row, col, newColor):
            if row<0 or row>=R or col<0 or col>=C or visited[row][col] == True or image[row][col] != oldColor:
                return
            image[row][col] = newColor
            visited[row][col] = True
            dfs(row-1, col, newColor)
            dfs(row+1, col, newColor)
            dfs(row, col-1, newColor)
            dfs(row, col+1, newColor)


        dfs(sr, sc, newColor)
        return image


if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))

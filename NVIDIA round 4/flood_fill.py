import numpy as np
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R,C = len(image), len(image[0])
        visited = np.full((R,C), 0)
        def dfs(row, col, visited, oldclr):
            if row<0 or row>=R or col <0 or col>=C or visited[row][col] == True or image[row][col]!=oldclr:
                return
            visited[row][col] = True
            image[row][col] = newColor
            dfs(row-1, col, visited, oldclr)
            dfs(row, col-1,visited, oldclr)
            dfs(row+1, col,visited, oldclr)
            dfs(row, col+1,visited, oldclr)
        dfs(sr, sc, visited, image[sr][sc])
        print(image)



if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
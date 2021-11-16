import numpy as np
class Solution:
    def countSquares(self, matrix):
        matrix  = np.array(matrix)
        row, col = matrix.shape
        dp = matrix[0][0]
        for i in range(1, row):
            dp += matrix[i][0]
        for i in range(1, col):
            dp += matrix[0][i]

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] ==0:
                    continue
                matrix[i][j]= min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                dp += matrix[i][j]
        print(dp)
        return dp

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSquares(matrix =[[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
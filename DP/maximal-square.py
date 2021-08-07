import numpy as np
def maximalSquare(matrix) -> int:
    R,C = np.array(matrix).shape
    dp = np.zeros((R+1, C+1), dtype=int)
    max_val = 0
    for i in range(1, R+1):
        for j in range(1, C+1):
            if(matrix[i-1][j-1] == '1'):
                dp[i][j] = min(min(dp[i-1][j], dp[i-1][j]), dp[i-1][j-1]) +1
                max_val = max(max_val, dp[i][j])
    return max_val**2

if __name__ == '__main__':
    print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
import numpy as np
def uniquePaths(m: int, n: int) -> int:
    dp = np.zeros((m, n), dtype=int)
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    print(dp[-1][-1])



if __name__ == '__main__':
    uniquePaths(3, 7)
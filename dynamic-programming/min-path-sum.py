import numpy as np
def minPathSum(grid) -> int:
    grid = np.array(grid)
    R,C = grid.shape
    dp = np.full((R,C),np.inf, dtype=int)
    dp[0][0] = grid[0][0]
    for i in range( R):
        for j in range( C):
            if(i==0 and j==0):
                continue
            t1 = dp[i-1][j]+grid[i][j] if(i>0) else np.inf

            t2 = dp[i][j-1]+grid[i][j] if (j>0) else np.inf
            dp[i][j] = min(t1, t2)
    print(dp)


if __name__ == '__main__':
    minPathSum([[1,3,1],[1,5,1],[4,2,1]])
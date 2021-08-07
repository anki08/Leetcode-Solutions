import numpy as np
def minScoreTriangulation(values) -> int:

    def minScoreTriangulationUtil(arr, i, j):
        if (j-i+1<3):
            return 0
        min_val = np.inf
        for k in range(i+1, j):
            print(i,k,j)
            mul1 = minScoreTriangulationUtil(arr, i, k) + minScoreTriangulationUtil(arr, k, j) + arr[i] * arr[k] * arr[j]
            min_val = min(mul1, min_val)
        return min_val

    return minScoreTriangulationUtil(values, 0, len(values)-1)

def minScoreTriangulationDP(values):
    n = len(values)
    dp = np.zeros((n, n), dtype=int)
    for d in range(2, n):
        for i in range(n-d):
            j = i+d
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
    return dp[0][n-1]

if __name__ == '__main__':
    print(minScoreTriangulationDP([1, 2, 3]))
    # print(minScoreTriangulation([3,7,4,5]))
    # print(minScoreTriangulation([1,3,1,4,1,5]))

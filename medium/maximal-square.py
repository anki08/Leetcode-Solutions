import numpy as np


def maximalSquare(matrix) -> int:
    matrix = np.array(matrix)
    R, C = matrix.shape
    dp = np.zeros(C + 1, dtype=int)
    max_val, prev = 0, 0
    for r in range(0, R):
        for c in range(0, C):
            temp = dp[c]
            if matrix[r - 1][c - 1] == '1':
                print("here")
                dp[c] = min(min(dp[c - 1], prev), dp[c]) + 1
                print(dp[c])
                max_val = max(dp[c], max_val)
            else:
                dp[c] = 0
            prev = temp
    return max_val ** 2


if __name__ == '__main__':
    matrix = [["0", "1"], ["1", "0"]]
    matrix = [["0"]]
    print(maximalSquare(matrix))

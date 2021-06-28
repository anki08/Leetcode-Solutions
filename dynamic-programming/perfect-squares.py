import numpy as np
import math
def numSquares(n: int) -> int:
    lim = int(math.sqrt(n))
    nums = [i ** 2 for i in range(1, lim + 1)]
    nums_length = len(nums)
    dp = np.full((nums_length + 1, n + 1), 1000000, dtype=int)
    for i in range(nums_length + 1):
        dp[i][0] = 0
    # for i in range(n+1):
    #     dp[0][i] = 0
    # dp[0][0] = 0
    for i in range(1, nums_length + 1):
        curr = nums[i - 1]
        for j in range(1, n + 1):
            if (curr > j):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - curr], dp[i - 1][j])
    if (dp[-1][-1] == 1000000):
        return 1
    return (dp[-1][-1])


if __name__ == '__main__':
    print(numSquares(12))
    print(numSquares(13))
    print(numSquares(1))
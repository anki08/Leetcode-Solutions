import numpy as np


def makesquare(matchsticks) -> bool:
    perimeter = sum(matchsticks)
    if (perimeter % 4 != 0):
        return False
    k = 4
    length = perimeter // 4
    n = len(matchsticks)
    dp = np.full((1 << n), -1)
    dp[0] = 0
    for mask in range(1 << n):
        if (dp[mask] == -1):
            continue
        for j in range(n):
            if ((mask & (1 << j) == False) and dp[mask] + matchsticks[j] <= length):
                dp[mask | (1 << j)] = (dp[mask] + matchsticks[j]) % length

    return dp[(1 << n) - 1] == 0


if __name__ == '__main__':
    print(makesquare([1, 1, 2, 2, 2]))

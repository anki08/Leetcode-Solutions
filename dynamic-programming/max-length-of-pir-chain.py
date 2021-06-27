import numpy as np


def findLongestChain(pairs) -> int:
    pairs = sorted(pairs)
    dp = np.ones(len(pairs), dtype=int)
    for i in range(len(pairs)):
        for j in range(i):
            if (pairs[i][0] > pairs[j][1] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
    print(dp)
    return max(dp)


if __name__ == '__main__':
    print(findLongestChain([[1, 2], [2, 3], [3, 4]]))
    print(findLongestChain([[1, 2], [7, 8], [4, 5]]))

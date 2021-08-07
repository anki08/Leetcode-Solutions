import numpy as np


def numDistinct(s, t) -> int:
    len1 = len(s)
    len2 = len(t)
    dp = np.zeros((len1 + 1, len2 + 1), dtype=int)
    for i in range(len1):
        for j in range(len2):
            if (s[i - 1] == t[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j - 1], dp[i - 1][j - 1]


if __name__ == '__main__':
    numDistinct(s="rabbbit", t="rabbit")

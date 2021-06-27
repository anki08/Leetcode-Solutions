import numpy as np


def minimumDeleteSum(s1, s2) -> int:
    len1 = len(s1)
    len2 = len(s2)
    dp = np.zeros((len1 + 1, len2 + 1), dtype=int)
    for i in range(1, len1 + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, len2 + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if (s1[i - 1] != s2[j - 1]):
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
            else:
                dp[i][j] = dp[i - 1][j - 1]
    print(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    minimumDeleteSum(s1="sea", s2="eat")

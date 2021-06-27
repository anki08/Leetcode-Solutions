import numpy as np


def longestCommonSubsequence(text1: str, text2: str) -> int:
    len1 = len(text1)
    len2 = len(text2)
    dp = np.zeros((len1 + 1, len2 + 1), dtype=int)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if (text1[i - 1] == text2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return (dp[-1][-1])


if __name__ == '__main__':
    print(longestCommonSubsequence(text1="abcde", text2="ace"))

import numpy as np


def countSubstrings(s) -> int:
    n = len(s)
    ans = n
    dp = np.full((n + 1, n + 1), False)
    for i in range(n + 1):
        dp[i][i] = True

    for i in range(n - 1):
        if (s[i] == s[i + 1]):
            dp[i][i + 1] = True
            ans += 1
    for l in range(3, n + 1):
        i = 0
        for j in range(i + l - 1, n):
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            ans += 1 if dp[i][j] == True else 0

            i += 1
    return ans


if __name__ == '__main__':
    countSubstrings("abc")
    countSubstrings("aaa")

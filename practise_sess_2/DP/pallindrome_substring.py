import numpy as np
class Solution:
    def countSubstrings(self, s: str):
        n = len(s)
        ans = len(s)
        dp = np.full((n, n), False)
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])
            ans += dp[i][i+1]

        for length in range(3,n+1):
            i = 0
            for j in range(i+length-1, n):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                ans += dp[i][j]
                i += 1

        return ans




if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("aaaaa"))
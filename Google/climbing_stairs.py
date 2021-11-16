import numpy as np
class Solution:
    def climbStairs(self, n):
        dp = np.full(n+1, 0)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(n = 2))
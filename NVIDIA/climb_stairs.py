import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = np.zeros(n+1, dtype=int)
        dp[0]= 1
        dp[1]= 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return (dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(n=2))
    print(sol.climbStairs(n=3))
import numpy as np
class Solution:
    def minCostClimbingStairs(self, cost):
        dp = np.full(len(cost)+2, 0)
        cost.append(0)
        dp[0] = 0
        dp[1] = 0
        for i in range(1, len(cost)+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-1]+dp[i-2])

        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))
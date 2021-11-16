import numpy as np
class Solution:
    def minCostClimbingStairs(self, cost):
        dp = np.full(len(cost), 0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        print(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))
import numpy as np
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = np.full(n+1, 0)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        print(dp)



if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20]))
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
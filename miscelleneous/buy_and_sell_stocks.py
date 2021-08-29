import numpy as np
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        buy_dp = np.zeros((n+1), dtype=int)
        sell_dp = np.zeros((n+1), dtype=int)
        buy_dp[0] = -prices[0]
        sell_dp[0] = 0
        for i in range(1, len(prices)+1):
            buy_dp[i] = max(buy_dp[i-1], -prices[i-1])
            sell_dp[i] = max(sell_dp[i-1], buy_dp[i-1]+prices[i-1])
        return sell_dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(prices = [7,1,5,3,6,4]))

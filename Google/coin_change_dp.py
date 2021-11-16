import numpy as np
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = np.full((len(coins) + 1, amount + 1), 9999999999, dtype=int)
        dp[0][0] = 0
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(coins) + 1):
            curr = coins[i - 1]
            for j in range(1, amount + 1):
                if j - curr < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
        return -1 if (dp[-1][-1]) == 9999999999 else dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.coinChange(coins = [1,2,5], amount = 11))
    print(sol.coinChange(coins = [1], amount = 2))
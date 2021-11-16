import numpy as np
def maxProfit(prices) -> int:
    buy_dp = np.full(len(prices) + 1, -1)
    sell_dp = np.full(len(prices) + 1, -1)
    buy_dp[0] = -prices[0]
    sell_dp[0] = 0
    # profit = sell - buy -> sell = buy+profit
    for i in range(1, len(prices) + 1):
        buy_dp[i] = max(buy_dp[i - 1], -prices[i - 1])
        sell_dp[i] = max(sell_dp[i - 1], buy_dp[i - 1] + prices[i - 1])
    print(buy_dp)
    print(sell_dp)
    return sell_dp[-1]


if __name__ == '__main__':
    maxProfit([7,1,5,3,6,4])
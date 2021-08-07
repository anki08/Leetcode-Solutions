import numpy as np
def maxProfit(prices) -> int:
    buy_dp = np.full(len(prices)+1, -1)
    sell_dp = np.full(len(prices)+1, -1)
    buy_dp[0] = 0
    sell_dp[0] = -100000000000
    old = 0
    for i in range(1,len(prices)+1):
        prev = buy_dp[i-1]
        buy_dp[i] = max(buy_dp[i-1], sell_dp[i-1]+prices[i-1])
        sell_dp[i] = max(sell_dp[i-1], old-prices[i-1])
        old = prev
    # print(sell_dp)
    return (buy_dp[-1])


if __name__ == '__main__':
    print(maxProfit([1,2,3,0,2]))
    print(maxProfit([1]))
    # print(maxProfit([7,6,4,3,1]))
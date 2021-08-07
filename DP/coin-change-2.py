import numpy as np
def coinChange(coins, amount) -> int:
    n = len(coins)
    dp = np.zeros((n, amount+1), dtype=int)
    for i in range(n):
        dp[i][0] = 1
    # print(dp)
    for i in range(n):
        curr = coins[i]
        for j in range(1, amount+1):
            if(curr <= j):
                dp[i][j] = dp[i-1][j] + dp[i][j-curr]
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    return (dp[-1][-1])

if __name__ == '__main__':
    print(coinChange([1,2,5], 5))
    print(coinChange([2], 3))
    print(coinChange(coins = [10], amount = 10))
    print(coinChange(coins = [1,101,102,103], amount = 100))
    print(coinChange(coins = [1], amount = 2))
    print(coinChange(coins = [186,419,83,408], amount = 6249))
    print(coinChange(coins = [1,2147483647], amount = 2))
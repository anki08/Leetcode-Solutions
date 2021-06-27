import numpy as np
def coinChange(coins, amount) -> int:
    n = len(coins)
    coins_sorted = sorted(coins)
    if (coins_sorted[0] > amount and amount > 0):
        return -1
    dp = np.full((n+1,amount+1),2**31, dtype=int)
    for i in range(n+1):
        dp[i][0]=0

    for i in range(1, n+1):
        curr = coins[i-1]
        for j in range(1, amount+1):
            if(curr > amount):
                dp[i][j]=dp[i-1][j]
                continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-curr]+1)


    print(dp)
    if(dp[-1][-1] == 2**31):
        return -1
    return dp[-1][-1]



if __name__ == '__main__':
    # print(coinChange([1,2,5], 11))
    # print(coinChange([2], 3))
    # print(coinChange(coins = [1], amount = 0))
    # print(coinChange(coins = [1], amount = 1))
    # print(coinChange(coins = [1], amount = 2))
    # print(coinChange(coins = [186,419,83,408], amount = 6249))
    print(coinChange(coins = [1,2147483647], amount = 2))
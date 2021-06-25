import numpy as np
def lastStoneWeightII(stones):
    stones = sorted(stones)
    n = len(stones)
    total_weight = sum(stones)
    subset_weight = total_weight//2
    dp = np.zeros((n+1, subset_weight+1))
    for i in range(1, n+1):
        curr = stones[i-1]
        for j in range(1, subset_weight+1):
            if(curr > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(curr + dp[i-1][j-curr], dp[i-1][j])

    # print(dp)
    return int(total_weight - 2*dp[-1][-1])

if __name__ == '__main__':
    print(lastStoneWeightII([2,7,4,1,8,1]))
    print(lastStoneWeightII([1,2,4,8,16,32,64,12,25,51]))
    print(lastStoneWeightII([31,26,33,21,40]))
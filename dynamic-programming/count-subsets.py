import numpy as np


def canPartitionKSubsets(nums, k) -> bool:
    nums = sorted(list(set(nums)))
    n = len(nums)
    dp = np.full((n + 1, k + 1), 0)
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (nums[i - 1] <= j):
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return (dp[n][k])


if __name__ == '__main__':
    # print(canPartitionKSubsets(nums = [1, 2, 3, 3], k = 6))
    # print(canPartitionKSubsets(nums = [1, 1, 1, 1], k = 1))
    print(canPartitionKSubsets(nums=[2, 2, 2, 2, 3, 4, 5], k=5))
    print(canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=5))

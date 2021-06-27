import numpy as np


def canPartitionKSubsets(nums, k) -> bool:
    total_sum = sum(nums)
    if (total_sum % k != 0):
        return False
    n = len(nums)
    target = total_sum // k
    dp = np.full((1 << n), -1)
    dp[0] = 0
    for i in range(1 << n):
        if (dp[i] == -1):
            continue
        for j in range(n):
            if (((i & 1 << j) == False) and dp[i] + nums[j] <= target):
                dp[i | 1 << j] = (dp[i] + nums[j]) % target

    return dp[(1 << n) - 1] == 0


if __name__ == '__main__':
    # print(canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
    print(canPartitionKSubsets(nums=[1, 2, 3], k=2))
    # print(canPartitionKSubsets(nums=[2, 2, 2, 2, 3, 4, 5], k=4))

import numpy as np


def findNumberOfLIS(nums) -> int:
    count = 0
    dp = np.ones(len(nums), dtype=int)
    dp_count = np.ones(len(nums), dtype=int)
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i] > nums[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                dp_count[i] = dp_count[j]
            elif (dp[i] == dp[j] + 1):
                dp_count[i] += dp_count[j]
    max_length = max(dp)
    for i in range(len(dp)):
        if (dp[i] == max_length):
            count += dp_count[i]
    print("count", dp_count)
    print("dp", dp)
    return count


if __name__ == '__main__':
    print(findNumberOfLIS([1, 3, 5, 4, 7]))
    print(findNumberOfLIS([2, 2, 2, 2, 2]))
    print(findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))

import numpy as np


def lengthOfLIS(nums) -> int:
    global maximum

    def lengthOfLISUtil(nums, n):
        global maximum
        if n == 1:
            return 1
        max_ending_here = 1
        for i in range(1, n):
            res = lengthOfLISUtil(nums, i)
            if (nums[i - 1] < nums[n - 1] and res + 1 > max_ending_here):
                max_ending_here = res + 1
        maximum = max(maximum, max_ending_here)

        return max_ending_here

    maximum = 1
    lengthOfLISUtil(nums, len(nums))
    return maximum


def lengthOfLIS_dp(nums):
    dp = np.ones(len(nums), dtype=int)

    for i in range(1, len(nums)):
        for j in range(i):
            if (nums[i] > nums[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == '__main__':
    print(lengthOfLIS_dp([3, 10, 2, 1, 20]))
    print(lengthOfLIS_dp([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS_dp([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS_dp([7, 7, 7, 7, 7, 7, 7]))

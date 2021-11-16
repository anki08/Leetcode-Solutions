import numpy as np


class Solution:
    def canPartition(self, nums):
        nums = np.array(nums)
        dp = np.full(12, False)
        if np.sum(nums) % 2 != 0:
            return False
        subset_sum = np.sum(nums) // 2

        def can_partition_util(nums, n, subset_sum):
            if dp[n] == True or subset_sum == 0:
                return True
            if n == 0 or subset_sum <= 0:
                return False
            result = can_partition_util(nums, n - 1, subset_sum - nums[n]) or can_partition_util(nums, n - 1, subset_sum)
            return result
        return can_partition_util(nums, len(nums) - 1, subset_sum)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))

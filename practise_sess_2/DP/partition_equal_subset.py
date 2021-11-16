import numpy as np


class Solution:
    def canPartition(self, nums):
        n = len(nums)
        nums = np.array(nums)
        target = np.sum(nums)
        if target % 2 != 0:
            return False
        subset_sum = target // 2

        dp = np.full((n + 1, subset_sum + 1), False)
        dp[0][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(1, subset_sum+1):
                if curr > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return (dp[-1][-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))

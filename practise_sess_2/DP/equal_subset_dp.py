import numpy as np
class Solution:
    def canPartition(self, nums):
        nums = np.array(nums)
        target_sum = np.sum(nums)
        if target_sum%2!=0:
            return False
        subset_sum = target_sum//2
        dp = np.full((len(nums)+1, subset_sum+1), False)
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            curr = nums[i-1]
            for j in range(1, subset_sum+1):
                if curr > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1,2,3,5]))
    print(sol.canPartition([1,5,11,5]))
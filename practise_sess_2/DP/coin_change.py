import numpy as np
class Solution:
    def combinationSum4(self, nums, target):
        n = len(nums)
        dp = np.full((n, target), 0)
        # dp[0][0] = 1
        for i in range(n):
            if (nums[i] <= target):
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        for i in range(target):
            if (nums[0] <= i):
                dp[0][i] = 1
            else:
                dp[i][0] = 0
        for i in range(n):
            curr = nums[i]
            for j in range(target):
                if curr>=target:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-curr] + dp[i-1][j]+ dp[i][j-curr]
        print(dp[-1][-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum4(nums = [1,2,3], target = 4))
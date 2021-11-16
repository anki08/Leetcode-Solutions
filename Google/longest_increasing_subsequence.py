import numpy as np
class Solution:
    def lengthOfLIS(self, nums):
        dp = np.full(len(nums), 1)
        dp_count = np.full(len(nums), 1)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                if dp[j]+1>dp[i]:
                    dp_count[i] += dp_count[j]

        return max(dp)



if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))

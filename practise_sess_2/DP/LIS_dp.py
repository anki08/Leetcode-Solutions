import numpy as np
class Solution:
    def lengthOfLIS(self, nums):
        dp = np.ones(len(nums), dtype=int)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        print(dp)
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
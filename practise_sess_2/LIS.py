import numpy as np
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = np.full(n, 1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i]>nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)



if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS([0,1,0,3,2,3]))
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
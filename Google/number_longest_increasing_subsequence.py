import numpy as np
class Solution:
    def lengthOfLIS(self, nums):
        dp = np.full(len(nums), 1)
        dp_count = np.full(len(nums), 1)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    dp_count[i] = dp_count[j]
                elif dp[j]+1==dp[i]:
                    dp_count[i] += dp_count[j]
        print(dp_count)
        print(dp)

        max_v = max(dp)
        count = 0
        for i in range(len(dp_count)):
            if dp[i] == max_v:
                count += dp_count[i]

        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS(nums = [1,3,5,4,7]))

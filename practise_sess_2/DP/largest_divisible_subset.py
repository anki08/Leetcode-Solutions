import numpy as np
class Solution:
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        dp = np.ones(len(nums), dtype=int)
        for i in range(len(nums)):
            for j in range(i):
                if ((nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0) and dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
        print(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset([1,3,5,4,7]))
    print(sol.largestDivisibleSubset([2,2,2,2,2]))
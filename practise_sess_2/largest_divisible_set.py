import numpy as np
class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        dp = np.full(n, 1)
        for i in range(1, n):
            for j in range(i):
                if (nums[i]%nums[j] ==0 or nums[j]%nums[i] ==0) and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1

        print (dp)
        ans = []
        max_val = max(dp)
        max_val_index = np.where(dp== max_val)
        print(max_val_index[0][0])
        ans.append(nums[max_val_index[0][0]])
        while max_val_index[0][0] > 0:
            for i in range(max_val_index[0][0]):
                if nums[i] <= max_val and dp[i] == max_val_index[0][0]:
                    ans.append(nums[i])
                    max_val_index[0][0] -= 1

        return (ans[::-1])

if __name__ == '__main__':
    sol = Solution()
    # print(sol.largestDivisibleSubset([1,2,3]))
    print(sol.largestDivisibleSubset([1,2,4,8]))
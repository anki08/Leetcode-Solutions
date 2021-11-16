from collections import defaultdict

import numpy as np
class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in nums]
        print(dp)
        res = 0
        currDiff = 0
        for i in range(n):
            for j in range(i):
                currDiff =  nums[i] - nums[j]
                if currDiff in dp[j]:
                    dp[i][currDiff] = max(dp[i][currDiff], dp[j][currDiff]+1)
                else:
                    dp[i][currDiff] = 2
            res =  max(res, dp[i][currDiff])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestArithSeqLength([3,6,9,12]))

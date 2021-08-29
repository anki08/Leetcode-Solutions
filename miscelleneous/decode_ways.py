import numpy as np
class Solution:
    def __init__(self):
        self.count = 0

    def numDecodings(self, s):
        dp = np.zeros(len(s)+1, dtype=int)
        dp[0] = 1
        for i in range(1, len(s)+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[-1])

if __name__ == '__main__':
    sol = Solution()
    sol.numDecodings("11111")
    sol.numDecodings("12")
    sol.numDecodings("226")
    # print(sol.count)

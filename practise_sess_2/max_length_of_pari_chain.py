import  numpy as np
class Solution:
    def findLongestChain(self, pairs):
        n = len(pairs)
        pairs = sorted(pairs)
        dp = np.full(n, 1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
        print(dp)
        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findLongestChain([[1,2],[2,3],[3,4]]))
    print(sol.findLongestChain([[1,2],[7,8],[4,5]]))
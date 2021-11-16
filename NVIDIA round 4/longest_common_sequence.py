import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        len1 = len(text1)
        len2 = len(text2)
        dp = np.full((len1+1, len2+1), 0)
        # dp[0][0] = 1
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
    print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
    print(sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))

import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        len1 = len(text1)
        len2 = len(text2)
        dp = np.full((len1, len2), 0)
        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
        return dp[-1][-1]




if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"))
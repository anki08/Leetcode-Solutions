import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = np.full((len(text1), len(text2)), 0)
        # dp[0][0] = 1
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return (dp[-1][-1])



if __name__ == '__main__':
    sol = Solution()
    # print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))

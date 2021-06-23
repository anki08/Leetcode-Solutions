import numpy as np
def numDecodings(s) -> int:

    if(len(s) == 0):
        return 0

    def numDecodingsUtil(s):
        if(len(s)==0):
            return 1
        if (s[0] == '0'):
            return 0

        ans = numDecodingsUtil(s[1:])
        if(int(s[:2])>9 and int(s[:2])<27):
            ans += numDecodingsUtil(s[2:])

        return ans

    return numDecodingsUtil(s)

def numDecodingsDp(s) -> int:
    if(s[0] == '0'):
        return 0
    dp = np.zeros(len(s)+1)
    dp[0] = 1
    if s[0] != '0':
        dp[1] = 1
    for i in range(2, len(s)+1):
        if(int(s[i-1]) != 0):
            dp[i] = dp[i-1]
        if(int(s[i-2:i])>9 and int(s[i-2:i])<27):
            dp[i] += dp[i-2]
    return dp[-1]


if __name__ == '__main__':
    print(numDecodingsDp("11116"))
import numpy as np
def numDecodings(s: str) -> int:
    dp = np.zeros(len(s)+1, dtype=int)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1
    for i in range(2, len(s)+1):
        if(s[i-1] != '0'):
            dp[i] = dp[i-1]
        if(int(s[i-2:i]) < 27 and int(s[i-2:i]) > 10 ):
            dp[i] += dp[i-2]

    print(dp)
    return dp[-1]




if __name__ == '__main__':
    s = "06"
    print(numDecodings(s))
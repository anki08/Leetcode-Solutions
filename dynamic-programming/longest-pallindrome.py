import numpy as np
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = np.zeros((n, n), dtype=bool)
    for i in range(n-1):
        dp[i][i] = True
        if(s[i] == s[i+1]):
            dp[i][i + 1] = True

    max_len = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == True and j-i+1 > max_len:
                max_len = j-i+1
                ans = s[i:j-i+1]
    return (ans)

def longestPalindromeExpandCenter(s: str) -> str:
    n = len(s)
    start, end  = 0, 0
    for i in range(n):
        l1 = expand_center(s,i,i)
        l2 = expand_center(s,i,i+1)
        max_len = max(l1, l2)
        if(max_len>end-start):
            start = int(i-(max_len-1)/2)
            end = int(i+max_len/2)
    return (s[start:end])
def expand_center(s, L, R):
    r = R
    l = L
    count = 0
    while r<=l and r>0 and L<len(s)-1 and s[r] == s[l]:
        count +=1
        r-=1
        l+=1
    return l-r+1




if __name__ == '__main__':
    print(longestPalindrome("babad"))
    print(longestPalindromeExpandCenter("babad"))
import numpy as np


def longestPalindrome(s) -> str:
    calc = np.zeros((len(s), len(s)), dtype=int)
    max_length = 1
    for i in range(len(s)):
        calc[i][i] = 1

    start = 0
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]):
            max_length = 2
            start = i
            calc[i][i + 1] = 1
    k = 3
    while k <= len(s):
        i = 0
        while i < (len(s) - k + 1):
            j = i + k - 1
            if (s[i] == s[j] and calc[i + 1][j - 1] == 1):
                calc[i][j] = 1
                if (k > max_length):
                    max_length = k
                    start = i
            i += 1
        k += 1

    print(calc)
    print(s[start:(start + max_length)])


if __name__ == '__main__':
    longestPalindrome("aaaaa")
    longestPalindrome("babad")

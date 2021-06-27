def isSubsequence(s: str, t: str) -> bool:
    def subsequenceUtil(s_i, t_i):
        if (s_i == len(s)):
            return True
        if (t_i == len(t)):
            return False
        if (s[s_i] == t[t_i]):
            return subsequenceUtil(s_i + 1, t_i + 1)
        else:
            return subsequenceUtil(s_i, t_i + 1)

    return subsequenceUtil(0, 0)


if __name__ == '__main__':
    print(isSubsequence("abc", "assbssc"))

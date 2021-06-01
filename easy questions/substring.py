def isSubsequence(s: str, t: str) -> bool:
    hash = {}
    s_i = 0
    t_i = 0
    while (s_i < len(s) and t_i < len(t)):
        if(s[s_i] == t[t_i]):
            t_i += 1
            s_i += 1
        else:
            t_i += 1
    print(s_i)
    if(s_i == len(s)):
        return True
    return False




if __name__ == '__main__':
    print(isSubsequence('aaab', 'aabbbb'))
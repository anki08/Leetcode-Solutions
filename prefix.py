def longestCommonPrefix(strs) -> str:
    prefix = strs[0]
    if (len(prefix) == 0):
        return prefix
    for word in strs[1:]:
        index = get_index(prefix, word)
        prefix = prefix[:index]
        if(len(prefix)==0):
            return prefix

    return prefix

def get_index(prefix, s):
    low = 0
    while(low < len(s) and low < len(prefix) and prefix[low] == s[low]):
        low = low+1
    return low
if __name__ == '__main__':
    s = ["ab", "a"]
    print(longestCommonPrefix(s))
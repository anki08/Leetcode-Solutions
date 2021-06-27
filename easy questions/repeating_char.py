def firstUniqChar(s: str) -> int:
    arr = []
    for i in range(len(s)):
        new_string = s[:i] + s[i + 1:]
        index = new_string.find(s[i])
        if (index == -1):
            return i
    return -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(firstUniqChar(s))

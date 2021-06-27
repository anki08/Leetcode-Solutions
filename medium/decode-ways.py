def numDecodings(s: str) -> int:
    return numDecodingsUtil(s, 0)


def numDecodingsUtil(s, index):
    if (index == len(s)):
        return 1
    if (index == len(s) - 1):
        return 1
    if (s[index] == '0'):
        return 0

    answer = numDecodingsUtil(s, index + 1)
    if (s[index:index + 2] <= '26'):
        answer += numDecodingsUtil(s, index + 2)
    return answer


if __name__ == '__main__':
    s = "2125"
    print(numDecodings(s))

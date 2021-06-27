def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(str1, str2):
        if len(str1) == 0:
            return ""
        if (len(str1) > len(str2)):
            return gcd(str2, str1)

        if (len(str1) == len(str2) and str1 == str2):
            return str1
        elif (len(str1) == len(str2) and str1 != str2):
            return ""

        if (not str2.startswith(str1)):
            return ""
        elif (len(str2) == 0):
            return str1
        else:
            return gcd(str1, str2[len(str1):])

    return gcd(str1, str2)


if __name__ == '__main__':
    print(gcdOfStrings("ABAB", "ABABAB"))

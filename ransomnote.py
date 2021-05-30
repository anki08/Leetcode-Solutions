def canConstruct(ransomNote: str, magazine: str) -> bool:
    hashalp = {}
    for i in magazine:
        if i in hashalp:
            hashalp[i] += 1
        else:
            hashalp[i] = 1

    for i in ransomNote:
        if i in hashalp and hashalp[i] > 0:
            hashalp[i] -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    a = "aa"
    b = "ab"
    print(canConstruct(a, b))
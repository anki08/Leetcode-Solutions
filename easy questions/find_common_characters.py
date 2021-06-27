def commonChars(words):
    hashalp = {}
    for i in range(len(words[0])):
        if (words[0][i] in hashalp):
            hashalp[words[0][i]][0] += 1
        else:
            hashalp[words[0][i]] = [1]

    for i in range(1, len(words)):
        for j in words[i]:
            if (j in hashalp and len(hashalp[j]) == i + 1):
                hashalp[j][i] += 1
            elif (j in hashalp and len(hashalp[j]) == i):
                hashalp[j].append(1)

    res = []
    for key in hashalp:
        if (len(hashalp[key]) == len(words)):
            val = min(hashalp[key])
            for i in range(val):
                res.append(key)
    return res


if __name__ == '__main__':
    print(commonChars(["acabcddd", "bcbdbcbd", "baddbadb", "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]))
    # print(commonChars(["cool","lock","cook"]))

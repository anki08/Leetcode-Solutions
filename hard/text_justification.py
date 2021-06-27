def fullJustify(words, maxWidth):
    i = 0
    res = []
    while i < len(words):
        maxWidth_copy = maxWidth
        line = []
        space = 0
        while (i < len(words) and maxWidth_copy > 0):
            if (maxWidth_copy - len(words[i]) > 0):
                line.append(words[i])
            maxWidth_copy -= len(words[i])

            if (i == len(words) - 1 or maxWidth_copy - len(words[i + 1]) <= 0):
                break

            if (maxWidth_copy > 0):
                maxWidth_copy -= 1
                space += 1
            i += 1

        space = maxWidth - sum(len(x) for x in line)
        print(space)
        if (i < len(words)):
            for k in range(len(line)):
                res.append(line[k])
            res.append(",")
        else:
            res.append(words[-1])
        i += 1
    return res


if __name__ == '__main__':
    print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))

def compress(chars) -> int:
    index, i = 0, 0
    while i < (len(chars)):
        if (i + 1 < len(chars) and chars[i] == chars[i + 1]):
            count = 1
            while i + 1 <= len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            index += 1
            chars[index] = count
            index += 1
            i += 1
        else:
            index += 1
            i += 1
    print(chars)
    print(index)


if __name__ == '__main__':
    chars = ["z", "a", "a", "b", "b", "c", "c", "c", "c"]
    # pr int(compress(chars))
    print(compress(["a"]))

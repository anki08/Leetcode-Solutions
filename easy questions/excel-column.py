def convertToTitle(columnNumber) -> str:
    hash_map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        0: 'Z',
        26: 'Z'
    }
    res = ''
    while (columnNumber > 26):
        rem = columnNumber % 26
        if (rem != 0):
            res += hash_map[rem]
            columnNumber = int(columnNumber / 26)
        elif (rem == 0):
            res += 'Z'
            columnNumber = int(columnNumber / 26) - 1

    res += hash_map[columnNumber]

    return res[::-1]


if __name__ == '__main__':
    print(convertToTitle(52))

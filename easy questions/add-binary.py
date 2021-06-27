def addBinary(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    sum = a + b
    return "{0:b}".format(sum)


if __name__ == '__main__':
    print(addBinary("11", "1"))

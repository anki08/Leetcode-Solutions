def mySqrt(x: int) -> int:
    low = 0
    high = x
    while (low <= high):
        mid = (low + high) // 2
        no = mid * mid
        if (x == no):
            return mid
        elif (no > x):
            high = mid - 1
        else:
            low = mid + 1
    # print(low)
    print(high)
    return high


if __name__ == '__main__':
    print(mySqrt(2))

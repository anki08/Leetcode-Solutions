def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    while (low < high):
        mid = (low + high) // 2
        if (isBadVersion(mid)):
            high = mid
        else:
            low = mid + 1
    return low


def isBadVersion(n):
    if (n >= 4):
        return True


if __name__ == '__main__':
    print(firstBadVersion(5))

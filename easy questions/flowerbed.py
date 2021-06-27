def canPlaceFlowers(flowerbed, n) -> bool:
    for i in range(len(flowerbed)):
        if (n == 0):
            return True

        if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
            n -= 1
            flowerbed[i] = 1
    print(n)
    if (n == 0):
        return True
    return False


if __name__ == '__main__':
    bed = [0, 0, 1, 0, 0]
    print(canPlaceFlowers(bed, 2))

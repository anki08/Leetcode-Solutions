import numpy as np


def floodFill(image, sr: int, sc: int, newColor):
    image = np.array(image)
    flood_fill_util(image, image[sr][sc], sr, sc, newColor)
    return image


def flood_fill_util(image, c, x, y, nC):
    len0, len1 = image.shape

    if (x < 0 or y < 0 or x >= len0 or y >= len1 or image[x][y] != c or image[x][y] == nC):
        return

    image[x][y] = nC

    flood_fill_util(image, c, x + 1, y, nC)
    # flood_fill_util(image, c, x, y + 1, nC)
    # flood_fill_util(image, c, x - 1, y, nC)
    # flood_fill_util(image, c, x, y - 1, nC)


if __name__ == '__main__':
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    nc = 2
    print(floodFill(image, sr, sc, nc))

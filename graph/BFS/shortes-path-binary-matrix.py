from collections import deque

import numpy as np


def shortestPathBinaryMatrix(grid) -> int:
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque()
    grid = np.array(grid)
    R, C = grid.shape
    visited = np.full((R, C), False)
    ans = np.full((R, C), -1)
    d = 1
    if grid[0][0] == 0:
        queue.append((d, 0, 0))
        visited[0][0] = True
    elif (grid[0][0] == 1 or grid[-1][-1] == 1):
        return -1
    step = 1
    while queue:
        step += 1
        d, l, r = queue.popleft()
        if (l == R - 1 and r == C - 1):
            return d
        for i, j in offset:
            x, y = l + i, r + j
            if (x >= 0 and x < R and y >= 0 and y < C and visited[x][y] == False and
                    grid[x][y] == 0):
                visited[x][y] = True
                # print("l", ans[-1][-1])
                queue.append((d + 1, x, y))

    return -1


if __name__ == '__main__':
    # print(shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    # print("%%%%%%%%%%%%%%%%%%")

    print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print("%%%%%%%%%%%%%%%%%%")
    #
    # print(shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print("%%%%%%%%%%%%%%%%%%")

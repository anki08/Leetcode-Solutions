from collections import deque

import numpy as np


def maxDistance(grid) -> int:
    grid = np.array(grid)
    R, C = grid.shape
    visited = np.full((R, C), False)
    max_dist = 0
    steps = 0
    queue = deque()
    for i in range(R):
        for j in range(C):
            if (grid[i][j] == 1):
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))

    if len(queue) == len(grid) * len(grid[0]) or len(queue) == 0:
        return -1

    while queue:
        steps += 1
        for i in range(len(queue)):
            l, r = queue.popleft()
            if (l >= 0 and r >= 0 and l < R and r < C and visited[l][r] == False and grid[l][r] == 0):
                visited[l][r] = True
                max_dist = max(steps, max_dist)
                queue.append((l - 1, r))
                queue.append((l + 1, r))
                queue.append((l, r - 1))
                queue.append((l, r + 1))
        # queue, queue2 = queue2, queue
        # visited = np.full((R, C), False)
    print(max_dist)


if __name__ == '__main__':
    maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]])

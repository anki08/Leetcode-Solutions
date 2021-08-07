import numpy as np
from collections import deque
def shortestBridge(grid) -> int:
    # grid = np.array(grid)
    R,C = len(grid),len(grid[0])
    offset = [(1,0), (0,1), (-1,0), (0,-1)]
    found = False
    first_island = deque()

    def dfs(grid, row, col):
        if(row<0 or row>R-1 or col<0 or col>C-1 or grid[row][col]== 2 or grid[row][col] == 0):
            return
        grid[row][col] = 2
        first_island.append((row,col))
        for x,y in offset:
            dfs(grid, row+x, col+y)

    for i in range(R):
        for j in range(C):
            if (grid[i][j] == 1):
                dfs(grid, i, j)
                found = True
                break
        if found == True:
            break
    print(grid)

    queue = first_island
    step = 0
    # queue.append(first_island[0])
    while queue:
        step += 1
        for i in range(len(queue)):
            row, col = queue.popleft()
            for x,y in offset:
                if(row+x < 0 or row+x>R-1 or col+y<0 or col+y > C-1 or grid[row+x][col+y] == 2):
                    continue
                if grid[row+x][col+y] == 1:
                    return step-1
                grid[row+x][col+y] = 2
                queue.append((row+x, col+y))
    return -1

if __name__ == '__main__':
    # print(shortestBridge([[0,1],[1,0]]))
    # print(shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    # print(shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
    print(shortestBridge([[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]]))
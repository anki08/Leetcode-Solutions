from queue import Queue

import numpy as np

def numIslands(grid):
    if (grid == None or len(grid) == 0):
        return 0

    grid_np = np.array(grid)
    nr = grid_np.shape[0]
    nc = grid_np.shape[1]
    num_islands = 0
    for i in range(nr):
        for j in range(nc):
            if (grid[i][j] == '1'):
                num_islands += 1
                queue = Queue()
                queue.put(i*nc+j)
                while(queue.empty() == False):
                    node = queue.get()
                    r = int(node // nc)
                    c = int(node % nc)
                    if(r-1 >= 0 and grid[r-1][c] == '1'):
                        queue.put((r-1) * nc + c)
                        grid[r-1][c] = '0'

                    if (r+1 < nr and grid[r+1][c] == '1'):
                        queue.put((r + 1) * nc + c)
                        grid[r+1][c] = '0'

                    if (c - 1>= 0 and grid[r][c-1] == '1'):
                        queue.put((r) * nc + (c-1))
                        grid[r][c-1] = '0'

                    if (c + 1 < nc and grid[r][c+1] == '1'):
                        queue.put((r) * nc + (c+1))
                        grid[r][c+1] = '0'
    return num_islands







if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))
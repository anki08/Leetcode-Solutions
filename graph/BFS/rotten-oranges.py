import numpy as np
from collections import deque
def orangesRotting(grid) -> int:
    grid = np.array(grid)
    R,C = grid.shape
    visited = np.full((R,C), False)
    queue = deque()
    ans = np.zeros((R,C), dtype=int)
    count_fresh = 0
    for i in range(R):
        for j in range(C):
            if(grid[i][j] == 2):
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))
            elif (grid[i][j] == 1):
                count_fresh += 1

    max_d = 0
    step = 0
    while(queue):
        step+=1
        for i in range(len(queue)):
            l,r = queue.popleft()
            if(l>=0 and l<R and r>=0 and r<C and visited[l][r]==False and grid[l][r]==1):
                count_fresh -= 1
                visited[l][r] = True
                ans[l][r] = step
                max_d = max(step, max_d)
                queue.append((l - 1, r))
                queue.append((l + 1, r))
                queue.append((l, r - 1))
                queue.append((l, r + 1))
    print(max_d)
    print(ans)
    print("fresh oranges count", count_fresh)




if __name__ == '__main__':
    orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    orangesRotting([[0,2]])
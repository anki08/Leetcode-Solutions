from collections import deque
import numpy as np
def updateMatrix(mat):
    queue = deque()
    mat = np.array(mat)
    R,C = mat.shape
    for i in range(R):
        for j in range(C):
            if(mat[i][j] == 0):
                if(i-1>0 or i+1<R  or j-1>0 or j+1<C):
                    queue.append((i-1, j))
                    queue.append((i+1, j))
                    queue.append((i, j-1))
                    queue.append((i, j+1))
    visited = np.full((R,C), False)
    step = 0
    while (len(queue)>0):
        step+=1
        for i in range(len(queue)):
            val = queue.popleft()
            l,r= val
            if(l>=0 and l<R  and r>=0 and r<C and visited[l][r] == False and mat[l][r] == 1):
                visited[l][r] = True
                mat[l][r] = step
                queue.append((l - 1, r))
                queue.append((l + 1, r))
                queue.append((l, r - 1))
                queue.append((l, r + 1))
    return (mat)


if __name__ == '__main__':
    updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
from collections import deque
import numpy as np
class Solution:
    def updateMatrix(self, mat):
        queue = deque()
        mat = np.array(mat)
        R,C = mat.shape
        visited = np.full((R,C), False)
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    queue.append((i+1,j))
                    queue.append((i,j+1))
                    queue.append((i-1,j))
                    queue.append((i,j-1))
        step = 0
        while queue:
            step+=1
            len_q = len(queue)
            for i in range(len_q):
                x,y = queue.popleft()
                if x>0 and y>0 and x<R and y<C and mat[x][y] ==1 and visited[x][y] == False:
                    mat[x][y] = step
                    visited[x][y] = True
                    queue.append((x+1, y))
                    queue.append((x-1, y))
                    queue.append((x, y+1))
                    queue.append((x, y-1))
        return mat

if __name__ == '__main__':
    sol = Solution()
    # print(sol.updateMatrix( [[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.updateMatrix( [[0,0,0],[0,1,0],[1,1,1]]))
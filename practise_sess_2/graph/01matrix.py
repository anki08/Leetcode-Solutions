from collections import deque
import numpy as np
class Solution:
    def updateMatrix(self, matrix):
        queue = deque()
        matrix = np.array(matrix)
        R, C = matrix.shape
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    if (i - 1 > 0 or i + 1 < R or j - 1 > 0 or j + 1 < C):
                        queue.append((i+1,j))
                        queue.append((i,j+1))
                        queue.append((i-1,j))
                        queue.append((i,j-1))
        step = 0
        visited = np.full((R, C), False)
        while len(queue)>0:
            step+=1
            for i in range(len(queue)):
                x, y = queue.popleft()
                if x>=0 and y>=0 and x<R and y<C and matrix[x][y] == 1 and visited[x][y] == False:
                    visited[x][y] = True
                    matrix[x][y] = step
                    queue.append((x + 1, y))
                    queue.append((x, y + 1))
                    queue.append((x - 1, y))
                    queue.append((x, y - 1))
        print(matrix)


if __name__ == '__main__':
    sol = Solution()
    print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
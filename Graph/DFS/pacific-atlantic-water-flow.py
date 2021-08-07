import numpy as np

def pacificAtlantic(heights):
    offset = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    R, C = len(heights), len(heights[0])
    ans1 = np.full((R, C), 0, int)
    ans2 = np.full((R, C), 0, int)

    def dfs(heights, row, col, res):
        if (row < 0 or row  > R - 1 or col < 0 or col > C - 1):
            return
        res[row][col] += 1
        for x, y in offset:
            if row+x >= 0 and row+x <= R - 1 and col+y >= 0 and col+y <= C - 1:
                if(heights[row+x][col+y] >= heights[row][col] and res[row+x][col+y] ==0):
                    # res[row+x][col+y] += 1
                    dfs(heights, row+x, col+y, res)

    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0:
                ans1[i][j] = 1
                dfs(heights, i, j, ans1)

    for i in range(R):
        for j in range(C):
            if i == R - 1 or j == C - 1:
                ans2[i][j] = 1
                dfs(heights, i, j, ans2)
    print(ans1)
    print(ans2)
    res = []
    for i in range(R):
        for j in range(C):
            if ans1[i][j] > 0 and ans2[i][j] > 0:
                res.append([i,j])
    print(res)


if __name__ == '__main__':
    pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    pacificAtlantic(heights=[[2,1],[1,2]])

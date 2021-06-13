import numpy as np

def spiralOrder(matrix):
    num_rows, num_cols = matrix.shape
    res = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c , di = 0, 0, 0
    seen = np.zeros((num_rows, num_cols), dtype=int)
    for i in range(num_cols * num_rows):
        res.append(matrix[r][c])
        seen[r][c] = 1
        nr, nc = r + dr[di], c + dc[di]
        if 0<=nc<num_cols and 0<=nr<num_rows and seen[nr][nc] == 0:
            r,c = nr,nc
        else:
            di = (di + 1)%4
            r,c = r + dr[di], c + dc[di]
    return res


if __name__ == '__main__':
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(spiralOrder(matrix))

import numpy as np
def matrixBlockSum(mat, k):
    mat = np.array(mat)
    R,C = mat.shape
    range_sum = np.zeros((R+1,C+1), dtype=int)
    ans = np.zeros((R,C), dtype=int)
    for i in range(R):
        for j in range(C):
            range_sum[i+1][j+1] = range_sum[i][j+1] + range_sum[i+1][j] - range_sum[i][j] + mat[i][j]
    for i in range(R):
        for j in range(C):
            r1 = max(0, i-k)
            r2 = min(R, i+k+1)
            c1 = max(0, j-k)
            c2 = min(C, j+k+1)
            ans[i][j] = range_sum[r2][c2] - range_sum[r2][c1]-range_sum[r1][c2] + range_sum[r1][c1]
    return  ans


if __name__ == '__main__':
    print(matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
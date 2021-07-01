import numpy as np
def minFallingPathSum(matrix) -> int:
    matrix = np.array(matrix)
    R,C = matrix.shape
    for i in range(1, R):
        min_val = np.inf
        for j in range(C):
            t1 = matrix[i-1][j-1] if (j-1 >=0) else np.inf
            t2 = matrix[i-1][j + 1] if (j +1 < C) else np.inf
            min_val = min(t1, t2, matrix[i-1][j])
            matrix[i][j] += min_val
    print(matrix)
    return (min(matrix[-1]))



if __name__ == '__main__':
    # minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
    print(minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
import numpy as np
def rotate(matrix) -> None:
    R,C = matrix.shape
    matrix_copy = matrix.copy()
    for row in range(R):
        for col in range(C):
            # print(row, col , " " , C-col-1, row)
            matrix[row][col]= matrix_copy[C-col-1][row]
    print(matrix)


if __name__ == '__main__':
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(matrix)
    rotate(matrix)

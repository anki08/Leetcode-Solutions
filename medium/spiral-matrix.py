import numpy as np

def spiralOrder(matrix):
    num_rows,num_cols = matrix.shape
    start_r , start_c = 0,0
    res = []
    r,c = 0,0
    while start_r<num_rows and start_c < num_cols:
        while r < num_rows and c < num_cols:
                res.append(matrix[r][c])
                if(r == start_r and c == start_c):
                    c += 1
                elif(r == start_r and c == num_cols-1):
                    r += 1
                elif(r==num_rows and c==num_cols):
                    c -=1
                elif(r == num_rows and c == start_c):
                    r -= 1
                else:
                    c+=1
            # r += 1

        start_c += 1
        start_r += 1
        num_cols -= 1
        num_rows -= 1
    return res





if __name__ == '__main__':

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(spiralOrder(matrix))
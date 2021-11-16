import numpy as  np
class Solution:
    def transpose(self, matrix):
        # matrix = np.array(matrix)
        print(matrix)

        R, C = len(matrix), len(matrix[0])
        out = np.full((R,C), 0)
        for r in range(R):
            for c in range(C):
                if r == c:
                    out[r][c] = matrix[r][c]
                else:
                    print("hjkb")
                    out[r][c] = matrix[c][r]
        return (out)



if __name__ == '__main__':
    sol =  Solution()
    print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))


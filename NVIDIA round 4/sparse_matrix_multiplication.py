import numpy as np
class Solution:
    def multiply(self, mat1, mat2):
        mat1 = np.array(mat1)
        mat2 = np.array(mat2)
        R1,C1 = mat1.shape
        R2,C2 = mat2.shape
        ans = np.zeros((R1,C2), dtype=int)

        for r1 in range(R1):
            for c1 in range(C2):
                sum = 0
                for r2 in range(R2):
                        sum += mat1[r1][r2]*mat2[r2][c1]
                ans[r1][c1] = sum
        return(ans)

if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply([[1,-5]], [[12],[-1]]))
    print(sol.multiply(mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]))
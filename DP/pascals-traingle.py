import numpy as np
def generate(numRows: int):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    dp = [[1], [1,1]]

    for i in range(2, numRows):
        val = [1]
        for j in range(1, i):
            val.append(dp[i-1][j-1]+dp[i-1][j])
        val.append(1)
        dp.append(val)
    print(dp)

if __name__ == '__main__':
    generate(4)
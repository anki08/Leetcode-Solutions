import numpy as np

def minimumTotal(triangle) -> int:
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            smallest_above = np.inf
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])



if __name__ == '__main__':
    print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    # minimumTotalDP([[-10]])
    # print(minimumTotal([[-1],[2,3],[1,-1,-3]]))


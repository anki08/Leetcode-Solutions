import collections

import numpy as np
class Solution:
    def findLonelyPixel(self, picture):
        R,C = np.array(picture).shape
        count = 0
        row_map = []
        col_map = []
        for row in  range(R):
            for col in range(C):
                if picture[row][col] == 'B':
                    row_map.append(row)
                    col_map.append(col)
        row_count = collections.Counter(row_map)
        col_count = collections.Counter(col_map)
        for x in range(len(row_map)):
            row = row_map[x]
            col = col_map[x]
            if row_count[row] == 1 and col_count[col] ==1:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLonelyPixel([["W","B","B"],["W","B","W"],["B","W","W"]]))
    print(sol.findLonelyPixel([["W","B","W","W"],["W","B","B","W"],["W","W","W","W"]]))




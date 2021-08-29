import numpy as np
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku(board =
[["1","5","9","4","7","3","2","8","6"]
,["3","2","6","9","1","8","7","5","4"]
,["7","8","1","6","5","2","9","3","."]
,["2","1","7","3","9","4","8","6","5"]
,["8","4","5","7","2","6","1","9","3"]
,["9","6","3","1","8","5","4","2","7"]
,["6","3","2","8","4","1","5","7","9"]
,["5","7",".","2","6","9","3","4","8"]
,["4","9","8","5","3","7","6","1","2"]]))

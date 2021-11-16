import numpy as np
class Solution:
    def tictactoe(self, moves):

        board = np.full((3,3), 0)
        for i in range(len(moves)):
            if i%2==0:
                board[moves[i][0]][moves[i][1]] = 1
            else:
                board[moves[i][0]][moves[i][1]] = 2
        print(board)


if __name__ == '__main__':
    sol = Solution()
    print(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
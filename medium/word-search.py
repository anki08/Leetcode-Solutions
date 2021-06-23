import numpy as np
def exist(board, word) -> bool:
    board = np.array(board)
    NR, NC = board.shape

    def backtrack(r,c,suffix):
        if(len(suffix) == 0):
            return True
        if(r<0 or r>NR or c<0 or c>NC or board[r][c]!= suffix[0]):
            return False

        board[r][c] = '#'
        offsets = [(1,0),(0,1),(-1,0), (0,-1)]
        for roffset, coffset in offsets:
            if backtrack(r+roffset, c+coffset, suffix[1:]):
                return True

        board[r][c]=suffix[0]
        return False

    for r in range(NR):
        for c in range(NC):
            if backtrack(r,c, word):
                return True

    return False





if __name__ == '__main__':
    print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
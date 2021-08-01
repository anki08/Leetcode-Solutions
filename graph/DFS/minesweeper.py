import numpy as np
def updateBoard(board, click):
    offset = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
    board = np.array(board)
    R,C = board.shape
    if(board[click[0]][click[1]] == 'M'):
        board[click[0]][click[1]]  = 'X'
        return board

    def dfs(board, row, col):
        if(row<0 or row > R-1 or col<0 or col>C-1 or board[row][col]  != 'E'):
            return
        num_of_bombs = count_bombs(row,col)
        if(num_of_bombs == 0):
            board[row][col] = 'B'
            for x,y in offset:
                dfs(board, row+x, col+y)
        else:
            board[row][col] = str(num_of_bombs)
        return board


    def count_bombs(row, col):
        num = 0
        for x,y in offset:
            if (row + x < 0 or row + x > R-1  or col + y < 0 or col + y > C-1):
                continue
            if(board[row+x][col+y] == 'M' or board[row+x][col+y] == 'X'):
                num+=1
        return num


    return dfs(board, click[0], click[1])


if __name__ == '__main__':
    print(updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))
import random

board = [['' for _ in range(3)]for _ in range(3)]
print(board)

def checker():
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != '':
                return True
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != '':
                return True
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != '':
            return True
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][0] != '':
            return True
    return False



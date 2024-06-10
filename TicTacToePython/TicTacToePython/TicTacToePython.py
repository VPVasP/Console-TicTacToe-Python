import numpy as np
import random
from time import sleep

#creating the board
def empty_board():
    board = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    return board

#return a list of all the empty places in the baord
def empty_places(board):
    list = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                list.append((i, j))
    return list

#place the player's move at an avalable empty position
def random_place(board, player):
    select = empty_places(board)
    if select:
        current_location = random.choice(select)
        board[current_location] = player
    return board

#check if a player has won if he has completed a row
def row_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

#check if player has won if he has completed a column
def col_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                break
        if win:
            return True
    return False

#check if the player has won by diagonal 
def diag_winner(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True

    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
            break
    return win


#check if there i s a winner or tie
def evaluate_game(board):

    winner = 0
    for player in [1, 2]:
        if (row_winner(board, player) or
                col_winner(board, player) or
                diag_winner(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


#start the game of tic tac toe
def tic_tac_toe():
    board = empty_board()
    print(board)
    sleep(2)
    winner = 0
    counter = 1
    while winner == 0:
        for player in [1, 2]:
            brd = random_place(board, player)
            print(f"Board after {counter} move")
            print(brd)
            sleep(2)
            counter += 1
            winner = evaluate_game(brd)
            if winner != 0:
                break
    return winner

# print the winner 
print("Winner is player: " + str(tic_tac_toe()))



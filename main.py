import numpy as np
import random

def display_board(board):
    print(board)

def create_board(x, y, num_bombs):
    bomb_positions = set()
    while len(bomb_positions) != num_bombs:
        pos = (random.randint(0, x-1), random.randint(0, y-1))
        bomb_positions.add(pos)
    board = np.zeros((x, y))
    for coords in bomb_positions:
        board[coords[0]][coords[1]] = x*y
    for i in range(x):
        for j in range(y):
            # need to set the values for all the non bomb spots
            pass
    return board

print("Welcome to Minesweeper!")

x = int(input("How wide do you want the game board?\n"))
y = int(input("How tall do you want it?\n"))
bombs = int(input("How many bombs do you want?\n"))

game_board = create_board(x, y, bombs)

display_board(game_board)

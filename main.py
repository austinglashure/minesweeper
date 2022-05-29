import numpy as np

def display_board(board):
    print(board)

def create_board(x, y, num_bombs):
    print(f"You want {num_bombs} bombs\n")
    return np.zeros((x, y))

print("Welcome to Minesweeper!")

x = int(input("How wide do you want the game board?\n"))
y = int(input("How tall do you want it?\n"))
bombs = int(input("How many bombs do you want?\n"))

game_board = create_board(x, y, bombs)

display_board(game_board)
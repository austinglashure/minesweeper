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
        print(f"coords: {coords[0]} {coords[1]}")
        if coords[0] == 0 and coords[1] == 0:
            print("top left")
            board[coords[0]+1][coords[1]+1] += 1
            board[coords[0]][coords[1]+1] += 1
            board[coords[0]+1][coords[1]] += 1
        elif coords[0] == x-1 and coords[1] == y-1:
            print("bottom right")
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]-1][coords[1]-1] += 1
            board[coords[0]-1][coords[1]] += 1
        elif coords[0] == 0 and coords[1] == y-1:
            print("top right")
            board[coords[0]+1][coords[1]] += 1
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]+1][coords[1]-1] += 1
        elif coords[0] == x-1 and coords[1] == 0:
            print("bottom left")
            board[coords[0]-1][coords[1]] += 1
            board[coords[0]-1][coords[1]+1] += 1
            board[coords[0]][coords[1]+1] += 1
        elif coords[0] == 0:
            print("top")
            board[coords[0]+1][coords[1]] += 1
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]+1][coords[1]-1] += 1
            board[coords[0]][coords[1]+1] += 1
            board[coords[0]+1][coords[1]+1] += 1
        elif coords[1] == 0:
            print("left")
            board[coords[0]+1][coords[1]+1] += 1
            board[coords[0]][coords[1]+1] += 1
            board[coords[0]+1][coords[1]] += 1
            board[coords[0]-1][coords[1]] += 1
            board[coords[0]-1][coords[1]+1] += 1
        elif coords[0] == x-1:
            print("bottom")
            board[coords[0]-1][coords[1]] += 1
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]-1][coords[1]-1] += 1
            board[coords[0]][coords[1]+1] += 1
            board[coords[0]-1][coords[1]+1] += 1
        elif coords[1] == y-1:
            print("right")
            board[coords[0]+1][coords[1]-1] += 1
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]+1][coords[1]] += 1
            board[coords[0]-1][coords[1]] += 1
            board[coords[0]-1][coords[1]-1] += 1
        else:
            board[coords[0]+1][coords[1]+1] += 1
            board[coords[0]-1][coords[1]-1] += 1
            board[coords[0]+1][coords[1]] += 1
            board[coords[0]-1][coords[1]] += 1
            board[coords[0]][coords[1]-1] += 1
            board[coords[0]][coords[1]+1] += 1
            board[coords[0]+1][coords[1]-1] += 1
            board[coords[0]-1][coords[1]+1] += 1
    return board

print("Welcome to Minesweeper!")

x = int(input("How wide do you want the game board?\n"))
y = int(input("How tall do you want it?\n"))
bombs = int(input("How many bombs do you want?\n"))

game_board = create_board(x, y, bombs)

display_board(game_board)

import random
import math

print("Welcome to Minesweeper!\n")
width = int(input("How wide do you want the board? (max is 10)\n"))
length = int(input ("How tall do you want the board? (max is 10)\n"))
print(f"Okay! Creating the board with dimensions {length}x{width}\n")
bomb = '@'
tile = '#'
empty = 'O'

class Tile:
    def __init__(self, position, hasBomb, board):
        self.x = position[0]
        self.y = position[1]
        self.isBomb = hasBomb
        self.initial_value = tile
        if self.isBomb:
            self.under_value = bomb
        else:
            self.under_value = empty


board = []
counter = 0
amount = round(math.sqrt(width*length))
print(amount)
size = width*length
print(size)
bomb_positions = [random.randint(0, size-1) for i in range(amount)]
print(bomb_positions)
for i in range(width):
    for j in range(length):
        if counter in bomb_positions:
            tile = Tile([i, j], True, board)
            board.append(tile)
        else:
            tile = Tile([i, j], False, board)
            board.append(tile)
        counter += 1

for tile in board:
    print(f"pos: {tile.x}{tile.y}")
    print(tile.isBomb)

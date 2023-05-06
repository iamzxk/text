import random
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

def new_board():
    return [[0 for _ in range(4)] for _ in range(4)]

def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    i, j = random.choice(empty_cells)
    board[i][j] = 2 if random.random() < 0.9 else 4

def move(board, direction):
    moved = False
    for _ in range(direction % 2 * 3): # Rotate the board to make it a left slide
        board = [[board[j][3 - i] for j in range(4)] for i in range(4)]
    for row in board:
        while 0 in row: row.remove(0) # Remove zeros
        while len(row) < 4: row.append(0) # Fill with zeros
        for i in range(3): # Merge cells
            if row[i] and row[i] == row[i + 1]:
                row[i], row[i + 1], moved = row[i] * 2, 0, True
    for _ in range((4 - direction) % 2 * 3): # Rotate back
        board = [[board[j][3 - i] for j in range(4)] for i in range(4)]
    return board, moved

def game_loop():
    board = new_board()
    add_random_tile(board)
    add_random_tile(board)

    while True:
        clear_screen()
        print_board(board)
        user_input = input("输入方向 (w/a/s/d): ").lower()

        if user_input in 'wasd':
            direction_map = {'w': 0, 'a': 1, 's': 2, 'd': 3}
            board, moved = move(board, direction_map[user_input])

            if moved:
                add_random_tile(board)

            if any(2048 in row for row in board):
                print("恭喜你，你赢了！")
                break
            elif all(any(cell != 0 for cell in row) for row in board):
                print("很遗憾，你输了。")
                break

game_loop()

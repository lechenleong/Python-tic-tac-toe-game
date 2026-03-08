import random
import time

# Create board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    print("\n    1   2   3")
    print("  -------------")
    for i in range(3):
        print(i+1, *board[i], "", sep=" | ")
        print("  -------------")


def start_game(board):
    print("\nWelcome to Tic-Tac-Toe!")
    time.sleep(1)

    print("""
The board is like this:

     1     2     3
   ----------------
 1 | 11 | 12 | 13 |
   ----------------
 2 | 21 | 22 | 23 |
   ----------------
 3 | 31 | 32 | 33 |
   ----------------
""")

    time.sleep(2)

    player = random.choice(["X", "O"])
    print(f'Player "{player}" starts the game.')

    print_board(board)
    return player


def switch_player(player):
    return "O" if player == "X" else "X"


def take_input(board, available, player):
    while True:
        print("Available positions:", available)

        try:
            pos = int(input("Enter position: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if pos not in available:
            print("Invalid position. Try again.\n")
            continue

        available.remove(pos)

        row = pos // 10 - 1
        col = pos % 10 - 1
        board[row][col] = player
        break


def check_win(board):

    # rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def play_game():
    board = create_board()
    available = [11,12,13,21,22,23,31,32,33]

    player = start_game(board)

    while True:

        take_input(board, available, player)

        print_board(board)

        if check_win(board):
            print(f"\n🎉 Player {player} wins!")
            break

        if not available:
            print("\n🤝 Game TIE!")
            break

        player = switch_player(player)


play_game()




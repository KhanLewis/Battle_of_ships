"""Welcome to my battle ships game"""
from random import randint


class Board:
    """This generates the board for the game"""
    def __init__(self, size):
        self.size = size
        self.board = []
        for x in range(size):
            self.board.append(["~"] * size)

    def print_board(self):
        """This prints the board"""
        for row in self.board:
            print(" ".join(row))


class Ship:
    """This places the ship on the board"""
    def __init__(self, size, board):
        self.size = size
        self.board = board
        self.row = randint(0, board.size - 1)
        self.col = randint(0, board.size - 1)

    def check_guess(self, guess_row, guess_col):
        if guess_row == self.row and guess_col == self.col:
            self.board.board[guess_row][guess_col] = "!"
            print("Congratulations! You have sank my battleship!")
            self.board.print_board()
            return True
        else:
            if (guess_row < 0 or guess_row > self.board.size - 1) or \
               (guess_col < 0 or guess_col > self.board.size - 1):
                print("Sorry but thats not even on the board!")
            elif self.board.board[guess_row][guess_col] == "X":
                print("You have already guessed that spot!")
            else:
                print(" Haha, You missed my battleship!")
                self.board.board[guess_row][guess_col] = "X"
                self.board.print_board()
            return False

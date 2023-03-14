from random import randint

"""Welcome to my battle ships game"""

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

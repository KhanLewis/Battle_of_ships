"""Welcome to my battle ships game"""
from random import randint


class Board:
    """This generates the board for the game"""
    def __init__(self, size):
        self.size = size
        self.board = []
        for _ in range(size):
            self.board.append(["~"] * size)

    def print_board(self):
        """This prints the board"""
        for row in self.board:
            print(" ".join(row))


class Ship:
    """This places the ship on the board"""
    def __init__(self, board):
        self.board = board
        self.row = randint(0, board.size - 1)
        self.col = randint(0, board.size - 1)

    def check_guess(self, guess_row, guess_col):
        """checks the users guesses and if they are in bounds"""
        if guess_row == self.row and guess_col == self.col:
            self.board.board[guess_row][guess_col] = "!"
            print("Congratulations! You have sank my battleship!")
            self.board.print_board()
            return True
        else:
            if (guess_row < 0 or guess_row > self.board.size - 1) or \
               (guess_col < 0 or guess_col > self.board.size - 1):
                print("Sorry but thats not even in the ocean!")
            elif self.board.board[guess_row][guess_col] == "?":
                print("You have already guessed that spot!")
            else:
                print("Haha, You missed my battleship!")
                self.board.board[guess_row][guess_col] = "?"
                self.board.print_board()
            return False


class Game:
    """defines a game class to manage the game"""
    def __init__(self, size):
        self.board = Board(size)
        self.ship = Ship(self.board)
        self.guesses = 5

    def start_game(self):
        """starts the game and checks users guess and turns """
        print("Let's play Battleships!")
        print(f"You have {self.guesses} guesses to find the ship")
        self.board.print_board()

        for turn in range(self.guesses):
            print("Turn", turn+1)

            while True:
                try:
                    guess_row = int(input("Guess Row: ")) - 1
                    if guess_row < 0:
                        raise ValueError()
                    guess_col = int(input("Guess Col: ")) - 1
                    if guess_col < 0:
                        raise ValueError()
                    break
                except ValueError:
                    print(
                     "Row or Column was invalid, please only enter a number")

            if self.ship.check_guess(guess_row, guess_col):
                break

            if turn == self.guesses - 1:
                print("You have ran out of guesses ... Game Over")


if __name__ == '__main__':
    game = Game(5)
    game.start_game()

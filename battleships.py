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
    def __init__(self, size, board):
        self.size = size
        self.board = board
        self.row = randint(0, board.size - 1)
        self.col = randint(0, board.size - 1)

    def check_guess(self, guess_row, guess_col):
        # checks the users guess  to see if there is a hit or miss also to see,
        #  if the guess is out of bounds
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


class Game:
    """defines a game class to manage the game"""
    def __init__(self, size, ship_size):
        self.board = Board(size)
        self.ship = Ship(ship_size, self.board)
        self.guesses = 5

    def start_game(self):
        print("Let's play Battleship!")
        print(f"You have {self.guesses} guesses to find the ship")
        self.board.print_board()

        for turn in range(self.guesses):
            print("Turn", turn+1)

            while True:
                try:
                    guess_row = int(input("Guess Row: ")) - 1
                    guess_col = int(input("Guess Col: ")) - 1
                    break
                except ValueError:
                    print("Please enter a number")

            if self.ship.check_guess(guess_row, guess_col):
                break

            if turn == self.guesses - 1:
                print("You have ran out of guesses ... Game Over")


game = Game(5, 3)
game.start_game()


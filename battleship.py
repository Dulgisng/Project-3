# Code Institute Project 3 - Python Battleship Game
# Author: Dulguun Sandagsuren
# Date: 25/04/2023
# This is a python program that will implement the simplification rules of the battleship game.
# The player objective is to guessed correctly the opponent's hidden battleship before the opponent guesses their battleship.
# The game will end either when there is a winner or if the player have run out of their given guesses.


# Importing the random module's randint function.
from random import randint

# Printing the game rules and greeting message.
print("٩(◕‿◕)۶ Hello welcome to the battleship game! ٩(◕‿◕)۶")
print("To play you must guessed the opponent's hidden battleship before they guessed correctly your battleship first.")
print("You will have 10 rounds to guess the opponent's battleship.")
print("╰( ^o^)╮ Best of luck! ╰( ^o^)╮")

# Prompting the user to enter the grid size for the game.
grid_size = None
while grid_size is None:
    try:
        grid_size = int(input("Please enter the size of the grid to start: "))

# This is an error checking if the user does not entered a number.
    except ValueError:
        print("Invalid input, please enter only number.")

# Initialising the game board with O's.
board = []

for x in range(0, grid_size):
    board.append(["O"] * grid_size)

# Function to print out the current board of the battleship game.
def print_board(board):
    print(" " + " ".join(str(i) for i in range(grid_size)))
    for row in range(grid_size):
        print(str(row) + " " + " ".join(board[row]))

# Function to print out the initial state of the board.
print_board(board)

# Functions to create random rows and columns for the opponent's and player's battleships.
def random_row(board):
    return randint(0, len(board) - 1)

def random_column(board):
    return randint(0, len(board[0]) - 1)

def opponent_guess(board):
    guess_row = random_row(board)
    guess_column = random_column(board)
    return guess_row, guess_column

# Creating random positions for the opponent's and player's battleships.
player_ship_row = random_row(board)
player_ship_column = random_column(board)
opponent_ship_row = random_row(board)
opponent_ship_column = random_column(board)

# Starting the game with 10 rounds.
for round in range(10):
    print("Round", round + 1)

# Asking the user to guess the row and column of the opponent's battleship.
    guess_row = None
    while guess_row is None:
        try:
            guess_row = int(input("Please guess the row of the opponent's battleship: "))
        except ValueError:
            print("Invalid input, please enter only number.")

    guess_column = None
    while guess_column is None:
        try:
            guess_column = int(input("Please guess the column of the opponent's battleship: "))
        except ValueError:
            print("Invalid input, please enter only number.")

    # Checking if the player has guessed the right position of the opponent's battleship correctly.
    if guess_row == opponent_ship_row and guess_column == opponent_ship_column:
        print("٩(◕‿◕)۶ WINNER WINNER! ٩(◕‿◕)۶")
        print("Congratulations you've won! You've successfully destroyed the opponent's battleship!")
        print("And this is the expected row and column of your battleship: ")
        print("row: ", player_ship_row)
        print("column: ", player_ship_column)
        print_board(board)
        print("***GAME OVER***")

        # Game is over if the player is the winner
        break

# If the player's guess is not correct.
    else:

        # Checking if the player's guess is off-grid.
        if guess_row not in range(grid_size) or guess_column not in range(grid_size):
            print("Oops, sorry your guess is off-grid")

        elif board[guess_row][guess_column] == "X":
            print("Oops, sorry you've already guessed that number")

        else:
            print("Sorry you've missed the opponent's battleship!")
            board[guess_row][guess_column] = "X"
            print_board(board)

        # If the opponent guessed correctly the player battleship position then the game is over.
        opponent_guess_row, opponent_guess_column = opponent_guess(board)
        if opponent_guess_row == player_ship_row and opponent_guess_column == player_ship_column:
            print("The opponent has guessed row", opponent_guess_row, "and column", opponent_guess_column)
            print("Oh no, the opponent have guessed correctly, your battleship is now destroyed!")
            print("And this is the expected row and column of the opponent's battleship: ")
            print("row: ", opponent_ship_row)
            print("column: ", opponent_ship_column)
            print_board(board)
            print("***GAME OVER***")
            break
        else:
            # When the opponent guessed the same number the program will let they know
            print("The opponent has guessed row", opponent_guess_row, "and column", opponent_guess_column)
            if board[opponent_guess_row][opponent_guess_column] == "Y":
                print("Oops, the opponent guessed a number that already been guessed")

            # When the opponent guesses is not in range it will let the player know
            elif opponent_guess_row not in range(grid_size) or opponent_guess_column not in range(grid_size):
                print("Oops, sorry the opponent guess is off-grid")

            else:
                print("The opponent missed your battleship!")
                board[opponent_guess_row][opponent_guess_column] = "Y"
                print_board(board)

    # If its the 10th round and player still haven't guessed the opponent battleship then the game is over.
    if round == 9:
        print("Sorry you ran out of guesses and lost the game!")
        print("This is the expected row and column of the opponent's battleship: ")
        # Printing out the positions of the opponent's and player's battleships (for debugging purposes)
        print("row: ", opponent_ship_row)
        print("column: ", opponent_ship_column)
        print("And this is the expected row and column of your battleship: ")
        print("row: ", player_ship_row)
        print("column: ", player_ship_column)
        print_board(board)
        print("***GAME OVER***")

        # Game is over if the player haven't guessed correctly after 10 rounds.
        break


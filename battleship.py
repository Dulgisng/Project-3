from random import randint

print("٩(◕‿◕)۶ Hello welcome to the battleship game! ٩(◕‿◕)۶")
print("To play you must guessed the opponent's hidden battleship before they guessed correctly your battleship first.")
print("You will have 10 rounds to guess the opponent's battleship.")
print("╰( ^o^)╮ Best of luck! ╰( ^o^)╮")

grid_size = None
while grid_size is None:
    try:
        grid_size = int(input("Please enter the size of the grid to start: "))

    except ValueError:
        print("Invalid input, please enter only number.")

board = []

for x in range(0, grid_size):
    board.append(["O"] * grid_size)

def print_board(board):
    print(" " + " ".join(str(i) for i in range(grid_size)))
    for row in range(grid_size):
        print(str(row) + " " + " ".join(board[row]))

print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)

def random_column(board):
    return randint(0, len(board[0]) - 1)

def opponent_guess(board):
    guess_row = random_row(board)
    guess_column = random_column(board)
    return guess_row, guess_column

player_ship_row = random_row(board)
player_ship_column = random_column(board)
opponent_ship_row = random_row(board)
opponent_ship_column = random_column(board)


for round in range(10):
    print("Round", round + 1)


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

   
    if guess_row == opponent_ship_row and guess_column == opponent_ship_column:
        print("٩(◕‿◕)۶ WINNER WINNER! ٩(◕‿◕)۶")
        print("Congratulations you've won! You've successfully destroyed the opponent's battleship!")
        print("And this is the expected row and column of your battleship: ")
        print("row: ", player_ship_row)
        print("column: ", player_ship_column)
        print_board(board)
        print("***GAME OVER***")
        break

    else:

     
        if guess_row not in range(grid_size) or guess_column not in range(grid_size):
            print("Oops, sorry your guess is off-grid")

        elif board[guess_row][guess_column] == "X":
            print("Oops, sorry you've already guessed that number")

        else:
            print("Sorry you've missed the opponent's battleship!")
            board[guess_row][guess_column] = "X"
            print_board(board)

       
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
           
            print("The opponent has guessed row", opponent_guess_row, "and column", opponent_guess_column)
            if board[opponent_guess_row][opponent_guess_column] == "Y":
                print("Oops, the opponent guessed a number that already been guessed")

           
            elif opponent_guess_row not in range(grid_size) or opponent_guess_column not in range(grid_size):
                print("Oops, sorry the opponent guess is off-grid")

            else:
                print("The opponent missed your battleship!")
                board[opponent_guess_row][opponent_guess_column] = "Y"
                print_board(board)

  
    if round == 9:
        print("Sorry you ran out of guesses and lost the game!")
        print("This is the expected row and column of the opponent's battleship: ")
        print("row: ", opponent_ship_row)
        print("column: ", opponent_ship_column)
        print("And this is the expected row and column of your battleship: ")
        print("row: ", player_ship_row)
        print("column: ", player_ship_column)
        print_board(board)
        print("***GAME OVER***")


        break


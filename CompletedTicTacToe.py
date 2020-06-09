usedPlaces = []

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         ]


def draw():
    result = 0
    for i in range(3):
        if 0 not in board[i]:
            result += 1
    if result == 3:
        return 1
    else:
        return 0


def print_board():
    for i in range(3):
        print(board[i])


def checkGrid(grid):
    # rows
    for x in range(0, 3):
        row = set([grid[x][0], grid[x][1], grid[x][2]])
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]

    # columns
    for x in range(0, 3):
        column = set([grid[0][x], grid[1][x], grid[2][x]])
        if len(column) == 1 and grid[0][x] != 0:
            return grid[0][x]

    # diagonals
    diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
    diag2 = set([grid[0][2], grid[1][1], grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0


def who_wins(number):
    if number == 1:
        print("Player 1 is a winner winner chicken dinner!")

    elif number == 2:
        print("Player 2 is a winner winner chicken dinner")


def players_board():
    p1c = input("Player 1. row, column: ")

    while p1c in usedPlaces:
        print("This place is already used, choose something else...")
        p1c = input("Player 1. row, column: ")
    p1Choice = p1c.split(",")
    board[int(p1Choice[0])][int(p1Choice[1])] = 1
    print_board()

    usedPlaces.append(p1c)
    p2c = input("Player 2. row, column: ")
    if len(usedPlaces) == 9:
        return 0

    while p2c in usedPlaces:
        print("This place is already used, choose something else...")
        p2c = input("Player 2. row, column: ")
    p2Choice = p2c.split(",")
    board[int(p2Choice[0])][int(p2Choice[1])] = 2
    usedPlaces.append(p2c)
    print_board()


def try_again():
    response = input("Do you want play again? (y,n)")
    if response == "y":
        game(board)
    else:
        print("Thank you for trying Tic Tac Toe game!")


def game(board):
    print("Welcome in Tic Tac Toe game!!!")
    while True:
        players_board()
        plays = players_board()
        if plays == 0:
            print("DRAW!")
            break
        answer = checkGrid(board)
        if answer == 1 or 2 and answer != 0:
            who_wins(answer)
            break
    try_again()


game(board)

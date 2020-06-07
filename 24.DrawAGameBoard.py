
def get_board(size):
    segment = "|_|"
    board = (segment*size + "\n") * size

    return board


board = get_board(3)


print(board)

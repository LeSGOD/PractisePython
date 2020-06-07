"""This exercise is Part 2 of 4 of the Tic Tac Toe exercise series"""

game = [[1, 0, 2],
        [0, 2, 2],
        [2, 0, 1],
        ]

p1w = "Player 1 wins"
p2w = "Player 2 wins"


def level_line_match(game):
    for i in range(3):
        if 0 not in game[i]:
            result = sum(game[i])
            if result == 3:
                return p1w
            elif result == 6:
                return p2w


def vertical_line_match(game):
    result = set()
    for i in range(3):
        result.clear()
        for j in range(3):
            result.add(game[j][i])

        if len(result) == 1 and 1 in result:
            return p1w
        elif len(result) == 1 and 2 in result:
            return p2w


def diagonal_line_match(game):
    diag1 = set([game[0][0], game[1][1], game[2][2]])
    diag2 = set([game[0][2], game[1][1], game[2][0]])

    if len(diag1) == 1 and game[1][1] != 0 and 1 in diag1:
        return p1w
    elif len(diag1) == 1 and game[1][1] != 0 and 2 in diag1:
        return p2w
    if len(diag2) == 1 and game[1][1] != 0 and 1 in diag2:
        return p1w
    if len(diag2) == 1 and game[1][1] != 0 and 2 in diag2:
        return p2w


def checkGrid(game):
    return vertical_line_match(game), level_line_match(game), diagonal_line_match(game)


print(checkGrid(game))

"""
Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.
"""


def check_square_and_cube(lst):
    fNum = lst[0] ** (1/2)
    sNum = lst[1] ** (1/3)
    if fNum == sNum:
        return True
    else:
        return False


print(check_square_and_cube([676, 17576]))

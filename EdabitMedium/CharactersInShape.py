"""
Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.
"""


def count_characters(lst):
    length = len(lst)
    width = 0
    if length > 0:
        for i in lst[0]:
            width += 1
        return width * length
    return 0

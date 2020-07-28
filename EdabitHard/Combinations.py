"""
Create a function that takes a variable number of groups of items, and returns the number of ways the items can be arranged, with one item from each group. Order does not matter.
combinations(2, 3) ➞ 6

combinations(3, 7, 4) ➞ 84

combinations(2, 3, 4, 5) ➞ 120
"""


def combinations(*items):
    result = 1
    for item in items:
        if(item == 0):
            item = 1
        result *= item
    return result

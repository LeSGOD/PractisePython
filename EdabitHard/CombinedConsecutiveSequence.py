"""
Write a function that returns True if two lists, when combined, form a consecutive sequence.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
"""


def consecutive_combo(lst1, lst2):
    lst1.extend(lst2)
    full_list = sorted(lst1)
    firstNum = full_list[0]
    for num in full_list:
        if firstNum != num:
            return False
        firstNum += 1

    return True

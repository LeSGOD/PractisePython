"""
Find the Largest Even Number

Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in function max() is prohibited.
"""


def largest_even(lst):
    for i in sorted(lst, reverse=True):
        if not i % 2:
            return i
    return -1

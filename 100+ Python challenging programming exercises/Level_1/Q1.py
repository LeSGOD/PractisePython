"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""


def divisible_by_7_and_are_not_multiple_of_5(startNumber, lastNumber):
    numbers = [i for i in range(startNumber, lastNumber + 1) if i % 7 == 0 and i % 5 != 0]
    return numbers


print(divisible_by_7_and_are_not_multiple_of_5(2000,3200))

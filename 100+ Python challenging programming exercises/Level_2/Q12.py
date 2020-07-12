"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def digit_even_numbers(numbers):
    numbers = numbers.split(",")
    numbers = [i for i in range(int(numbers[0]), int(numbers[1]) + 1)]
    b = [0, 2, 4, 6, 8]
    result = []
    for i in numbers:
        integers = (list(map(int, str(i))))
        if integers[0] % 2 == 0 and integers[1] % 2 == 0 and integers[2] % 2 == 0 and integers[3] % 2 == 0:
            result.append(i)
    return result

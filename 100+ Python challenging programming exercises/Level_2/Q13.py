"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def number_of_letters_and_digits(sequence):
    result = {"Digits":0, "Letters":0}
    for item in sequence:
        if item.isdigit():
            result['Digits'] += 1
        elif item.isalpha():
            result["Letters"] += 1
        else:
            pass
    return result['Digits'],result["Letters"]



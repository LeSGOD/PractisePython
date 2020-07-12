"""

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def get_upper_and_lower_case_letters(sequence):
    result = {"upper": 0, "lower": 0}

    for item in sequence:
        if item.islower():
            result['lower'] += 1
        elif item.isupper():
            result['upper'] += 1
        else:
            pass
    return result['lower'], result['upper']

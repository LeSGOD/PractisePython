"""
Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line
"""


def print_maximum_length_word(a, b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    else:
        print(a)
        print(b)


print_maximum_length_word("One", "Three")

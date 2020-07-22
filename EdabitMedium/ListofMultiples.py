"""
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
"""


def list_of_multiples (num, length):
    return [num*i for i in range(1,length+1)]



"""


Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

"""


def value(number):
    number = str(number)
    result = 0
    for i in range(1, 5):
        sequence = number * i
        result += int(sequence)
    return result

"""
TASK 1. Write a postcode generator that accepts 2 strings: "79-900" and "80-155" and returns a list of codes between them.
"""


def get_zip_codes_between_two_codes(code1, code2):
    zipCodes = []

    a = [int(s) for s in code1.split("-") if s.isdigit()]
    b = [int(s) for s in code2.split("-") if s.isdigit()]

    if a[0] > b[0]:
        firstDecimal = b[0]
        firstHundred = b[1]
        secondDecimal = a[0]
        secondHundred = a[1]
    else:
        firstDecimal = a[0]
        firstHundred = a[1]
        secondDecimal = b[0]
        secondHundred = b[1]

    for i in range(1000-firstHundred):
        x = firstHundred + i
        zipCodes.append("{}-{}".format(firstDecimal, f"{x:03}"))

    for j in range(secondHundred + 1):
        zipCodes.append("{}-{}".format(secondDecimal, f"{j:03}"))

    return zipCodes

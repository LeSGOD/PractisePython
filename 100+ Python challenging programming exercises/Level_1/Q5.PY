"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""


class Bike:

    def __init__(self, company, style):
        self.company = company
        self.style = style

    def getString(self):
        print(self.company)

    def printString(self):
        print(self.company.upper())

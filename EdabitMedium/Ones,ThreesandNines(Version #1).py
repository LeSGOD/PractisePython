"""
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this
"""


class ones_threes_nines:

    def __init__(self, n):
        self.ones = n
        self.threes = n // 3
        self.nines = n // 9

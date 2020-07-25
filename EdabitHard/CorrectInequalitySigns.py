"""
Create a function that returns true if a given inequality expression is correct and false otherwise.
"""

def correct_signs(txt):
    return eval(txt)



print(correct_signs("3 < 7 < 11"))

#correct_signs("3 < 7 < 11") ➞ True
"""
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
"""

def print_dictionary(a,b):
    result_dict = {key:key**2 for (key) in range(a,b+1)}
    print(result_dict)

print_dictionary(1,3)
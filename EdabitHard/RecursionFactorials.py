"""
Write a function that calculates the factorial of a number recursively.
"""

def factorial(n):
    result = 1
    for item in range(1,n+1):
        result = result*item
    return result



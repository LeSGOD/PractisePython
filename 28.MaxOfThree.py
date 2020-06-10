def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return 
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(max_of_three(1,2,3))
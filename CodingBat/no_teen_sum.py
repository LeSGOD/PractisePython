"""

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- 
then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):
"that takes in an int value and returns that value fixed for the teen rule. In this way,
you avoid repeating the teen code 3 times (i.e. "decomposition").
Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3


"""


def fix_teen(n):
    if n in range(13, 20):
        if n == 15 or n == 16:
            return n
        else:
            n = 0
    return n


def no_teen_sum(a, b, c):
    aa = fix_teen(a)
    bb = fix_teen(b)
    cc = fix_teen(c)
    return aa + bb + cc

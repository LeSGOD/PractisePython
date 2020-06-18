"""

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more.
Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True

"""


def close_far(a, b, c):
    ab = abs(a-b)
    ac = abs(a-c)
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    santander = [a, b, c]
    minimumV = 0
    maximumV = 0
    if ab <= 1 or ac <= 1:
        for i in range(3):
            if abs(minimum-santander[i]) >= 2:
                minimumV += 1
            if abs(maximum-santander[i]) >= 2:
                maximumV += 1
    return minimumV == 2 or maximumV == 2

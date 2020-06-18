"""

We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

"""


def make_chocolate(small, big, goal):
    blocks = int(goal / 5)
    if blocks > big:
        blocks = big
    bc = blocks * 5
    restForSmall = 0
    if goal - bc >= 0:
        restForSmall = goal - bc
        if restForSmall - small <= 0:
            result = abs(restForSmall-small)
            small -= result
            return small
        return -1

    return -1


print(make_chocolate(4, 1, 4))

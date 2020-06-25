"""

♦ TASK 3. Generate a list of numbers from 2 to 5.5 in steps of 0.5.
The resulting data must be of type decimal.

"""


def get_list():
    steps = int((5.5-2) / 0.5)
    return [i*0.5 + 2 for i in range(1, steps)]

"""

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

"""


def get_number_divisible(n):
    for i in range(n):
        if i % 7 == 0:
            yield i


result = get_number_divisible(30)

for item in result:
    print(item)

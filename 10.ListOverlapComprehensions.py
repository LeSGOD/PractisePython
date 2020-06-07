from random import sample
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = sample(range(10), 5)
y = sample(range(10), 5)


def get_common_numbers(list1, list2):
    print(list1)
    print(list2)
    result = [i for i in set(list1) if i in list2]
    print(result)
    return result


get_common_numbers(x, y)


a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]


def get_numbers_from_list(choosenList):
    element = []
    for i in range(len(choosenList) - 1):
        if (a[i] < 5):
            element.append(a[i])
    print(element)


print([a[i] for i in range(len(a) - 1) if a[i] < 5])


def get_numbers_lower_than(x):
    element = []
    for i in range(len(a) - 1):
        if (a[i] < x):
            element.append(a[i])
    print(element)


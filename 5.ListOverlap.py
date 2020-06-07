import random

x = []

for i in range(20):
    number = random.randrange(0, 100)
    x.append(number)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34]


# 1 extra
def return_common_elements_between_lists(b, a):
    checkList = []
    for i in range(0, len(a)):
        if a[i] in b:
            checkList.append(a[i])
    print(checkList)


randomList1 = random.sample(range(0, 101), 5)
randomList2 = random.sample(range(0, 101), 5)
oneLine = [a[i] for i in range(0, len(a)) if (a[i] in b)]


# 2 extra
print([a[i] for i in range(0, len(a)) if (a[i] in b)])


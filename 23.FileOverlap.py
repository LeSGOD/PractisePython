def overlap(filename):
    list_to_return = []
    with open(filename) as file:
        line = file.readline()
        while line:
            list_to_return.append(int(line))
            line = file.readline()

    return list_to_return


primelist = overlap("primeNumbers.txt")
happylist = overlap("happyNumbers.txt")

overlaplist = [element for element in primelist if element in happylist]
print(overlaplist)

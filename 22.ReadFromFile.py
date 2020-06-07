
fileToOpen = input("Which file you wanna count ")

names = {}
with open(fileToOpen + ".txt", "r") as f:
    line = f.readline()
    while line:

        line = line.strip()
        if line not in names:
            names[line] = 1
        else:
            names[line] += 1
        line = f.readline()

print(names)

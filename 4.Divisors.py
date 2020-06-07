def get_devisors_of_number(x):
    if (x > 1):
        listOfDividednumbers = []
        for i in range(1, x + 1):
            if (x % i == 0):
                listOfDividednumbers.append(i)
    else:
        print("Your number is wrong ")

    print(listOfDividednumbers)


get_devisors_of_number(1234)



def is_prime():
    choice = int(input("Which number you will choose? "))
    dividersList = []
    for i in range(2, choice):
        if choice % i == 0:
            dividersList.append(i)

    if len(dividersList) >= 1:
        print("This is not prime number")
        print("It has " + str(len(dividersList)) +
              " dividers " + str(dividersList))
    else:
        print("This is prime number")

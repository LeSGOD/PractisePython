


def check_odd_or_even():
    askedNumber = int(input("Type number: "))
    if (askedNumber % 2 == 0):
        if (askedNumber % 4 == 0):
            print("This number is divided by 4")                      
        else:
            print("This number is even")

    else:
        print("this number is odd")

def is_it_even_divided():
    num = int(input("Divided number "))
    numDivided = int(input("Number to divide "))

    if(num % numDivided == 0):
        print(str(num) + " is divided by " + str(numDivided))
    else:
        print(str(num) + " is not divided by " + str(numDivided))


is_it_even_divided()
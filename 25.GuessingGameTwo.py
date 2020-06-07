from statistics import median


def get_number_from_your_head():
    searchRange = [i for i in range(0, 101)]
    shots = 0
    while True:

        firstNumber = searchRange[0]
        lastNumber = searchRange[-1]

        middleNumber = median(searchRange)
        middleNumber = int(middleNumber)

        print(middleNumber)
        response = input("It is your number?  ")

        if (response == "yes"):
            print("attempts: " + str(shots))
            break
        elif response == "no":
            shots += 1
            higherOrLower = input("It is higher or lower: ")

            if (higherOrLower == "higher"):
                for element in range(firstNumber, middleNumber + 1):
                    searchRange.remove(element)

            else:
                for element in range(middleNumber, lastNumber + 1):
                    searchRange.remove(element)

        elif (response == "q"):
            break


get_number_from_your_head()

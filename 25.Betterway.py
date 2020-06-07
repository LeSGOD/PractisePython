from statistics import median


def get_number_from_your_head():

    game = "x"
    searchRange = [i for i in range(0, 101)]
    shots = 0

    print("===================== Guess the number ======================")
    print("=========== Think in a number between 0 and 100 =============")
    print('''Type "h" if the machine guess is too high.
    Type "l" if the machine guess is too low.
    Type "r" if the machine guess is right.''')
    print("=============================================================")

    while game != "q":

        shots += 1
        firstNumber = searchRange[0]
        lastNumber = searchRange[-1]

        middleNumber = median(searchRange)
        middleNumber = int(middleNumber)

        print('The machine guess is:', middleNumber)
        print("=============================================================")
        response = input("l, h or r?  ")

        if (response == "r"):
            print("*********************** Right guess! ************************")
            print("===================== It took",
                  shots, "tries. ======================")
            game = input(
                "Press 'Enter' to play a new game or type 'q' to end the game ")

        if (response == "h"):
            for element in range(firstNumber, middleNumber + 1):
                searchRange.remove(element)

        elif(response == "l"):
            for element in range(middleNumber, lastNumber + 1):
                searchRange.remove(element)


get_number_from_your_head()

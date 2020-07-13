"""
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


def net_amount_of_a_bank():
    result = 0
    print("Welcome in net bank!")
    while True:
        response = str(
            input("Do you wanna deposit or withdraw? (type: D or W): "))
        response = response.capitalize()
        if response == 'D':
            try:
                amount = int(input("How much do you wanna deposit?: "))
                result += amount
            except ValueError:
                print("You have to put there integer!")
                continue
        elif response == "W":
            try:
                amount = int(input("How much do you wanna withdraw?: "))
                result -= amount
            except ValueError:
                print("You have to put there integer!")
                continue
        else:
            break
    print("Thank you for using our content!")
    return "net amount: " + str(result)


print(net_amount_of_a_bank())

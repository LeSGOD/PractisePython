
def get_fibonacci_numbers():
    amount = int(input("How much numbers you want? "))
    fibo = [1, 1]
    for _ in range(amount - 2):
        x = fibo[len(fibo) - 1] + fibo[len(fibo) - 2]
        fibo.append(x)
    print(fibo)


get_fibonacci_numbers()
